"""Figures for SE-409 to SE-414 (synthetic data, fixed seeds, virtual time; CPython 3.12.9 on Windows 11 and 3.12.3 on Ubuntu/WSL2)."""
from __future__ import annotations

from experiments_part34_a import (e409_cola, e409_lotes, e409_ramas, e410_cache, e410_dag, e410_matriz, e411_orden, e411_politicas,
                                  e411_reintentos, e412_escaner, e412_tokens, e412_ventana, e413_banderas, e413_despliegue,
                                  e413_potencia, e414_deriva, e414_estado, e414_plan)
from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos con semilla fija y tiempo virtual; Windows y Ubuntu (WSL2) dan cifras idénticas."


def n(x: float, d: int = 1) -> str:
    """Spanish number: decimal comma, space as thousands separator."""
    s = f"{x:,.{d}f}".replace(",", " ").replace(".", ",")
    return s


def pc(x: float, d: int = 1) -> str:
    return n(x * 100, d) + " %"


# ---------------------------------------------------------------- SE-409
def se409_ramas() -> Fig:
    d = e409_ramas()
    rows = [[f"{n(k, 1) if k < 1 else int(k)} día{'s' if k != 1 else ''}", pc(v[0], 0), n(v[1], 1)] for k, v in d.items()]
    return tab("Vida de una rama y choque de archivos con la troncal (8 personas, 400 archivos con puntos calientes)",
               "Tabla: con una rama de medio día el 21 por ciento de las ramas toca algún archivo que otra persona también cambió; con un día el 49 por ciento, con dos días el 89 por ciento y con cinco días o más prácticamente todas, con 6 a 31 archivos en choque.",
               ["Vida de la rama", "Ramas con algún archivo en choque", "Archivos en choque (media)"], rows, [260, 380, 300], row_h=44, size=13,
               note="La probabilidad de choque no crece de forma lineal sino saturada: pasa de 21 % a 89 % en un día y medio y después ya no puede empeorar, aunque el trabajo por resolver sigue creciendo (de 0,2 a 31 archivos). Los puntos calientes (los archivos que todos tocan) y las tres modificaciones diarias por persona son supuestos del autor.",
               note_kind="gold", foot=SINT)


def se409_lotes() -> Fig:
    d = e409_lotes()
    rows = [[str(k), pc(v[0], 1), n(v[1], 2)] for k, v in d.items()]
    return tab("Integrar por lotes: cuántas veces se construye hasta aislar cada cambio defectuoso (24 000 cambios, 4 % defectuosos)",
               "Tabla: con un cambio por lote cada cambio exige 1,00 construcciones; con lotes de 5 baja a 0,38; el mínimo está en lotes de 10 con 0,35 construcciones por cambio y el 33 por ciento de los lotes rojos; con lotes de 50 el 85 por ciento de los lotes sale rojo y se vuelve a 0,37.",
               ["Cambios por lote", "Lotes en rojo", "Construcciones por cambio (con bisección)"], rows, [260, 300, 380], row_h=44, size=13,
               note="Agrupar ahorra construcciones hasta unos 10 cambios por lote y deja de ahorrar: con 50 cambios casi todos los lotes salen rojos y hay que aislar a mano. El ahorro se paga con retraso: el cambio bueno espera al lote y el defectuoso se localiza más tarde. El 4 % de defectos por cambio y la independencia entre cambios son supuestos.",
               note_kind="gold", foot=SINT)


