"""Figures for SE-199 to SE-204 (Git real en repositorios temporales o datos sintéticos con semilla fija; resultados idénticos en Windows y Ubuntu salvo los tiempos)."""
from __future__ import annotations

from figure_flow_rows import chain_rows
from figure_kit import Fig, fmt_exact, grouped_bars, heatmap, line_chart, stacked_bars
from figures_part07_a import bars


GIT = "Git real en repositorios temporales con identidad y fechas fijas; salidas idénticas con Git 2.55 (Windows) y 2.43 (Ubuntu, WSL2)."
SINT = "Datos sintéticos, semilla fija; idénticos en Windows y Ubuntu (WSL2). Los parámetros son supuestos del autor."


# ---------------------------------------------------------------- SE-199
def se199_codeowners() -> Fig:
    return grouped_bars(
        "Un CODEOWNERS sintético de 24 reglas evaluado sobre 600 rutas",
        "Barras horizontales con rutas de 600: ninguna sin propietario con la regla «*» y 31 sin ella; 520 cambian de propietario al invertir el orden de las reglas; el equipo más cargado recibe 108 rutas y el menos cargado 25.",
        ["Sin propietario, con la regla «*» al principio", "Sin propietario si se quita «*»", "Cambian de propietario al invertir el orden", "Carga del equipo más cargado", "Carga del equipo menos cargado"],
        [("Rutas", [0, 31, 520, 108, 25], "teal")],
        unit="Rutas de 600", horizontal=True, label_w=330, ticks=[0, 150, 300, 450, 600],
        note="El último patrón que coincide gana, así que el orden es la semántica; 1 regla de 24 («/CODEOWNERS») nunca gana. El modelo de coincidencia es una simplificación de lo que describe la documentación, no el motor de una plataforma: sirve para auditar reglas, no para sustituir la comprobación en el alojamiento real.",
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
    return stacked_bars(
        "Autoría de 300 líneas tras un commit que solo cambia la sangría de 150",
        "Barras apiladas horizontales con las líneas atribuidas a la autora, a otra persona y a un bot: git blame sin ignorar atribuye 150 líneas al bot que reformateó; con --ignore-rev o --ignore-revs-file el bot no figura y la autora recupera 270 líneas y la otra persona 30.",
        ["git blame sin ignorar", "git blame --ignore-rev del reformateo", "git blame --ignore-revs-file"],
        [("Autora", [120, 270, 270], "teal"), ("Otra persona", [30, 30, 30], "gold"), ("Bot que reformateó", [150, 0, 0], "coral")],
        unit="Líneas atribuidas (de 300)", horizontal=True, label_w=250,
        note="Ignorar el reformateo recupera la autoría solo porque cada línea cambió de forma pero no de sentido. Un commit que mezcla reformateo y lógica no puede ignorarse sin ocultar la lógica.",
        note_kind="teal", foot=GIT)


# ---------------------------------------------------------------- SE-200
def se200_concentracion() -> Fig:
    return line_chart(
        "Archivos que solo tocó la persona más activa según la concentración de commits (30 contribuyentes, 400 commits)",
        "Línea con el porcentaje de archivos que solo tocó la persona más activa según el exponente de concentración: 2,6 por ciento con 0,5, 7,6 con 1,0, 17,1 con 1,5 y 31,6 con 2,0; los rótulos añaden los autores que cubren la mitad de los commits: 9,1, 4,1, 2,0 y 1,0.",
        [("Archivos que solo tocó la persona más activa", [(0.5, 2.6, "2,6 % · 9,1 autores cubren el 50 %", "r"), (1.0, 7.6, "7,6 % · 4,1 autores", "t"),
                                                           (1.5, 17.1, "17,1 % · 2,0 autores", "t"), (2.0, 31.6, "31,6 % · 1,0 autor", "l")], "coral")],
        x_label="Exponente de la distribución de commits", y_label="Archivos que solo tocó la persona más activa (%)",
        x_ticks=[(0.5, "0,5"), (1.0, "1,0"), (1.5, "1,5"), (2.0, "2,0")], y_ticks=[0, 10, 20, 30, 40], point_labels="none",
        note="Con un exponente de 2 una sola persona produce la mitad de los commits y 3 de cada 10 archivos pierden a la única persona que los conocía si se va. Los exponentes son supuestos; sirven para ver la sensibilidad, no para describir un proyecto real.",
        note_kind="coral", foot=SINT)


def se200_decision() -> Fig:
    return grouped_bars(
        "Reglas de decisión cuando solo el 30 % de las personas mantenedoras lee la propuesta",
        "Barras agrupadas con los porcentajes de propuestas dañinas aceptadas, buenas rechazadas y sin decisión para tres reglas: el consenso perezoso acepta 40,5 por ciento de las dañinas y nunca deja sin decisión; la mayoría de 3 de 5 acepta 1,0 y deja sin decisión 83,5; la unanimidad de quienes votan, 0,5 y 83,5.",
        ["Consenso perezoso (72 h)", "Mayoría de 3 de 5", "Unanimidad de votantes (mín. 3)"],
        [("Dañinas aceptadas", [40.5, 1.0, 0.5], "coral"), ("Buenas rechazadas", [12.3, 3.1, 4.1], "gold"), ("Sin decisión", [0, 83.5, 83.5], "grey")],
        unit="Propuestas (%)", plot_h=260, ticks=[0, 20, 40, 60, 80, 100], value_fmt=lambda v: fmt_exact(v) + " %",
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
    return grouped_bars(
        "Política de licencias sobre 300 expresiones: decisiones erróneas de la comparación literal y avisos del analizador (el analizador no se equivoca sin avisar en ninguna)",
        "Barras horizontales por tipo de expresión con las decisiones erróneas de la comparación literal y los avisos del analizador: la literal falla en 39 disyunciones, 28 de 50 conjunciones, 15 con paréntesis, 26 en minúsculas y 18 con barra; el analizador no se equivoca sin avisar nunca y avisa en 26 minúsculas, 18 con barra, 16 identificadores obsoletos y 22 remisiones a un archivo.",
        ["Disyunción «A OR B» (39 casos)", "Conjunción «A AND B» (50)", "Con paréntesis (15)", "Minúsculas «mit» (26)", "Barra «MIT/Apache-2.0» (18)",
         "Identificador obsoleto «GPL-3.0» (16)", "Remisión a un archivo (22)"],
        [("La comparación literal se equivoca", [39, 28, 15, 26, 18, 0, 0], "coral"), ("El analizador emite un aviso", [0, 0, 0, 26, 18, 16, 22], "teal")],
        unit="Casos", horizontal=True, label_w=270,
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
    return grouped_bars(
        "Razón de similitud de difflib frente a la huella del texto de licencia normalizado",
        "Barras horizontales con la razón de similitud de difflib de cinco variantes del texto de la licencia MIT: otro año y otro titular y los saltos de línea distintos dan 1,000 con la misma huella; quitar la cláusula del aviso da 0,486; cambiar «AS IS» por otro texto da 0,971, casi igual aunque la huella difiere; el texto de otra licencia da 0,024.",
        ["Otro año y otro titular (huella igual)", "Saltos de línea y espacios distintos (huella igual)", "Se elimina la cláusula del aviso (huella distinta)",
         "«AS IS» sustituido por otro texto (huella distinta)", "Texto de otra licencia (huella distinta)"],
        [("Razón de difflib", [1.0, 1.0, 0.486, 0.971, 0.024], "gold")],
        unit="Razón de similitud de difflib", horizontal=True, label_w=330, ticks=[0, 0.25, 0.5, 0.75, 1], value_fmt=lambda v: f"{v:.3f}".replace(".", ","),
        note="Una razón de 0,971 puede esconder el cambio que elimina la garantía. La huella exacta detecta cualquier diferencia pero no dice cuál; la similitud dice cuánto, no si importa. En 400 archivos sintéticos, 14 etiquetas SPDX (GPL-3.0-only) contradecían el LICENSE (MIT) y 165 archivos no tenían etiqueta.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-202
def se202_firmas() -> Fig:
    return stacked_bars(
        "Verificar commits firmados con SSH: resultado de git verify-commit",
        "Barras apiladas horizontales con el resultado de git verify-commit en tres casos: 60 de 60 commits firmados con una clave SSH desechable verifican; una copia con el mensaje cambiado y la misma firma falla con código 1; una firma válida de un firmante que no figura en el archivo de firmantes falla con código 1.",
        ["60 commits firmados con una clave SSH desechable", "Copia con el mensaje cambiado y la misma firma", "Firma válida con otro archivo de firmantes"],
        [("Verifican", [60, 0, 0], "teal"), ("Fallan (código 1)", [0, 1, 1], "coral")],
        unit="Comprobaciones de git verify-commit", horizontal=True, label_w=300,
        note="La firma vive en una cabecera del propio objeto y cubre el contenido exacto del commit; válida no significa de confianza. Firmar añadió unos 92 ms por commit en Windows y 7 ms en Ubuntu, y verificar costó 15 ms por commit en Ubuntu y 234 ms en Windows (60 repeticiones, medidas de un equipo): no se comparan entre sistemas.",
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
        [("(a) Sin publicar", "plain"), ("Reset al primer padre y fusionar de nuevo: se reescribe un commit que nadie tiene", "plain"), ("Pruebas verdes", "teal")],
        [("(b) Publicada", "plain"), ("Nuevo commit que restaura lo perdido: el commit malo sigue en la historia", "plain"), ("Pruebas verdes", "teal")],
        [("(c) Revertir la fusión", "plain"), ("revert -m 1 y volver a fusionar: Git responde «Already up to date», la rama figura integrada", "plain"), ("Pruebas rojas", "coral")],
    ]
    return chain_rows(
        "Rescatar una fusión que se resolvió con «ours» y perdió el periodo de gracia",
        "Diagrama de flujo de tres rescates de una fusión mal resuelta: reiniciar y repetir si no se publicó y dejar las pruebas verdes, un commit de corrección si se publicó con las pruebas verdes, y revertir la fusión y volver a fusionar, que no hace nada y deja las pruebas en rojo.",
        ["Camino", "Qué se hace y qué ocurre en la historia", "Resultado"], rows, [200, 430, 170],
        note="Tras la fusión mala la rama figuraba como ancestro, así que fusionarla otra vez no hace nada. El revert devuelve el árbol al primer padre pero no devuelve la intención perdida.",
        note_kind="coral", foot=GIT)


def se203_marcas() -> Fig:
    return grouped_bars(
        "Líneas de marca de conflicto según el estilo (y si muestran la base)",
        "Barras horizontales con las líneas de marca de conflicto de tres estilos: merge, el predeterminado, usa 3 y no muestra el original común; diff3 y zdiff3 usan 4 y sí lo muestran, zdiff3 con menos contexto repetido; abortar la fusión devuelve HEAD, índice y estado limpio.",
        ["merge (predeterminado): dos versiones y nada más", "diff3: añade el original común", "zdiff3: igual que diff3 con menos contexto repetido"],
        [("Líneas de marca", [3, 4, 4], "teal")],
        unit="Líneas de marca por conflicto", horizontal=True, label_w=330, ticks=[0, 1, 2, 3, 4, 5],
        note="Ver el original común (la cuarta línea) permite decidir qué lado cambió qué. Con el estilo por defecto solo se ve el resultado de cada lado y es fácil elegir uno sin entender el otro. merge --abort a mitad de un conflicto devuelve HEAD, índice y estado limpio idénticos.",
        note_kind="teal", foot=GIT)


# ---------------------------------------------------------------- SE-204
def se204_matriz() -> Fig:
    defects = ["Contribución correcta", "Mensaje sin tipo", "Un commit gigante que mezcla", "Commit intermedio roto", "Prueba que falla en la punta",
               "Archivo nuevo sin cabecera SPDX", "Descripción sin issue", "Secreto sintético en el diff", "Commits sin firmar", "Sin Signed-off-by",
               "PR de más de 400 líneas", "Toca src/auth sin pedir al equipo dueño", "Cambia el tope sin tocar pruebas", "Prueba que no comprueba nada"]
    hits = [[], [1], [2], [3], [3, 4], [5], [6], [7], [8], [9], [2, 10], [11], [12], []]
    values = [[1 if c in h else 0 for c in range(1, 13)] for h in hits]
    return heatmap(
        "Qué comprobación detecta cada defecto plantado en una contribución",
        "Mapa de calor de catorce contribuciones, una correcta y trece con un defecto plantado, frente a las doce comprobaciones: cada defecto dispara una o dos casillas, el commit gigante y el PR de más de 400 líneas comparten la comprobación 2, la prueba que falla dispara la 3 y la 4, y la contribución correcta y la prueba que no comprueba nada no disparan ninguna.",
        defects, [str(n) for n in range(1, 13)], values,
        unit="1 = la comprobación falla", row_title="Contribución", col_title="Número de la comprobación",
        scale="coral", vmin=0, vmax=1, cell_fmt=lambda v: "●" if v else "", cell_h=30, label_w=290,
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
        [("Cambia el tope de 72 a 48 sin tocar pruebas", "plain"), ("Pasan: ninguna prueba mira el tope", "gold"), ("Sí: la comprobación 12 exige cambiar alguna prueba", "teal")],
        [("Cambia pruebas pero una afirmación pasa a ser vacía", "plain"), ("Pasan: la prueba siempre es verdadera", "gold"), ("No: cumple la regla de «cambiar una prueba»", "coral")],
    ]
    return chain_rows(
        "Dos defectos con las pruebas verdes: uno se ve y otro no",
        "Diagrama de flujo de dos defectos que dejan las pruebas en verde: el cambio de tope sin tocar pruebas, que la comprobación de pruebas modificadas detecta, y una afirmación vacía, que ninguna comprobación de forma detecta.",
        ["Defecto", "Qué dicen las pruebas", "¿Lo detecta alguna comprobación?"], rows, [300, 250, 270],
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
