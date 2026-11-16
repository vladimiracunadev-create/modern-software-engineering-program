"""Figures for SE-193 to SE-198 (Git real en repositorios temporales o datos sintéticos con semilla fija; resultados idénticos en Windows y Ubuntu salvo los tiempos)."""
from __future__ import annotations

from figure_flow_rows import chain_rows
from figure_kit import AXIS, Fig, _kit_finish, _kit_start, grouped_bars, heatmap, stacked_bars
from figures_part07_a import bars


GIT = "Git real en repositorios temporales con identidad y fechas fijas; salidas idénticas con Git 2.55 (Windows) y 2.43 (Ubuntu, WSL2)."
SINT = "Datos sintéticos, semilla fija; idénticos en Windows y Ubuntu (WSL2). Los parámetros son supuestos del autor."


# ---------------------------------------------------------------- SE-193
def se193_ids() -> Fig:
    rows = [
        [("Blob de «hola entrega»", "plain"), ("SHA-1 de «blob 13», un byte nulo y el contenido", "plain"), ("Idéntico al de git hash-object: coincide", "teal")],
        [("Árbol con un directorio", "plain"), ("Entradas ordenadas tratando el directorio como «src/»", "plain"), ("Idéntico al de git write-tree: coincide", "teal")],
        [("El mismo árbol con orden ingenuo", "plain"), ("Entradas ordenadas solo por nombre, sin la barra", "plain"), ("Otro identificador: «src.b» queda antes que «src»", "coral")],
        [("Commit inicial", "plain"), ("Árbol, autoría, fecha y mensaje escritos a mano", "plain"), ("Idéntico al de git commit-tree: coincide", "teal")],
    ]
    return chain_rows(
        "Reconstruir a mano los identificadores de objetos: de la entrada al identificador",
        "Diagrama de flujo de cuatro objetos de Git reconstruidos con hashlib: del contenido y el formato al identificador; el blob, el árbol con el orden correcto y el commit coinciden con Git y el árbol con orden ingenuo da otro identificador.",
        ["Objeto", "Cómo se construyó", "Resultado frente a Git"], rows, [220, 330, 270],
        note="El identificador es una función del contenido y de su formato, no un número asignado. El detalle del orden de los árboles basta para obtener otro objeto.",
        note_kind="teal", foot=GIT)


def se193_areas() -> Fig:
    f, y = _kit_start("Las tres áreas de Git y lo que cuenta cada diff (a.py: 3 líneas en HEAD, 1 agregada y 2 más sin agregar)",
                      "Diagrama de las tres áreas de Git, HEAD, índice y árbol de trabajo, con los comandos que mueven el contenido entre ellas y las líneas que cuenta cada diff: git diff cuenta 2 entre el índice y el árbol de trabajo, git diff --cached cuenta 1 entre HEAD y el índice y git diff HEAD cuenta 3.",
                      940, None)
    top = y + 8
    xs = [(40, "HEAD", "3 líneas", "grey"), (370, "Índice", "+1 línea agregada", "gold"), (700, "Árbol de trabajo", "+2 líneas sin agregar", "teal")]
    for x, name, body, kind in xs:
        f.box(x, top, 200, 84, f"{name}\n{body}", kind, 14, bold=True)
    f.arrow([(700, top + 30), (572, top + 30)], "git add", label_at=(636, top + 20))
    f.arrow([(370, top + 30), (242, top + 30)], "git commit", label_at=(306, top + 20))
    f.arrow([(242, top + 62), (370, top + 62)], "restore --staged", dashed=True, label_at=(306, top + 78))
    f.arrow([(572, top + 62), (700, top + 62)], "restore", dashed=True, label_at=(636, top + 78))
    brackets = [(470, 800, "git diff: 2 líneas (índice frente a árbol de trabajo)", 0), (140, 470, "git diff --cached: 1 línea (HEAD frente a índice)", 1),
                (140, 800, "git diff HEAD: 3 líneas (HEAD frente a árbol de trabajo)", 2)]
    for a, b, label, row in brackets:
        by = top + 112 + row * 50
        f.line(a, by, b, by, "#32505f", width=1.6)
        f.line(a, by - 7, a, by, "#32505f", width=1.6)
        f.line(b, by - 7, b, by, "#32505f", width=1.6)
        f.text((a + b) / 2, by + 20, label, 13, "middle", 700, "#142231")
    yy = top + 112 + 2 * 50 + 44
    f.text(14, yy, "git status --porcelain: la primera letra compara el índice con HEAD; la segunda, el árbol de trabajo con el índice.", 13, "start", 400, AXIS)
    return _kit_finish(f, yy + 14,
                       "Un restore posterior borra las 2 líneas sin agregar y conserva la agregada. Un archivo nuevo sin agregar (??) no está en ninguna de las tres áreas: Git no lo rastrea y no aparece en ningún diff.",
                       "gold", GIT)


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
    return grouped_bars(
        "Ejecuciones de la prueba de git bisect run sobre la misma pérdida de puntos con cuatro historias",
        "Barras horizontales con las ejecuciones de la prueba que necesita git bisect run en cuatro historias con el mismo defecto: 6 con 64 commits atómicos, 4 con 16 commits de cuatro cambios, 6 con tres intermedios rotos lejos del defecto y 6 con un intermedio roto junto al defecto, donde Git ya no encuentra un culpable único.",
        ["64 commits atómicos: culpable único, 4 líneas en 2 archivos", "16 commits de 4 cambios: culpable único, 10 líneas en 5 archivos",
         "64 atómicos con 3 intermedios rotos lejos: culpable único, 4 líneas", "64 atómicos con un intermedio roto junto al defecto: sin culpable único"],
        [("Ejecuciones de la prueba", [6, 4, 6, 6], "teal")],
        unit="Ejecuciones de la prueba", horizontal=True, label_w=400, ticks=[0, 2, 4, 6, 8],
        note="Agrupar cambios ahorra dos ejecuciones pero multiplica por 2,5 lo que se lee. Un commit intermedio que no compila junto al defecto impide que Git señale un solo commit: solo quedan commits omitidos y hay que leer los candidatos a mano.",
        note_kind="coral", foot=GIT)


