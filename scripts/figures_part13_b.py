"""Figures for SE-163 to SE-168 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3 unless a time or a hash is shown)."""
from __future__ import annotations

from figure_kit import Fig, dumbbell, grouped_bars, heatmap, line_chart
from figure_diagrams import fan
from figures_part07_a import bars


SINT = "Datos sintéticos, semilla fija; idénticos en Windows y Ubuntu (WSL2), salvo lo indicado."


# ---------------------------------------------------------------- SE-163
def se163_linter() -> Fig:
    return grouped_bars(
        'Linter de un documento OpenAPI mínimo: 240 mutaciones',
        "Barras horizontales con las mutaciones inyectadas y detectadas por un linter de un documento OpenAPI mínimo: detecta las seis familias de defectos de forma (173 de 173) y ninguna de las 67 que cambian el código de éxito o hacen que una descripción mienta.",
        ["Parámetro de ruta sin declarar", "Renombrar el parámetro solo en la ruta", "operationId repetido", "Operación de escritura sin respuesta de error",
         "Parámetro de ruta no marcado como requerido", "Operación sin respuestas", "Cambiar el código de éxito de 201 a 200", "Descripción que miente («devuelve una lista»)"],
        [("Inyectados", [28, 31, 25, 32, 30, 27, 29, 38], "grey"), ("Detectados", [28, 31, 25, 32, 30, 27, 0, 0], "teal")],
        unit="Mutaciones", horizontal=True, label_w=290, ticks=[0, 10, 20, 30, 40],
        note='Un documento puede ser sintácticamente impecable y describir otra cosa. El linter protege la forma del contrato; que el servicio responda lo que el documento promete lo comprueba una prueba contractual (SE-166).', note_kind='coral', foot=SINT)


def se163_coste() -> Fig:
    pts = [(b, 1 + b + b ** 2 + b ** 3) for b in (2, 5, 10, 20, 50)]
    return line_chart(
        'Quién decide qué viaja: coste de una consulta anidada de profundidad 3 según la ramificación',
        "Línea en escalas logarítmicas con los resolvedores que ejecuta una consulta anidada de profundidad 3 según la ramificación, 1 más b más b al cuadrado más b al cubo: 15 con ramificación 2, 1 111 con 10 y 127 551 con 50, sin tope; las dos cifras medidas son 10 y 50.",
        [("Resolvedores de la consulta", [(b, v, f"{v:,}".replace(",", " ") + (" · medido" if b in (10, 50) else ""), "t") for b, v in pts], "coral")],
        x_label="Ramificación b (hijos por nodo)", y_label="Resolvedores ejecutados", log_x=True, log_y=True,
        x_ticks=[(2, "2"), (5, "5"), (10, "10"), (20, "20"), (50, "50"), (100, "")], y_ticks=[10, 100, 1000, 10000, 100000, 1000000], point_labels="none",
        note='Dejar al cliente elegir campos reduce los bytes y desplaza el riesgo al servidor: sin límite de profundidad o de coste, una consulta pequeña puede costar miles de llamadas. El número de resolvedores es un cálculo (1 + b + b² + b³), no una medición de un servidor.', note_kind='gold', foot=SINT)


