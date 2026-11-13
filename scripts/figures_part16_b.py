"""Figures for SE-199 to SE-204 (Git real en repositorios temporales o datos sintéticos con semilla fija; resultados idénticos en Windows y Ubuntu salvo los tiempos)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

GIT = "Git real en repositorios temporales con identidad y fechas fijas; salidas idénticas con Git 2.55 (Windows) y 2.43 (Ubuntu, WSL2)."
SINT = "Datos sintéticos, semilla fija; idénticos en Windows y Ubuntu (WSL2). Los parámetros son supuestos del autor."


# ---------------------------------------------------------------- SE-199
def se199_codeowners() -> Fig:
    rows = [
        ["Rutas evaluadas / reglas", "600 / 24", "Rutas y reglas sintéticas del autor"],
        ["Rutas sin propietario", "0", "La regla «*» del principio cubre todo"],
        ["Rutas sin propietario si se quita «*»", "31", "Archivos de informes y carpetas sin regla propia"],
        ["Reglas que nunca ganan", "1 de 24", "«/CODEOWNERS»: ninguna ruta de la muestra la usa"],
        ["Rutas que cambian de propietario al invertir el orden", "520 de 600", "El último patrón que coincide gana, así que el orden es la semántica"],
        ["Carga del equipo más cargado / del menos cargado", "108 / 25", "108 de 600 rutas recaen en un solo equipo"],
    ]
    return tab("Un CODEOWNERS sintético evaluado sobre 600 rutas",
               "Tabla con las métricas de un archivo de propietarios de 24 reglas evaluado sobre 600 rutas: rutas sin propietario, reglas que nunca ganan, efecto de invertir el orden y carga por equipo.",
               ["Medida", "Valor", "Lectura"], rows, [380, 150, 450], row_h=46, size=12,
               note="El modelo de coincidencia es una simplificación de lo que describe la documentación, no el motor de una plataforma. Sirve para auditar reglas, no para sustituir la comprobación en el alojamiento real.",
               note_kind="gold", foot=SINT)


def se199_mensajes() -> Fig:
    items = [
        ("Sin tipo (53 de 400)", 53, "coral", "53"),
        ("Tipo inventado, «mejora:» (24)", 24, "coral", "24"),
        ("Tipo en mayúscula (23)", 23, "gold", "23"),
        ("Sin espacio tras los dos puntos (23)", 23, "gold", "23"),
        ("Alcance con espacio (18)", 18, "gold", "18"),
        ("Rompedores con «!» o con pie BREAKING CHANGE (54)", 0, "teal", "0 rechazados"),
    ]
    return bars("Mensajes que rechaza un validador de commits convencionales (400 sintéticos)",
                "Barras: de 400 mensajes sintéticos el validador rechaza 53 sin tipo, 24 con tipo inventado, 23 en mayúscula, 23 sin espacio y 18 con alcance con espacio, y acepta los 54 cambios rompedores bien formados.",
                items, 15, "Una herramienta que solo lee el «!» detecta 16 de los 54 cambios rompedores; una que solo lee el pie, 38; leer ambos detecta 54. El validador comprueba la forma: no sabe si un cambio sin «!» rompía a alguien.",
                label_w=440, width=1040, note_kind="gold", foot=SINT)


def se199_blame() -> Fig:
    rows = [
        ["git blame sin ignorar", "120", "30", "150", "El bot que reformateó figura como autor de 150 líneas"],
        ["git blame --ignore-rev del reformateo", "270", "30", "0", "Cada línea vuelve a su autoría real"],
        ["git blame --ignore-revs-file", "270", "30", "0", "Mismo resultado con un archivo versionado"],
    ]
    return tab("Autoría de 300 líneas tras un commit que solo cambia la sangría de 150",
               "Tabla de líneas atribuidas a la autora, a otra persona y a un bot según se ignore o no el commit de reformateo.",
               ["Comando", "Autora", "Otra persona", "Bot", "Lectura"], rows, [310, 90, 120, 70, 380], row_h=58, size=12,
               note="Ignorar el reformateo recupera la autoría solo porque cada línea cambió de forma pero no de sentido. Un commit que mezcla reformateo y lógica no puede ignorarse sin ocultar la lógica.",
               note_kind="teal", foot=GIT)


# ---------------------------------------------------------------- SE-200
def se200_concentracion() -> Fig:
    rows = [
        ["0,5 (reparto casi uniforme)", "9,1", "2,6 %"],
        ["1,0", "4,1", "7,6 %"],
        ["1,5", "2,0", "17,1 %"],
        ["2,0 (muy concentrado)", "1,0", "31,6 %"],
    ]
    return tab("Concentración de commits entre 30 contribuyentes sintéticos (400 commits, 300 archivos)",
               "Tabla con cuatro exponentes de concentración: cuántos autores cubren la mitad de los commits y qué porcentaje de archivos solo tocó la persona más activa.",
               ["Exponente de la distribución", "Autores que cubren el 50 % de los commits", "Archivos que solo tocó la persona más activa"], rows, [320, 330, 330], row_h=46, size=12,
               note="Con un exponente de 2 una sola persona produce la mitad de los commits y 3 de cada 10 archivos pierden a la única persona que los conocía si se va. Los exponentes son supuestos; sirven para ver la sensibilidad, no para describir un proyecto real.",
               note_kind="coral", foot=SINT)


def se200_decision() -> Fig:
    rows = [
        ["Consenso perezoso (72 h sin objeción)", "40,5 %", "12,3 %", "0 %"],
        ["Mayoría de 3 de 5", "1,0 %", "3,1 %", "83,5 %"],
        ["Unanimidad de quienes votan, mínimo 3", "0,5 %", "4,1 %", "83,5 %"],
    ]
    return tab("Reglas de decisión cuando solo el 30 % de las personas mantenedoras lee la propuesta",
               "Tabla de tres reglas de decisión con 30 por ciento de disponibilidad: propuestas dañinas aceptadas, propuestas buenas rechazadas y propuestas sin decisión.",
               ["Regla", "Dañinas aceptadas", "Buenas rechazadas", "Sin decisión"], rows, [400, 190, 190, 190], row_h=46, size=12,
               note="Con 90 % de disponibilidad el consenso perezoso acepta 2,6 % de las dañinas pero rechaza 30,3 % de las buenas, y la mayoría de 3 de 5 acepta 29,7 % de las dañinas. Ninguna regla es mejor en general: cada una cambia qué error se tolera.",
               note_kind="gold", foot=SINT)


def se200_fork() -> Fig:
    items = [
        ("5 commits nuevos en el original", 33, "gold", "2 de 6"),
        ("20 commits nuevos", 67, "coral", "4 de 6"),
        ("60 commits nuevos", 100, "coral", "6 de 6"),
    ]
    return bars("Rebase con conflicto de una contribución de 3 líneas tras quedarse atrás",
                "Barras: una contribución de tres líneas en un archivo de 50 líneas entra en conflicto al rebasar en 2 de 6 casos si el original avanzó 5 commits, 4 de 6 si avanzó 20 y 6 de 6 si avanzó 60.",
                items, 8.5, "El número de commits por detrás coincidió en las seis semillas con los commits del original: rev-list lo mide sin ambigüedad. Cuanto más tiempo pasa sin sincronizar, más cuesta enviar el cambio.",
                label_w=360, width=1000, note_kind="gold", foot=GIT)


# ---------------------------------------------------------------- SE-201
def se201_expresiones() -> Fig:
    rows = [
        ["Disyunción «A OR B»", "39", "39", "0", "0"],
        ["Conjunción «A AND B»", "50", "28", "0", "0"],
        ["Con paréntesis", "15", "15", "0", "0"],
        ["Minúsculas («mit»)", "26", "26", "0", "26"],
        ["Barra («MIT/Apache-2.0»)", "18", "18", "0", "18"],
        ["Identificador obsoleto («GPL-3.0»)", "16", "0", "0", "16"],
        ["Remisión a un archivo", "22", "0", "0", "22"],
    ]
    return tab("Política de licencias sobre 300 expresiones: comparación literal frente a analizador",
               "Tabla de siete tipos de expresión con cuántas decisiones erróneas toma la comparación literal, cuántas toma el analizador sin avisar y cuántas veces el analizador emite un aviso.",
               ["Tipo de expresión", "Casos", "Literal se equivoca", "Analizador se equivoca sin avisar", "Avisos del analizador"], rows, [310, 90, 170, 220, 190], row_h=40, size=12,
               note="De 300 expresiones la comparación literal decide mal 146; el analizador, ninguna sin avisar. Lo que no entiende («mit», «MIT/Apache-2.0», identificadores obsoletos) lo marca para revisión humana en lugar de decidir.",
               note_kind="teal", foot=SINT)


def se201_transitivas() -> Fig:
    items = [
        ("Paquetes directos", 60, "grey", "60"),
        ("Paquetes en total (media de 20 grafos)", 514, "grey", "514"),
        ("Fuera de política entre los directos", 6.8, "gold", "6,8"),
        ("Fuera de política en todo el grafo", 60.5, "coral", "60,5"),
    ]
    return bars("Licencias fuera de política que ve un análisis solo de directos frente a uno transitivo",
                "Barras: con 60 dependencias directas que arrastran unos 514 paquetes, un análisis solo de directos halla 6,8 paquetes fuera de política y uno transitivo halla 60,5, un 89 por ciento que no habría visto.",
                items, 1.55, "El 89 % que un análisis de directos no ve sale de una mezcla del autor (80 % permisivas, 6 % de copyleft fuerte, 6 % sin declarar); lo robusto es la forma: la mayoría de los paquetes está en la transitividad.",
                label_w=420, width=1040, note_kind="coral", foot=SINT)


def se201_huella() -> Fig:
    rows = [
        ["Otro año y otro titular", "Igual", "1,000"],
        ["Saltos de línea y espacios distintos", "Igual", "1,000"],
        ["Se elimina la cláusula del aviso", "Distinta", "0,486"],
        ["«AS IS» sustituido por otro texto", "Distinta", "0,971"],
        ["Texto de otra licencia", "Distinta", "0,024"],
    ]
    return tab("Huella del texto de licencia normalizado frente a una razón de similitud",
               "Tabla de cinco variantes del texto de la licencia MIT con si la huella del texto normalizado coincide y qué razón de similitud devuelve difflib.",
               ["Variante", "Huella del texto normalizado", "Razón de difflib"], rows, [450, 280, 220], row_h=44, size=12,
               note="Una razón de 0,971 puede esconder el cambio que elimina la garantía. La huella exacta detecta cualquier diferencia pero no dice cuál; la similitud dice cuánto, no si importa. En 400 archivos sintéticos, 14 etiquetas SPDX (GPL-3.0-only) contradecían el LICENSE (MIT) y 165 archivos no tenían etiqueta.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-202
def se202_firmas() -> Fig:
    rows = [
        ["60 commits firmados con una clave SSH desechable", "60 de 60 verifican", "Cada firma cubre el contenido exacto del commit"],
        ["Copia del commit con el mensaje cambiado y la misma firma", "Código 1", "La firma ya no corresponde al contenido"],
        ["Firma válida con otro archivo de firmantes", "Código 1", "El firmante no figura: válida no significa de confianza"],
    ]
    return tab("Verificar commits firmados con SSH",
               "Tabla de tres comprobaciones de firma con el resultado de git verify-commit: 60 firmados que verifican, una copia con mensaje alterado que falla y una firma válida de un firmante no listado que falla.",
               ["Caso", "Resultado", "Lectura"], rows, [380, 180, 420], row_h=58, size=12,
               note="La firma vive en una cabecera del propio objeto. Firmar añadió unos 92 ms por commit en Windows y 7 ms en Ubuntu, y verificar costó 15 ms por commit en Ubuntu y 234 ms en Windows (60 repeticiones, medidas de un equipo): no se comparan entre sistemas.",
               note_kind="teal", foot=GIT)


def se202_cadena() -> Fig:
    items = [
        ("Commits cuyo identificador cambia al reescribir el 11.º", 40, "coral", "40 de 50"),
        ("Firmas válidas antes de reescribir", 50, "teal", "50"),
        ("Firmas válidas después, sin volver a firmar", 10, "coral", "10"),
    ]
    return bars("Reescribir el mensaje de un commit antiguo en una cadena de 50 firmados",
                "Barras: al cambiar el mensaje del undécimo commit de una cadena de 50 firmados cambia el identificador de 40 y solo 10 firmas siguen siendo válidas; el tip viejo deja de ser ancestro del nuevo.",
                items, 15, "Cada commit incluye el identificador de su padre, así que cualquier reescritura cambia a todos los descendientes y rompe sus firmas. Quien tenga el tip viejo detecta que el nuevo no desciende de él.",
                label_w=470, width=1080, note_kind="coral", foot=GIT)


def se202_politicas() -> Fig:
    items = [
        ("Sin protección", 387, "coral", "387"),
        ("Exigir PR", 255, "coral", "255"),
        ("PR + 1 aprobación", 105, "gold", "105"),
        ("+ comprobaciones superadas", 79, "gold", "79"),
        ("+ commits firmados", 1, "teal", "1"),
        ("+ sin push forzado", 0, "teal", "0"),
    ]
    return bars("Eventos problemáticos que dejan pasar seis políticas (de 500 eventos sintéticos)",
                "Barras: de 500 eventos sintéticos, 387 tienen algún problema; sin protección pasan los 387, con PR 255, con una aprobación 105, con comprobaciones 79, con firmas 1 y sin push forzado 0.",
                items, 1.45, "Cada control cierra una clase de problema y el último deja 0 por construcción del experimento: los problemas se definieron con estos controles. Lo informativo es el orden de reducción y los 37 eventos de administradores que un bypass deja pasar.",
                label_w=340, width=1000, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-203
def se203_estrategia() -> Fig:
    items = [
        ("Resolver siempre con «ours»", 3, "gold", "3 de 6"),
        ("Resolver siempre con «theirs»", 3, "gold", "3 de 6"),
        ("Unir ambos lados (--union)", 0, "coral", "0 de 6"),
        ("Resolución manual correcta", 6, "teal", "6 de 6"),
    ]
    return bars("Órdenes de fusión de tres ramas cuyas pruebas quedan verdes según la estrategia",
                "Barras: al fusionar las seis permutaciones de tres ramas, resolver siempre con ours o con theirs deja las pruebas verdes en 3 órdenes, unir ambos lados en 0 y la resolución manual correcta en 6.",
                items, 90, "Una estrategia automática acierta o falla según el orden: no es una política. Unir ambos lados no dejó ningún orden en verde. En los seis órdenes hubo un solo archivo en conflicto, pero la resolución correcta combinaba las tres intenciones.",
                label_w=360, width=1000, note_kind="gold", foot=GIT)


def se203_rescate() -> Fig:
    rows = [
        ["(a) Sin publicar: reset al primer padre y fusionar de nuevo", "Pruebas verdes", "Se reescribe un commit que nadie tiene"],
        ["(b) Publicada: nuevo commit que restaura lo perdido", "Pruebas verdes", "El commit malo sigue en la historia"],
        ["(c) revert -m 1 y volver a fusionar", "Pruebas rojas", "Git responde «Already up to date»: la rama figura integrada"],
    ]
    return tab("Rescatar una fusión que se resolvió con «ours» y perdió el periodo de gracia",
               "Tabla de tres rescates de una fusión mal resuelta: reiniciar y repetir si no se publicó, un commit de corrección si se publicó, y revertir la fusión, que deja las pruebas en rojo.",
               ["Camino", "Resultado", "Lectura"], rows, [420, 170, 390], row_h=58, size=12,
               note="Tras la fusión mala la rama figuraba como ancestro, así que fusionarla otra vez no hace nada. El revert devuelve el árbol al primer padre pero no devuelve la intención perdida.",
               note_kind="coral", foot=GIT)


def se203_marcas() -> Fig:
    rows = [
        ["merge (predeterminado)", "3", "No", "Dos versiones y nada más"],
        ["diff3", "4", "Sí", "Añade el original común"],
        ["zdiff3", "4", "Sí", "Igual que diff3 con menos contexto repetido"],
        ["merge --abort a mitad de un conflicto", "—", "—", "HEAD, índice y estado limpio vuelven a ser idénticos"],
    ]
    return tab("Marcas de conflicto según el estilo y vuelta atrás con --abort",
               "Tabla de tres estilos de marcas de conflicto con sus líneas de marca y si muestran la base, más el resultado de abortar una fusión a medias.",
               ["Estilo", "Líneas de marca", "¿Muestra la base?", "Lectura"], rows, [300, 150, 190, 340], row_h=46, size=12,
               note="Ver el original común permite decidir qué lado cambió qué. Con el estilo por defecto solo se ve el resultado de cada lado y es fácil elegir uno sin entender el otro.",
               note_kind="teal", foot=GIT)


# ---------------------------------------------------------------- SE-204
def se204_matriz() -> Fig:
    rows = [
        ["Contribución correcta", "Ninguna"],
        ["Mensaje sin tipo", "1 mensaje convencional"],
        ["Un commit gigante que mezcla", "2 commits atómicos"],
        ["Commit intermedio roto", "3 cada commit pasa las pruebas"],
        ["Prueba que falla en la punta", "3 y 4"],
        ["Archivo nuevo sin cabecera SPDX", "5 cabecera SPDX"],
        ["Descripción sin issue", "6 issue enlazado"],
        ["Secreto sintético en el diff", "7 sin secreto"],
        ["Commits sin firmar", "8 firmados"],
        ["Sin Signed-off-by", "9 Signed-off-by"],
        ["PR de más de 400 líneas", "2 y 10"],
        ["Toca src/auth sin pedir al equipo dueño", "11 revisores del CODEOWNERS"],
        ["Cambia el tope sin tocar pruebas", "12 si cambia src, cambia una prueba"],
        ["Prueba que no comprueba nada", "Ninguna"],
    ]
    return tab("Qué comprobación detecta cada defecto plantado en una contribución",
               "Tabla de catorce contribuciones, una correcta y trece con un defecto plantado, con las comprobaciones que fallan en cada una; la prueba que no comprueba nada no dispara ninguna.",
               ["Contribución", "Comprobaciones que fallan"], rows, [420, 440], row_h=34, size=12,
               note="12 de 13 defectos tocan alguna comprobación y la contribución correcta no dispara ninguna alarma falsa. El que escapa pasa todas las comprobaciones de forma: cambia una prueba por una afirmación vacía.",
               note_kind="gold", foot=GIT)


def se204_solapes() -> Fig:
    items = [
        ("Contribución correcta", 0, "teal", "0"),
        ("Diez defectos con una sola comprobación", 1, "gold", "1 cada uno"),
        ("Prueba que falla en la punta", 2, "coral", "2"),
        ("PR de más de 400 líneas", 2, "coral", "2"),
        ("Prueba que no comprueba nada", 0, "coral", "0 (escapa)"),
    ]
    return bars("Comprobaciones disparadas por cada defecto plantado",
                "Barras: la contribución correcta no dispara ninguna comprobación, once defectos disparan una cada uno, dos defectos disparan dos y la prueba que no comprueba nada no dispara ninguna.",
                items, 190, "Un defecto con dos comprobaciones no es redundancia sino dos síntomas de una causa: un PR enorme viene casi siempre con un commit enorme. El defecto con cero no es un fallo de las comprobaciones sino de lo que miden.",
                label_w=400, width=1000, note_kind="gold", foot=GIT)


def se204_equivalentes() -> Fig:
    rows = [
        ["Cambia el tope de 72 a 48 sin tocar pruebas", "Pasan: ninguna prueba mira el tope", "Sí: la comprobación 12 exige cambiar alguna prueba"],
        ["Cambia pruebas pero una afirmación pasa a ser vacía", "Pasan: la prueba siempre es verdadera", "No: cumple la regla de «cambiar una prueba»"],
    ]
    return tab("Dos defectos con las pruebas verdes: uno se ve y otro no",
               "Tabla con dos defectos que dejan las pruebas en verde: el cambio de tope sin tocar pruebas, que la comprobación de pruebas modificadas detecta, y una afirmación vacía, que ninguna comprobación de forma detecta.",
               ["Defecto", "Qué dicen las pruebas", "¿Lo detecta alguna comprobación?"], rows, [330, 300, 350], row_h=64, size=12,
               note="Para ver el segundo hace falta una prueba que falle contra una versión errónea de la regla (mutación) o la lectura de una persona. Un paquete aprobado por comprobaciones automáticas no es un paquete correcto.",
               note_kind="coral", foot=GIT)


FIGURES = {
    "se-199-codeowners-sobre-600-rutas.svg": se199_codeowners,
    "se-199-mensajes-que-rechaza-el-validador.svg": se199_mensajes,
    "se-199-blame-tras-un-reformateo.svg": se199_blame,
    "se-200-concentracion-de-commits.svg": se200_concentracion,
    "se-200-reglas-de-decision.svg": se200_decision,
    "se-200-fork-desfasado.svg": se200_fork,
    "se-201-expresiones-de-licencia.svg": se201_expresiones,
    "se-201-licencias-transitivas.svg": se201_transitivas,
    "se-201-huella-del-texto-de-licencia.svg": se201_huella,
    "se-202-firmas-que-verifican.svg": se202_firmas,
    "se-202-reescribir-la-cadena.svg": se202_cadena,
    "se-202-politicas-de-proteccion.svg": se202_politicas,
    "se-203-estrategia-de-resolucion.svg": se203_estrategia,
    "se-203-rescatar-una-fusion-mala.svg": se203_rescate,
    "se-203-marcas-de-conflicto.svg": se203_marcas,
    "se-204-matriz-de-comprobaciones.svg": se204_matriz,
    "se-204-comprobaciones-por-defecto.svg": se204_solapes,
    "se-204-dos-defectos-con-pruebas-verdes.svg": se204_equivalentes,
}