def se194_recuperacion() -> Fig:
    f, y = _kit_start("¿Sigue el contenido en la base de objetos después del error? Depende de hasta dónde llegó",
                      "Diagrama del recorrido de un cambio en cuatro etapas: nunca guardado, objeto suelto o colgante, alcanzable desde el reflog y podado; un cambio editado sin agregar o un archivo no rastreado no se recupera, un agregado o un stash descartado sí, un commit con reset sí, y un commit con el reflog expirado y gc --prune=now no.",
                      940, None)
    cols = [("1 · Nunca guardado", "coral", [("Editado sin agregar y luego reset --hard: no. Nunca entró en la base de objetos", "coral"),
                                              ("Archivo no rastreado y luego clean -fd: no. Nunca entró en la base de objetos", "coral")]),
            ("2 · Objeto suelto o colgante", "gold", [("Agregado y luego reset --hard: sí. Un blob suelto; git fsck --lost-found lo encuentra", "teal"),
                                                     ("Stash y luego stash drop: sí. El commit del stash queda colgando hasta la poda", "teal")]),
            ("3 · Alcanzable desde el reflog", "teal", [("Commit y luego reset --hard: sí. El objeto sigue y el reflog apunta a él", "teal")]),
            ("4 · Inalcanzable y podado", "coral", [("Commit, reset, expirar el reflog y gc --prune=now: no. Ya no es alcanzable y se poda", "coral")])]
    w, gap, top = 205, 30, y + 6
    for i, (head, kind, boxes) in enumerate(cols):
        x = 14 + i * (w + gap)
        f.group(x, top, w, 330, head, kind)
        for j, (text, k) in enumerate(boxes):
            f.box(x + 10, top + 38 + j * 140, w - 20, 126, text, k, 13)
        if i < len(cols) - 1:
            f.arrow([(x + w + 3, top + 165), (x + w + gap - 3, top + 165)])
    return _kit_finish(f, top + 340, "Git solo puede recuperar lo que alguna vez guardó. Un cambio que no se agregó ni se confirmó no tiene copia.", "teal", GIT)


def se194_reset_revert() -> Fig:
    return grouped_bars(
        "Deshacer dos commits ya publicados mientras otro clon tiene trabajo local: commits en el remoto al final",
        "Barras horizontales con los commits que quedan en el remoto tras deshacer dos commits publicados: con reset --hard y push forzado quedan 6 y lo deshecho reaparece cuando el otro clon publica; con revert y push normal quedan 9, incluidos los dos revert, y no reaparece.",
        ["reset --hard HEAD~2 y push --force: el otro clon tiene 3 por delante, 0 por detrás y lo deshecho reaparece (a3 y a4)",
         "revert de los dos últimos y push normal: el otro clon tiene 1 por delante, 2 por detrás y lo deshecho no reaparece"],
        [("Commits en el remoto", [6, 9], "gold")],
        unit="Commits en el remoto al final", horizontal=True, label_w=400, ticks=[0, 3, 6, 9, 12],
        note="Quien tiene los dos commits publicados los devuelve al remoto en su siguiente push. Revertir produce una historia más larga pero converge sin coordinación.",
        note_kind="gold", foot=GIT)


