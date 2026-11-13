"""Figures for SE-157 to SE-162 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3 unless a time is shown)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos, semilla fija; idénticos en Windows y Ubuntu (WSL2), salvo los tiempos indicados."


# ---------------------------------------------------------------- SE-157
def se157_interpretaciones() -> Fig:
    items = [
        ("1 ejemplo típico: 48 h tarde, nota 80", 8, "coral", "8 de 16"),
        ("1 ejemplo al azar (media de 200 semillas)", 3.63, "gold", "3,63"),
        ("2 ejemplos al azar", 1.79, "gold", "1,79"),
        ("3 ejemplos al azar", 1.32, "gold", "1,32"),
        ("6 ejemplos al azar", 1.02, "gold", "1,02"),
        ("1 ejemplo elegido sabiendo las 16 lecturas", 1, "teal", "1"),
    ]
    return bars("Interpretaciones del enunciado informal que sobreviven a k ejemplos",
                "Barras: de 16 lecturas posibles de una regla de penalización por retraso, el ejemplo típico de 48 horas y nota 80 deja vivas 8; uno al azar deja 3,63 en media; seis dejan 1,02; un ejemplo elegido con conocimiento de todas las lecturas deja 1.",
                items, 62, "El ejemplo que cualquiera escribiría primero elimina solo la mitad de las lecturas. Los ejemplos aleatorios convergen despacio; el que discrimina se elige mirando dónde difieren las lecturas, no repitiendo el caso típico.",
                label_w=330, width=1000, note_kind="gold", foot=SINT)


def se157_tabla() -> Fig:
    items = [
        ("Con hueco (algún caso sin regla)", 83, "coral", "83"),
        ("Con solape (dos reglas aplican)", 51, "gold", "51"),
        ("Con hueco y solape a la vez", 32, "coral", "32"),
        ("Sin hueco ni solape (mutante equivalente)", 34, "teal", "34"),
    ]
    return bars("200 mutaciones de una tabla de decisión de 18 combinaciones",
                "Barras: de 200 mutaciones de una tabla de ocho reglas sobre 18 combinaciones, 83 dejan al menos un hueco, 51 un solape, 32 ambos y 34 no cambian el comportamiento.",
                items, 5.4, "Enumerar las 18 combinaciones encuentra todos los huecos y solapes. El coste crece al doble por cada condición binaria: 2^22 = 4 194 304 combinaciones tardaron 0,53 s en Windows y 0,62 s en Ubuntu, y con 40 condiciones la enumeración deja de ser posible.",
                label_w=330, width=1000, note_kind="gold", foot=SINT)


def se157_deteccion() -> Fig:
    items = [
        ("10 casos aleatorios", 32.4, "coral", "32,4 %"),
        ("50 casos aleatorios", 88.6, "gold", "88,6 %"),
        ("100 casos aleatorios", 98.8, "gold", "98,8 %"),
        ("300 casos aleatorios", 100, "teal", "100 %"),
        ("Recorrido exhaustivo (721 casos): falla en el caso 25", 100, "teal", "100 %"),
    ]
    return bars("Probabilidad de encontrar un defecto de frontera (4,16 % de las entradas)",
                "Barras: un defecto en 30 de 721 entradas se detecta con 10 casos aleatorios en 32,4 por ciento de 500 semillas, con 50 en 88,6, con 100 en 98,8 y con 300 en 100; el recorrido exhaustivo lo halla siempre en el caso 25.",
                items, 4.6, "Un dominio acotado y una especificación ejecutable permiten comprobar todo; con dominios grandes solo queda el muestreo, y un defecto que ocupa una fracción pequeña del dominio puede escapar a decenas de casos.",
                label_w=430, width=1100, note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-158
def se158_mutantes() -> Fig:
    items = [
        ("3 ejemplos de camino feliz", 3, "coral", "3 de 9"),
        ("3 ejemplos aleatorios (media de 300)", 6.12, "gold", "6,12"),
        ("6 ejemplos aleatorios (media de 300)", 6.86, "gold", "6,86"),
        ("10 ejemplos aleatorios (media de 300)", 7.15, "gold", "7,15"),
        ("6 ejemplos de frontera", 8, "teal", "8 de 9"),
        ("3 ejemplos de cobertura voraz", 9, "teal", "9 de 9"),
    ]
    return bars("Mutantes de la regla de penalización que cada suite de ejemplos mata",
                "Barras: de once mutantes, dos equivalentes y nueve distinguibles; tres ejemplos de camino feliz matan 3, diez aleatorios en media 7,15, seis ejemplos de frontera 8 y tres ejemplos elegidos por cobertura voraz los 9.",
                items, 55, "El número de ejemplos importa menos que su ubicación: tres ejemplos elegidos para separar mutantes superan a diez al azar. Los dos mutantes equivalentes no mueren con ningún ejemplo: no son defectos.",
                label_w=330, width=980, note_kind="gold", foot=SINT)


def se158_gherkin() -> Fig:
    rows = [
        ["1", "plazo 24 h · entrega con 30 h · nota 90", "El paso 2 encaja con dos patrones", "Ambiguo: el ejecutor no sabe cuál usar"],
        ["2", "entrega con 0 h de retraso · nota 100", "El paso 2 encaja con dos patrones", "Ambiguo, igual que el anterior"],
        ["3", "«envía con 30 h de retraso»", "Ningún patrón reconoce «envía»", "Indefinido por un cambio de redacción"],
        ["4", "paso 2 ambiguo y «se muestra una alerta»", "Un paso con dos patrones y otro sin ninguno", "Ambiguo e indefinido: no comprueba nada"],
    ]
    return tab("Mini ejecutor de Gherkin: pasos indefinidos, ambiguos y definiciones sin uso",
               "Tabla de cuatro escenarios con doce pasos contra cinco definiciones: dos pasos indefinidos, tres ambiguos y una definición sin uso, lo que muestra qué errores de redacción detecta un ejecutor antes de probar el producto.",
               ["N.º", "Pasos del escenario", "Resultado del emparejamiento", "Lectura"], rows, [60, 330, 330, 290], row_h=58, size=12,
               note="En total: 12 pasos, 2 indefinidos, 3 ambiguos (la definición «la estudiante entrega (.+)» solapa con la específica) y 1 de 5 definiciones sin uso. El ejecutor detecta forma, no significado.",
               note_kind="gold", foot=SINT)


def se158_pares() -> Fig:
    items = [
        ("Producto completo de 4 factores", 81, "grey", "81 filas"),
        ("Suite de todos los pares", 9, "teal", "9 filas"),
        ("Fallos de 2 factores: matados por los pares", 246, "teal", "246 de 246"),
        ("Fallos de 3 factores: matados por los pares", 92, "coral", "92 de 300"),
        ("Fallos de 3 factores: 9 filas al azar", 87, "gold", "87 de 300"),
    ]
    return bars("Tabla de ejemplos: producto completo frente a cobertura de pares",
                "Barras: cuatro factores de tres valores dan 81 filas; una suite de todos los pares tiene 9 y mata los 246 fallos de dos factores, pero solo 92 de 300 fallos de tres factores, apenas más que 87 con nueve filas al azar.",
                items, 2.0, "Cubrir todos los pares es un acuerdo económico: reduce 81 filas a 9 y es exacto para interacciones de dos factores. No protege contra interacciones de tres: ahí 9 filas bien elegidas rinden casi como 9 al azar.",
                label_w=380, width=1040, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-159
def se159_contratos() -> Fig:
    rows = [
        ["1", "Nota sin acotar", "No", "117 de 200"],
        ["2", "Salta a «publicada» al calificar", "No", "200 de 200"],
        ["3", "Nota sin cota inferior", "No", "62 de 200"],
        ["4", "Estado redundante", "No (equivalente)", "0 de 200"],
        ["5", "Prórroga duplicada, tope intacto", "No", "0 de 200"],
        ["6, 7", "Prórroga sin tope", "No", "198 de 200"],
        ["8", "Publicar conserva la nota (equivalente)", "No (equivalente)", "0 de 200"],
        ["9", "Publicar borra la nota", "No", "200 de 200"],
    ]
    return tab("Nueve mutantes de una clase con contratos: pruebas de ejemplo frente a contratos",
               "Tabla de nueve mutantes de una clase de calificación: cinco pruebas de ejemplo no matan ninguno; los contratos con un conductor aleatorio de 200 ejecuciones saltan en cinco familias de defecto y no detectan el mutante 5, donde la prórroga queda duplicada pero dentro del tope.",
               ["Mutante", "Defecto", "Cinco pruebas de ejemplo", "Ejecuciones en que salta un contrato"], rows, [110, 380, 250, 270], row_h=34, size=12,
               note="Los contratos detectan lo que afirman: nota acotada, estado válido, prórroga ≤ 72. El mutante 5 duplica la prórroga sin pasar el tope y nadie declaró cuánto debía valer: lo no escrito no se comprueba. Sobrecoste de comprobar: 1,44 veces en Windows y 1,47 en Ubuntu (100 000 llamadas).",
               note_kind="gold", foot=SINT)


def se159_subtipos() -> Fig:
    items = [
        ("Llamadas válidas para la clase base", 5224, "grey", "5 224"),
        ("Rechazadas si el subtipo refuerza la precondición", 1777, "coral", "1 777 (34,0 %)"),
        ("Rechazadas si el subtipo debilita la precondición", 0, "teal", "0"),
        ("Resultados negativos si el subtipo debilita la postcondición", 913, "coral", "913 de 10 000"),
    ]
    return bars("Subtipado conductual: qué rompe un cliente que usa la clase base",
                "Barras: de 10 000 entradas aleatorias, 5 224 son válidas para la base; un subtipo que exige más las rechaza 1 777 veces, uno que acepta más ninguna, y uno que garantiza menos devuelve 913 resultados negativos que el cliente no espera.",
                items, 0.09, "Reforzar la precondición o debilitar la postcondición viola lo que el cliente de la base daba por seguro; aceptar más o garantizar más no lo viola. La regla vale para las promesas escritas: si el contrato no dice nada, el cliente dependerá de lo que observó.",
                label_w=470, width=1130, note_kind="coral", foot=SINT)


def se159_distancia() -> Fig:
    items = [
        ("Comprobar el invariante tras cada operación", 0, "teal", "0 de 1 000 sin detectar"),
        ("Comprobar cada 20 operaciones", 356, "gold", "356 sin detectar"),
        ("Comprobar solo al final de 200 operaciones", 997, "coral", "997 sin detectar"),
    ]
    return bars("Invariante violado y reparado en silencio: cuántas veces se escapa",
                "Barras: en 1 000 corridas de 200 operaciones con un defecto introducido entre la operación 20 y la 120 y una operación que repara el estado con 5 por ciento de probabilidad, comprobar tras cada operación no pierde ninguna, cada 20 pierde 356 y solo al final pierde 997.",
                items, 0.45, "Comprobar más cerca del cambio localiza (distancia media 0 frente a 8,0 operaciones) y evita que el estado se repare solo antes del examen. Las cifras dependen de la probabilidad de reparación (5 %), que es un supuesto del autor.",
                label_w=400, width=1060, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-160
def se160_defectos() -> Fig:
    rows = [
        ["Referencia a una entidad inexistente", "53", "53", "Estructural"],
        ["Herencia circular", "50", "50", "Estructural"],
        ["Campo duplicado", "46", "46", "Estructural"],
        ["Entidad sin identificador", "48", "48", "Estructural"],
        ["Cardinalidad cambiada (1 pasa a 0..*)", "49", "0", "Semántico"],
        ["Relación invertida (Tarea↔Curso)", "54", "0", "Semántico"],
    ]
    return tab("Comprobador de un modelo de ocho entidades: qué defectos ve",
               "Tabla de 300 mutaciones de un modelo estructural: el comprobador detecta las 197 mutaciones de referencias, herencia, duplicados e identificadores y ninguna de las 103 que cambian la cardinalidad o invierten una relación.",
               ["Defecto inyectado", "Inyectados", "Detectados", "Tipo"], rows, [450, 150, 150, 200], row_h=40, size=13,
               note="Un modelo puede ser estructuralmente perfecto y falso: la regla «una tarea pertenece a un curso» sobrevive a un cambio a «0..*» porque ambas versiones son consistentes. La semántica la revisa una persona con el dominio.",
               note_kind="coral", foot=SINT)


def se160_deriva() -> Fig:
    rows = [
        ["Renombrar un campo", "40", "40", "40"],
        ["Borrar un campo", "49", "49", "49"],
        ["Agregar un campo", "44", "44", "44"],
        ["Renombrar una clase", "62", "62", "62"],
        ["Cambiar el tipo de un campo", "55", "0", "55"],
    ]
    return tab("Deriva entre el modelo y el código leída con ast: nombres frente a nombres y tipos",
               "Tabla de 250 mutaciones del código fuente de seis clases: comparar solo nombres detecta renombrados, borrados y agregados pero ninguno de los 55 cambios de tipo; comparar nombres y anotaciones de tipo los detecta todos.",
               ["Mutación del código", "Aplicadas", "Detecta solo nombres", "Detecta nombres y tipos"], rows, [330, 140, 220, 260], row_h=42, size=13,
               note="Comparar más propiedades detecta más deriva; ninguna comparación estática ve que un campo conserva nombre y tipo pero cambió de significado (por ejemplo, horas por minutos).",
               note_kind="gold", foot=SINT)


def se160_normalizacion() -> Fig:
    rows = [
        ["Tamaño del archivo (5 000 entregas, 50 cursos)", "245 760 bytes", "73 728 bytes"],
        ["Filas que toca el cambio de nombre de un curso", "54 de 109 (interrumpido)", "1"],
        ["Nombres distintos para el curso 7 tras interrumpir", "2", "0"],
    ]
    return tab("SQLite 3.45: la misma información desnormalizada y normalizada",
               "Tabla comparativa con SQLite: con el nombre del curso repetido en cada entrega el archivo pesa 245 760 bytes y una actualización interrumpida deja dos nombres para el mismo curso; normalizado pesa 73 728 bytes y cambiar el nombre toca una sola fila.",
               ["Medida", "Desnormalizado", "Normalizado"], rows, [440, 270, 220], row_h=44, size=13,
               note="La normalización elimina una clase de inconsistencia a cambio de uniones al leer. Los tamaños son de este generador sintético (SQLite 3.45.3 en Windows y 3.45.1 en Ubuntu, mismas cifras) y no se extrapolan a un sistema real.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-161
def se161_contraejemplo() -> Fig:
    f = Fig(1000, 330, "Contraejemplo mínimo hallado por búsqueda en anchura",
            "Diagrama de una traza de cuatro pasos: pendiente, enviada, calificada, publicada y, tras apelar, enviada con la nota todavía puesta, lo que viola el invariante de que una entrega enviada no tiene nota.")
    xs = [20, 215, 410, 605]
    names = [("pendiente", "sin nota", "grey"), ("enviada", "sin nota", "teal"), ("calificada", "con nota", "teal"), ("publicada", "con nota", "teal")]
    for x, (n, s, k) in zip(xs, names):
        f.box(x, 40, 170, 70, f"{n}\n{s}", k, 15, bold=True)
    for x, a in zip(xs[:-1], ["enviar", "calificar", "publicar"]):
        f.arrow([(x + 170, 75), (x + 195, 75)], a, label_at=(x + 182, 28))
    f.box(800, 40, 180, 70, "enviada\nCON nota", "coral", 15, bold=True)
    f.arrow([(775, 75), (800, 75)], "apelar", color="#c0432f", label_at=(787, 28))
    f.box(20, 150, 960, 56, "Invariante: si hay nota, el estado es «calificada» o «publicada». La búsqueda en anchura devuelve la traza más corta que lo viola: enviar → calificar → publicar → apelar (4 pasos, 6 estados explorados).", "coral", 14)
    f.box(20, 220, 960, 56, "La máquina correcta tiene 13 estados alcanzables y ninguna violación. El defecto es una sola transición (la apelación vuelve a «enviada» sin borrar la nota).", "gold", 14)
    f.text(500, 312, SINT, 12, "middle", 400, "#5c1f14")
    return f


def se161_explosion() -> Fig:
    items = [
        ("N = 4 estudiantes, sin simetría", 144, "gold", "144"),
        ("N = 4, con simetría", 24, "teal", "24"),
        ("N = 8, sin simetría", 6144, "coral", "6 144"),
        ("N = 8, con simetría", 48, "teal", "48"),
        ("N = 11, sin simetría", 82944, "coral", "82 944 (0,34 s)"),
        ("N = 11, con simetría", 66, "teal", "66"),
    ]
    return bars("Estados alcanzables con N estudiantes que envían a la vez",
                "Barras: con cuatro estudiantes hay 144 estados sin simetría y 24 con simetría; con ocho 6 144 y 48; con once 82 944, que tardan 0,34 s, y 66; el crecimiento es exponencial sin simetría y lineal con ella.",
                items, 0.0058, "Cada estudiante adicional multiplica los estados por 2,4 aproximadamente; tratar a los estudiantes como intercambiables (ordenar el estado) los reduce a 6N. La reducción solo es válida si de verdad lo son: una cola con prioridad distinta por persona la destruiría.",
                label_w=300, width=980, note_kind="gold", foot=SINT)


def se161_carrera() -> Fig:
    items = [
        ("2 revisoras", 66.7, "gold", "66,7 % (4 de 6)"),
        ("3 revisoras", 93.3, "gold", "93,3 % (84 de 90)"),
        ("4 revisoras", 99.0, "coral", "99,0 % (2 496 de 2 520)"),
        ("5 revisoras", 99.9, "coral", "99,9 % (113 280 de 113 400)"),
        ("Hilos reales de CPython, 10 × 400 000 sumas", 0, "teal", "0 pérdidas observadas"),
    ]
    return bars("Intercalados con actualización perdida (cada revisora lee y luego escribe)",
                "Barras: con dos revisoras 4 de 6 ordenaciones pierden una actualización, con cuatro 2 496 de 2 520; el mismo defecto no apareció en diez ejecuciones con hilos reales de CPython que sumaron 400 000 veces.",
                items, 4.0, "Casi todos los órdenes posibles son defectuosos, pero el planificador del sistema operativo con el intérprete casi nunca los produce: la prueba natural dice «nada» mientras la exploración sistemática dice «casi siempre». Las pérdidas con hilos reales dependen de la versión y la carga y no son reproducibles.",
                label_w=400, width=1060, note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-162
def se162_semantica() -> Fig:
    items = [
        ("Documentos válidos según el esquema", 5000, "teal", "5 000 de 5 000"),
        ("Con fin anterior a inicio (regla entre campos)", 2410, "coral", "2 410 (48,2 %)"),
    ]
    return bars("Lo que un esquema acepta y la regla de negocio rechaza",
                "Barras: de 5 000 documentos generados que cumplen el esquema, 2 410 tienen una fecha de fin anterior a la de inicio, una regla entre campos que el esquema de tipos y formatos no expresa.",
                items, 0.1, "Un validador ingenuo aceptó además nota=true como entero porque en Python bool es subclase de int; con la exclusión explícita lo rechazó. La nota 100.0 (flotante) y '100' (texto) se rechazaron. Validar forma no garantiza sentido: la regla entre campos exige código aparte.",
                label_w=400, width=1030, note_kind="coral", foot=SINT)


def se162_abierto_cerrado() -> Fig:
    rows = [
        ["Campo requerido mal escrito (1 000 documentos)", "1 000", "1 000"],
        ["Campo opcional mal escrito: «comentaro»", "0", "1 000"],
        ["Campo nuevo legítimo «prioridad» (1 000 documentos)", "0 rechazados", "1 000 rechazados"],
    ]
    return tab("Esquema abierto frente a cerrado: qué errores atrapa y qué cambios rechaza",
               "Tabla con mil documentos: ambos esquemas detectan un campo requerido mal escrito; solo el cerrado detecta un campo opcional mal escrito, y el cerrado rechaza también un campo nuevo legítimo que el abierto acepta.",
               ["Situación", "Esquema abierto", "Esquema cerrado"], rows, [480, 220, 220], row_h=44, size=13,
               note="El esquema abierto deja pasar el error de escritura y descarta el comentario sin avisar; el cerrado lo atrapa pero convierte cada campo nuevo del productor en un cambio incompatible. Elegir uno es decidir cómo evoluciona el contrato.",
               note_kind="gold", foot=SINT)


def se162_regex() -> Fig:
    items = [
        ("Patrón con retroceso, 17 caracteres", 0.0063, "teal", "0,0063 s"),
        ("19 caracteres", 0.0256, "gold", "0,026 s"),
        ("21 caracteres", 0.1103, "gold", "0,11 s"),
        ("23 caracteres", 0.4106, "coral", "0,41 s"),
        ("25 caracteres", 1.6472, "coral", "1,65 s"),
        ("Patrón lineal, 5 001 caracteres", 0.00007, "teal", "0,00007 s"),
    ]
    return bars("Tiempo de una expresión regular con retroceso sobre una entrada casi válida (Windows)",
                "Barras: el patrón (\\w+\\s?)* con una entrada de letras seguida de un signo tarda 0,0063 s con 17 caracteres y 1,65 s con 25, cuadruplicando cada dos caracteres; un patrón lineal tarda 0,00007 s con 5 001 caracteres.",
                items, 280, "Cada carácter extra duplica el tiempo. En Ubuntu la serie fue 0,0074 / 0,028 / 0,090 / 0,36 / 1,46 s: mismo crecimiento, distinto equipo. Comprobar la longitud máxima antes del patrón (1 µs con maxLength 20) y escribir patrones lineales evita el problema.",
                label_w=420, width=1020, note_kind="coral", foot="Datos sintéticos; tiempos medidos en un equipo con CPython 3.12.9 (Windows); la forma del crecimiento se repite en Ubuntu.")


FIGURES = {
    "se-157-interpretaciones-que-sobreviven.svg": se157_interpretaciones,
    "se-157-mutaciones-de-una-tabla-de-decision.svg": se157_tabla,
    "se-157-aleatorio-frente-a-exhaustivo.svg": se157_deteccion,
    "se-158-mutantes-segun-la-suite.svg": se158_mutantes,
    "se-158-pasos-indefinidos-y-ambiguos.svg": se158_gherkin,
    "se-158-producto-completo-frente-a-pares.svg": se158_pares,
    "se-159-pruebas-de-ejemplo-frente-a-contratos.svg": se159_contratos,
    "se-159-subtipado-conductual.svg": se159_subtipos,
    "se-159-cuando-comprobar-el-invariante.svg": se159_distancia,
    "se-160-defectos-que-ve-el-comprobador.svg": se160_defectos,
    "se-160-deriva-modelo-codigo.svg": se160_deriva,
    "se-160-normalizacion-en-sqlite.svg": se160_normalizacion,
    "se-161-contraejemplo-minimo.svg": se161_contraejemplo,
    "se-161-explosion-de-estados.svg": se161_explosion,
    "se-161-actualizacion-perdida.svg": se161_carrera,
    "se-162-esquema-valido-no-implica-correcto.svg": se162_semantica,
    "se-162-esquema-abierto-o-cerrado.svg": se162_abierto_cerrado,
    "se-162-expresion-regular-con-retroceso.svg": se162_regex,
}
