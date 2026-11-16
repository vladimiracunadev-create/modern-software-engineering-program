"""Figures for SE-415 to SE-420 (synthetic data, fixed seeds, virtual time; CPython 3.12.9 on Windows 11 and 3.12.3 on Ubuntu/WSL2)."""
from __future__ import annotations

from experiments_part34_b import (e415_bucle, e415_pelea, e415_poda, e416_previews, e416_reidentificacion, e416_uniones, e417_adopcion,
                                  e417_catalogo, e417_cola, e418_definiciones, e418_gaming, e418_ruido, e419_endurecer, e419_inyeccion,
                                  e419_permisos, e419_pin, e420_ablacion, e420_paquete, e420_rollback)
from figure_kit import Fig
from figures_part07_a import bars, tab
from figures_part34_a import SINT, n, pc


# ---------------------------------------------------------------- SE-415
def se415_bucle() -> Fig:
    d = e415_bucle()
    rows = []
    for k in ("cada 30 s", "cada 3 min", "cada 15 min", "cada hora"):
        v = d[k]
        rows.append([k, n(v[0], 0) + " s", n(v[1], 0) + " s", n(v[2], 0), n(v[3], 0) + " s"])
    return tab("Intervalo de reconciliación: cuánto vive una deriva manual y cuántas lecturas cuesta (200 aplicaciones)",
               "Tabla: reconciliar cada 30 segundos corrige una deriva manual en 15 segundos de media y 28 en el percentil 95 con 1 152 000 lecturas al día; cada 3 minutos, 91 y 171 segundos con 192 000 lecturas; cada 15 minutos, 453 y 857 con 38 400; cada hora, 1 803 y 3 417 con 9 600.",
               ["Intervalo", "Deriva: espera media", "Percentil 95", "Lecturas por día", "Cambio en Git sin aviso"], rows, [180, 210, 160, 180, 210], row_h=44, size=12,
               note="Bajar el intervalo de una hora a 30 segundos acorta la deriva en 120 veces y multiplica las lecturas por 120. Un aviso del repositorio (unos 2 s) resuelve los cambios en Git, no las derivas del clúster, que solo se ven al comparar. Las dos lecturas por ciclo y el reparto uniforme de las derivas son supuestos.",
               note_kind="gold", foot=SINT)


def se415_pelea() -> Fig:
    d = e415_pelea()
    a, b = d["el repositorio fija réplicas = 3"], d["el repositorio ignora el campo de réplicas"]
    rows = [["El repositorio fija «réplicas: 3»", str(a[0]), str(a[1]), str(a[2])],
            ["El repositorio omite el campo de réplicas", str(b[0]), str(b[1]), str(b[2])]]
    return tab("Un controlador de GitOps y un escalador automático que se disputan el número de réplicas (24 h, 1 440 minutos)",
               "Tabla: si el repositorio fija tres réplicas el sistema pasa 361 minutos con menos capacidad que carga, el escalador actúa 854 veces y el reconciliador revierte 425; si el repositorio omite el campo hay 0 minutos de capacidad insuficiente con 640 acciones del escalador y ninguna reversión.",
               ["Configuración", "Minutos sin capacidad", "Acciones del escalador", "Reversiones del reconciliador"], rows, [360, 190, 190, 200], row_h=52, size=12,
               note="Dos bucles de control que gobiernan el mismo campo no convergen: cada uno deshace al otro y el servicio paga 361 minutos de capacidad insuficiente. La solución es que el repositorio deje de declarar lo que otro actor decide (ignorar el campo), no subir la frecuencia de reconciliación. Carga sinusoidal con ruido; capacidad de 100 solicitudes por réplica: supuestos.",
               note_kind="coral", foot=SINT)