def se163_eventos() -> Fig:
    items = [
        ("Consumidor ingenuo, duplicados del 15 %", 0, "coral", "0 de 1 000"),
        ("Consumidor idempotente por identificador", 1000, "teal", "1 000 de 1 000"),
        ("Último mensaje gana, 20 % reordenado", 804, "coral", "804 de 1 000"),
        ("Número de versión por entidad", 1000, "teal", "1 000 de 1 000"),
    ]
    return bars("Estado final correcto con entrega al-menos-una-vez y mensajes reordenados",
                "Barras de 1 000 corridas: un consumidor sin idempotencia nunca obtiene el total correcto con 15 por ciento de duplicados; con identificador siempre; si el último mensaje gana el estado final es correcto 804 veces, y con número de versión 1 000.",
                items, 0.46, "El contrato de un evento incluye identificador, versión o clave de orden y la semántica de entrega. Las tasas de duplicado (15 %) y reordenamiento (20 %) son supuestos del autor, no medidas de un broker.",
                label_w=420, width=1080, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-164
def se164_matriz() -> Fig:
    return heatmap(
        'Documentos legibles de 2 000 tras cada cambio de esquema',
        "Mapa de calor con los documentos legibles, de 2 000, tras cada cambio de esquema según quién lee: el lector nuevo lee todos salvo con campo requerido agregado, campo renombrado u opcional que pasa a requerido; el viejo estricto falla con 0 en agregar un requerido, quitar un requerido y renombrar, y con 2 000 en quitar un opcional.",
        ["Agregar campo opcional", "Agregar campo requerido", "Quitar campo opcional", "Quitar campo requerido", "Opcional pasa a requerido", "Requerido pasa a opcional",
         "Ampliar tipo de entero a decimal", "Agregar valor de enum", "Quitar valor de enum", "Renombrar un campo"],
        ["Nuevo lee viejos", "Viejo tolerante lee nuevos", "Viejo estricto lee nuevos"],
        [[2000, 2000, 1027], [0, 2000, 0], [2000, 2000, 2000], [2000, 0, 0], [995, 2000, 2000], [2000, 1014, 977], [2000, 997, 1025], [2000, 1338, 1313], [1016, 2000, 2000], [0, 0, 0]],
        unit="documentos legibles, de 2 000", row_title="Cambio de esquema", col_title="Documentos legibles (de 2 000)",
        scale="teal", vmin=0, vmax=2000, cell_fmt=lambda v: f"{int(v):,}".replace(",", " "), cell_h=34, label_w=250,
        note='Un cambio es compatible solo si lee 2 000 de 2 000 en la dirección que importa. «Agregar campo opcional» es seguro para el consumidor tolerante y rompe la mitad de los documentos para el estricto.', note_kind='gold', foot=SINT)


def se164_estrictos() -> Fig:
    items = [
        ("0 % de consumidores estrictos", 6.87, "teal", "6,87 de 20"),
        ("25 %", 9.56, "gold", "9,56"),
        ("50 %", 12.25, "gold", "12,25"),
        ("75 %", 14.94, "coral", "14,94"),
        ("100 %", 17.63, "coral", "17,63"),
    ]
    return bars("Consumidores rotos por lanzamiento (de 20) según cuántos son estrictos",
                "Barras: con 2 000 lanzamientos sintéticos y una mezcla de cambios, el promedio de consumidores rotos por lanzamiento sube de 6,87 de 20 sin consumidores estrictos a 17,63 si todos son estrictos.",
                items, 26, "Incluso con todos tolerantes se rompen casi siete de cada veinte, porque la mezcla de cambios incluye renombrados y campos requeridos nuevos. La mezcla de cambios (45 % campos opcionales, 15 % enums…) es un supuesto del autor.",
                label_w=360, width=980, note_kind="gold", foot=SINT)


def se164_ventana() -> Fig:
    items = [
        ("Ventana de 30 días", 22.4, "coral", "22,4 de 40"),
        ("90 días", 8.8, "gold", "8,8"),
        ("180 días", 4.6, "gold", "4,6"),
        ("365 días", 4.0, "gold", "4,0 (98,7 % de las simulaciones: al menos uno)"),
    ]
    return bars("Consumidores que siguen en la versión vieja al cerrarse la ventana de deprecación",
                "Barras de 2 000 simulaciones con 40 consumidores: con una ventana de 30 días quedan 22,4 en media, con 90 quedan 8,8, con 180 quedan 4,6 y con 365 quedan 4,0, porque 10 por ciento nunca migra solo.",
                items, 15, "Alargar la ventana de 180 a 365 días casi no ayuda: el resto son consumidores abandonados que solo migran si alguien los contacta o se les corta el servicio. Migración exponencial de media 45 días y 10 % abandonado son supuestos del autor.",
                label_w=300, width=1100, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-165
def se165_deriva() -> Fig:
    items = [
        ("Comprobar en cada commit", 1.0, "teal", "1,0 commits"),
        ("Cada 5 commits", 3.2, "gold", "3,2"),
        ("Cada 20 commits", 13.2, "coral", "13,2 (1 de 300 trayectorias termina con deriva)"),
    ]
    return bars("Cuántos commits dura una deriva entre especificación y código",
                "Barras de 300 trayectorias de 200 commits con 8 por ciento de probabilidad de deriva por commit: comprobar en cada commit la deja 1,0 commits, cada 5 la deja 3,2 y cada 20 la deja 13,2; sin comprobar, las 300 trayectorias terminan con deriva.",
                items, 18, "La comprobación mecánica no impide la deriva, acorta su vida. La probabilidad de 8 % por commit es un supuesto; la detección usa la firma real de funciones leída con inspect, lo que ve nombres y parámetros, no comportamiento.",
                label_w=300, width=1100, note_kind="gold", foot=SINT)


def se165_regeneracion() -> Fig:
    return fan(
        'Regenerar código desde la especificación: qué se pierde',
        "Diagrama de lo que pasa al regenerar código desde la especificación: las 3 líneas editadas a mano dentro del archivo generado, de 21 distintas del generador, se sobrescriben; el código manual fuera de una región delimitada sobrevive; lo editado dentro de la región delimitada se pierde igualmente porque la región es del generador.",
        ("Regenerar desde la especificación", "el generador reescribe lo que considera suyo", "navy"),
        [("3 líneas editadas a mano dentro del archivo generado", "3 de 21 líneas distintas del generador: regenerar las sobrescribe", "coral"),
         ("Código manual fuera de la región delimitada", "sobrevive a la regeneración; hace falta un límite explícito", "teal"),
         ("Lo editado dentro de la región delimitada", "se pierde igualmente: la región es del generador", "coral")],
        note='Spec-as-source exige que lo editable no viva en lo generado. Delimitar una región resuelve la pérdida silenciosa y no resuelve la pregunta de fondo: ¿quién es dueño de ese comportamiento, la especificación o el código?', note_kind='gold', foot=SINT)


def se165_huella() -> Fig:
    items = [
        ("Salida en el orden de iteración de un conjunto", 8, "coral", "8 huellas distintas en 8 semillas"),
        ("Salida ordenada explícitamente", 1, "teal", "1 huella en 8 semillas"),
    ]
    return bars("Un generador determinista: la misma especificación, ocho semillas de hash de Python",
                "Barras: un generador que recorre un conjunto de siete campos produce ocho salidas distintas con ocho valores de PYTHONHASHSEED; el mismo generador con orden explícito produce una sola salida.",
                items, 40, "El orden de un conjunto de cadenas depende de la semilla de hash por proceso. Un generador que no ordena produce diffs fantasma, rompe las comprobaciones de «regenerar y comparar» y hace irrepetible el artefacto. Se comprobó en Windows y Ubuntu con el mismo resultado.",
                label_w=420, width=1100, note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-166
def se166_matriz() -> Fig:
    return grouped_bars(
        'Ocho cambios del proveedor y cinco consumidores con contratos propios',
        "Barras horizontales con los consumidores rotos, de cinco, por cada cambio del proveedor que detecta el contrato del consumidor, frente a la prueba propia del proveedor, que no detecta ninguno: quitar la nota, pasarla a texto o a decimal rompe a 3, renombrar el plazo a 2 y archivos nulo a 1; agregar, reordenar o anidar no rompe a nadie.",
        ["Quitar nota", "Renombrar plazo a vence", "Nota pasa a texto", "Nota pasa a decimal (80.0)", "Archivos pasa a nulo", "Agregar campo", "Reordenar campos", "Anidar el enlace «links»"],
        [("Contratos de los consumidores", [3, 2, 3, 3, 1, 0, 0, 0], "teal"), ("Prueba propia del proveedor", [0, 0, 0, 0, 0, 0, 0, 0], "grey")],
        unit="Consumidores rotos detectados, de 5", horizontal=True, label_w=240, ticks=[0, 1, 2, 3, 4, 5],
        note='Cada consumidor fija solo los campos que usa; por eso agregar un campo no rompe a nadie, y por eso un contrato que fijara los seis campos habría rechazado 1 de los 3 cambios inocuos. Un proveedor que genera su esquema desde su código siempre se aprueba a sí mismo.', note_kind='gold', foot=SINT)


def se166_reduccion() -> Fig:
    items = [
        ("Intentos hasta el primer contraejemplo (media)", 8.3, "gold", "8,3 (máximo 48)"),
        ("Tamaño medio del contraejemplo hallado", 22.7, "coral", "22,7 elementos"),
        ("Tamaño tras reducirlo", 3.0, "teal", "3,0 (siempre 3)"),
    ]
    return bars("Pruebas basadas en propiedades: hallar y reducir un contraejemplo (300 semillas)",
                "Barras de 300 semillas: una propiedad de deduplicación falla en media al 8,3 intento y el contraejemplo hallado tiene 22,7 elementos; tras reducirlo siempre quedan 3, la forma mínima a, b, a.",
                items, 18, "La reducción lleva un caso difícil de leer a [3, 0, 3]: dos valores iguales no adyacentes. Esa forma mínima revela el defecto (el algoritmo solo compara con el elemento anterior) sin examinar 22 números.",
                label_w=420, width=1000, note_kind="teal", foot=SINT)


def se166_doble() -> Fig:
    items = [
        ("Servidor local real, Windows", 901, "gold", "901 µs por llamada"),
        ("Servidor local real, Ubuntu (WSL2)", 667, "gold", "667 µs"),
        ("Doble de prueba en proceso, Windows", 0.30, "teal", "0,30 µs"),
        ("Doble de prueba en proceso, Ubuntu", 0.20, "teal", "0,20 µs"),
    ]
    return bars("Mediana por llamada: servidor HTTP local frente a un doble de prueba",
                "Barras con la mediana de 300 llamadas: un servidor HTTP local real tarda 901 microsegundos en Windows y 667 en Ubuntu; un doble de prueba en proceso tarda 0,30 y 0,20, pero sigue pasando después de que el proveedor renombra el campo y el servidor real ya no.",
                items, 0.45, "El doble es unas tres mil veces más rápido y por eso se usa; cuando el proveedor renombró «nota» a «calificacion», la prueba con doble siguió pasando y la prueba contra el proveedor real falló. Los tiempos son de un equipo y varían; la razón, no.",
                label_w=420, width=1000, note_kind="gold", foot="Tiempos medidos en un equipo (127.0.0.1); varían entre ejecuciones. El resultado de pasar o fallar es idéntico en ambos sistemas.")


# ---------------------------------------------------------------- SE-167
def se167_clausulas() -> Fig:
    return heatmap(
        'Linter de cláusulas de contrato con seis cláusulas que no vio al escribirse',
        "Mapa de calor de seis cláusulas nuevas según el juicio del autor y la decisión de la regla: dos completas aceptadas, una completa rechazada (el falso negativo con «excepto» y «estudiante») y tres incompletas rechazadas; ninguna incompleta aceptada.",
        ["Cláusula completa (juicio del autor)", "Cláusula incompleta (juicio del autor)"], ["La regla acepta", "La regla rechaza"],
        [[2, 1], [0, 3]], unit="cláusulas, de 6", row_title="Juicio", col_title="Decisión de la regla",
        scale="gold", vmin=0, vmax=3, decimals=0, highlight=[(0, 1)], cell_h=52, label_w=280,
        note='Ajuste: 4 aceptadas y 4 rechazadas correctas (8 de 8). Casos nuevos: 5 de 6. La regla mide forma (actor, modal, observable, límite) y no verdad; una cláusula completa puede ser falsa y una incompleta, intencionalmente abierta.', note_kind='gold', foot=SINT)


def se167_rondas() -> Fig:
    items = [
        ("Ronda 0: solo el ejemplo de la intención", 63, "coral", "63 supervivientes"),
        ("Ronda 1: un contraejemplo", 51, "coral", "51"),
        ("Ronda 2", 43, "gold", "43"),
        ("Ronda 3", 7, "gold", "7"),
        ("Ronda 4: 5 ejemplos en total", 2, "teal", "2 (los equivalentes)"),
        ("5 ejemplos al azar", 7.6, "gold", "7,6"),
        ("10 ejemplos al azar", 5.2, "gold", "5,2"),
        ("20 ejemplos al azar", 4.3, "gold", "4,3"),
    ]
    return bars("Mutantes que sobreviven a cada ronda de contraejemplos (255 mutantes, 2 equivalentes)",
                "Barras: el ejemplo de la intención deja vivos 63 de 255 mutantes de una regla de penalización; cada contraejemplo del mutante superviviente los baja a 51, 43, 7 y 2, el mínimo posible; cinco, diez y veinte ejemplos al azar dejan 7,6, 5,2 y 4,3.",
                items, 7, "Tomar un mutante vivo y añadir el ejemplo más pequeño que lo distingue converge en cinco ejemplos; la suite aleatoria no llega al mínimo ni con veinte. El bucle no sabe si un mutante superviviente es equivalente: detenerse es una decisión humana.",
                label_w=400, width=1020, note_kind="teal", foot=SINT)


def se167_contrato() -> Fig:
    return grouped_bars(
        'Revisor del propio contrato: 210 mutaciones',
        "Barras horizontales con las mutaciones inyectadas y detectadas por un revisor del propio contrato: detecta las cuatro familias de coherencia interna (118 de 118) y ninguna de las 92 que cambian el texto de un invariante, el mensaje de un error o ensanchan el rango de horas.",
        ["Estrechar el rango de horas", "Quitar el ejemplo de un código de error", "Agregar un error sin ejemplo", "Agregar un invariante sin prueba", "Cambiar el texto de un invariante", "Cambiar el mensaje de un error", "Ensanchar el rango de horas"],
        [("Inyectadas", [33, 29, 27, 29, 21, 38, 33], "grey"), ("Detectadas", [33, 29, 27, 29, 0, 0, 0], "teal")],
        unit="Mutaciones", horizontal=True, label_w=270, ticks=[0, 10, 20, 30, 40],
        note='El revisor garantiza que el contrato sea coherente consigo mismo. Un contrato más permisivo, un mensaje que miente o un invariante con el sentido contrario pasan: esa revisión es de una persona con el dominio.', note_kind='coral', foot=SINT)


# ---------------------------------------------------------------- SE-168
def se168_trazabilidad() -> Fig:
    return grouped_bars(
        'Validador de un paquete trazable de 41 artefactos: 240 mutaciones',
        "Barras horizontales con las mutaciones inyectadas y detectadas por un validador de un paquete trazable: detecta las siete familias mecánicas (216 de 216) y ninguna de las 24 en que el texto cambia de sentido con el rastro intacto.",
        ["Enlace a un identificador inexistente", "Requisito sin contrato (huérfano)", "Contrato sin ejemplo ni prueba", "Ciclo entre artefactos", "Prueba enlazada a una intención (tipo no permitido)",
         "Contenido cambiado sin actualizar el rastro", "Renombrar un identificador sin actualizar enlaces", "Texto cambiado de sentido, con el rastro intacto"],
        [("Inyectadas", [33, 32, 34, 35, 26, 29, 27, 24], "grey"), ("Detectadas", [33, 32, 34, 35, 26, 29, 27, 0], "teal")],
        unit="Mutaciones", horizontal=True, label_w=300, ticks=[0, 10, 20, 30, 40],
        note='La trazabilidad mecánica prueba que los eslabones existen y no se han movido, no que digan lo mismo. Si el texto de un requisito cambia de sentido y su rastro queda intacto, el validador lo da por bueno.', note_kind='coral', foot=SINT)


def se168_impacto() -> Fig:
    items = [
        ("Requisito, 1 enlace por artefacto", 4.9, "teal", "4,9"),
        ("Requisito, 2 enlaces", 14.1, "gold", "14,1"),
        ("Requisito, 3 enlaces", 33.1, "coral", "33,1 de 170"),
        ("Contrato, 1 enlace", 2.7, "teal", "2,7"),
        ("Contrato, 2 enlaces", 6.1, "gold", "6,1"),
        ("Contrato, 3 enlaces", 11.3, "coral", "11,3"),
    ]
    return bars("Artefactos afectados al cambiar un requisito o un contrato (200 grafos sintéticos)",
                "Barras: en grafos sintéticos de cinco capas, cambiar un requisito afecta en media 4,9 artefactos con un enlace por artefacto, 14,1 con dos y 33,1 con tres; cambiar un contrato afecta 2,7, 6,1 y 11,3.",
                items, 13, "Densificar los enlaces multiplica el alcance de un cambio por unas siete veces al pasar de 1 a 3. El análisis de impacto lista qué revisar; no dice si esos artefactos necesitan cambiar. Las capas y grados son supuestos del autor.",
                label_w=360, width=980, note_kind="gold", foot=SINT)


def se168_huella() -> Fig:
    return fan(
        'Huella de un paquete de 200 archivos en dos sistemas',
        "Diagrama de la huella de un paquete de 200 archivos en dos sistemas: con el modo de texto por defecto Windows da 480485af12cf44f9 y Ubuntu 55f841e9f3d4b56f; con el salto de línea fijo los dos dan 55f841e9f3d4b56f; alterar 3 bytes cambia la huella en ambos y calcularla tarda 0,033 s en Windows y 0,004 s en Ubuntu.",
        ("Mismo contenido, 200 archivos", "huella calculada en Windows y en Ubuntu (WSL2)", "navy"),
        [("Modo de texto por defecto: dos huellas", "Windows 480485af12cf44f9 · Ubuntu 55f841e9f3d4b56f", "coral"),
         ("Salto de línea fijo (newline=\"\\n\"): una huella", "55f841e9f3d4b56f en los dos sistemas", "teal"),
         ("Alterar 3 bytes de un archivo", "la huella cambia en los dos sistemas: se detecta la manipulación", "gold"),
         ("Calcular la huella de 200 archivos", "0,033 s en Windows · 0,004 s en Ubuntu, de un equipo", "grey")],
        note='Sin fijar el salto de línea, el mismo contenido tiene dos huellas: un manifiesto firmado en un sistema no verifica en el otro. La huella detecta cambios en los bytes, no su autoría ni su sentido. Los tiempos son de un equipo y no son comparables entre sistemas.', note_kind='coral', foot="Datos sintéticos; las huellas son deterministas, los tiempos no.")


FIGURES = {
    "se-163-linter-de-un-documento-openapi.svg": se163_linter,
    "se-163-bytes-y-resolvedores.svg": se163_coste,
    "se-163-eventos-duplicados-y-reordenados.svg": se163_eventos,
    "se-164-cambios-de-esquema-y-lectura.svg": se164_matriz,
    "se-164-consumidores-estrictos.svg": se164_estrictos,
    "se-164-ventana-de-deprecacion.svg": se164_ventana,
    "se-165-duracion-de-la-deriva.svg": se165_deriva,
    "se-165-regeneracion-y-ediciones-manuales.svg": se165_regeneracion,
    "se-165-generador-determinista.svg": se165_huella,
    "se-166-contratos-de-consumidor.svg": se166_matriz,
    "se-166-reduccion-de-contraejemplos.svg": se166_reduccion,
    "se-166-doble-de-prueba-frente-a-proveedor-real.svg": se166_doble,
    "se-167-linter-de-clausulas.svg": se167_clausulas,
    "se-167-rondas-de-contraejemplos.svg": se167_rondas,
    "se-167-revisor-del-contrato.svg": se167_contrato,
    "se-168-validador-de-trazabilidad.svg": se168_trazabilidad,
    "se-168-alcance-de-un-cambio.svg": se168_impacto,
    "se-168-huella-del-paquete.svg": se168_huella,
}
