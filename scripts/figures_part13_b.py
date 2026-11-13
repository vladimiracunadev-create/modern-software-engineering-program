"""Figures for SE-163 to SE-168 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3 unless a time or a hash is shown)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos, semilla fija; idénticos en Windows y Ubuntu (WSL2), salvo lo indicado."


# ---------------------------------------------------------------- SE-163
def se163_linter() -> Fig:
    rows = [
        ["Parámetro de ruta sin declarar", "28", "28"],
        ["Renombrar el parámetro solo en la ruta", "31", "31"],
        ["operationId repetido", "25", "25"],
        ["Operación de escritura sin respuesta de error", "32", "32"],
        ["Parámetro de ruta no marcado como requerido", "30", "30"],
        ["Operación sin respuestas", "27", "27"],
        ["Cambiar el código de éxito de 201 a 200", "29", "0"],
        ["Descripción que miente («devuelve una lista»)", "38", "0"],
    ]
    return tab("Linter de un documento OpenAPI mínimo: 240 mutaciones",
               "Tabla de ocho tipos de defecto inyectados en un documento OpenAPI mínimo: el linter detecta los 173 defectos de estructura y no detecta los 67 que cambian el significado, como un código de éxito distinto o una descripción falsa.",
               ["Defecto inyectado", "Inyectados", "Detectados"], rows, [500, 160, 160], row_h=38, size=13,
               note="Un documento puede ser sintácticamente impecable y describir otra cosa. El linter protege la forma del contrato; que el servicio responda lo que el documento promete lo comprueba una prueba contractual (SE-166).",
               note_kind="coral", foot=SINT)


def se163_coste() -> Fig:
    rows = [
        ["100 entregas completas (recurso REST)", "69 629 bytes", "100 %"],
        ["Las mismas 100 con solo id y nota (selección de campos)", "3 193 bytes", "4,6 %"],
        ["Consulta anidada: profundidad 3, ramificación 10", "1 111 resolvedores", "sin tope"],
        ["Consulta anidada: profundidad 3, ramificación 50", "127 551 resolvedores", "sin tope"],
    ]
    return tab("Quién decide qué viaja: tamaño de la respuesta y coste de una consulta anidada",
               "Tabla: cien entregas sintéticas pesan 69 629 bytes completas y 3 193 con solo id y nota; una consulta anidada de profundidad 3 invoca 1 111 resolvedores con ramificación 10 y 127 551 con ramificación 50.",
               ["Caso", "Medida", "Frente a la respuesta completa"], rows, [520, 230, 180], row_h=44, size=13,
               note="Dejar al cliente elegir campos reduce los bytes y desplaza el riesgo al servidor: sin límite de profundidad o de coste, una consulta pequeña puede costar miles de llamadas. El número de resolvedores es un cálculo (1 + b + b² + b³), no una medición de un servidor.",
               note_kind="gold", foot=SINT)


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
    rows = [
        ["Agregar campo opcional", "2000", "2000", "1027"],
        ["Agregar campo requerido", "0", "2000", "0"],
        ["Quitar campo opcional", "2000", "2000", "2000"],
        ["Quitar campo requerido", "2000", "0", "0"],
        ["Opcional pasa a requerido", "995", "2000", "2000"],
        ["Requerido pasa a opcional", "2000", "1014", "977"],
        ["Ampliar tipo de entero a decimal", "2000", "997", "1025"],
        ["Agregar valor de enum", "2000", "1338", "1313"],
        ["Quitar valor de enum", "1016", "2000", "2000"],
        ["Renombrar un campo", "0", "0", "0"],
    ]
    return tab("Documentos legibles de 2 000 tras cada cambio de esquema",
               "Tabla de diez cambios de esquema con tres lecturas: un consumidor nuevo que lee documentos viejos, un consumidor viejo tolerante que lee documentos nuevos y uno estricto; solo quitar un campo opcional es legible siempre, y renombrar rompe las tres.",
               ["Cambio", "Nuevo lee viejos", "Viejo tolerante lee nuevos", "Viejo estricto lee nuevos"], rows, [380, 190, 240, 240], row_h=33, size=12,
               note="Un cambio es compatible solo si lee 2 000 de 2 000 en la dirección que importa. «Agregar campo opcional» es seguro para el consumidor tolerante y rompe la mitad de los documentos para el estricto.",
               note_kind="gold", foot=SINT)


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
    rows = [
        ["Se editan 3 líneas a mano dentro del archivo generado", "3 de 21 líneas distintas del generador", "Regenerar las sobrescribe"],
        ["Código manual fuera de la región delimitada", "Sobrevive a la regeneración", "Hace falta un límite explícito"],
        ["Lo editado dentro de la región delimitada", "Se pierde igualmente", "La región es del generador"],
    ]
    return tab("Regenerar código desde la especificación: qué se pierde",
               "Tabla de un experimento de regeneración: tres líneas editadas a mano en un archivo generado se pierden al regenerar; el código manual fuera de una región delimitada sobrevive y lo editado dentro de ella se pierde.",
               ["Situación", "Resultado", "Consecuencia"], rows, [380, 290, 260], row_h=52, size=13,
               note="Spec-as-source exige que lo editable no viva en lo generado. Delimitar una región resuelve la pérdida silenciosa y no resuelve la pregunta de fondo: ¿quién es dueño de ese comportamiento, la especificación o el código?",
               note_kind="gold", foot=SINT)


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
    rows = [
        ["Quitar nota", "3: panel, exporta, informes", "0"],
        ["Renombrar plazo a vence", "2: avisos, informes", "0"],
        ["Nota pasa a texto", "3: panel, exporta, informes", "0"],
        ["Nota pasa a decimal (80.0)", "3: panel, exporta, informes", "0"],
        ["Archivos pasa a nulo", "1: exporta", "0"],
        ["Agregar campo", "0", "0"],
        ["Reordenar campos", "0", "0"],
        ["Anidar el enlace «links»", "0", "0"],
    ]
    return tab("Ocho cambios del proveedor y cinco consumidores con contratos propios",
               "Tabla de ocho cambios de un proveedor: los contratos dirigidos por los consumidores detectan qué consumidores rompe cada cambio, entre cero y tres, mientras que las pruebas del proveedor sobre su propio esquema no detectan ninguno.",
               ["Cambio del proveedor", "Consumidores rotos (detecta el contrato del consumidor)", "Detecta la prueba propia del proveedor"], rows, [320, 420, 230], row_h=36, size=12,
               note="Cada consumidor fija solo los campos que usa; por eso agregar un campo no rompe a nadie, y por eso un contrato que fijara los seis campos habría rechazado 1 de los 3 cambios inocuos. Un proveedor que genera su esquema desde su código siempre se aprueba a sí mismo.",
               note_kind="gold", foot=SINT)


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
    rows = [
        ["Ninguna estudiante podrá entregar después del cierre, excepto con prórroga aprobada por escrito.", "Completa", "Rechaza", "Falso negativo: «excepto» y «estudiante» no están en la lista"],
        ["El servicio debe responder 429 si una cuenta supera 5 envíos por minuto…", "Completa", "Acepta", "Acierto"],
        ["La plataforma debe ser segura y cumplir la ley.", "Incompleta", "Rechaza", "Acierto: sin observable ni límite"],
        ["El sistema muestra siempre un mensaje de error comprensible y rápido.", "Incompleta", "Rechaza", "Acierto: sin modal «debe»"],
        ["El docente debe corregir cada entrega.", "Incompleta", "Rechaza", "Acierto: sin observable"],
        ["La plataforma debe devolver exactamente 3 campos y rechaza los demás.", "Completa", "Acepta", "Acierto"],
    ]
    return tab("Linter de cláusulas de contrato con seis cláusulas que no vio al escribirse",
               "Tabla de seis cláusulas nuevas: la regla léxica, que acertó 8 de 8 en sus ejemplos de ajuste, acierta 5 de 6 con las nuevas y falla en una cláusula completa redactada con palabras que no estaban en sus listas.",
               ["Cláusula", "Juicio del autor", "Regla", "Lectura"], rows, [430, 130, 100, 280], row_h=58, size=11,
               note="Ajuste: 4 aceptadas y 4 rechazadas correctas (8 de 8). Casos nuevos: 5 de 6. La regla mide forma (actor, modal, observable, límite) y no verdad; una cláusula completa puede ser falsa y una incompleta, intencionalmente abierta.",
               note_kind="gold", foot=SINT)


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
    rows = [
        ["Estrechar el rango de horas", "33", "33"],
        ["Quitar el ejemplo de un código de error", "29", "29"],
        ["Agregar un error sin ejemplo", "27", "27"],
        ["Agregar un invariante sin prueba", "29", "29"],
        ["Cambiar el texto de un invariante", "21", "0"],
        ["Cambiar el mensaje de un error", "38", "0"],
        ["Ensanchar el rango de horas", "33", "0"],
    ]
    return tab("Revisor del propio contrato: 210 mutaciones",
               "Tabla de siete mutaciones de un contrato con ejemplos, errores e invariantes: el revisor detecta las 118 que dejan ejemplos fuera del rango, errores sin ejemplo o invariantes sin prueba, y no detecta las 92 que cambian el sentido sin romper la coherencia interna.",
               ["Mutación del contrato", "Inyectadas", "Detectadas"], rows, [500, 160, 160], row_h=38, size=13,
               note="El revisor garantiza que el contrato sea coherente consigo mismo. Un contrato más permisivo, un mensaje que miente o un invariante con el sentido contrario pasan: esa revisión es de una persona con el dominio.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-168
def se168_trazabilidad() -> Fig:
    rows = [
        ["Enlace a un identificador inexistente", "33", "33"],
        ["Requisito sin contrato (huérfano)", "32", "32"],
        ["Contrato sin ejemplo ni prueba", "34", "34"],
        ["Ciclo entre artefactos", "35", "35"],
        ["Prueba enlazada a una intención (tipo no permitido)", "26", "26"],
        ["Contenido cambiado sin actualizar el rastro", "29", "29"],
        ["Renombrar un identificador sin actualizar enlaces", "27", "27"],
        ["Texto cambiado de sentido, con el rastro intacto", "24", "0"],
    ]
    return tab("Validador de un paquete trazable de 41 artefactos: 240 mutaciones",
               "Tabla de ocho mutaciones de un paquete con intenciones, requisitos, contratos, ejemplos y pruebas: el validador detecta las 216 que rompen enlaces, tipos, ciclos o huellas y ninguna de las 24 que cambian el sentido de un texto.",
               ["Mutación del paquete", "Inyectadas", "Detectadas"], rows, [560, 160, 160], row_h=36, size=13,
               note="La trazabilidad mecánica prueba que los eslabones existen y no se han movido, no que digan lo mismo. Si el texto de un requisito cambia de sentido y su rastro queda intacto, el validador lo da por bueno.",
               note_kind="coral", foot=SINT)


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
    rows = [
        ["Escribir archivos con el modo de texto por defecto", "480485af12cf44f9", "55f841e9f3d4b56f"],
        ["Escribir con newline=\"\\n\" fijo", "55f841e9f3d4b56f", "55f841e9f3d4b56f"],
        ["Alterar 3 bytes de un archivo (comprobación de manipulación)", "Huella cambia", "Huella cambia"],
        ["Calcular la huella de 200 archivos (un equipo)", "0,033 s", "0,004 s"],
    ]
    return tab("Huella de un paquete de 200 archivos en dos sistemas",
               "Tabla: el mismo paquete de 200 documentos produce la huella 480485af12cf44f9 en Windows y 55f841e9f3d4b56f en Ubuntu cuando se escribe con el modo de texto por defecto, y la misma huella en ambos cuando se fija el salto de línea; alterar tres bytes cambia la huella.",
               ["Situación", "Windows", "Ubuntu (WSL2)"], rows, [480, 220, 220], row_h=44, size=13,
               note="Sin fijar el salto de línea, el mismo contenido tiene dos huellas: un manifiesto firmado en un sistema no verifica en el otro. La huella detecta cambios en los bytes, no su autoría ni su sentido. Los tiempos son de un equipo y no son comparables entre sistemas.",
               note_kind="coral", foot="Datos sintéticos; las huellas son deterministas, los tiempos no.")


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