def se415_poda() -> Fig:
    d = e415_poda()
    rows = [[k, n(v[0], 2), n(v[1], 2)] for k, v in d.items()]
    return tab("Refactorizar manifiestos con poda activada: recursos borrados por cada refactorización que mueve archivos",
               "Tabla: sin poda, mover manifiestos no borra nada; con poda se borran en promedio 1,97 recursos por refactorización y 0,32 tienen estado; con poda y protección de los recursos con estado se borran 1,71 y ninguno tiene estado.",
               ["Política de poda", "Recursos borrados por refactorización", "De ellos, con estado"], rows, [430, 270, 230], row_h=52, size=13,
               note="Para el controlador, renombrar un recurso es «borrar el viejo y crear el nuevo»: con poda, una refactorización de apariencia inofensiva borra casi dos recursos, y uno de cada tres de esas refactorizaciones tocaría un volumen con datos. La protección explícita de lo que tiene estado cuesta una anotación. 15 % de manifiestos con estado: supuesto.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-416
def se416_reident() -> Fig:
    d = e416_reidentificacion()
    rows = [[k, pc(v[0], 1), pc(v[1], 1), pc(v[2], 1), str(v[3])] for k, v in d.items()]
    return tab("Datos de 6 000 estudiantes sintéticos sin nombre: unicidad y reidentificación por vinculación con una lista externa del 70 %",
               "Tabla: con fecha de nacimiento, código postal y género el 97,6 por ciento de las personas es único y el 97,6 por ciento de las de la lista externa se reidentifica; con año, código postal y género queda el 1,2 por ciento; con año, tres dígitos postales y género, el 0,02 por ciento único y ninguna reidentificación; con bienio y dos dígitos, ningún caso.",
               ["Cuasi-identificadores conservados", "Únicos", "Reidentificados", "En grupos de menos de 5", "Grupos"], rows, [380, 110, 160, 190, 110], row_h=52, size=12,
               note="Quitar el nombre no anonimiza: tres datos corrientes bastan para identificar a casi todas las personas. Generalizar reduce el riesgo a costa de detalle: con 12 grupos ya no se distingue casi nada. El 22,3 % de grupos pequeños con año y código postal completo recuerda que no basta con que casi nadie sea único. Población y lista externa sintéticas.",
               note_kind="coral", foot=SINT)


def se416_uniones() -> Fig:
    d = e416_uniones()
    nt = d["_notas"]
    rows = [
        ["Identificador sin enmascarar", pc(d["sin enmascarar"], 0), "sin cambio", "identifica a la persona"],
        ["Aleatorio por tabla", pc(d["aleatorio por tabla"], 0), "—", "rompe las pruebas que unen tablas"],
        ["Determinista con HMAC y sal", pc(d["determinista (HMAC con sal)"], 0), "—", "conserva las uniones; la sal es un secreto"],
        ["Notas con ruido gaussiano (σ = 1)", "—", f"media {n(nt['ruido'][0], 2)}, σ {n(nt['ruido'][1], 2)}, r {n(nt['ruido'][2], 2)}", "la desviación crece de 1,11 a 1,52"],
        ["Notas permutadas", "—", f"media {n(nt['permutación'][0], 2)}, σ {n(nt['permutación'][1], 2)}, r {n(nt['permutación'][2], 3)}", "conserva la distribución, borra la relación"],
    ]
    return tab("Enmascarar datos para una prueba: uniones que sobreviven y distribución de las notas (3 000 estudiantes, 15 000 entregas)",
               "Tabla: el enmascarado aleatorio por tabla conserva el 0 por ciento de las uniones entre estudiantes y entregas, el determinista con HMAC conserva el 100 por ciento; las notas con ruido mantienen la media 5,20 pero suben la desviación de 1,11 a 1,52; la permutación conserva la distribución y destruye la correlación con el original.",
               ["Técnica", "Uniones que sobreviven", "Distribución de las notas", "Consecuencia"], rows, [270, 160, 250, 270], row_h=56, size=12,
               note="Cada técnica protege algo y rompe otra cosa: el aleatorio protege la identidad y anula la prueba de integridad; el determinista conserva las uniones y permite vincular registros si se filtra la sal. No existe un enmascarado que conserve utilidad y privacidad sin decisión: hay que elegir qué se prueba con ese dato.",
               note_kind="gold", foot=SINT)


def se416_previews() -> Fig:
    d = e416_previews()
    base = d["solo se destruye al cerrar el PR"][0]
    rows = []
    for k in ("solo se destruye al cerrar el PR", "TTL de 72 h desde la creación", "TTL de 24 h renovado con cada push"):
        h, rec, orph = d[k]
        rows.append([k, n(h, 0), pc(h / base, 0), str(rec), str(orph)])
    return tab(f"Entornos de vista previa de {d['_prs']} PR en 60 días (8 por día, 15 % abandonados): horas de entorno según la política",
               "Tabla: destruir el entorno solo al cerrar el PR suma 74 357 horas de entorno y deja 64 huérfanos al final; un TTL de 72 horas desde la creación suma 33 383 horas (45 por ciento) con 186 recreaciones; un TTL de 24 horas renovado con cada push suma 30 460 horas (41 por ciento) con 293 recreaciones y ningún huérfano.",
               ["Política", "Horas de entorno", "Frente a «al cerrar»", "Recreaciones", "Huérfanos"], rows, [330, 160, 170, 150, 130], row_h=48, size=12,
               note="Los PR abandonados dominan el costo: el 15 % que nadie cierra consume más de la mitad de las horas. El TTL lo corta a cambio de recrear el entorno cuando alguien vuelve (186 o 293 veces). La actividad del PR (un push cada 14 h) y el abandono son supuestos; las horas se leen como razones, no como dinero.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-417
def se417_adopcion() -> Fig:
    d = e417_adopcion()
    rows = []
    for cov in (3, 4, 6):
        rows.append([f"El camino cubre {cov} de 6 capacidades"] + [f"{pc(d[cov][s][0], 0)} ({pc(d[cov][s][1], 0)} parcial)" for s in (4, 20, 60)])
    return tab("Equipos que adoptan el camino dorado según su cobertura y el esfuerzo de empezar (400 equipos por celda)",
               "Tabla: si el camino cubre 3 de 6 capacidades lo adopta el 31 por ciento con 4 horas de puesta en marcha, 16 con 20 y 2 con 60; si cubre 4, el 55, 33 y 5; si cubre las 6, el 100, 92 y 20 por ciento.",
               ["Cobertura del camino", "4 h para empezar", "20 h para empezar", "60 h para empezar"], rows, [300, 210, 210, 210], row_h=48, size=12,
               note="Un camino fácil de empezar pero incompleto lo adopta la mitad de los equipos y casi todos acaban improvisando lo que falta. Uno completo pero costoso de usar (60 h) casi nadie lo toma. La adopción no mide calidad: mide que el camino compite bien contra el costo de construirlo por cuenta propia (mediana de 40 h, supuesto del autor).",
               note_kind="gold", foot=SINT)


def se417_catalogo() -> Fig:
    d = e417_catalogo()
    rows = [[k, str(v), pc(v / d["_total"], 0)] for k, v in d.items() if not k.startswith("_")]
    rows.append(["Entradas con algún problema sembrado (dueño, enlace o revisión)", str(d["_con_problema"]), pc(d["_con_problema"] / d["_total"], 0)])
    return tab("Un catálogo de 150 servicios: entradas que pasan según el rigor de la validación",
               "Tabla: comprobar solo que los campos existan aprueba 130 de 150 entradas; exigir que el dueño exista en el registro de equipos, 122; que el enlace no sea de relleno, 108; que la revisión sea de los últimos 180 días, 43; hay 107 entradas con algún problema sembrado.",
               ["Validación acumulada", "Entradas que pasan", "Fracción"], rows, [520, 200, 170], row_h=48, size=12,
               note="Con la validación de presencia el catálogo parece completo al 87 % y en realidad solo 43 entradas (29 %) están al día. Medir la completitud por campos lleno invita a rellenar con «TBD»; comprobar contra otra fuente (el registro de equipos, la fecha de revisión) es lo que distingue completo de actual. Las proporciones de problemas son supuestos del autor.",
               note_kind="coral", foot=SINT)


def se417_cola() -> Fig:
    d = e417_cola()
    rows = []
    for lam, v in d.items():
        rows.append([f"{n(float(lam), 2)} solicitudes por hora", pc(v[0], 0), n(v[1], 1) + " h", n(v[2], 1) + " h"])
    return tab("Aprovisionar por ticket con dos personas de plataforma (3 horas por solicitud): espera antes de empezar",
               "Tabla: con 0,2 solicitudes por hora la utilización es del 30 por ciento y la espera media 0,3 horas; con 0,4 la utilización es del 60 por ciento y la espera media 1,7 horas con 5,7 en el percentil 90; con 0,55 la utilización es del 83 por ciento y la espera media 6,4 horas con 16,6 en el percentil 90.",
               ["Demanda", "Utilización", "Espera media", "Espera p90"], rows, [330, 190, 200, 200], row_h=44, size=13,
               note="La espera no crece proporcionalmente: al subir la demanda 2,75 veces (de 0,2 a 0,55), la espera media se multiplica por 22. Es la misma curva de saturación de la cola de SE-376 aplicada a un equipo humano. El autoservicio saca el tiempo de espera de la cola, a cambio de construir y mantener la automatización. Servicio exponencial de 3 h: supuesto.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-418
def se418_definiciones() -> Fig:
    d = e418_definiciones()
    f, p, fl, rs = d["frecuencia"], d["plazo"], d["fallos"], d["restauracion"]
    rows = [
        ["Frecuencia de despliegue", f"{n(f['por servicio y semana (media)'], 1)} por servicio y semana", f"{n(f['del conjunto por semana'], 1)} del conjunto", f"{n(f['solo producción de los dos servicios mayores'], 1)} solo dos servicios"],
        ["Plazo de entrega (mediana)", f"{n(p['desde el primer commit (mediana)'], 1)} h desde el primer commit", f"{n(p['desde que se abre el PR (mediana)'], 1)} h desde el PR", f"{n(p['desde la fusión (mediana)'], 1)} h desde la fusión"],
        ["Tasa de fallos", pc(fl["fallos con incidente"], 1) + " con incidente", pc(fl["solo los que se revierten"], 1) + " solo revertidos", "—"],
        ["Recuperación tras un despliegue fallido", f"{n(rs['mediana (h)'], 2)} h mediana", f"{n(rs['media (h)'], 2)} h media", "—"],
    ]
    return tab(f"Cuatro métricas de entrega (de las cinco de DORA) calculadas del mismo registro de {n(d['_n'], 0)} despliegues de 6 servicios en 52 semanas",
               "Tabla: la frecuencia de despliegue es 3,5 por servicio y semana o 21 del conjunto; el plazo de entrega mediano es 32 horas desde el primer commit, 29 desde el PR y 4,6 desde la fusión; la tasa de fallos es 11,4 por ciento con incidente o 6,3 por ciento solo con retroceso; la restauración tiene mediana de 0,64 horas y media de 1,01.",
               ["Métrica", "Definición A", "Definición B", "Definición C"], rows, [220, 260, 240, 200], row_h=56, size=12,
               note="Un mismo registro produce plazos de 4,6 a 32 horas y tasas de fallos de 6,3 % a 11,4 % según dónde empiece y qué cuente la definición. Comparar un número entre equipos que definen distinto no compara equipos. La media y la mediana de la restauración difieren un 57 % porque pocos incidentes son largos. Registro sintético.",
               note_kind="gold", foot=SINT)


def se418_gaming() -> Fig:
    d = e418_gaming()
    rows = []
    for k, v in d.items():
        rows.append([k, n(v[0], 0), pc(v[1], 1), n(v[2], 1) + " h", n(v[3], 2), n(v[4], 0)])
    return tab("Una métrica se vuelve meta: el mismo trabajo y los mismos defectos en 26 semanas",
               "Tabla: sin incentivo hay 4 despliegues por semana, 24 por ciento de fallos y plazo mediano de 32 horas; con despliegues vacíos, 16 por semana, 6 por ciento y 0,1 horas; partiendo los cambios en tres, 30 por semana, 3,2 por ciento y 8 horas; en los tres casos hay 0,96 defectos por semana y 10 cambios de valor.",
               ["Caso", "Despliegues por semana", "Tasa de fallos", "Plazo mediano", "Defectos por semana", "Cambios de valor"], rows, [320, 120, 120, 120, 130, 110], row_h=60, size=12,
               note="Las tres métricas mejoraron (más frecuencia, menos fallos, menos plazo) y el trabajo entregado (10 cambios) y los defectos (0,96 por semana) son idénticos. Partir cambios puede ser una buena práctica real, pero medido por el ratio sale lo mismo que el truco de los despliegues vacíos. La defensa es mirar las métricas juntas con una medida de valor y desconfiar de la que mejora sola.",
               note_kind="coral", foot=SINT)


def se418_ruido() -> Fig:
    d = e418_ruido()
    rows = [[f"{k} despliegues al mes", n(v[2] * 100, 1) + " puntos", pc(v[0], 0), pc(v[1], 0)] for k, v in d.items()]
    return tab("Ruido de la tasa de fallos mensual (verdadera 12 %): dos equipos idénticos y una mejora real de 12 % a 8 %",
               "Tabla: con 8 despliegues al mes el intervalo del 95 por ciento mide ±22,5 puntos, dos equipos idénticos difieren en 5 puntos o más el 69 por ciento de los meses y una mejora real del 12 al 8 por ciento se ve en el 42 por ciento; con 30, ±11,6 puntos, 55 y 61 por ciento; con 100, ±6,4 puntos, 29 y 80 por ciento.",
               ["Volumen", "Semiancho del intervalo", "Equipos idénticos que difieren ≥ 5 puntos", "Mejora real que se ve"], rows, [260, 200, 280, 200], row_h=56, size=12,
               note="Con el volumen de un equipo pequeño, comparar la tasa mensual de dos equipos es comparar ruido: casi siete de cada diez meses difieren cinco puntos sin que nada haya cambiado. La tendencia sobre muchos meses o un intervalo declarado dicen más que un ranking mensual. Simulación binomial con semilla fija; el intervalo es el de Wald.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-419
def se419_pasos() -> Fig:
    d = e419_endurecer()
    rows = [[("0. " if i == 0 else f"{i}. ") + name, str(c)] for i, (name, c, _) in enumerate(d["pasos"])]
    return tab("Endurecer un workflow vulnerable paso a paso: hallazgos del verificador tras cada cambio",
               "Tabla: el workflow original tiene 8 hallazgos; cada uno de los 8 cambios elimina exactamente uno (fijar la acción a un SHA, permisos mínimos, pull_request en lugar de pull_request_target, título por variable de entorno, script versionado, no escribir el secreto, que el trabajo falle cuando falla, sin credencial en el texto) y el final tiene 0.",
               ["Cambio aplicado", "Hallazgos restantes"], rows, [640, 230], row_h=42, size=12,
               note="Cada cambio es pequeño y elimina un hallazgo concreto: no se reescribe la canalización. Que el verificador llegue a 0 no prueba que el workflow sea seguro, solo que no contiene las ocho formas que sabe buscar. La credencial del texto, además, sigue en el historial: borrarla del archivo no la revoca.",
               note_kind="gold", foot=SINT)


def se419_inyeccion() -> Fig:
    d = e419_inyeccion()
    rows = []
    for text, res, ok in d["filas"]:
        label = text if len(text) < 46 else text[:43] + "…"
        rows.append([label, {"ejecuta": "se ejecuta como código", "inerte": "inerte", "rompe": "rompe el programa"}[res], "inerte" if ok else "alterado"])
    return tab("Insertar un título en un programa antes de ejecutarlo o pasarlo como dato (6 títulos, ejecución real)",
               "Tabla: expandir el título dentro del texto del programa ejecuta 4 de los 6 títulos como código, incluidos los que imprimen INYECTADO y evalúan una operación; pasar el título por una variable de entorno deja los 6 como datos.",
               ["Título de entrada", "Expandido en el programa", "Por variable de entorno"], rows, [400, 270, 220], row_h=44, size=12,
               note="El mecanismo es el de una expresión de workflow dentro de un script: el texto se sustituye antes de que el intérprete lo lea, así que una comilla y un paréntesis lo convierten en código. Aquí el intérprete es Python y la carga es inofensiva; el principio no cambia con el intérprete. Se ejecuta de verdad en cada máquina.",
               note_kind="coral", foot=SINT)


def se419_permisos() -> Fig:
    p = e419_permisos()
    pin = e419_pin()
    jobs = list(p["write-all"])
    rows = [[j, str(p["write-all"][j]) + " de " + str(p["ambitos"]), str(p["mínimo"][j])] for j in jobs]
    rows.append(["Etiqueta de una acción de terceros movida", "el contenido cambia (no coincide con la huella fijada)" if pin["etiqueta_cambio"] else "—", "la referencia por SHA no cambia"])
    return tab("Ámbitos con escritura del token por job con «write-all» frente al mínimo, y la etiqueta que se mueve",
               "Tabla: con permisos de escritura generales cada job de la canalización recibe escritura en 16 ámbitos; con el mínimo, lint y pruebas reciben 0, la construcción 1, la publicación 3 y el despliegue 2; si alguien mueve la etiqueta de una acción, su contenido deja de coincidir con la huella que se había fijado, mientras que la referencia por SHA no cambia.",
               ["Job o situación", "Con permisos amplios", "Con el mínimo (escrituras)"], rows, [360, 330, 220], row_h=56, size=12,
               note="Un job de lint con escritura en 16 ámbitos es una superficie de ataque sin función; el mínimo reduce el daño que hace una acción comprometida. La etiqueta es un puntero mutable; el SHA identifica contenido. La lista de 16 ámbitos con escritura sale de la página de sintaxis consultada el 15 de noviembre de 2026 y puede cambiar.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-420
def se420_rollback() -> Fig:
    d = e420_rollback()
    rows = []
    for k in ("renombrar de golpe", "expandir sin doble escritura", "expandir con doble escritura", "contraer antes de tiempo"):
        e, nul, ok = d[k]
        rows.append([k, str(e), str(nul), str(ok)])
    return tab("Volver a la versión anterior de la aplicación tras migrar el esquema (SQLite en memoria, 10 lecturas)",
               "Tabla: renombrar la columna de golpe hace que la versión anterior falle en las 10 lecturas; expandir sin doble escritura deja 5 lecturas bien y 5 vacías; expandir con doble escritura deja las 10 bien; contraer antes de tiempo vuelve a fallar en las 10.",
               ["Estrategia de migración", "Lecturas con error", "Lecturas vacías", "Lecturas correctas"], rows, [380, 190, 170, 170], row_h=44, size=13,
               note="Volver atrás el código no revierte los datos: la reversión funciona solo si el esquema en producción todavía es compatible con la versión anterior. La doble escritura mantiene esa compatibilidad y contraer (borrar lo viejo) la rompe: se hace en un despliegue posterior, cuando ya no hay vuelta atrás prevista. Ejecución real con sqlite3.",
               note_kind="coral", foot=SINT)


def se420_ablacion() -> Fig:
    d = e420_ablacion()
    rows = []
    for g in ("revisión y lint", "pruebas unitarias", "pruebas de integración", "escaneo de dependencias y secretos", "política sobre el plan de infraestructura", "humo en preproducción", "canario con métricas", "alerta en producción"):
        later, esc, cost = d[g]
        rows.append([g, str(later), str(esc), n(cost, 0)])
    return tab(f"Quitar una compuerta cada vez: 12 fallos tipo; costo relativo total sin ninguna ausencia: {n(d['_base_coste'], 0)}",
               "Tabla: quitar el escaneo de dependencias y secretos deja 2 fallos sin detectar y sube el costo de 214 a 802; quitar la política del plan, 1 sin detectar y 604; quitar el canario retrasa la detección de 3 fallos y sube el costo a 439; quitar lint, pruebas unitarias o integración retrasa 1 fallo cada una.",
               ["Compuerta que se quita", "Fallos que se detectan más tarde", "Fallos que escapan", "Costo relativo"], rows, [380, 190, 160, 160], row_h=48, size=12,
               note="Las compuertas baratas retrasan poco, las únicas para una clase de fallo hacen escapar: el escaneo es la única que ve un secreto o una dependencia vulnerable. La matriz de qué compuerta ve qué fallo es juicio del autor, y los costos (1 a 100) son relativos; el ejercicio es construir la propia y ver qué fallos solo tienen un guardián.",
               note_kind="gold", foot=SINT)


def se420_paquete() -> Fig:
    d = e420_paquete()
    ops = d["ops"]
    groups = {}
    for name, (kind, a, b, c) in ops.items():
        g = groups.setdefault(kind, [0, 0, 0, 0])
        g[0] += 1; g[1] += a; g[2] += b; g[3] += c
    names = {"forma": "Forma (campo ausente, commit o digest mal escritos)", "cruce": "Cruce entre campos (digest o commit distinto, autoaprobación, ensayo caducado)", "verosimilitud": "Verosimilitud (0 segundos, entorno ajeno, canario sin tráfico)", "juicio": "Juicio (ensayo copiado, aprobador sin permisos reales)"}
    rows = []
    for kind in ("forma", "cruce", "verosimilitud", "juicio"):
        g = groups[kind]
        total = g[0] * d["n"]
        rows.append([names[kind], f"{g[1]} de {total}", f"{g[2]} de {total}", f"{g[3]} de {total}"])
    tot = d["n"] * len(ops)
    rows.append(["Todas las mutaciones", f"{sum(v[1] for v in ops.values())} de {tot}", f"{sum(v[2] for v in ops.values())} de {tot}", f"{sum(v[3] for v in ops.values())} de {tot}"])
    return tab("Un validador del paquete de evidencia frente a 120 mutaciones (12 operadores × 10 paquetes)",
               "Tabla: un validador de forma detecta 30 de las 120 mutaciones, uno que cruza campos detecta 70 y uno con reglas de verosimilitud 100; las 20 mutaciones de juicio, como un ensayo copiado de otra versión o un aprobador sin permisos reales, no las ve ninguno; los 10 paquetes sin mutar pasan en los tres.",
               ["Tipo de mutación", "Solo forma", "+ cruce de campos", "+ verosimilitud"], rows, [440, 150, 170, 150], row_h=60, size=12,
               note="Cada capa de validación añade lo que la anterior no podía ver y todas dejan pasar la mutación que parece correcta: un ensayo copiado de otra versión tiene forma, cruces y duración verosímiles. Eso solo lo detecta una persona que conozca el sistema o una comprobación contra el sistema real. Mutaciones y reglas escritas por el mismo autor.",
               note_kind="coral", foot=SINT)


FIGURES = {
    "se-415-intervalo-de-reconciliacion.svg": se415_bucle,
    "se-415-controladores-que-se-disputan.svg": se415_pelea,
    "se-415-poda-y-recursos-con-estado.svg": se415_poda,
    "se-416-reidentificacion-sin-nombre.svg": se416_reident,
    "se-416-uniones-y-distribucion-enmascaradas.svg": se416_uniones,
    "se-416-costo-de-entornos-de-vista-previa.svg": se416_previews,
    "se-417-adopcion-del-camino-dorado.svg": se417_adopcion,
    "se-417-catalogo-completo-o-actual.svg": se417_catalogo,
    "se-417-espera-del-aprovisionamiento-por-ticket.svg": se417_cola,
    "se-418-un-registro-cuatro-definiciones.svg": se418_definiciones,
    "se-418-cuando-la-metrica-es-la-meta.svg": se418_gaming,
    "se-418-ruido-de-la-tasa-de-fallos.svg": se418_ruido,
    "se-419-hallazgos-tras-cada-cambio.svg": se419_pasos,
    "se-419-inyeccion-en-el-script.svg": se419_inyeccion,
    "se-419-permisos-y-fijacion-por-huella.svg": se419_permisos,
    "se-420-retroceso-tras-migrar-el-esquema.svg": se420_rollback,
    "se-420-quitar-una-compuerta.svg": se420_ablacion,
    "se-420-validador-del-paquete-de-evidencia.svg": se420_paquete,
}
