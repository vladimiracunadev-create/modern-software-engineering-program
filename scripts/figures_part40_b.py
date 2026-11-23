"""Figures for SE-487 to SE-492 (synthetic data, fixed seeds, virtual time; CPython 3.12.9 on Windows 11 and 3.12.3 on Ubuntu/WSL2)."""
from __future__ import annotations

from experiments_part40_b import (e415_bucle, e415_pelea, e415_poda, e416_previews, e416_reidentificacion, e416_uniones, e417_adopcion,
                                  e417_catalogo, e417_cola, e418_definiciones, e418_gaming, e418_ruido, e419_endurecer, e419_inyeccion,
                                  e419_permisos, e419_pin, e420_ablacion, e420_paquete, e420_rollback)
from figure_kit import Fig, grouped_bars, heatmap, line_chart, percentile_intervals, stacked_bars
from figures_part07_a import bars
from figures_part40_a import SINT, n, pc


# ---------------------------------------------------------------- SE-487
def se415_bucle() -> Fig:
    d = e415_bucle()
    ks = ("cada 30 s", "cada 3 min", "cada 15 min", "cada hora")
    lect = "; ".join(f"{k}: {n(d[k][2], 0)}" for k in ks)
    return grouped_bars(
        "Intervalo de reconciliación: cuánto vive una deriva manual y cuántas lecturas cuesta (200 aplicaciones)",
        "Barras agrupadas en escala logarítmica con la espera media y el percentil 95 hasta corregir una deriva manual: reconciliar cada 30 segundos da 15 y 28 segundos, cada 3 minutos 91 y 171, cada 15 minutos 453 y 857 y cada hora 1 803 y 3 417.",
        list(ks), [("Deriva: espera media", [d[k][0] for k in ks], "teal"), ("Percentil 95", [d[k][1] for k in ks], "coral")],
        unit="Segundos hasta corregir", log=True, decimals=0, plot_h=280,
        note=f"Lecturas por día: {lect}. Bajar el intervalo de una hora a 30 segundos acorta la deriva en 120 veces y multiplica las lecturas por 120. Un aviso del repositorio (unos 2 s) resuelve los cambios en Git, no las derivas del clúster, que solo se ven al comparar. Las dos lecturas por ciclo y el reparto uniforme de las derivas son supuestos.",
        note_kind="gold", foot=SINT)


def se415_pelea() -> Fig:
    d = e415_pelea()
    a, b = d["el repositorio fija réplicas = 3"], d["el repositorio ignora el campo de réplicas"]
    return grouped_bars(
        "Un controlador de GitOps y un escalador automático que se disputan el número de réplicas (24 h, 1 440 minutos)",
        "Barras agrupadas con los minutos sin capacidad, las acciones del escalador y las reversiones del reconciliador: si el repositorio fija tres réplicas son 361, 854 y 425; si omite el campo, 0, 640 y ninguna reversión.",
        ["El repositorio fija «réplicas: 3»", "El repositorio omite el campo de réplicas"],
        [("Minutos sin capacidad", [a[0], b[0]], "coral"), ("Acciones del escalador", [a[1], b[1]], "navy"), ("Reversiones del reconciliador", [a[2], b[2]], "gold")],
        unit="Minutos o acciones", decimals=0, plot_h=280,
        note="Dos bucles de control que gobiernan el mismo campo no convergen: cada uno deshace al otro y el servicio paga 361 minutos de capacidad insuficiente. La solución es que el repositorio deje de declarar lo que otro actor decide (ignorar el campo), no subir la frecuencia de reconciliación. Carga sinusoidal con ruido; capacidad de 100 solicitudes por réplica: supuestos.",
        note_kind="coral", foot=SINT)