def se409_cola() -> Fig:
    d = e409_cola()
    rows = [[f"{n(k, 2) if k < 1 else int(k)} día{'s' if k != 1 else ''}", n(v[0], 0), "0 (se detectan al entrar)"] for k, v in d.items()]
    return tab("Troncal rota por un choque semántico entre dos cambios que pasan por separado (por cada 1 000 integraciones)",
               "Tabla: si cada cambio solo se prueba contra su base, la troncal queda en rojo 54 veces por cada mil integraciones cuando los cambios viven un cuarto de día, 213 con un día y 490 con tres días; una cola que prueba el resultado combinado los detecta antes de integrar.",
               ["Vida del cambio", "Troncal en rojo sin cola (por 1 000)", "Con cola de integración"], rows, [260, 380, 300], row_h=44, size=13,
               note="El choque no está en ningún cambio por separado: aparece en la combinación. Con 12 cambios al día y una probabilidad de choque del 2 % por pareja solapada, vivir tres días multiplica por nueve la tasa de troncal rota. La cola no elimina el choque: lo convierte en un rechazo al entrar, antes de que lo vea el resto del equipo.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-410
def se410_dag() -> Fig:
    d = e410_dag()
    items = []
    for k in (1, 2, 3, 4, 8):
        kind = "coral" if k == 1 else ("teal" if k >= 4 else "gold")
        items.append((f"{k} ejecutor{'es' if k > 1 else ''}", d[k][0], kind, f"{n(d[k][0], 1)} min"))
    items.append(("Camino crítico", d["critico"], "navy", f"{n(d['critico'], 1)} min"))
    return bars("Duración de la misma canalización de 9 jobs según el número de ejecutores",
                "Barras: con un ejecutor la canalización tarda 46,5 minutos; con dos 26,5, con tres 23,5 y con cuatro u ocho 22 minutos, que es el camino crítico; más ejecutores no la acortan.",
                items, 14.0, "El trabajo total son 46,5 minutos (con 0,5 min de arranque por job); el camino crítico (preparar, compilar, pruebas e2e, empaquetar) es de 22. Pasar de 1 a 4 ejecutores ahorra 24,5 minutos; pasar de 4 a 8 no ahorra nada pero sí cuesta. Las duraciones de los jobs son supuestos del autor.",
                label_w=150, width=940, note_kind="gold", foot=SINT)


def se410_matriz() -> Fig:
    d = e410_matriz()
    rows = []
    for name in ("completa", "pareja a pareja", "una a la vez", "9 al azar"):
        v = d[name]
        rows.append([name, str(v[0]), pc(v[1], 0), pc(v[2], 0), pc(v[3], 0)])
    return tab("Matriz 3 sistemas × 4 versiones × 3 bases (36 combinaciones): qué defectos encuentra cada estrategia",
               "Tabla: la matriz completa de 36 combinaciones encuentra el 100 por ciento de los defectos de uno, dos y tres factores; pareja a pareja con 12 combinaciones encuentra el 100 por ciento de los de uno y dos factores y el 39 por ciento de los de tres; una a la vez con 8 combinaciones, el 52 y el 28 por ciento; nueve al azar, el 99, el 62 y el 23 por ciento.",
               ["Estrategia", "Combinaciones", "Defecto de 1 factor", "De 2 factores", "De 3 factores"], rows, [250, 150, 190, 170, 170], row_h=44, size=13,
               note="Cubrir todas las parejas con 12 de 36 combinaciones no deja escapar ningún defecto de dos factores pero sí el 61 % de los de tres. Una a la vez mira cada nivel pero no las interacciones. Cada defecto es de un solo tipo y se eligió al azar entre 400 conjuntos; la distribución real de defectos de interacción es desconocida.",
               note_kind="gold", foot=SINT)


def se410_cache() -> Fig:
    d = e410_cache()
    order = ["hash del lockfile", "hash + respaldo", "SHA del commit", "clave fija"]
    rows = [[k, pc(d[k][0], 0), pc(d[k][1], 0), n(d[k][2], 1) + " s", pc(d[k][3], 0)] for k in order]
    return tab("Cuatro claves de caché en 600 construcciones (la dependencia cambia en el 10 % de ellas)",
               "Tabla: la clave con el hash del lockfile acierta el 89 por ciento de las veces y tarda 26,6 segundos de instalación media; con respaldo por prefijo baja a 12,2 segundos con 11 por ciento de restauraciones parciales; la clave con el SHA del commit acierta el 17,5 por ciento y tarda 149,9 segundos; una clave fija siempre acierta pero el 97 por ciento de las construcciones usa dependencias obsoletas.",
               ["Clave de la caché", "Aciertos", "Parciales", "Instalación media", "Entorno obsoleto"], rows, [260, 130, 140, 220, 190], row_h=44, size=13,
               note="Una clave fija da el mejor tiempo (8 s) y el peor resultado: el 97 % de las construcciones corre con dependencias que ya no coinciden con el lockfile. El tiempo ahorrado no compensa un resultado que no es reproducible. Los tiempos de 180, 45 y 8 segundos son supuestos del autor.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-411
def se411_orden() -> Fig:
    d = e411_orden()
    items = [
        ("Barato primero", d["barato primero"][0], "teal", f"{n(d['barato primero'][0], 1)} min"),
        ("Media de las 120 órdenes", d["media de 120 órdenes"][0], "gold", f"{n(d['media de 120 órdenes'][0], 1)} min"),
        ("Caro primero", d["caro primero"][0], "coral", f"{n(d['caro primero'][0], 1)} min"),
    ]
    return bars("Minutos esperados hasta ver el primer rojo en un build fallido, según el orden de cinco etapas",
                "Barras: ordenar las etapas de la más barata a la más cara da 7,4 minutos hasta el primer rojo; la media de las 120 órdenes posibles es 15,4 y el orden inverso, 23,4 minutos.",
                items, 26.0, "Las cinco etapas (lint 0,3 min, tipos 1, unitarias 3, integración 8, e2e 14) y la fracción de fallos que detecta cada una son supuestos del autor. El orden por razón probabilidad/costo coincide con el óptimo de las 120 permutaciones. Un build verde cuesta 26,3 min en cualquier orden: ordenar solo ayuda a los rojos.",
                label_w=230, width=940, note_kind="gold", foot=SINT)


def se411_politicas() -> Fig:
    d = e411_politicas()
    rows = []
    for label in ("ingenua", "afinada"):
        tp, fp, fn = d[label]
        rows.append([f"Reglas {label}", str(tp), str(fp), str(fn), pc(tp / (tp + fp), 0), pc(tp / (tp + fn), 0)])
    fpr = d["_fp_regla"]
    rows.append(["Falsos positivos de la ingenua por regla", f"inyección {fpr['inyeccion']}", f"target {fpr['target_checkout']}", f"curl {fpr['curl_bash']}", "—", "—"])
    return tab("Reglas de texto sobre 160 workflows con 8 clases de defecto sembrado y 6 señuelos",
               "Tabla: sobre 209 defectos sembrados, las reglas ingenuas encuentran todos pero producen 180 falsas alarmas (precisión 54 por ciento); las afinadas reducen las falsas alarmas a 45 y pierden 5 defectos (precisión 82 por ciento y exhaustividad 98 por ciento).",
               ["Conjunto de reglas", "Aciertos", "Falsos positivos", "Defectos no vistos", "Precisión", "Exhaustividad"], rows, [330, 120, 170, 170, 130, 150], row_h=48, size=12,
               note="Las reglas ingenuas ven todo y avisan de demasiado: por eso un equipo las desactiva. Las afinadas ignoran comentarios y acciones locales, pero se equivocan donde el defecto cambia de forma (un bloque de varias líneas) y donde el valor es seguro (el número del PR). Se afinaron con los mismos señuelos que las evalúan: son una frontera, no una tasa.",
               note_kind="gold", foot=SINT)


def se411_reintentos() -> Fig:
    d = e411_reintentos()
    rows = []
    for m in (0.5, 0.2, 0.05):
        row = d["defecto"][m]
        rows.append([f"Defecto que aparece en el {pc(m, 0)} de las ejecuciones"] + [pc(row[k], 1) for k in (0, 1, 2)])
    rr = d["rojos_falsos"]
    rows.append(["Rojo falso por pruebas inestables (600 pruebas, 0,05 % cada una)"] + [pc(rr[k], 3) for k in (0, 1, 2)])
    return tab("Reintentar pruebas: porcentaje de ejecuciones que pasan con 0, 1 o 2 reintentos",
               "Tabla: un defecto real que aparece en el 20 por ciento de las ejecuciones pasa el 80 por ciento sin reintentos, el 96 con uno y el 99 con dos; los rojos falsos por pruebas inestables bajan de 25,9 por ciento a 0,015 por ciento con un reintento.",
               ["Situación", "Sin reintentos", "1 reintento", "2 reintentos"], rows, [450, 160, 160, 170], row_h=52, size=12,
               note="El reintento hace desaparecer los rojos falsos (25,9 % → 0,015 %) y también hace pasar los defectos intermitentes: uno que aparece 1 vez de 5 pasa el 99,2 % con dos reintentos. Reintentar sin registrar qué se reintentó convierte una señal en ruido silencioso; hay que contar los reintentos y cuarentenar la prueba.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-412
def se412_tokens() -> Fig:
    d = e412_tokens()
    order = ["solo firma", "firma + vigencia", "+ emisor y audiencia", "+ sujeto con prefijo «repo:org»", "+ sujeto exacto y vida corta"]
    rows = [[k, f"{d[k][0]} de {d['_n']}", f"{d[k][2]} de {d['_legit']}", ", ".join(d[k][1][:3]) + ("…" if len(d[k][1]) > 3 else "") if d[k][1] else "ninguno"] for k in order]
    return tab("Verificar un token de identidad con más o menos comprobaciones: 12 tokens manipulados y 3 legítimos",
               "Tabla: verificar solo la firma acepta 9 de 12 tokens manipulados; añadir vigencia, 6; añadir emisor y audiencia, 4; comprobar el sujeto con un prefijo sigue aceptando 4, incluido un repositorio de otra organización con nombre parecido; el sujeto exacto con vida corta no acepta ninguno y sigue aceptando los 3 legítimos.",
               ["Comprobaciones", "Manipulados aceptados", "Legítimos aceptados", "Primeros que se cuelan"], rows, [330, 170, 160, 290], row_h=52, size=12,
               note="El prefijo «repo:org» deja pasar «repo:org-malicioso/…» y todos los repositorios de la organización: no basta con que el sujeto empiece bien. Solo el sujeto exacto (repositorio, rama o entorno) y una vida de 15 min dejan fuera a los 12. Los tokens y la clave son sintéticos y firmados con HMAC, no con la clave pública de un proveedor.",
               note_kind="gold", foot=SINT)


def se412_ventana() -> Fig:
    d = e412_ventana()
    items = []
    for k, v in d.items():
        kind = "coral" if v[0] > 0.5 else ("gold" if v[0] > 0.01 else "teal")
        items.append((k, v[0] * 100, kind, f"{pc(v[0], 1)} · {n(v[1], 1)} h"))
    return bars("Probabilidad de que una credencial filtrada siga siendo útil y horas de exposición media",
                "Barras: un secreto estático con rotación anual o de 90 días es utilizable en el 99,9 y el 99,8 por ciento de las filtraciones con unas 330 y 310 horas de exposición; un token de una hora, en el 4,8 por ciento con 0,5 horas; uno de 15 minutos, en el 0,18 por ciento con 0,12 horas.",
                items, 5.2, "La exposición del secreto estático la fija el tiempo en detectar la fuga (14 días supuestos), no la rotación: rotar cada 90 días en vez de cada año apenas la cambia. Que el token dure 15 minutos limita el daño aunque se filtre. El atacante con mediana de 3 h (lognormal) y la detección a 14 días son supuestos del autor.",
                label_w=290, width=1000, note_kind="gold", foot=SINT)


def se412_escaner() -> Fig:
    d = e412_escaner
    d = d()
    rows = []
    for k in ("prefijos conocidos", "entropía", "asignación sospechosa", "prefijos + asignación"):
        tp, fp, fn = d[k]
        rows.append([k, str(tp), str(fp), str(fn), pc(tp / (tp + fp), 0), pc(tp / (tp + fn), 0)])
    return tab(f"Buscar secretos en {d['_lineas']} líneas sintéticas con {d['_secretos']} secretos sembrados",
               "Tabla: buscar prefijos conocidos no da falsos positivos pero pierde 202 de 460 secretos; la entropía encuentra 343 pero señala 414 identificadores y hashes que no son secretos; buscar asignaciones sospechosas encuentra 393 con 4 falsos positivos y pierde 67 secretos con otra forma, como una cabecera Bearer o una URL con credencial.",
               ["Detector", "Aciertos", "Falsos positivos", "Secretos perdidos", "Precisión", "Exhaustividad"], rows, [270, 120, 170, 170, 120, 150], row_h=44, size=12,
               note="Cada detector ve una forma y ciega ante otra: la entropía confunde 170 SHA de git, 153 UUID y 91 imágenes en base64 con secretos y aun así pierde las contraseñas de baja entropía. Un detector no sustituye a la rotación: lo que encuentra ya estaba expuesto. Los secretos y señuelos son cadenas inventadas.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-413
def se413_despliegue() -> Fig:
    d = e413_despliegue()
    rows = []
    for k, v in d.items():
        rows.append([k, n(v[0], 0), n(v[1], 0), n(v[2], 1) + " min", pc(v[4], 1)])
    return tab("Una versión con 4 puntos de error adicional a 100 solicitudes por segundo: solicitudes fallidas hasta el retroceso (600 repeticiones)",
               "Tabla: si la versión mala se despliega de una vez fallan 240 solicitudes de media y 268 en el percentil 95; con cuatro tandas, 59 y 72; con un canario del 1 por ciento al 100 por ciento, 6 y 9; las tres estrategias la detectan el 100 por ciento de las veces y provocan retrocesos falsos entre el 0,5 y el 2,3 por ciento de las versiones buenas.",
               ["Estrategia", "Fallos medios", "Fallos p95", "Detección media", "Retrocesos falsos"], rows, [350, 140, 130, 170, 150], row_h=48, size=12,
               note="El canario reduce el daño en un 98 % no porque detecte antes (2,4 min frente a 1) sino porque solo lo ve una fracción del tráfico. La detección es estadística: con 1 % del tráfico y umbral estricto hay que esperar. Un retroceso falso cuesta una versión buena perdida. Poisson y normal aproximan al binomial; error base 0,5 %.",
               note_kind="gold", foot=SINT)


def se413_potencia() -> Fig:
    d = e413_potencia()
    rows = []
    for share in (0.01, 0.05, 0.25):
        row = [pc(share, 0) + " del tráfico"]
        for ex in (0.005, 0.01, 0.02, 0.04):
            row.append(pc(d[f"{share}|{ex}"][2], 1))
        rows.append(row)
    return tab("Probabilidad de detectar una subida del error en 10 minutos de canario (error base 0,5 %, umbral 0,1 %)",
               "Tabla: con el 1 por ciento del tráfico una subida de 0,5 puntos se detecta el 4 por ciento de las veces, una de 1 punto el 29, una de 2 puntos el 88 y una de 4 puntos el 99,98; con el 5 por ciento del tráfico, el 60, 99,6, 100 y 100; con el 25 por ciento todas superan el 99,99 por ciento.",
               ["Tráfico del canario", "+0,5 puntos", "+1 punto", "+2 puntos", "+4 puntos"], rows, [250, 170, 170, 170, 170], row_h=44, size=13,
               note="Un canario del 1 % no ve una degradación sutil: 600 solicitudes en 10 minutos dan 3 errores esperados y el umbral exige 11. La potencia depende del tráfico, no de la voluntad de mirar. Si el servicio recibe poco tráfico, el canario es un trámite. Cálculo exacto con la cola de Poisson (normal si la media supera 50).",
               note_kind="coral", foot=SINT)


def se413_banderas() -> Fig:
    d = e413_banderas()
    rows = [[str(k), n(d[k][0], 0), str(d[k][1]), pc(d[k][1] / d[k][0], 1)] for k in (2, 4, 6, 8, 10)]
    vivas = d["_vivas"]
    return tab("Banderas de funcionalidad: configuraciones posibles frente a las necesarias para cubrir todas las parejas",
               "Tabla: con 2 banderas hay 4 configuraciones y hacen falta las 4; con 6 hay 64 y bastan 7; con 8 hay 256 y bastan 8; con 10 hay 1 024 y bastan 9, el 0,9 por ciento; tras 12 meses creando 3 banderas al mes quedan 36 si no se retiran y unas 12 si se retira el 25 por ciento cada mes.",
               ["Banderas binarias", "Configuraciones", "Para cubrir parejas", "Fracción"], rows, [260, 220, 250, 190], row_h=44, size=13,
               note=f"Cubrir las parejas cuesta casi nada, pero no cubre las interacciones de tres banderas ni el comportamiento de las que nadie recuerda. Con 3 banderas nuevas al mes y ninguna retirada hay {vivas[1]} a los 12 meses; retirando una de cada cuatro al mes quedan {vivas[0]}. Una bandera es deuda con fecha de caducidad.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-414
def se414_plan() -> Fig:
    d = e414_plan()
    rows = [
        ["Aplicar en orden aleatorio", pc(d["aleatorio_falla"], 0) + " de los planes fallan", "—"],
        ["Aplicar en orden topológico", pc(d["topologico_falla"], 0) + " fallan", f"{d['idempotente']} de {d['runs']} dejan un plan vacío al repetir"],
        ["Acciones por plan (12 recursos)", n(d["acciones"], 2), f"{n(d['destructivas'], 2)} destructivas (borrar o reemplazar)"],
        ["Acciones destructivas sobre recursos con estado", n(d["con_estado"], 2) + " por plan", "se detectan solo si la política las examina"],
        ["Grafos con un ciclo inyectado", f"{d['ciclos']} de 100 detectados", "el ciclo se rechaza antes de aplicar"],
    ]
    return tab("Un planificador de infraestructura mínimo: 300 grafos aleatorios de 12 recursos",
               "Tabla: aplicar las acciones de un plan en orden aleatorio falla en el 79 por ciento de los planes y en orden topológico en ninguno; repetir la aplicación deja un plan vacío en los 300 casos; cada plan tiene unas 7,8 acciones de las cuales 1,3 son destructivas y 0,47 tocan recursos con estado; los 100 ciclos inyectados se detectan.",
               ["Medida", "Resultado", "Observación"], rows, [310, 280, 340], row_h=52, size=12,
               note="El orden no es un detalle: el 79 % de los planes se rompe si las acciones no respetan las dependencias. Lo que el plan muestra como «reemplazar» es borrar y crear, y en un recurso con estado es perder datos: el promedio de este modelo es de 0,47 acciones destructivas sobre recursos con estado por plan. Los grafos y los porcentajes de recursos con estado (25 %) son supuestos del autor.",
               note_kind="gold", foot=SINT)


def se414_estado() -> Fig:
    d = e414_estado()
    rows = [[f"{k} canalizaciones sin bloqueo", str(v[0]), str(v[1]), pc(v[1] / v[0], 1)] for k, v in d.items()]
    rows.append(["Con bloqueo o cola (una a la vez)", "solo órdenes en serie", "0", "0 %"])
    return tab("Dos o tres canalizaciones que aplican a la vez sobre el mismo archivo de estado: todas las intercalaciones",
               "Tabla: con dos canalizaciones hay 20 intercalaciones de leer, aplicar y escribir y 18 dejan el estado distinto de la nube; con tres hay 1 680 y 1 674 lo hacen; con un bloqueo solo hay órdenes en serie y ninguna diverge.",
               ["Situación", "Intercalaciones", "Estado ≠ nube", "Porcentaje"], rows, [360, 200, 190, 180], row_h=44, size=13,
               note="La pérdida no es un accidente raro: solo las ejecuciones en serie son seguras (2 de 20, 6 de 1 680). Cada canalización escribe el estado completo que leyó, así que la última escritura borra lo que la otra aplicó. Un bloqueo del estado (o una cola) vuelve la ejecución serial. El modelo supone que el estado se guarda entero.",
               note_kind="coral", foot=SINT)


def se414_deriva() -> Fig:
    d = e414_deriva()
    order = ["plan cada hora", "plan cada 6 horas", "plan diario", "solo al fusionar (3 por semana)", "plan semanal"]
    items = []
    for k in order:
        v = d[k][0]
        kind = "teal" if v < 5 else ("gold" if v < 30 else "coral")
        items.append((k, v, kind, f"{n(v, 1)} h"))
    return bars("Horas que vive una deriva manual hasta que una comprobación la ve (media de 5 000 derivas)",
                "Barras: con un plan cada hora una deriva vive 0,5 horas de media; cada 6 horas, 3,0; diario, 11,9; solo al fusionar, 55,8, y con un plan semanal, 83 horas.",
                items, 2.2, "La espera media es la mitad del intervalo entre comprobaciones; comprobar solo al fusionar depende del ritmo del equipo (3 fusiones por semana ⇒ 56 h) y es peor cuando el equipo para. Detectar más pronto no corrige: si la deriva es una corrección de emergencia, revertirla automáticamente puede provocar la caída que se quiso evitar.",
                label_w=290, width=1000, note_kind="gold", foot=SINT)


FIGURES = {
    "se-409-vida-de-la-rama-y-conflictos.svg": se409_ramas,
    "se-409-lotes-y-aislamiento-de-fallos.svg": se409_lotes,
    "se-409-troncal-rota-sin-cola.svg": se409_cola,
    "se-410-ruta-critica-y-ejecutores.svg": se410_dag,
    "se-410-matriz-y-cobertura-de-defectos.svg": se410_matriz,
    "se-410-claves-de-cache.svg": se410_cache,
    "se-411-orden-de-las-etapas.svg": se411_orden,
    "se-411-reglas-sobre-workflows.svg": se411_politicas,
    "se-411-reintentos-y-defectos-intermitentes.svg": se411_reintentos,
    "se-412-validacion-de-tokens-por-niveles.svg": se412_tokens,
    "se-412-ventana-de-exposicion.svg": se412_ventana,
    "se-412-detectores-de-secretos.svg": se412_escaner,
    "se-413-estrategias-de-despliegue.svg": se413_despliegue,
    "se-413-potencia-del-canario.svg": se413_potencia,
    "se-413-banderas-y-combinaciones.svg": se413_banderas,
    "se-414-orden-de-aplicacion.svg": se414_plan,
    "se-414-estado-sin-bloqueo.svg": se414_estado,
    "se-414-deriva-y-frecuencia-de-plan.svg": se414_deriva,
}