# ---------------------------------------------------------------- SE-195
def se195_estrategias() -> Fig:
    return grouped_bars(
        "Tres formas de integrar una rama de 4 commits cuando main avanzó 3",
        "Barras agrupadas con los commits en main, las fusiones y los commits de la rama que conservan su identificador al integrar una rama de cuatro commits: merge deja 10 commits, 1 fusión y 4 de 4 hashes; rebase deja 9, ninguna fusión y 0 de 4; squash deja 6, ninguna fusión y 0 de 4.",
        ["Merge sin avance rápido", "Rebase y avance rápido", "Squash"],
        [("Commits en main", [10, 9, 6], "navy"), ("Fusiones", [1, 0, 0], "gold"), ("Commits de la rama con su hash conservado (de 4)", [4, 0, 0], "teal")],
        unit="Commits", plot_h=250,
        note="El árbol final fue idéntico en las tres. Cambia la historia, no el contenido: merge conserva la forma de la bifurcación, rebase reescribe los 4 commits y squash crea uno nuevo; por eso la elección es de trazabilidad y de quién ya tiene esos commits.",
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
    return grouped_bars(
        "Repetir la misma fusión con rerere inactivo y activo: marcas de conflicto",
        "Barras agrupadas con el número de fusiones que dejan marcas de conflicto en la primera y la segunda fusión de las mismas ramas: con rerere inactivo hay marcas en las dos; con rerere activo solo en la primera y la segunda reaplica la resolución previa.",
        ["1.ª fusión", "2.ª fusión"],
        [("rerere inactivo", [1, 1], "coral"), ("rerere activo", [1, 0], "teal")],
        unit="Fusiones con marcas de conflicto", plot_h=220, ticks=[0, 1, 2],
        note="Con rerere el código de salida de la segunda fusión sigue siendo 1: Git avisa de que había conflicto y aun así deja resuelto el archivo (tope=60, la resolución previa se reaplica). Hay que revisarlo y agregarlo; la reutilización no valida que la resolución siga siendo correcta.",
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
    return stacked_bars(
        "Corregir el primer PR de una pila de cuatro y reapilar con rebase --update-refs",
        "Barras apiladas horizontales con las tres ramas de la pila que quedan actualizadas tras corregir el primer pull request: con una corrección lejana se actualizan 3 de 3; con una corrección contigua a la línea que edita el segundo PR hay conflicto y 0 de 3, porque Git se detiene en el primero.",
        ["Corrección en una zona lejana de los demás PR", "Corrección junto a la línea que edita el PR 2"],
        [("Ramas actualizadas", [3, 0], "teal"), ("Ramas sin actualizar", [0, 3], "coral")],
        unit="Ramas de la pila que se actualizan (de 3)", horizontal=True, label_w=270,
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
    return heatmap(
        "Veces que main queda roto por 500 PR si no se prueba la fusión (media de 20 semillas)",
        "Mapa de calor con la media de veces que main se rompe por 500 pull requests verdes por separado pero incompatibles: con el 10 por ciento de solapamientos, 0,9, 2,4 y 5,1 según rompan con probabilidad 2, 5 y 10 por ciento; con el 30 por ciento, 3,0, 7,0 y 14,8.",
        ["10 % de los PR toca lo mismo que otro abierto", "30 % de los PR toca lo mismo que otro abierto"],
        ["Incompatibles el 2 %", "Incompatibles el 5 %", "Incompatibles el 10 %"],
        [[0.9, 2.4, 5.1], [3.0, 7.0, 14.8]],
        unit="veces que main queda roto", row_title="Solapamiento", col_title="Probabilidad de que dos PR solapados sean incompatibles",
        scale="coral", decimals=1, cell_h=56, label_w=250,
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
    return grouped_bars(
        "Mensajes con Fixes o Closes que sobreviven en main (60 cambios generados)",
        "Barras agrupadas con los mensajes, los que llevan Fixes o Closes y los visibles en main para tres orígenes de cambio: el commit directo en main conserva sus 12 referencias de 50 mensajes; la rama que nunca se integra tiene 4 mensajes y ninguna referencia; la rama integrada con squash sin copiar el cuerpo tiene 1 referencia en 6 mensajes y ninguna visible.",
        ["Commit directo en main", "Rama que nunca se integra", "Rama integrada con squash sin copiar el cuerpo"],
        [("Mensajes", [50, 4, 6], "navy"), ("Con Fixes o Closes", [12, 0, 1], "gold"), ("Visibles en main", [12, 0, 0], "teal")],
        unit="Mensajes", plot_h=250,
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
