"""Figures for SE-193 to SE-198 (Git real en repositorios temporales o datos sintéticos con semilla fija; resultados idénticos en Windows y Ubuntu salvo los tiempos)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

GIT = "Git real en repositorios temporales con identidad y fechas fijas; salidas idénticas con Git 2.55 (Windows) y 2.43 (Ubuntu, WSL2)."
SINT = "Datos sintéticos, semilla fija; idénticos en Windows y Ubuntu (WSL2). Los parámetros son supuestos del autor."


# ---------------------------------------------------------------- SE-193
def se193_ids() -> Fig:
    rows = [
        ["Blob de «hola entrega»", "SHA-1 de «blob 13», un byte nulo y el contenido", "Idéntico al de git hash-object", "Coincide"],
        ["Árbol con un directorio", "Entradas ordenadas tratando el directorio como «src/»", "Idéntico al de git write-tree", "Coincide"],
        ["El mismo árbol con orden ingenuo", "Entradas ordenadas solo por nombre, sin la barra", "Otro identificador", "No coincide: «src.b» queda antes que «src»"],
        ["Commit inicial", "Árbol, autoría, fecha y mensaje escritos a mano", "Idéntico al de git commit-tree", "Coincide"],
    ]
    return tab("Reconstruir a mano los identificadores de objetos",
               "Tabla de cuatro objetos de Git reconstruidos con hashlib: el blob, el árbol con el orden correcto y el commit coinciden con Git y el árbol con orden ingenuo no coincide.",
               ["Objeto", "Cómo se construyó", "Resultado frente a Git", "Lectura"], rows, [250, 330, 270, 250], row_h=58, size=12,
               note="El identificador es una función del contenido y de su formato, no un número asignado. El detalle del orden de los árboles basta para obtener otro objeto.",
               note_kind="teal", foot=GIT)


def se193_areas() -> Fig:
    rows = [
        ["Archivo nuevo sin agregar", "??", "Git no lo rastrea; no aparece en ningún diff"],
        ["Archivo nuevo, agregado", "A·", "Está en el índice; git diff --cached lo muestra"],
        ["Agregado y editado después", "AM", "El índice tiene la versión vieja y el árbol de trabajo la nueva"],
        ["Editado sin agregar", "·M", "Solo cambia el árbol de trabajo"],
        ["Editado y agregado", "M·", "El índice y el árbol de trabajo coinciden; difiere de HEAD"],
        ["Quitado solo del índice", "D· y ??", "El archivo sigue en disco pero deja de estar rastreado"],
    ]
    return tab("Estados de git status --porcelain en cada paso",
               "Tabla de seis operaciones con el código de dos letras que muestra git status y qué significa respecto del árbol de trabajo, el índice y HEAD.",
               ["Situación", "Código", "Qué significa"], rows, [330, 120, 520], row_h=46, size=12,
               note="En a.py con 3 líneas en HEAD, 1 agregada y 2 más sin agregar: git diff cuenta 2, git diff --cached cuenta 1 y git diff HEAD cuenta 3. Un restore posterior borra las 2 sin agregar y conserva la agregada.",
               note_kind="gold", foot=GIT)


def se193_almacen() -> Fig:
    items = [
        ("301 versiones sin comprimir (35 830 B cada una)", 10.78, "grey", "10,78 MB"),
        ("903 objetos sueltos, comprimidos uno a uno", 5.59, "coral", "5,59 MB"),
        ("Los mismos 903 objetos tras gc --aggressive", 0.096, "teal", "96 000 B"),
    ]
    return bars("Espacio de 301 versiones de un archivo con 300 ediciones de una línea",
                "Barras: 301 versiones de un archivo de 35 830 bytes ocupan 10,78 millones de bytes sin comprimir, 5,59 millones como objetos sueltos y 96 000 bytes empaquetados con deltas.",
                items, 80, "Los objetos sueltos solo comprimen cada versión por separado; el paquete guarda diferencias entre versiones y es unas 58 veces menor. Con --object-format=sha256 el identificador mide 64 caracteres en lugar de 40.",
                label_w=380, width=1040, note_kind="gold", foot=GIT)


# ---------------------------------------------------------------- SE-194
def se194_bisect() -> Fig:
    rows = [
        ["64 commits atómicos", "6", "Sí", "4 líneas en 2 archivos"],
        ["16 commits de 4 cambios cada uno", "4", "Sí", "10 líneas en 5 archivos"],
        ["64 atómicos con 3 intermedios rotos lejos del defecto", "6", "Sí", "4 líneas en 2 archivos"],
        ["64 atómicos con un intermedio roto junto al defecto", "6", "No: solo quedan commits omitidos", "Hay que leer los candidatos a mano"],
    ]
    return tab("git bisect run sobre la misma pérdida de puntos con cuatro historias",
               "Tabla de cuatro historias con el mismo defecto en el cambio 41: ejecuciones de la prueba, si Git encuentra un culpable único y cuánto hay que leer después.",
               ["Historia", "Ejecuciones de la prueba", "¿Culpable único?", "Qué hay que leer después"], rows, [340, 150, 230, 260], row_h=58, size=12,
               note="Agrupar cambios ahorra dos ejecuciones pero multiplica por 2,5 lo que se lee. Un commit intermedio que no compila junto al defecto impide que Git señale un solo commit.",
               note_kind="coral", foot=GIT)


def se194_recuperacion() -> Fig:
    rows = [
        ["Commit y luego reset --hard", "Sí", "El objeto sigue y el reflog apunta a él"],
        ["Agregado al índice y luego reset --hard", "Sí", "Queda un blob suelto; git fsck --lost-found lo encuentra"],
        ["Editado sin agregar y luego reset --hard", "No", "Nunca entró en la base de objetos"],
        ["Archivo no rastreado y luego clean -fd", "No", "Nunca entró en la base de objetos"],
        ["Stash y luego stash drop", "Sí", "El commit del stash queda colgando hasta la poda"],
        ["Commit, reset, expirar el reflog y gc --prune=now", "No", "El objeto ya no es alcanzable y se poda"],
    ]
    return tab("¿Sigue el contenido en la base de objetos después del error?",
               "Tabla de seis errores con la respuesta de si el contenido sigue en la base de objetos de Git y por qué.",
               ["Qué ocurrió", "¿Sigue?", "Motivo"], rows, [370, 100, 500], row_h=46, size=12,
               note="Git solo puede recuperar lo que alguna vez guardó. Un cambio que no se agregó ni se confirmó no tiene copia.",
               note_kind="teal", foot=GIT)


def se194_reset_revert() -> Fig:
    rows = [
        ["reset --hard HEAD~2 y push --force", "3 por delante, 0 por detrás", "6", "Sí: a3 y a4 vuelven al remoto"],
        ["revert de los dos últimos y push normal", "1 por delante, 2 por detrás", "9", "No: quedan los dos revert"],
    ]
    return tab("Deshacer dos commits ya publicados mientras otra clon tiene trabajo local",
               "Tabla de dos formas de deshacer commits publicados: reescribir con reset y fuerza, o revertir, y qué ocurre cuando otro clon fusiona y publica.",
               ["Forma de deshacer", "Estado del otro clon tras fetch", "Commits en el remoto al final", "¿Reaparece lo deshecho?"], rows, [310, 260, 190, 230], row_h=58, size=12,
               note="Quien tiene los dos commits publicados los devuelve al remoto en su siguiente push. Revertir produce una historia más larga pero converge sin coordinación.",
               note_kind="gold", foot=GIT)


# ---------------------------------------------------------------- SE-195
def se195_estrategias() -> Fig:
    rows = [
        ["Merge sin avance rápido", "10", "1", "4 de 4", "Conserva la forma de la bifurcación"],
        ["Rebase y avance rápido", "9", "0", "0 de 4", "Reescribe los 4 commits: cambian de identificador"],
        ["Squash", "6", "0", "0 de 4", "Un commit nuevo; los 4 originales no entran"],
    ]
    return tab("Tres formas de integrar una rama de 4 commits cuando main avanzó 3",
               "Tabla de merge, rebase y squash con el número de commits en main, fusiones y cuántos commits de la rama conservan su identificador.",
               ["Estrategia", "Commits en main", "Fusiones", "Hashes conservados", "Lectura"], rows, [220, 130, 110, 150, 360], row_h=58, size=12,
               note="El árbol final fue idéntico en las tres. Cambia la historia, no el contenido; por eso la elección es de trazabilidad y de quién ya tiene esos commits.",
               note_kind="teal", foot=GIT)


def se195_conflicto() -> Fig:
    items = [
        ("Dos ediciones en la misma línea", 100, "coral", "100 %"),
        ("Dos ediciones en líneas contiguas", 100, "coral", "100 %"),
        ("Con una línea de separación", 0, "teal", "0 %"),
        ("1 edición por rama, 200 líneas", 0.3, "teal", "0,3 %"),
        ("4 ediciones por rama", 21, "gold", "21 %"),
        ("8 ediciones por rama", 60.7, "gold", "60,7 %"),
        ("16 ediciones por rama", 98.7, "coral", "98,7 %"),
    ]
    return bars("Probabilidad de conflicto de texto al fusionar dos ramas",
                "Barras: dos ediciones en la misma línea o en líneas contiguas siempre entran en conflicto; con una línea de separación nunca; con ediciones al azar la probabilidad pasa de 0,3 por ciento con una edición a 98,7 con dieciséis.",
                items, 6.2, "Git señala conflicto cuando dos cambios tocan líneas contiguas, no solo la misma. Con ediciones al azar la probabilidad crece como una colisión: cuadruplicar las ediciones de 4 a 16 la lleva de 21 % a casi 99 %.",
                label_w=330, width=1000, note_kind="gold", foot=SINT)


def se195_rerere() -> Fig:
    rows = [
        ["Inactivo", "1", "1 (hay que resolver otra vez)", "Con marcas"],
        ["Activo", "1", "0", "tope=60 (la resolución previa se reaplica)"],
    ]
    return tab("Repetir la misma fusión con rerere inactivo y activo",
               "Tabla con las marcas de conflicto en la primera y la segunda fusión de las mismas ramas, con rerere desactivado y activado.",
               ["rerere", "Marcas en la 1.ª fusión", "Marcas en la 2.ª fusión", "Contenido de la 2.ª"], rows, [140, 220, 290, 320], row_h=58, size=12,
               note="Con rerere el código de salida de la segunda fusión sigue siendo 1: Git avisa de que había conflicto y aun así deja resuelto el archivo. Hay que revisarlo y agregarlo; la reutilización no valida que la resolución siga siendo correcta.",
               note_kind="gold", foot=GIT)


# ---------------------------------------------------------------- SE-196
def se196_range_diff() -> Fig:
    items = [
        ("git diff entre las dos puntas (incluye lo que cambió main)", 26, "coral", "26 líneas"),
        ("Líneas +/− dentro de los commits que range-diff marca", 6, "teal", "6 líneas"),
        ("Commits de la rama marcados como cambiados", 2, "gold", "2 de 4"),
    ]
    return bars("Qué muestra cada comparación tras reordenar una rama y pedir un cambio",
                "Barras: tras rebasar una rama de cuatro commits sobre un main que avanzó doce commits y corregir uno, el diff plano entre puntas cambia 26 líneas y range-diff solo muestra 6 dentro de dos commits.",
                items, 30, "El diff plano mezcla lo que cambió main con la corrección pedida. range-diff compara commit contra commit y marca con «!» los que cambiaron. Fue «==!!»: el cuarto commit cambia porque su contexto incluye la línea corregida, no porque alguien lo editara.",
                label_w=420, width=1060, note_kind="gold", foot=GIT)


def se196_triaje() -> Fig:
    items = [
        ("Al azar (media de 100 barajados)", 25.5, "grey", "25,5"),
        ("En el orden en que aparecen los archivos", 26, "grey", "26"),
        ("Primero los archivos más grandes", 27, "gold", "27"),
        ("Primero el mayor nivel de riesgo (3 niveles)", 29, "gold", "29"),
        ("Por defectos esperados por línea", 40, "teal", "40"),
    ]
    return bars("Defectos plantados que alcanza a ver una lectura del 30 % de cada PR",
                "Barras: de 91 defectos plantados en 300 pull requests sintéticos, leer el 30 por ciento de las líneas al azar halla 25,5; por tamaño 27; por tres niveles de riesgo 29 y por defectos esperados por línea 40.",
                items, 13, "Ordenar por defectos esperados por línea ve un 57 % más defectos que el azar con el mismo esfuerzo. La densidad de defectos por tipo de archivo es un supuesto del autor: el experimento muestra el efecto de priorizar, no cuántos defectos hay en proyectos reales.",
                label_w=400, width=1040, note_kind="teal", foot=SINT)


def se196_apilados() -> Fig:
    rows = [
        ["En una zona lejana de los demás PR", "No", "3 de 3"],
        ["Junto a la línea que edita el PR 2", "Sí", "0 de 3: se detiene en el primero"],
    ]
    return tab("Corregir el primer PR de una pila de cuatro y reapilar con rebase --update-refs",
               "Tabla con dos correcciones del primer pull request de una pila: una lejana que reapila sin conflicto y otra contigua al segundo PR que provoca conflicto.",
               ["Dónde cae la corrección", "¿Conflicto al reapilar?", "Ramas de la pila actualizadas"], rows, [380, 220, 380], row_h=58, size=12,
               note="Una pila de PR pequeños reduce lo que se lee, pero cada corrección del primero se paga en reapilados. Cuando hay conflicto Git detiene todo y hay que resolverlo para continuar.",
               note_kind="gold", foot=GIT)


# ---------------------------------------------------------------- SE-197
def se197_vida() -> Fig:
    items = [
        ("Ramas de 1 día (1 200 integraciones)", 45.3, "gold", "45,3 %"),
        ("Ramas de 2 días (600)", 84.0, "coral", "84,0 %"),
        ("Ramas de 5 días (240)", 97.5, "coral", "97,5 %"),
        ("Ramas de 10 días (120)", 95.0, "coral", "95,0 %"),
        ("Ramas de 20 días (60)", 90.0, "coral", "90,0 %"),
    ]
    return bars("Integraciones con conflicto según los días que vive la rama",
                "Barras: con cinco personas editando un archivo de 400 líneas con una zona caliente, 45,3 por ciento de las integraciones de ramas de un día tienen conflicto y más de 84 por ciento cuando duran dos o más días.",
                items, 8.2, "Aun con ramas de un día casi la mitad tiene conflicto en este modelo, porque el archivo concentra las ediciones. Desde los 5 días el porcentaje deja de crecer y las integraciones se vuelven raras pero casi siempre dolorosas.",
                label_w=360, width=1020, note_kind="coral", foot=SINT)


def se197_semantico() -> Fig:
    rows = [
        ["10 % de los PR toca lo mismo que otro abierto", "0,9", "2,4", "5,1"],
        ["30 % de los PR toca lo mismo que otro abierto", "3,0", "7,0", "14,8"],
    ]
    return tab("Veces que main queda roto por 500 PR si no se prueba la fusión (media de 20 semillas)",
               "Tabla con la media de veces que main se rompe por 500 pull requests cuando dos PR verdes por separado son incompatibles, según la proporción de solapamientos y la probabilidad de incompatibilidad.",
               ["Solapamiento", "Rompe 2 %", "Rompe 5 %", "Rompe 10 %"], rows, [430, 160, 160, 160], row_h=58, size=12,
               note="En Git real, dos ramas fusionaron sin conflicto de texto y el panel imprimió 42 en lugar de 60 porque una cambió el orden de los parámetros y la otra seguía llamando con el orden antiguo. Una cola de fusión prueba el resultado combinado y lleva esta cifra a 0 a costa de espera.",
               note_kind="coral", foot=SINT)


def se197_backports() -> Fig:
    items = [
        ("10 commits tras el corte (4 correcciones)", 0, "teal", "0 %"),
        ("20 commits (8 correcciones)", 25, "gold", "25 %"),
        ("40 commits (16 correcciones)", 37.5, "coral", "37,5 %"),
        ("80 commits (32 correcciones)", 50, "coral", "50 %"),
    ]
    return bars("Cherry-picks con conflicto al portar correcciones a una rama de versión",
                "Barras: portar una de cada diez correcciones a una rama de versión provoca conflicto en 0 por ciento de los casos con 10 commits de deriva, 25 con 20, 37,5 con 40 y 50 con 80.",
                items, 14, "Cada commit que no se porta cambia el contexto de los que sí. Cuanto más se deja derivar el tronco, más correcciones requieren resolución manual y más se parece el backport a reescribir el arreglo.",
                label_w=400, width=1000, note_kind="gold", foot=GIT)


# ---------------------------------------------------------------- SE-198
def se198_cierres() -> Fig:
    items = [
        ("Cierres que la persona quería hacer", 132, "grey", "132"),
        ("Expresión ingenua #número: cierres hallados", 113, "gold", "113"),
        ("Expresión ingenua: vínculos que no eran cierres", 57, "coral", "57 falsos"),
        ("Palabra clave + #número: cierres hallados", 86, "teal", "86"),
        ("Palabra clave + #número: vínculos falsos", 0, "teal", "0"),
    ]
    return bars("Extraer los issues que cierra cada mensaje (150 mensajes sintéticos)",
                "Barras: de 132 cierres que la persona quería hacer, la expresión ingenua halla 113 y añade 57 vínculos falsos; la regla de palabra clave halla 86 y ninguno falso.",
                items, 6.2, "La regla estricta no se equivoca de más pero pierde lo escrito sin espacio, con una dirección completa, con «GH-» o con un segundo número tras «y». La ingenua halla más y vincula referencias que no cierran nada.",
                label_w=420, width=1060, note_kind="gold", foot=SINT)


def se198_reproducir() -> Fig:
    items = [
        ("Solo un título", 6.7, "coral", "6,7 %"),
        ("Título y síntoma", 6.7, "coral", "6,7 %"),
        ("Pasos sin los valores exactos", 28.3, "gold", "28,3 %"),
        ("Pasos con los valores exactos de entrada", 100, "teal", "100 %"),
    ]
    return bars("Informes reproducidos de 120 según el detalle (6 defectos, 5 intentos al azar)",
                "Barras: un script que intenta reproducir seis defectos solo con lo que dice el informe reproduce 6,7 por ciento con un título, 28,3 con pasos sin valores y 100 con los valores exactos.",
                items, 6.2, "Los valores que activan el defecto separan un informe accionable de uno que obliga a adivinar. El 28,3 % depende de que la persona recuerde un valor una de cada cuatro veces: es un supuesto, no una medición de personas.",
                label_w=380, width=1000, note_kind="teal", foot=SINT)


def se198_trazabilidad() -> Fig:
    rows = [
        ["Commit directo en main", "50", "12", "12"],
        ["Rama que nunca se integra", "4", "0", "0"],
        ["Rama integrada con squash sin copiar el cuerpo", "6", "1", "0"],
    ]
    return tab("Mensajes con Fixes o Closes que sobreviven en main (60 cambios generados)",
               "Tabla de tres orígenes de cambio con el número de mensajes, cuántos llevan Fixes o Closes y cuántos siguen visibles en el historial de main.",
               ["Origen del cambio", "Mensajes", "Con Fixes o Closes", "Visibles en main"], rows, [400, 130, 220, 190], row_h=46, size=12,
               note="En main quedaron 56 commits, 18 con referencia y 13 de 25 issues con alguna. El squash que no copia el cuerpo borra el vínculo: la trazabilidad depende de cómo se integra, no solo de lo que se escribió.",
               note_kind="gold", foot=GIT)


FIGURES = {
    "se-193-identificadores-reconstruidos.svg": se193_ids,
    "se-193-las-tres-areas.svg": se193_areas,
    "se-193-sueltos-frente-a-empaquetado.svg": se193_almacen,
    "se-194-ejecuciones-de-bisect.svg": se194_bisect,
    "se-194-que-se-recupera.svg": se194_recuperacion,
    "se-194-reset-frente-a-revert.svg": se194_reset_revert,
    "se-195-merge-rebase-y-squash.svg": se195_estrategias,
    "se-195-conflicto-segun-ediciones.svg": se195_conflicto,
    "se-195-rerere.svg": se195_rerere,
    "se-196-range-diff.svg": se196_range_diff,
    "se-196-triaje-por-riesgo.svg": se196_triaje,
    "se-196-pull-requests-apilados.svg": se196_apilados,
    "se-197-vida-de-la-rama.svg": se197_vida,
    "se-197-conflicto-semantico.svg": se197_semantico,
    "se-197-backports.svg": se197_backports,
    "se-198-cierres-recuperados.svg": se198_cierres,
    "se-198-reproducir-segun-detalle.svg": se198_reproducir,
    "se-198-trazabilidad-en-main.svg": se198_trazabilidad,
}