def se415_poda() -> Fig:
    d = e415_poda()
    return grouped_bars(
        "Refactorizar manifiestos con poda activada: recursos borrados por cada refactorización que mueve archivos",
        "Barras agrupadas con los recursos borrados por refactorización y los que tienen estado: sin poda no se borra nada; con poda se borran 1,97 y 0,32 tienen estado; con poda y protección de los recursos con estado se borran 1,71 y ninguno tiene estado.",
        [k.replace("protección de recursos con estado", "protección del estado") for k in d], [("Recursos borrados por refactorización", [v[0] for v in d.values()], "coral"), ("De ellos, con estado", [v[1] for v in d.values()], "gold")],
        unit="Recursos por refactorización", decimals=2, plot_h=260,
        note="Para el controlador, renombrar un recurso es «borrar el viejo y crear el nuevo»: con poda, una refactorización de apariencia inofensiva borra casi dos recursos, y uno de cada tres de esas refactorizaciones tocaría un volumen con datos. La protección explícita de lo que tiene estado cuesta una anotación. 15 % de manifiestos con estado: supuesto.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-488
def se416_reident() -> Fig:
    d = e416_reidentificacion()
    grupos = ", ".join(f"{k}: {v[3]}" for k, v in d.items())
    return grouped_bars(
        "Datos de 6 000 estudiantes sintéticos sin nombre: unicidad y reidentificación por vinculación con una lista externa del 70 %",
        "Barras horizontales con el porcentaje de personas únicas, reidentificadas y en grupos de menos de cinco según los cuasi-identificadores conservados: con fecha de nacimiento, código postal y género el 97,6 por ciento es único y se reidentifica; con año, código postal y género el 1,2; con año, tres dígitos postales y género el 0,02 y ninguna reidentificación.",
        list(d),
        [("Únicos", [v[0] * 100 for v in d.values()], "coral"), ("Reidentificados", [v[1] * 100 for v in d.values()], "navy"), ("En grupos de menos de 5", [v[2] * 100 for v in d.values()], "gold")],
        unit="Personas (%)", horizontal=True, decimals=2, label_w=300,
        note=f"Número de grupos por conjunto: {grupos}. Quitar el nombre no anonimiza: tres datos corrientes bastan para identificar a casi todas las personas. Generalizar reduce el riesgo a costa de detalle: con 12 grupos ya no se distingue casi nada. El 22,3 % de grupos pequeños con año y código postal completo recuerda que no basta con que casi nadie sea único. Población y lista externa sintéticas.",
        note_kind="coral", foot=SINT)


def se416_uniones() -> Fig:
    d = e416_uniones()
    nt = d["_notas"]
    return grouped_bars(
        "Enmascarar datos para una prueba: uniones que sobreviven y distribución de las notas (3 000 estudiantes, 15 000 entregas)",
        "Barras con el porcentaje de uniones entre estudiantes y entregas que sobreviven a cada enmascarado: el identificador sin enmascarar conserva el 100 por ciento, el aleatorio por tabla el 0 y el determinista con HMAC y sal el 100.",
        ["Identificador sin enmascarar", "Aleatorio por tabla", "Determinista con HMAC y sal"],
        [("Uniones que sobreviven", [d["sin enmascarar"] * 100, d["aleatorio por tabla"] * 100, d["determinista (HMAC con sal)"] * 100], "teal")],
        unit="Uniones que sobreviven (%)", decimals=0, plot_h=240,
        note=f"Notas con ruido gaussiano (σ = 1): media {n(nt['ruido'][0], 2)}, σ {n(nt['ruido'][1], 2)}, r {n(nt['ruido'][2], 2)}; la desviación crece de 1,11 a 1,52. Notas permutadas: media {n(nt['permutación'][0], 2)}, σ {n(nt['permutación'][1], 2)}, r {n(nt['permutación'][2], 3)}; conservan la distribución y borran la relación. Cada técnica protege algo y rompe otra cosa: el aleatorio protege la identidad y anula la prueba de integridad; el determinista conserva las uniones y permite vincular registros si se filtra la sal.",
        note_kind="gold", foot=SINT)


def se416_previews() -> Fig:
    d = e416_previews()
    ks = ("solo se destruye al cerrar el PR", "TTL de 72 h desde la creación", "TTL de 24 h renovado con cada push")
    base = d[ks[0]][0]
    det = "; ".join(f"{k}: {pc(d[k][0] / base, 0)} de las horas, {d[k][1]} recreaciones, {d[k][2]} huérfanos" for k in ks)
    return grouped_bars(
        f"Entornos de vista previa de {d['_prs']} PR en 60 días (8 por día, 15 % abandonados): horas de entorno según la política",
        "Barras horizontales con las horas de entorno según la política: destruir solo al cerrar el PR suma 74 357 y deja 64 huérfanos; un TTL de 72 horas suma 33 383, el 45 por ciento, con 186 recreaciones; un TTL de 24 horas renovado con cada push suma 30 460, el 41 por ciento, con 293 recreaciones y ningún huérfano.",
        list(ks), [("Horas de entorno", [d[k][0] for k in ks], "navy")],
        unit="Horas de entorno", horizontal=True, decimals=0, label_w=270,
        note=f"{det}. Los PR abandonados dominan el costo: el 15 % que nadie cierra consume más de la mitad de las horas. El TTL lo corta a cambio de recrear el entorno cuando alguien vuelve. La actividad del PR (un push cada 14 h) y el abandono son supuestos; las horas se leen como razones, no como dinero.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-489
def se417_adopcion() -> Fig:
    d = e417_adopcion()
    covs = (3, 4, 6)
    hs = (4, 20, 60)
    parc = "; ".join(f"cobertura {c} de 6: " + ", ".join(pc(d[c][s][1], 0) for s in hs) for c in covs)
    return line_chart(
        "Equipos que adoptan el camino dorado según su cobertura y el esfuerzo de empezar (400 equipos por celda)",
        "Líneas con el porcentaje de equipos que adoptan el camino según las horas para empezar: si cubre 3 de 6 capacidades lo adopta el 31 por ciento con 4 horas, 16 con 20 y 2 con 60; si cubre 4, el 55, 33 y 5; si cubre las 6, el 100, 92 y 20.",
        [(f"Cubre {c} de 6 capacidades", [(s, d[c][s][0] * 100) for s in hs], kind) for c, kind in zip(covs, ("coral", "gold", "teal"))],
        x_label="Horas para empezar", y_label="Equipos que adoptan (%)", log_x=True,
        x_ticks=[(4, "4 h"), (20, "20 h"), (60, "60 h")], y_ticks=[0, 20, 40, 60, 80, 100], point_labels="all", decimals=0, plot_h=300,
        note=f"Adopción parcial (4, 20 y 60 h): {parc}. Un camino fácil de empezar pero incompleto lo adopta la mitad de los equipos y casi todos acaban improvisando lo que falta. Uno completo pero costoso de usar (60 h) casi nadie lo toma. La adopción no mide calidad: mide que el camino compite bien contra el costo de construirlo por cuenta propia (mediana de 40 h, supuesto del autor).",
        note_kind="gold", foot=SINT)


def se417_catalogo() -> Fig:
    d = e417_catalogo()
    cats = [k for k in d if not k.startswith("_")]
    return grouped_bars(
        "Un catálogo de 150 servicios: entradas que pasan según el rigor de la validación",
        "Barras horizontales con las entradas de 150 que pasan según el rigor de la validación: comprobar solo que los campos existan aprueba 130; exigir que el dueño exista en el registro de equipos, 122; que el enlace no sea de relleno, 108; que la revisión sea de los últimos 180 días, 43; hay 107 entradas con algún problema sembrado.",
        cats + ["Entradas con algún problema sembrado (dueño, enlace o revisión)"],
        [("Entradas", [d[k] for k in cats] + [d["_con_problema"]], "navy")],
        unit="Entradas de 150", horizontal=True, decimals=0, label_w=300, ref_lines=[(d["_total"], "150 entradas")],
        note="Con la validación de presencia el catálogo parece completo al 87 % y en realidad solo 43 entradas (29 %) están al día. Medir la completitud por campos lleno invita a rellenar con «TBD»; comprobar contra otra fuente (el registro de equipos, la fecha de revisión) es lo que distingue completo de actual. Las proporciones de problemas son supuestos del autor.",
        note_kind="coral", foot=SINT)


def se417_cola() -> Fig:
    d = e417_cola()
    xs = [float(k) for k in d]
    return line_chart(
        "Aprovisionar por ticket con dos personas de plataforma (3 horas por solicitud): espera antes de empezar",
        "Líneas con la espera media y el percentil 90 según la demanda: con 0,2 solicitudes por hora la utilización es del 30 por ciento y la espera media 0,3 horas; con 0,4 la utilización es del 60 por ciento y la espera media 1,7 horas con 5,7 en el percentil 90; con 0,55 la utilización es del 83 por ciento y 6,4 horas con 16,6 en el percentil 90.",
        [("Espera media", [(x, v[1], f"{n(v[1], 1)} h", "r" if i == 0 else "b") for i, (x, v) in enumerate(zip(xs, d.values()))], "teal"),
         ("Espera p90", [(x, v[2], f"{n(v[2], 1)} h", "t") for x, v in zip(xs, d.values())], "coral")],
        x_label="Demanda (solicitudes por hora)", y_label="Horas de espera", x_ticks=[(x, n(x, 2)) for x in xs], y_ticks=[0, 5, 10, 15, 20],
        point_labels="none", decimals=1, plot_h=300,
        note="Utilización de las dos personas: 30 %, 60 % y 83 %. La espera no crece proporcionalmente: al subir la demanda 2,75 veces (de 0,2 a 0,55), la espera media se multiplica por 22. Es la misma curva de saturación de la cola de SE-436 aplicada a un equipo humano. El autoservicio saca el tiempo de espera de la cola, a cambio de construir y mantener la automatización. Servicio exponencial de 3 h: supuesto.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-490
def se418_definiciones() -> Fig:
    d = e418_definiciones()
    f, p, fl, rs = d["frecuencia"], d["plazo"], d["fallos"], d["restauracion"]
    return grouped_bars(
        f"Cuatro métricas de entrega (de las cinco de DORA) calculadas del mismo registro de {n(d['_n'], 0)} despliegues de 6 servicios en 52 semanas",
        "Barras horizontales con el plazo de entrega mediano del mismo registro según la definición: 32 horas desde el primer commit, 29 desde que se abre el PR y 4,6 desde la fusión; la tasa de fallos es 11,4 por ciento con incidente o 6,3 solo con retroceso.",
        ["Desde el primer commit", "Desde que se abre el PR", "Desde la fusión"],
        [("Plazo de entrega (mediana)", [p["desde el primer commit (mediana)"], p["desde que se abre el PR (mediana)"], p["desde la fusión (mediana)"]], "navy")],
        unit="Horas", horizontal=True, decimals=1, label_w=190,
        note=f"El mismo registro da también una frecuencia de {n(f['por servicio y semana (media)'], 1)} despliegues por servicio y semana, {n(f['del conjunto por semana'], 1)} del conjunto o {n(f['solo producción de los dos servicios mayores'], 1)} solo en los dos servicios mayores; una tasa de fallos de {pc(fl['fallos con incidente'], 1)} con incidente o {pc(fl['solo los que se revierten'], 1)} solo revertidos; y una restauración de {n(rs['mediana (h)'], 2)} h de mediana y {n(rs['media (h)'], 2)} h de media. Comparar un número entre equipos que definen distinto no compara equipos. La media y la mediana de la restauración difieren un 57 % porque pocos incidentes son largos. Registro sintético.",
        note_kind="gold", foot=SINT)


def se418_gaming() -> Fig:
    d = e418_gaming()
    ks = list(d)
    return grouped_bars(
        "Una métrica se vuelve meta: el mismo trabajo y los mismos defectos en 26 semanas",
        "Barras agrupadas en escala logarítmica con tres métricas en tres casos: sin incentivo hay 4 despliegues por semana, 24 por ciento de fallos y plazo mediano de 32 horas; con despliegues vacíos, 16, 6 por ciento y 0,1 horas; partiendo los cambios en tres, 30, 3,2 por ciento y 8 horas.",
        ["Despliegues por semana", "Tasa de fallos (%)", "Plazo mediano (h)"],
        [(k, [v[0], v[1] * 100, v[2]], kind) for (k, v), kind in zip(d.items(), ("grey", "coral", "gold"))],
        unit="Valor de la métrica", log=True, decimals=1, plot_h=280,
        note=f"En los tres casos hay {n(d[ks[0]][3], 2)} defectos por semana y {n(d[ks[0]][4], 0)} cambios de valor. Las tres métricas mejoraron (más frecuencia, menos fallos, menos plazo) y el trabajo entregado y los defectos son idénticos. Partir cambios puede ser una buena práctica real, pero medido por el ratio sale lo mismo que el truco de los despliegues vacíos. La defensa es mirar las métricas juntas con una medida de valor y desconfiar de la que mejora sola.",
        note_kind="coral", foot=SINT)


def se418_ruido() -> Fig:
    d = e418_ruido()
    xs = list(d)
    semi = "; ".join(f"{k} despliegues: ±{n(v[2] * 100, 1)} puntos" for k, v in d.items())
    return line_chart(
        "Ruido de la tasa de fallos mensual (verdadera 12 %): dos equipos idénticos y una mejora real de 12 % a 8 %",
        "Líneas con dos porcentajes de meses según el volumen: dos equipos idénticos difieren en 5 puntos o más el 69 por ciento de los meses con 8 despliegues al mes, el 55 con 30 y el 29 con 100; una mejora real del 12 al 8 por ciento se ve en el 42, 61 y 80 por ciento.",
        [("Equipos idénticos que difieren ≥ 5 puntos", [(k, v[0] * 100) for k, v in d.items()], "coral"), ("Mejora real que se ve", [(k, v[1] * 100) for k, v in d.items()], "teal")],
        x_label="Despliegues al mes", y_label="Meses (%)", log_x=True, x_ticks=[(k, str(k)) for k in xs], y_ticks=[0, 20, 40, 60, 80, 100],
        point_labels="all", decimals=0, plot_h=280,
        note=f"Semiancho del intervalo del 95 %: {semi}. Con el volumen de un equipo pequeño, comparar la tasa mensual de dos equipos es comparar ruido: casi siete de cada diez meses difieren cinco puntos sin que nada haya cambiado. La tendencia sobre muchos meses o un intervalo declarado dicen más que un ranking mensual. Simulación binomial con semilla fija; el intervalo es el de Wald.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-491
def se419_pasos() -> Fig:
    d = e419_endurecer()
    cats = [("0. " if i == 0 else f"{i}. ") + name for i, (name, c, _) in enumerate(d["pasos"])]
    return grouped_bars(
        "Endurecer un workflow vulnerable paso a paso: hallazgos del verificador tras cada cambio",
        "Barras horizontales con los hallazgos del verificador tras cada cambio: el workflow original tiene 8 y cada uno de los 8 cambios elimina exactamente uno (fijar la acción a un SHA, permisos mínimos, pull_request en lugar de pull_request_target, título por variable de entorno, script versionado, no escribir el secreto, que el trabajo falle cuando falla, sin credencial en el texto) hasta llegar a 0.",
        cats, [("Hallazgos restantes", [c for _, c, _ in d["pasos"]], "teal")],
        unit="Hallazgos restantes", horizontal=True, decimals=0, label_w=380,
        note="Cada cambio es pequeño y elimina un hallazgo concreto: no se reescribe la canalización. Que el verificador llegue a 0 no prueba que el workflow sea seguro, solo que no contiene las ocho formas que sabe buscar. La credencial del texto, además, sigue en el historial: borrarla del archivo no la revoca.",
        note_kind="gold", foot=SINT)


def se419_inyeccion() -> Fig:
    d = e419_inyeccion()
    cnt = {"ejecuta": 0, "inerte": 0, "rompe": 0}
    ok = 0
    for _, res, good in d["filas"]:
        cnt[res] += 1
        ok += 1 if good else 0
    alt = len(d["filas"]) - ok
    return stacked_bars(
        "Insertar un título en un programa antes de ejecutarlo o pasarlo como dato (6 títulos, ejecución real)",
        "Barras apiladas horizontales con el resultado de seis títulos: expandir el título dentro del texto del programa ejecuta 4 de los 6 como código; pasar el título por una variable de entorno deja los 6 como datos.",
        ["Expandido en el programa", "Por variable de entorno"],
        [("Se ejecuta como código", [cnt["ejecuta"], 0], "coral"), ("Rompe el programa", [cnt["rompe"], 0], "gold"), ("Inerte", [cnt["inerte"], ok], "teal"), ("Alterado", [0, alt], "grey")],
        unit="Títulos", horizontal=True, decimals=0, label_w=210,
        note="El mecanismo es el de una expresión de workflow dentro de un script: el texto se sustituye antes de que el intérprete lo lea, así que una comilla y un paréntesis lo convierten en código. Aquí el intérprete es Python y la carga es inofensiva; el principio no cambia con el intérprete. Se ejecuta de verdad en cada máquina.",
        note_kind="coral", foot=SINT)


def se419_permisos() -> Fig:
    p = e419_permisos()
    pin = e419_pin()
    jobs = list(p["write-all"])
    etiqueta = "el contenido cambia y deja de coincidir con la huella fijada" if pin["etiqueta_cambio"] else "sin cambio"
    return grouped_bars(
        "Ámbitos con escritura del token por job con «write-all» frente al mínimo, y la etiqueta que se mueve",
        "Barras horizontales con los ámbitos con escritura del token por job: con permisos amplios cada job recibe 16; con el mínimo, lint y pruebas 0, la construcción 1, la publicación 3 y el despliegue 2.",
        jobs, [("Con permisos amplios (write-all)", [p["write-all"][j] for j in jobs], "coral"), ("Con el mínimo", [p["mínimo"][j] for j in jobs], "teal")],
        unit=f"Ámbitos con escritura (de {p['ambitos']})", horizontal=True, decimals=0, label_w=160,
        note=f"Si alguien mueve la etiqueta de una acción de terceros, {etiqueta}, mientras que la referencia por SHA no cambia. Un job de lint con escritura en 16 ámbitos es una superficie de ataque sin función; el mínimo reduce el daño que hace una acción comprometida. La etiqueta es un puntero mutable; el SHA identifica contenido. La lista de 16 ámbitos con escritura sale de la página de sintaxis consultada el 15 de noviembre de 2026 y puede cambiar.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-492
def se420_rollback() -> Fig:
    d = e420_rollback()
    ks = ("renombrar de golpe", "expandir sin doble escritura", "expandir con doble escritura", "contraer antes de tiempo")
    return stacked_bars(
        "Volver a la versión anterior de la aplicación tras migrar el esquema (SQLite en memoria, 10 lecturas)",
        "Barras apiladas horizontales con las 10 lecturas de la versión anterior según la estrategia de migración: renombrar de golpe da 10 con error; expandir sin doble escritura 5 correctas y 5 vacías; expandir con doble escritura 10 correctas; contraer antes de tiempo, 10 con error.",
        list(ks),
        [("Lecturas correctas", [d[k][2] for k in ks], "teal"), ("Lecturas vacías", [d[k][1] for k in ks], "gold"), ("Lecturas con error", [d[k][0] for k in ks], "coral")],
        unit="Lecturas", horizontal=True, decimals=0, label_w=250,
        note="Volver atrás el código no revierte los datos: la reversión funciona solo si el esquema en producción todavía es compatible con la versión anterior. La doble escritura mantiene esa compatibilidad y contraer (borrar lo viejo) la rompe: se hace en un despliegue posterior, cuando ya no hay vuelta atrás prevista. Ejecución real con sqlite3.",
        note_kind="coral", foot=SINT)


def se420_ablacion() -> Fig:
    d = e420_ablacion()
    gs = ("revisión y lint", "pruebas unitarias", "pruebas de integración", "escaneo de dependencias y secretos", "política sobre el plan de infraestructura", "humo en preproducción", "canario con métricas", "alerta en producción")
    return grouped_bars(
        f"Quitar una compuerta cada vez: 12 fallos tipo; costo relativo total sin ninguna ausencia: {n(d['_base_coste'], 0)}",
        "Barras horizontales con los fallos que se detectan más tarde y los que escapan al quitar cada compuerta: quitar el escaneo de dependencias y secretos deja escapar 2 y sube el costo de 214 a 802; quitar la política del plan, 1 y 604; quitar el canario retrasa 3 fallos y sube el costo a 439; quitar lint, unitarias o integración retrasa 1 cada una.",
        [f"{g} (costo {n(d[g][2], 0)})" for g in gs],
        [("Fallos que se detectan más tarde", [d[g][0] for g in gs], "gold"), ("Fallos que escapan", [d[g][1] for g in gs], "coral")],
        unit="Fallos de 12", horizontal=True, decimals=0, label_w=330,
        note="Entre paréntesis, el costo relativo total al quitar esa compuerta. Las compuertas baratas retrasan poco, las únicas para una clase de fallo hacen escapar: el escaneo es la única que ve un secreto o una dependencia vulnerable. La matriz de qué compuerta ve qué fallo es juicio del autor, y los costos (1 a 100) son relativos; el ejercicio es construir la propia y ver qué fallos solo tienen un guardián.",
        note_kind="gold", foot=SINT)


def se420_paquete() -> Fig:
    d = e420_paquete()
    ops = d["ops"]
    groups = {}
    for name, (kind, a, b, c) in ops.items():
        g = groups.setdefault(kind, [0, 0, 0, 0])
        g[0] += 1
        g[1] += a
        g[2] += b
        g[3] += c
    names = {"forma": "Forma (campo ausente, commit o digest mal escritos)", "cruce": "Cruce entre campos (digest o commit distinto, autoaprobación)", "verosimilitud": "Verosimilitud (0 segundos, entorno ajeno, canario sin tráfico)", "juicio": "Juicio (ensayo copiado, aprobador sin permisos reales)"}
    kinds = ("forma", "cruce", "verosimilitud", "juicio")
    tot = d["n"] * len(ops)
    return grouped_bars(
        "Un validador del paquete de evidencia frente a 120 mutaciones (12 operadores × 10 paquetes)",
        "Barras horizontales con las mutaciones que detecta cada capa de validación por tipo: un validador de forma detecta 30 de las 120, uno que cruza campos 70 y uno con reglas de verosimilitud 100; las 20 mutaciones de juicio no las ve ninguno.",
        [f"{names[k]} ({groups[k][0] * d['n']})" for k in kinds] + [f"Todas las mutaciones ({tot})"],
        [("Solo forma", [groups[k][1] for k in kinds] + [sum(v[1] for v in ops.values())], "grey"), ("+ cruce de campos", [groups[k][2] for k in kinds] + [sum(v[2] for v in ops.values())], "gold"),
         ("+ verosimilitud", [groups[k][3] for k in kinds] + [sum(v[3] for v in ops.values())], "teal")],
        unit="Mutaciones detectadas", horizontal=True, decimals=0, label_w=330,
        note="Entre paréntesis, las mutaciones de cada tipo. Los 10 paquetes sin mutar pasan en las tres capas. Cada capa de validación añade lo que la anterior no podía ver y todas dejan pasar la mutación que parece correcta: un ensayo copiado de otra versión tiene forma, cruces y duración verosímiles. Eso solo lo detecta una persona que conozca el sistema o una comprobación contra el sistema real. Mutaciones y reglas escritas por el mismo autor.",
        note_kind="coral", foot=SINT)


FIGURES = {
    "se-487-intervalo-de-reconciliacion.svg": se415_bucle,
    "se-487-controladores-que-se-disputan.svg": se415_pelea,
    "se-487-poda-y-recursos-con-estado.svg": se415_poda,
    "se-488-reidentificacion-sin-nombre.svg": se416_reident,
    "se-488-uniones-y-distribucion-enmascaradas.svg": se416_uniones,
    "se-488-costo-de-entornos-de-vista-previa.svg": se416_previews,
    "se-489-adopcion-del-camino-dorado.svg": se417_adopcion,
    "se-489-catalogo-completo-o-actual.svg": se417_catalogo,
    "se-489-espera-del-aprovisionamiento-por-ticket.svg": se417_cola,
    "se-490-un-registro-cuatro-definiciones.svg": se418_definiciones,
    "se-490-cuando-la-metrica-es-la-meta.svg": se418_gaming,
    "se-490-ruido-de-la-tasa-de-fallos.svg": se418_ruido,
    "se-491-hallazgos-tras-cada-cambio.svg": se419_pasos,
    "se-491-inyeccion-en-el-script.svg": se419_inyeccion,
    "se-491-permisos-y-fijacion-por-huella.svg": se419_permisos,
    "se-492-retroceso-tras-migrar-el-esquema.svg": se420_rollback,
    "se-492-quitar-una-compuerta.svg": se420_ablacion,
    "se-492-validador-del-paquete-de-evidencia.svg": se420_paquete,
}
