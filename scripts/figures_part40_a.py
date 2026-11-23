"""Figures for SE-481 to SE-486 (synthetic data, fixed seeds, virtual time; CPython 3.12.9 on Windows 11 and 3.12.3 on Ubuntu/WSL2)."""
from __future__ import annotations

from experiments_part40_a import (e409_cola, e409_lotes, e409_ramas, e410_cache, e410_dag, e410_matriz, e411_orden, e411_politicas,
                                  e411_reintentos, e412_escaner, e412_tokens, e412_ventana, e413_banderas, e413_despliegue,
                                  e413_potencia, e414_deriva, e414_estado, e414_plan)
from figure_kit import Fig, grouped_bars, heatmap, line_chart, percentile_intervals, stacked_bars
from figures_part07_a import bars

SINT = "Datos sintéticos con semilla fija y tiempo virtual; Windows y Ubuntu (WSL2) dan cifras idénticas."


def n(x: float, d: int = 1) -> str:
    """Spanish number: decimal comma, space as thousands separator."""
    s = f"{x:,.{d}f}".replace(",", " ").replace(".", ",")
    return s


def pc(x: float, d: int = 1) -> str:
    return n(x * 100, d) + " %"


# ---------------------------------------------------------------- SE-481
def se409_ramas() -> Fig:
    d = e409_ramas()
    cats = [f"{n(k, 1) if k < 1 else int(k)} día{'s' if k != 1 else ''}" for k in d]
    files = ", ".join(n(v[1], 1) for v in d.values())
    return grouped_bars(
        "Vida de una rama y choque de archivos con la troncal (8 personas, 400 archivos con puntos calientes)",
        "Barras con el porcentaje de ramas que tocan algún archivo que otra persona también cambió según su vida: con medio día el 21 por ciento, con un día el 49, con dos días el 89 y con cinco días o más prácticamente todas.",
        cats, [("Ramas con algún archivo en choque", [v[0] * 100 for v in d.values()], "coral")],
        unit="Ramas con choque (%)", decimals=0, plot_h=260,
        note=f"Archivos en choque (media) por vida de la rama: {files}. La probabilidad de choque no crece de forma lineal sino saturada: pasa de 21 % a 89 % en un día y medio y después ya no puede empeorar, aunque el trabajo por resolver sigue creciendo (de 0,2 a 31 archivos). Los puntos calientes (los archivos que todos tocan) y las tres modificaciones diarias por persona son supuestos del autor.",
        note_kind="gold", foot=SINT)


def se409_lotes() -> Fig:
    d = e409_lotes()
    rojos = ", ".join(f"{k}: {pc(v[0], 0)}" for k, v in d.items())
    return line_chart(
        "Integrar por lotes: cuántas veces se construye hasta aislar cada cambio defectuoso (24 000 cambios, 4 % defectuosos)",
        "Línea con las construcciones por cambio, con bisección, según el tamaño del lote: un cambio por lote exige 1,00; con lotes de 5 baja a 0,38; el mínimo está en lotes de 10 con 0,35 y con lotes de 50 vuelve a 0,37.",
        [("Construcciones por cambio (con bisección)", [(k, v[1], n(v[1], 2), "t") for k, v in d.items()], "teal")],
        x_label="Cambios por lote", y_label="Construcciones por cambio", log_x=True,
        x_ticks=[(k, str(k)) for k in d], y_ticks=[0, 0.25, 0.5, 0.75, 1.0], point_labels="none", decimals=2, plot_h=280,
        note=f"Lotes en rojo según el tamaño: {rojos}. Agrupar ahorra construcciones hasta unos 10 cambios por lote y deja de ahorrar: con 50 cambios casi todos los lotes salen rojos y hay que aislar a mano. El ahorro se paga con retraso: el cambio bueno espera al lote y el defectuoso se localiza más tarde. El 4 % de defectos por cambio y la independencia entre cambios son supuestos.",
        note_kind="gold", foot=SINT)


