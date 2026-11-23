"""Figures for SE-343 to SE-348 (architectural styles: runs of real CPython code and seeded models over the Avisos case; Windows CPython 3.12.9; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, heatmap, line_chart, percentile_intervals, stacked_bars

from figures_part45_a import bars, flow

EJEC = "Código ejecutado de verdad en Windows 11 con CPython 3.12.9; los recuentos se repiten y los tiempos varían de un equipo a otro."
MODELO = "Modelo con parámetros del autor y semilla fija 44; muestra un mecanismo, no mide un sistema real."


# ---------------------------------------------------------------- SE-343
def se535_cola_central() -> Fig:
    xs = [5, 10, 15, 20, 24]
    return line_chart(
        "Un equipo de datos central de cuatro personas atendiendo a D dominios: espera por solicitud de un conjunto de datos nuevo",
        "Líneas con la espera por solicitud según los dominios atendidos por un equipo central de cuatro personas, cada dominio con 0,15 solicitudes por semana: la espera media simulada es 0,00 semanas con 5 dominios, 0,03 con 10, 0,14 con 15, 0,53 con 20 y 2,17 con 24; la analítica de Erlang C coincide y el percentil 90 llega a 5,65 semanas con 24.",
        [("Espera media simulada", list(zip(xs, [0.00, 0.03, 0.14, 0.53, 2.17])), "teal"), ("Espera media analítica", list(zip(xs, [0.00, 0.03, 0.14, 0.51, 1.97])), "navy"),
         ("Espera p90 simulada", list(zip(xs, [0.00, 0.00, 0.50, 1.66, 5.65])), "coral")],
        x_label="Dominios atendidos", y_label="Semanas de espera", x_ticks=[(x, str(x)) for x in xs], y_ticks=[0, 1, 2, 3, 4, 5, 6], point_labels="none", decimals=2, plot_h=300,
        note="Utilización del equipo con 5, 10, 15, 20 y 24 dominios: 19 %, 38 %, 56 %, 75 % y 90 %. La espera no crece en línea recta: pasar de 20 a 24 dominios (un 20 % más de demanda) multiplica la espera media por cuatro. La simulación coincide con la fórmula de Erlang C hasta el 90 % de utilización, lo que valida la simulación, no el modelo de organización.",
        note_kind="coral", foot=MODELO)


def se535_personas_necesarias() -> Fig:
    return grouped_bars(
        "Con 20 dominios, personas necesarias para que la espera media no pase de 0,5 semanas según quién es dueño del dato",
        "Barras horizontales con las personas necesarias con 20 dominios para que la espera media no pase de 0,5 semanas: un equipo central necesita 5 personas sin penalización de contexto, 6 con penalización 0,5 y 8 con 1,0; equipos por dominio necesitan 10 en total con 0,5 persona por dominio, con una espera de 0,87 que no cumple, y 13 con 0,65.",
        ["Central, sin penalización de contexto (0,12 semanas)", "Central, penalización 0,5 (0,44)", "Central, penalización 1,0 (0,38)", "Un equipo por dominio, 0,5 persona cada uno (0,87: no cumple)", "Un equipo por dominio, 0,65 persona cada uno (0,47)"],
        [("Personas en total", [5, 6, 8, 10, 13], "navy")],
        unit="Personas en total", horizontal=True, decimals=0, label_w=350,
        note="Entre paréntesis, la espera media en semanas. En este modelo la propiedad por dominio no ahorra personas: mueve el trabajo y necesita más. Lo que compra es que el conocimiento del dominio deje de ser una penalización del equipo central y que el producto de datos tenga un dueño. La penalización de contexto es un supuesto del autor.",
        note_kind="gold", foot=MODELO)


def se535_derivas() -> Fig:
    return heatmap(
        "Ocho derivas de un producto de datos y un cambio legítimo: qué comprobación del contrato las detecta",
        "Mapa de calor con nueve cambios sobre un producto de datos de 1000 filas y las comprobaciones que fallan: D1 a D3 las detecta el esquema, D4 la completitud y el esquema, D5 la unicidad, D6 la frescura y D7 y D8 la distribución; el cambio legítimo de temporada L1 también falla la distribución y es una falsa alarma; solo con el esquema se detectan 4 de las 8 derivas.",
        ["D1 columna renombrada", "D2 tipo cambiado a texto", "D3 columna eliminada", "D4 nulos en estudiante (12,5 %)", "D5 identificadores duplicados", "D6 datos atrasados (30 h)", "D7 unidad cambiada a minutos", "D8 significado invertido", "L1 cambio legítimo de temporada"],
        ["Esquema", "Completitud", "Unicidad", "Frescura", "Distribución"],
        [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1]],
        unit="falla", scale="navy", vmin=0, vmax=1, cell_fmt=lambda v: "falla" if v else "—", highlight=[(8, 4)], cell_h=36, label_w=290,
        note="Las ocho derivas se detectan con cinco comprobaciones; con solo el esquema se detectarían 4. La celda resaltada es la falsa alarma: el cambio legítimo de temporada también falla la distribución. La unidad cambiada y el significado invertido son válidos para el esquema y solo se ven por su efecto en la distribución, que no distingue un defecto de un cambio real del negocio.",
        note_kind="teal", foot=EJEC)


# ---------------------------------------------------------------- SE-344
def se536_reubicacion() -> Fig:
    return grouped_bars(
        "Pasar de 8 a 9 celdas con 100 000 inquilinos: cuántos cambian de celda según la función de asignación",
        "Barras horizontales con los inquilinos reubicados al pasar de 8 a 9 celdas con 100000 inquilinos: el módulo del hash reubica 88985, un 89,0 por ciento; el hash por encuentro 11176, un 11,2 por ciento; el mínimo teórico es un noveno, 11111, un 11,1 por ciento.",
        ["Módulo del hash (89,0 %)", "Hash por encuentro (11,2 %)", "Mínimo teórico, 1/9 (11,1 %)"], [("Inquilinos reubicados", [88985, 11176, 11111], "navy")],
        unit="Inquilinos reubicados de 100 000", horizontal=True, decimals=0, label_w=250,
        note="Entre paréntesis, la proporción reubicada. Con el módulo, añadir una celda mueve casi todo; con el hash por encuentro solo se mueve lo que la celda nueva se queda. Mover un inquilino es una migración de datos, de modo que la función de asignación decide el costo de crecer. El reparto entre las 8 celdas fue de 12 339 a 12 713 inquilinos por celda.",
        note_kind="gold", foot=EJEC)


def se536_radio() -> Fig:
    return bars('Fracción de los 1 000 inquilinos que un solo inquilino venenoso deja sin servicio según cómo está repartida la flota',
                'Gráfico de barras con la fracción de inquilinos afectada por un inquilino venenoso: en una flota compartida el 100 por ciento según el supuesto de reintentos, con ocho celdas el 10,9 por ciento, con fragmentación aleatoria de dos trabajadores de ocho el 3,0 por ciento queda caído del todo y el 45,6 por ciento queda degradado.',
                [('Flota compartida (supuesto)', 100, 'coral', '100 %'), ('Ocho celdas', 10.9, 'gold', '10,9 %'), ('Fragmentación: caídos del todo', 3.0, 'teal', '3,0 %'),
                 ('Fragmentación: degradados', 45.6, 'gold', '45,6 %')],
                scale=4, label_w=330,
                note='Las celdas acotan el daño a una fracción fija y la fragmentación lo reduce aún más a quien comparte todos sus trabajadores con el venenoso, a costa de degradar a casi la mitad. El 100 % de la flota compartida es un supuesto (los reintentos del cliente recorren todos los trabajadores), no una medición.',
                note_kind='teal', foot=MODELO)


def se536_costo_de_celdas() -> Fig:
    return grouped_bars(
        "Costo de repartir 1 000 inquilinos en 8 celdas frente a una flota compartida: capacidad, disponibilidad y punto de fallo",
        "Barras con la capacidad necesaria para cubrir el percentil 99 de la carga: 1824 unidades con una flota compartida y 2184 con ocho celdas, un 19,8 por ciento más.",
        ["Capacidad para cubrir el p99 de la carga"], [("Flota compartida", [1824], "teal"), ("Ocho celdas", [2184], "coral")],
        unit="Unidades de capacidad", decimals=0, plot_h=240, width=700,
        note="Disponibilidad de un inquilino: la de la flota (99,9 %) frente a 99,890 % con el enrutador al 99,99 % y la celda al 99,9 %. Punto de fallo compartido: la flota entera frente al enrutador. Repartir cuesta capacidad (cada celda se dimensiona a su propio p99, y los picos no se compensan entre celdas) y mueve el punto de fallo al enrutador. La carga de cada inquilino es lognormal con semilla 44; una carga real tiene otra forma.",
        note_kind="coral", foot=MODELO)


# ---------------------------------------------------------------- SE-345
def se537_linter() -> Fig:
    return grouped_bars(
        "Un linter de cuatro señales de 12-factor sobre una aplicación con defectos y su versión corregida",
        "Barras agrupadas con las señales contadas por un linter de árbol sintáctico sobre dos versiones de la misma aplicación: URL fija 1 y 0, estado en memoria del proceso 2 y 0, registro en archivo local 1 y 0, y lecturas del entorno 1 y 2 en la versión corregida.",
        ["URL fija en el código", "Estado en memoria del proceso", "Registro en archivo local", "Lecturas del entorno"],
        [("Aplicación con defectos", [1, 2, 1, 1], "coral"), ("Aplicación corregida", [0, 0, 0, 2], "teal")],
        unit="Señales encontradas", decimals=0, plot_h=260,
        note="Las tres primeras señales son defectos y desaparecen al corregir; las lecturas del entorno son la señal buena y suben de 1 a 2. El linter ve la forma del código, no su comportamiento: una URL construida por concatenación o un estado guardado en un atributo de clase pasarían. Detecta cuatro señales de dos aplicaciones de juguete; no certifica que una aplicación sea 12-factor.",
        note_kind="gold", foot=EJEC)


def se537_sesiones() -> Fig:
    return bars('Peticiones sin sesión de 1 000 con tres instancias, 100 usuarios y una instancia que cae en la petición 500',
                'Gráfico de barras con las peticiones que no encuentran su sesión de 1 000: con sesiones en memoria y balanceo sin afinidad 611, con afinidad por usuario 140 que corresponden a la instancia caída, y con un almacén externo compartido 0.',
                [('En memoria, sin afinidad', 611, 'coral', '611'), ('En memoria, con afinidad', 140, 'gold', '140'), ('Almacén externo', 0, 'teal', '0')],
                scale=0.6, label_w=300,
                note='Una aplicación con estado en el proceso no puede escalar horizontalmente ni sobrevivir a una caída: sin afinidad falla en 611 de 1 000 peticiones aun sin caída; con afinidad pierde las sesiones de la instancia que cae. El estado externo lo resuelve a costa de una dependencia más, que el modelo no cuenta.',
                note_kind='coral', foot=MODELO)


def se537_desechabilidad() -> Fig:
    return grouped_bars(
        "Desechabilidad y configuración: qué pasa al parar un proceso, y un mismo artefacto con tres entornos",
        "Barras agrupadas con el resultado de parar un proceso con 100 trabajos en una cola en memoria: un corte inmediato completa 40 y pierde 60; un drenaje ordenado completa 41, devuelve 60 a la cola y no pierde ninguno.",
        ["Corte inmediato con 100 trabajos", "Drenaje ordenado, devuelve lo pendiente"],
        [("Completados", [40, 41], "teal"), ("Perdidos", [60, 0], "coral"), ("Devueltos a la cola", [0, 60], "gold")],
        unit="Trabajos", decimals=0, plot_h=260,
        note="El mismo artefacto con configuración de desarrollo sale con código 0 y umbrales 12 y 48; con la de producción, con código 0 y umbrales 1, 24 y 72; sin configurar, con código 1 y el mensaje «falta AVISOS_UMBRALES». El arranque de un proceso Python tarda una mediana de 116 ms vacío y 249 ms con cuatro módulos. La misma huella del archivo con configuración distinta es la paridad que pide el factor de configuración; fallar de inmediato cuando falta es mejor que arrancar con un valor por defecto invisible. Los trabajos y el corte son un modelo; el arranque y la ejecución del artefacto sí se midieron.",
        note_kind="teal", foot=EJEC)


# ---------------------------------------------------------------- SE-346
def se538_divergencias() -> Fig:
    return grouped_bars(
        "Módulo heredado y módulo nuevo ejecutados sobre las mismas 20 000 peticiones: divergencias por causa",
        "Barras horizontales con las divergencias entre un módulo de avisos heredado y su reemplazo sobre 20000 peticiones sintéticas: 145 por redondeo en el borde, 57 por el plazo de extensión que el módulo nuevo olvidó y 1 por cambio de hora, 203 en total, un 1,01 por ciento.",
        ["Redondeo en el borde, el módulo nuevo trunca minutos (71,4 %)", "Plazo de extensión, el módulo nuevo lo olvidó (28,1 %)", "Cambio de hora, solo 2 días al año (0,5 %)"],
        [("Divergencias", [145, 57, 1], "navy")],
        unit="Divergencias (203 en total)", horizontal=True, decimals=0, label_w=340,
        note="Entre paréntesis, la proporción de las divergencias. Tres defectos sembrados por el autor, con frecuencias tan distintas como 145, 57 y 1. Ejecutar los dos módulos en paralelo y comparar las salidas es la forma más barata de encontrar lo que ninguna prueba imaginó, pero solo encuentra lo que el tráfico real contiene.",
        note_kind="gold", foot=MODELO)


def se538_modo_sombra() -> Fig:
    xs = [1, 5, 25, 100]
    return line_chart(
        "Probabilidad de ver cada causa de divergencia según la fracción del tráfico que se compara (500 repeticiones por fila)",
        "Líneas en escala logarítmica con la probabilidad de observar cada divergencia según la fracción del tráfico comparada en modo sombra: con 1 por ciento se ve el plazo de extensión el 46 por ciento de las veces, el cambio de hora el 1 y el redondeo el 75; con 5 por ciento, 95, 6 y 100; con 25 por ciento, 100, 27 y 100; con todo el tráfico, siempre los tres.",
        [("Plazo de extensión", list(zip(xs, [46, 95, 100, 100])), "gold"), ("Cambio de hora", list(zip(xs, [1, 6, 27, 100])), "coral"), ("Redondeo en el borde", list(zip(xs, [75, 100, 100, 100])), "teal")],
        x_label="Fracción del tráfico comparada (%)", y_label="Probabilidad de verla (%)", log_x=True, x_ticks=[(x, f"{x} %") for x in xs], y_ticks=[0, 20, 40, 60, 80, 100],
        point_labels="none", decimals=0, plot_h=300,
        note="Un defecto que ocurre una vez en 20 000 peticiones no se ve comparando el 1 % ni el 25 % del tráfico con fiabilidad: su probabilidad es la fracción comparada. Comparar todo es la única forma de ver lo raro, y aun así solo si ocurre durante la comparación.",
        note_kind="coral", foot=MODELO)


def se538_escalones() -> Fig:
    xs = [1, 5, 25, 50, 100]
    return line_chart(
        "Un defecto visible en 0,4 % de las peticiones con 20 000 peticiones por escalón: usuarios afectados y probabilidad de detectarlo",
        "Línea con la probabilidad de ver al menos 3 errores de un defecto que afecta al 0,4 por ciento de las peticiones según el escalón de tráfico: 4,7 por ciento con el 1 por ciento, 76,2 con el 5 y 100 desde el 25; los usuarios afectados esperados son 0,8, 4,0, 20,0, 40,0 y 80,0.",
        [("Probabilidad de ver al menos 3 errores", [(1, 4.7, "4,7 %", "t"), (5, 76.2, "76,2 %", "b"), (25, 100.0, "100 %", "t"), (50, 100.0, "100 %", "t"), (100, 100.0, "100 %", "t")], "teal")],
        x_label="Escalón de tráfico (%)", y_label="Probabilidad (%)", log_x=True, x_ticks=[(x, f"{x} %") for x in xs], y_ticks=[0, 20, 40, 60, 80, 100], point_labels="none", decimals=1, plot_h=280,
        note="Usuarios afectados esperados por escalón: 0,8, 4,0, 20,0, 40,0 y 80,0. Un escalón demasiado pequeño no detecta y uno demasiado grande daña: con 1 % no se alcanza a ver el defecto (4,7 %) y con 5 % se ve tres de cada cuatro veces afectando a unos 4 usuarios. Si el 5 % lo detiene, el daño acumulado es de 4,8 usuarios frente a 80 si se cambia de golpe.",
        note_kind="teal", foot=MODELO)


# ---------------------------------------------------------------- SE-347
def se539_escenarios() -> Fig:
    return heatmap(
        "Seis escenarios de calidad de Avisos con su medida y su importancia en dos contextos",
        "Mapa de calor con la importancia de seis escenarios de calidad en dos contextos: latencia y disponibilidad son de importancia alta en ambos, el radio de impacto de hasta 15 por ciento de los inquilinos es alta con un cliente dominante y baja sin él, y la coordinación de despliegue, el costo y la extensión son de importancia media en ambos.",
        ["S1 latencia: p99 ≤ 200 ms", "S2 disponibilidad: ≥ 99,9 %", "S3 radio de impacto: ≤ 15 % de inquilinos", "S4 coordinación de despliegue: ≤ 2 equipos", "S5 costo: ≤ 12 unidades", "S6 extensión: canal nuevo sin tocar el núcleo"],
        ["Con cliente dominante", "Sin cliente dominante"],
        [[3, 3], [3, 3], [3, 1], [2, 2], [2, 2], [2, 2]],
        unit="Importancia", scale="navy", vmin=1, vmax=3, cell_fmt=lambda v: {3: "alta", 2: "media", 1: "baja"}[int(v)], label_w=340, cell_h=40,
        note="Cada escenario tiene una medida que se puede comprobar; la importancia es una decisión de negocio, no una medición. El único escenario que cambia de importancia entre los dos contextos es el radio de impacto, y eso es suficiente para cambiar el resultado.",
        note_kind="gold", foot=MODELO)


def se539_candidatos() -> Fig:
    return grouped_bars(
        "Tres candidatos con 12 equipos: valores que produce el modelo y utilidad ponderada en cada contexto",
        "Barras agrupadas con la utilidad ponderada de tres candidatos con 12 equipos en dos contextos: el monolito modular 0,596 con cliente dominante y 0,685 sin él; los microservicios 0,583 y 0,670; las celdas con monolito modular 0,710 y 0,652.",
        ["Monolito modular", "Microservicios (4)", "Celdas (8) con monolito modular"],
        [("Con cliente dominante", [0.596, 0.583, 0.710], "teal"), ("Sin cliente dominante", [0.685, 0.670, 0.652], "navy")],
        unit="Utilidad ponderada", decimals=3, plot_h=260,
        note="Valores del modelo (p99 en ms, disponibilidad, equipos a coordinar, costo): monolito modular 80, 99,950 %, 11 y 3; microservicios 194, 99,601 %, 0 y 16; celdas 125, 99,890 %, 11 y 18. Ningún candidato cumple los seis escenarios y los tres dejan tres o cuatro sin cumplir; las utilidades difieren en menos de 0,13. Con cliente dominante ganan las celdas y sin él el monolito modular; la decisión depende del contexto antes que del estilo.",
        note_kind="teal", foot=MODELO)


def se539_sensibilidad() -> Fig:
    return stacked_bars(
        "Qué candidato gana según el contexto, el número de equipos y la disponibilidad supuesta de la cadena de microservicios",
        "Barras apiladas horizontales con los casos, de tres tamaños de equipo, en que gana cada candidato en cuatro situaciones: con cliente dominante ganan las celdas en los 3; sin él, el monolito modular en 2 y los microservicios desde 26 equipos en 1; con la cadena de microservicios al 99,95 por ciento ganan los microservicios en los 3 casos de ambos contextos.",
        ["Con cliente dominante", "Sin cliente dominante", "Con cliente dominante y cadena al 99,95 %", "Sin cliente dominante y cadena al 99,95 %"],
        [("Celdas", [3, 0, 0, 0], "teal"), ("Monolito modular", [0, 2, 0, 0], "navy"), ("Microservicios", [0, 1, 3, 3], "coral")],
        unit="Casos de 3 tamaños de equipo (4, 12 y 30)", horizontal=True, decimals=0, label_w=290,
        note="Sin cliente dominante, el monolito modular gana con 4 y 12 equipos y los microservicios con 30 (desde 26). El punto de sensibilidad más fuerte no es el número de equipos sino un supuesto: que la cadena de cuatro servicios tenga 99,601 % de disponibilidad. Cambiarlo a 99,95 % (con degradación y reintentos) invierte la decisión en todos los casos, y por eso esa medida debe ir al ADR como supuesto a verificar.",
        note_kind="coral", foot=MODELO)


# ---------------------------------------------------------------- SE-348
def se540_lint_de_adr() -> Fig:
    names = ["Sección Contexto", "Sección Decisión", "Sección Alternativas", "Sección Consecuencias", "Sección Reversibilidad", "Sección Disparador de revisión",
             "Sección Evidencia", "Al menos 2 alternativas con motivo", "Consecuencia negativa declarada", "Criterio medible", "Disparador numérico"]
    b = [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    c = [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]
    return heatmap(
        "Un linter de once criterios sobre tres ADR: el completo, el que justifica con una moda y el que olvida su reversibilidad",
        "Mapa de calor con once criterios aplicados a tres registros de decisión: el ADR-A, monolito modular con disparador de revisión, cumple 11 de 11; el ADR-B, que dice usar microservicios porque son la mejor práctica, cumple 3 de 11 y le faltan alternativas, reversibilidad, disparador, evidencia, consecuencias negativas y criterio medible; el ADR-C, celdas para el cliente grande, cumple 8 de 11 y le faltan la reversibilidad, el disparador y su criterio numérico.",
        names, ["ADR-A", "ADR-B", "ADR-C"], [[1, y, z] for y, z in zip(b, c)],
        unit="cumple", scale="teal", vmin=0, vmax=1, cell_fmt=lambda v: "cumple" if v else "falta", cell_h=34, label_w=300,
        note="Criterios cumplidos: 11 de 11 el ADR-A, 3 de 11 el ADR-B y 8 de 11 el ADR-C. El linter comprueba presencia y forma, no verdad: un ADR con once criterios cumplidos puede decidir mal. Sirve para rechazar lo evidentemente incompleto (el ADR-B) antes de gastar tiempo de revisión humana.",
        note_kind="gold", foot=EJEC)


def se540_funcion_de_aptitud() -> Fig:
    return grouped_bars(
        "Una función de aptitud de capas sobre un paquete de juguete: violaciones y ciclos que detecta en cuatro variantes",
        "Barras agrupadas con las violaciones de capa y los ciclos que detecta una prueba de arquitectura sobre cuatro variantes de un paquete: la limpia no tiene ninguno y pasa; cuando el dominio importa la infraestructura hay 1 violación y 1 ciclo y falla; cuando dos módulos de aplicación se importan entre sí hay 0 violaciones y 1 ciclo y falla; una importación dinámica no se detecta y pasa.",
        ["Limpia (pasa)", "El dominio importa la infraestructura (falla)", "Dos módulos de aplicación se importan entre sí (falla)", "Importación dinámica de la infraestructura (pasa, no la ve)"],
        [("Violaciones de capa", [0, 1, 0, 0], "coral"), ("Ciclos", [0, 1, 1, 0], "gold")],
        unit="Violaciones o ciclos detectados", horizontal=True, decimals=0, label_w=330,
        note="La última variante tiene una violación real que la prueba no ve. La prueba corre en unos 10 a 40 ms y detecta lo que está escrito como importación; una importación por nombre en una cadena la elude. Una función de aptitud protege una decisión contra la deriva solo en la medida en que su mecanismo ve la forma en que se rompe.",
        note_kind="teal", foot=EJEC)


def se540_ciclo_de_decision() -> Fig:
    return flow('Ciclo de una decisión arquitectónica defendida: de los escenarios al disparador de revisión',
                'Diagrama de cinco cajas en dos filas: escenarios de calidad con medida, alternativas evaluadas con evidencia, ADR con consecuencias negativas, función de aptitud que protege la decisión y disparador de revisión numérico; una flecha de retorno lleva del disparador a los escenarios.',
                [[('Escenarios\nCon medida y contexto', 'teal'), ('Alternativas\nEvaluadas con evidencia y supuestos', 'gold'), ('ADR\nDecisión, costos y reversibilidad', 'teal')],
                 [('Función de aptitud\nProtege la decisión contra la deriva', 'coral'), ('Disparador de revisión\nUn número y un plazo', 'gold')]],
                note='Una decisión arquitectónica es una hipótesis con fecha de revisión: el disparador numérico (por ejemplo, p99 mayor que 200 ms durante 3 días seguidos) dice cuándo la evidencia obliga a volver a los escenarios.',
                note_kind='teal', box_h=96, foot=MODELO)


FIGURES = {
    "se-343-cola-central.svg": se535_cola_central,
    "se-343-personas-necesarias.svg": se535_personas_necesarias,
    "se-343-derivas.svg": se535_derivas,
    "se-344-reubicacion.svg": se536_reubicacion,
    "se-344-radio.svg": se536_radio,
    "se-344-costo-de-celdas.svg": se536_costo_de_celdas,
    "se-345-linter.svg": se537_linter,
    "se-345-sesiones.svg": se537_sesiones,
    "se-345-desechabilidad.svg": se537_desechabilidad,
    "se-346-divergencias.svg": se538_divergencias,
    "se-346-modo-sombra.svg": se538_modo_sombra,
    "se-346-escalones.svg": se538_escalones,
    "se-347-escenarios.svg": se539_escenarios,
    "se-347-candidatos.svg": se539_candidatos,
    "se-347-sensibilidad.svg": se539_sensibilidad,
    "se-348-lint-de-adr.svg": se540_lint_de_adr,
    "se-348-funcion-de-aptitud.svg": se540_funcion_de_aptitud,
    "se-348-ciclo-de-decision.svg": se540_ciclo_de_decision,
}