def se409_cola() -> Fig:
    d = e409_cola()
    cats = [f"{n(k, 2) if k < 1 else int(k)} día{'s' if k != 1 else ''}" for k in d]
    return grouped_bars(
        "Troncal rota por un choque semántico entre dos cambios que pasan por separado (por cada 1 000 integraciones)",
        "Barras con las veces que la troncal queda en rojo por cada mil integraciones: sin cola, 54 cuando los cambios viven un cuarto de día, 213 con un día y 490 con tres días; una cola que prueba el resultado combinado los detecta antes de integrar y deja 0.",
        cats, [("Troncal en rojo sin cola", [v[0] for v in d.values()], "coral"), ("Con cola de integración", [0 for _ in d], "teal")],
        unit="Troncal en rojo (por 1 000 integraciones)", decimals=0, plot_h=260,
        note="Con cola, los choques se detectan al entrar (0 en la troncal). El choque no está en ningún cambio por separado: aparece en la combinación. Con 12 cambios al día y una probabilidad de choque del 2 % por pareja solapada, vivir tres días multiplica por nueve la tasa de troncal rota. La cola no elimina el choque: lo convierte en un rechazo al entrar, antes de que lo vea el resto del equipo.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-482
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
    names = ("completa", "pareja a pareja", "una a la vez", "9 al azar")
    return grouped_bars(
        "Matriz 3 sistemas × 4 versiones × 3 bases (36 combinaciones): qué defectos encuentra cada estrategia",
        "Barras agrupadas con el porcentaje de defectos de uno, dos y tres factores que encuentra cada estrategia: la matriz completa de 36 combinaciones encuentra el 100 por ciento de todos; pareja a pareja con 12 combinaciones el 100, 100 y 39; una a la vez con 8, el 100, 52 y 28; nueve al azar, el 99, 62 y 23.",
        [f"{name} ({d[name][0]})" for name in names],
        [("Defecto de 1 factor", [d[k][1] * 100 for k in names], "teal"), ("De 2 factores", [d[k][2] * 100 for k in names], "gold"), ("De 3 factores", [d[k][3] * 100 for k in names], "coral")],
        unit="Defectos encontrados (%)", decimals=0, plot_h=280,
        note="Entre paréntesis, las combinaciones de cada estrategia. Cubrir todas las parejas con 12 de 36 combinaciones no deja escapar ningún defecto de dos factores pero sí el 61 % de los de tres. Una a la vez mira cada nivel pero no las interacciones. Cada defecto es de un solo tipo y se eligió al azar entre 400 conjuntos; la distribución real de defectos de interacción es desconocida.",
        note_kind="gold", foot=SINT)


def se410_cache() -> Fig:
    d = e410_cache()
    order = ["hash del lockfile", "hash + respaldo", "SHA del commit", "clave fija"]
    return grouped_bars(
        "Cuatro claves de caché en 600 construcciones (la dependencia cambia en el 10 % de ellas)",
        "Barras horizontales con aciertos, restauraciones parciales y entorno obsoleto de cuatro claves de caché: el hash del lockfile acierta el 89 por ciento y tarda 26,6 segundos; con respaldo por prefijo baja a 12,2 segundos con 11 por ciento parciales; el SHA del commit acierta el 17,5 por ciento y tarda 149,9; una clave fija acierta siempre pero el 97 por ciento usa dependencias obsoletas.",
        [f"{k} ({n(d[k][2], 1)} s)" for k in order],
        [("Aciertos", [d[k][0] * 100 for k in order], "teal"), ("Parciales", [d[k][1] * 100 for k in order], "gold"), ("Entorno obsoleto", [d[k][3] * 100 for k in order], "coral")],
        unit="Construcciones (%)", horizontal=True, decimals=1, label_w=250,
        note="Entre paréntesis, la instalación media. Una clave fija da el mejor tiempo (8 s) y el peor resultado: el 97 % de las construcciones corre con dependencias que ya no coinciden con el lockfile. El tiempo ahorrado no compensa un resultado que no es reproducible. Los tiempos de 180, 45 y 8 segundos son supuestos del autor.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-483
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
    ti, fi, ni = d["ingenua"]
    ta, fa, na = d["afinada"]
    return grouped_bars(
        "Reglas de texto sobre 160 workflows con 8 clases de defecto sembrado y 6 señuelos",
        "Barras agrupadas con aciertos, falsos positivos y defectos no vistos de dos conjuntos de reglas sobre 209 defectos sembrados: las ingenuas encuentran todos pero producen 180 falsas alarmas, con precisión de 54 por ciento; las afinadas reducen las falsas alarmas a 45 y pierden 5 defectos, con precisión de 82 y exhaustividad de 98.",
        ["Reglas ingenuas", "Reglas afinadas"],
        [("Aciertos", [ti, ta], "teal"), ("Falsos positivos", [fi, fa], "coral"), ("Defectos no vistos", [ni, na], "gold")],
        unit="Defectos o alarmas", decimals=0, plot_h=260,
        note=f"Precisión {pc(ti / (ti + fi), 0)} y exhaustividad {pc(ti / (ti + ni), 0)} las ingenuas; {pc(ta / (ta + fa), 0)} y {pc(ta / (ta + na), 0)} las afinadas. Las reglas ingenuas ven todo y avisan de demasiado: por eso un equipo las desactiva. Las afinadas ignoran comentarios y acciones locales, pero se equivocan donde el defecto cambia de forma (un bloque de varias líneas) y donde el valor es seguro (el número del PR). Se afinaron con los mismos señuelos que las evalúan: son una frontera, no una tasa.",
        note_kind="gold", foot=SINT)


def se411_reintentos() -> Fig:
    d = e411_reintentos()
    xs = (0, 1, 2)

    def lab(v: float) -> str:
        return n(v, 1) + " %" if v >= 1 else n(v, 3) + " %"

    series = [("Defecto en el 50 % de las ejecuciones (pasan)", [(k, d["defecto"][0.5][k] * 100) for k in xs], "teal"),
              ("Defecto en el 20 % de las ejecuciones (pasan)", [(k, d["defecto"][0.2][k] * 100, lab(d["defecto"][0.2][k] * 100), "t") for k in xs], "gold"),
              ("Defecto en el 5 % de las ejecuciones (pasan)", [(k, d["defecto"][0.05][k] * 100) for k in xs], "navy"),
              ("Rojo falso por pruebas inestables", [(k, d["rojos_falsos"][k] * 100, lab(d["rojos_falsos"][k] * 100), "t") for k in xs], "coral")]
    return line_chart(
        "Reintentar pruebas: porcentaje de ejecuciones que pasan con 0, 1 o 2 reintentos",
        "Líneas en escala logarítmica con el porcentaje de ejecuciones que pasan según los reintentos: un defecto real que aparece en el 20 por ciento de las ejecuciones pasa el 80 por ciento sin reintentos, el 96 con uno y el 99 con dos; los rojos falsos por pruebas inestables bajan de 25,9 por ciento a 0,015 con un reintento.",
        series, x_label="Reintentos permitidos", y_label="Ejecuciones (%)", log_y=True,
        x_ticks=[(0, "0"), (1, "1"), (2, "2")], y_ticks=[0.01, 0.1, 1, 10, 100], point_labels="none", decimals=2, plot_h=300,
        note="Las tres primeras líneas son el porcentaje de ejecuciones que pasan con un defecto real; la roja es el porcentaje de ejecuciones en rojo por pruebas inestables (600 pruebas, 0,05 % cada una). El reintento hace desaparecer los rojos falsos (25,9 % → 0,015 %) y también hace pasar los defectos intermitentes: uno que aparece 1 vez de 5 pasa el 99,2 % con dos reintentos. Reintentar sin registrar qué se reintentó convierte una señal en ruido silencioso; hay que contar los reintentos y cuarentenar la prueba.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-484
def se412_tokens() -> Fig:
    d = e412_tokens()
    order = ["solo firma", "firma + vigencia", "+ emisor y audiencia", "+ sujeto con prefijo «repo:org»", "+ sujeto exacto y vida corta"]
    return grouped_bars(
        "Verificar un token de identidad con más o menos comprobaciones: 12 tokens manipulados y 3 legítimos",
        "Barras horizontales con los tokens que acepta cada nivel de verificación: solo la firma acepta 9 de 12 manipulados; añadir vigencia, 6; emisor y audiencia, 4; el sujeto con prefijo sigue aceptando 4, incluido un repositorio de otra organización; el sujeto exacto con vida corta no acepta ninguno y sigue aceptando los 3 legítimos.",
        order,
        [(f"Manipulados aceptados (de {d['_n']})", [d[k][0] for k in order], "coral"), (f"Legítimos aceptados (de {d['_legit']})", [d[k][2] for k in order], "teal")],
        unit="Tokens aceptados", horizontal=True, decimals=0, label_w=270,
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
    d = e412_escaner()
    order = ["prefijos conocidos", "entropía", "asignación sospechosa", "prefijos + asignación"]
    return grouped_bars(
        f"Buscar secretos en {d['_lineas']} líneas sintéticas con {d['_secretos']} secretos sembrados",
        "Barras horizontales con aciertos, falsos positivos y secretos perdidos de cuatro detectores: buscar prefijos conocidos no da falsos positivos pero pierde 202 de 460 secretos; la entropía encuentra 343 pero señala 414 identificadores y hashes; buscar asignaciones sospechosas encuentra 393 con 4 falsos positivos y pierde 67.",
        order,
        [("Aciertos", [d[k][0] for k in order], "teal"), ("Falsos positivos", [d[k][1] for k in order], "coral"), ("Secretos perdidos", [d[k][2] for k in order], "gold")],
        unit="Secretos o alarmas", horizontal=True, decimals=0, label_w=190,
        note="Cada detector ve una forma y ciega ante otra: la entropía confunde 170 SHA de git, 153 UUID y 91 imágenes en base64 con secretos y aun así pierde las contraseñas de baja entropía. Un detector no sustituye a la rotación: lo que encuentra ya estaba expuesto. Los secretos y señuelos son cadenas inventadas.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-485
def se413_despliegue() -> Fig:
    d = e413_despliegue()
    det = "; ".join(f"{k}: {n(v[2], 1)} min y {pc(v[4], 1)} de retrocesos falsos" for k, v in d.items())
    return grouped_bars(
        "Una versión con 4 puntos de error adicional a 100 solicitudes por segundo: solicitudes fallidas hasta el retroceso (600 repeticiones)",
        "Barras agrupadas con las solicitudes fallidas hasta el retroceso: si la versión mala se despliega de una vez fallan 240 de media y 268 en el percentil 95; con cuatro tandas, 59 y 72; con un canario del 1 por ciento al 100 por ciento, 6 y 9.",
        list(d), [("Fallos medios", [v[0] for v in d.values()], "navy"), ("Fallos p95", [v[1] for v in d.values()], "coral")],
        unit="Solicitudes fallidas", decimals=0, plot_h=260,
        note=f"Detección media y retrocesos falsos de las versiones buenas, por estrategia: {det}. El canario reduce el daño en un 98 % no porque detecte antes (2,4 min frente a 1) sino porque solo lo ve una fracción del tráfico. La detección es estadística: con 1 % del tráfico y umbral estricto hay que esperar. Un retroceso falso cuesta una versión buena perdida. Poisson y normal aproximan al binomial; error base 0,5 %.",
        note_kind="gold", foot=SINT)


def se413_potencia() -> Fig:
    d = e413_potencia()
    shares = (0.01, 0.05, 0.25)
    exs = (0.005, 0.01, 0.02, 0.04)
    return heatmap(
        "Probabilidad de detectar una subida del error en 10 minutos de canario (error base 0,5 %, umbral 0,1 %)",
        "Mapa de calor con la probabilidad de detectar una subida del error según el tráfico del canario: con el 1 por ciento una subida de 0,5 puntos se detecta el 4 por ciento de las veces, una de 1 punto el 29, una de 2 puntos el 88 y una de 4 puntos el 99,98; con el 5 por ciento, el 60, 99,6, 100 y 100; con el 25 por ciento todas superan el 99,99.",
        [pc(s, 0) + " del tráfico" for s in shares], ["+0,5 puntos", "+1 punto", "+2 puntos", "+4 puntos"],
        [[d[f"{s}|{ex}"][2] * 100 for ex in exs] for s in shares],
        unit="Probabilidad de detección (%)", scale="navy", vmin=0, vmax=100, decimals=1, label_w=180,
        note="Un canario del 1 % no ve una degradación sutil: 600 solicitudes en 10 minutos dan 3 errores esperados y el umbral exige 11. La potencia depende del tráfico, no de la voluntad de mirar. Si el servicio recibe poco tráfico, el canario es un trámite. Cálculo exacto con la cola de Poisson (normal si la media supera 50).",
        note_kind="coral", foot=SINT)


def se413_banderas() -> Fig:
    d = e413_banderas()
    ks = (2, 4, 6, 8, 10)
    vivas = d["_vivas"]
    return grouped_bars(
        "Banderas de funcionalidad: configuraciones posibles frente a las necesarias para cubrir todas las parejas",
        "Barras agrupadas en escala logarítmica con las configuraciones posibles y las necesarias para cubrir todas las parejas: con 2 banderas 4 y 4; con 6, 64 y 7; con 8, 256 y 8; con 10, 1 024 y 9, el 0,9 por ciento.",
        [f"{k} banderas" for k in ks],
        [("Configuraciones", [d[k][0] for k in ks], "grey"), ("Para cubrir parejas", [d[k][1] for k in ks], "teal")],
        unit="Configuraciones", log=True, decimals=0, plot_h=280,
        note=f"Cubrir las parejas cuesta casi nada, pero no cubre las interacciones de tres banderas ni el comportamiento de las que nadie recuerda. Con 3 banderas nuevas al mes y ninguna retirada hay {vivas[1]} a los 12 meses; retirando una de cada cuatro al mes quedan {vivas[0]}. Una bandera es deuda con fecha de caducidad.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-486
def se414_plan() -> Fig:
    d = e414_plan()
    return grouped_bars(
        "Un planificador de infraestructura mínimo: 300 grafos aleatorios de 12 recursos",
        "Barras horizontales con el porcentaje de casos de cada comprobación: aplicar las acciones en orden aleatorio falla en el 79 por ciento de los planes y en orden topológico en ninguno; repetir la aplicación deja un plan vacío en los 300 casos y los 100 ciclos inyectados se detectan.",
        ["Orden aleatorio: planes que fallan", "Orden topológico: planes que fallan", "Repetir la aplicación: plan vacío", "Ciclos inyectados que se detectan"],
        [("Casos", [d["aleatorio_falla"] * 100, d["topologico_falla"] * 100, d["idempotente"] / d["runs"] * 100, d["ciclos"]], "navy")],
        unit="Casos (%)", horizontal=True, decimals=0, label_w=270,
        note=f"Cada plan tiene {n(d['acciones'], 2)} acciones de las cuales {n(d['destructivas'], 2)} son destructivas (borrar o reemplazar) y {n(d['con_estado'], 2)} tocan recursos con estado, que solo se detectan si la política las examina. El orden no es un detalle: el 79 % de los planes se rompe si las acciones no respetan las dependencias. Los grafos y los porcentajes de recursos con estado (25 %) son supuestos del autor.",
        note_kind="gold", foot=SINT)


def se414_estado() -> Fig:
    d = e414_estado()
    cats = [f"{k} canalizaciones sin bloqueo" for k in d]
    return stacked_bars(
        "Dos o tres canalizaciones que aplican a la vez sobre el mismo archivo de estado: todas las intercalaciones",
        "Barras apiladas horizontales con las intercalaciones de leer, aplicar y escribir: con dos canalizaciones hay 20 y 18 dejan el estado distinto de la nube; con tres hay 1 680 y 1 674 lo hacen; con un bloqueo solo hay órdenes en serie y ninguna diverge.",
        cats, [("Estado = nube", [v[0] - v[1] for v in d.values()], "teal"), ("Estado ≠ nube", [v[1] for v in d.values()], "coral")],
        unit="Intercalaciones", horizontal=True, decimals=0, label_w=240,
        note="Con un bloqueo o una cola solo hay órdenes en serie y 0 intercalaciones divergen. La pérdida no es un accidente raro: solo las ejecuciones en serie son seguras (2 de 20, 6 de 1 680). Cada canalización escribe el estado completo que leyó, así que la última escritura borra lo que la otra aplicó. Un bloqueo del estado (o una cola) vuelve la ejecución serial. El modelo supone que el estado se guarda entero.",
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
    "se-481-vida-de-la-rama-y-conflictos.svg": se409_ramas,
    "se-481-lotes-y-aislamiento-de-fallos.svg": se409_lotes,
    "se-481-troncal-rota-sin-cola.svg": se409_cola,
    "se-482-ruta-critica-y-ejecutores.svg": se410_dag,
    "se-482-matriz-y-cobertura-de-defectos.svg": se410_matriz,
    "se-482-claves-de-cache.svg": se410_cache,
    "se-483-orden-de-las-etapas.svg": se411_orden,
    "se-483-reglas-sobre-workflows.svg": se411_politicas,
    "se-483-reintentos-y-defectos-intermitentes.svg": se411_reintentos,
    "se-484-validacion-de-tokens-por-niveles.svg": se412_tokens,
    "se-484-ventana-de-exposicion.svg": se412_ventana,
    "se-484-detectores-de-secretos.svg": se412_escaner,
    "se-485-estrategias-de-despliegue.svg": se413_despliegue,
    "se-485-potencia-del-canario.svg": se413_potencia,
    "se-485-banderas-y-combinaciones.svg": se413_banderas,
    "se-486-orden-de-aplicacion.svg": se414_plan,
    "se-486-estado-sin-bloqueo.svg": se414_estado,
    "se-486-deriva-y-frecuencia-de-plan.svg": se414_deriva,
}
