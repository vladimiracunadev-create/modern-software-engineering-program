"""Figures for SE-445 to SE-450 (critical systems and safety standards: runs of real CPython code and seeded models over the Horno de curado case; Windows CPython 3.12.9; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig, dumbbell, grouped_bars, line_chart, stacked_bars

from figures_part45_a import bars, flow

EJEC = "Código ejecutado de verdad en Windows 11 con CPython 3.12.9; los recuentos se repiten con la misma semilla."
MODELO = "Modelo con parámetros del autor y semilla fija 47; muestra un mecanismo, no mide un producto real."


def _sci(v: float) -> str:
    return f"{v:.2e}".replace(".", ",")


# ---------------------------------------------------------------- SE-445
def se565_causa_comun() -> Fig:
    return grouped_bars(
        "Probabilidad del evento tope de un árbol de fallos del Horno de curado, sin y con una causa común",
        "Barras en escala logarítmica con la probabilidad anual del evento tope: 2,07 por diez a la menos cinco con nueve cortes mínimos de orden dos, y 3,21 por diez a la menos cuatro cuando una calibración compartida por el lazo y el limitador añade un corte de orden uno, unas 15,5 veces más.",
        ["Sin causa común (9 cortes de orden 2)", "Con una calibración común (corte de orden 1)"],
        [("Probabilidad del evento tope por año", [2.07e-5, 3.21e-4], "navy")],
        unit="Probabilidad por año", log=True, value_fmt=_sci, plot_h=250,
        note="La calibración común aporta el 93,5 % de la probabilidad del tope con una probabilidad propia de solo 3,0e-4, mayor que la del evento tope sin ella. Una simulación Monte Carlo con las probabilidades multiplicadas por 20 y 400 000 corridas (semilla 47) dio 1,40e-2 frente a 1,38e-2 exacto. Las tasas las fijó el autor.",
        note_kind="coral", foot=MODELO)


def se565_rpn_contra_gravedad() -> Fig:
    names = ["Deriva de calibración", "Conector de puerta", "Sensor en lectura baja", "Relé soldado", "Ruido del convertidor", "Reinicio por perro guardián", "Pantalla rezagada", "Memoria del registro"]
    s_rank = {"Relé soldado": 1, "Sensor en lectura baja": 2, "Deriva de calibración": 3, "Conector de puerta": 4, "Reinicio por perro guardián": 5, "Ruido del convertidor": 6, "Pantalla rezagada": 7, "Memoria del registro": 8}
    r_rank = {n: i + 1 for i, n in enumerate(names)}
    rows = [(n, float(s_rank[n]), float(r_rank[n])) for n in names]
    return dumbbell(
        "Ocho modos de fallo del Horno de curado: puesto por gravedad y puesto por número de prioridad de riesgo",
        "Gráfico de pares con el puesto de ocho modos de fallo según su gravedad y según su RPN: el relé del limitador soldado, de gravedad 10, pasa del puesto 1 al 4 por RPN; la deriva de calibración sube del 3 al 1 y el conector de puerta del 4 al 2.",
        rows, unit="Puesto (1 es el más urgente)", names=("Puesto por gravedad", "Puesto por RPN"), decimals=0, lower_is_better=True, label_w=250,
        note="El RPN multiplica tres escalas ordinales de 1 a 10: las 1000 combinaciones dan solo 120 valores distintos, y 24 combinaciones comparten el mismo número, con gravedades desde 2 hasta 10. Con cambios de una unidad en el 20 % de las valoraciones, el mismo trío encabeza en el 76,8 % de 2000 repeticiones. Las valoraciones son del autor.",
        note_kind="gold", foot=MODELO)


def se565_sin_fallo() -> Fig:
    return grouped_bars(
        "Una corrida sin ningún fallo de componente: temperatura máxima y segundos con calentador y puerta abierta, sin y con limitador",
        "Barras con el resultado de una corrida de 900 segundos en la que el controlador cumple su especificación, pero la consigna es de 300 grados: sin limitador la temperatura llega a 300,1 y hay 684 segundos con el calentador conectado y la puerta abierta; con un limitador independiente en 250 llega a 185,4 y hay 0 segundos.",
        ["Sin limitador", "Con limitador independiente"],
        [("Temperatura máxima (C)", [300.1, 185.4], "coral"), ("Segundos con calentador y puerta abierta", [684, 0], "navy")],
        unit="Grados o segundos", decimals=1, ref_lines=[(250, "límite 250 C")], plot_h=260,
        note="Ningún componente falló: la especificación pedía calentar mientras la temperatura fuera menor que la consigna y nadie había escrito qué hacer con una puerta abierta o con una consigna superior al límite. Un análisis de fallos de componentes no ve este caso; el análisis de acciones de control no seguras lo enumera: 22 de 72 combinaciones evaluadas son peligrosas.",
        note_kind="teal", foot=MODELO)


# ---------------------------------------------------------------- SE-446
def se566_arquitecturas() -> Fig:
    return grouped_bars(
        "Probabilidad media de fallo bajo demanda de tres arquitecturas según el intervalo entre pruebas",
        "Barras en escala logarítmica con la PFD media: con prueba anual, 1oo1 da 8,76 por diez a la menos tres, 1oo2 5,30 por diez a la menos cuatro y 2oo3 7,15 por diez a la menos cuatro; con prueba cada dos años 1,75 por diez a la menos dos, 1,25 por diez a la menos tres y 1,98 por diez a la menos tres; con prueba cada cinco años 4,38 por diez a la menos dos, 4,50 por diez a la menos tres y 9,12 por diez a la menos tres.",
        ["1oo1", "1oo2 (beta 0,05)", "2oo3 (beta 0,05)"],
        [("Prueba anual", [8.76e-3, 5.30e-4, 7.15e-4], "teal"), ("Cada 2 años", [1.75e-2, 1.25e-3, 1.98e-3], "gold"), ("Cada 5 años", [4.38e-2, 4.50e-3, 9.12e-3], "coral")],
        unit="PFD media", log=True, value_fmt=_sci, ref_lines=[(1e-3, "frontera 1e-3"), (1e-2, "frontera 1e-2")], plot_h=300,
        note="Fórmulas simplificadas de baja demanda con una tasa de fallo peligroso no detectado de 2e-6 por hora. Las fronteras de las bandas son de 1e-2 a 1e-1 para el nivel 1, de 1e-3 a 1e-2 para el 2 y de 1e-4 a 1e-3 para el 3 en modo de baja demanda. Una simulación de 400 000 vidas dio 8,62e-3 para 1oo1 frente a 8,76e-3 de la fórmula.",
        note_kind="gold", foot=MODELO)


def se566_beta() -> Fig:
    betas = [0.0, 0.02, 0.05, 0.10, 0.20]
    pfd = [1.02e-4, 2.73e-4, 5.30e-4, 9.59e-4, 1.82e-3]
    return line_chart(
        "Una arquitectura 1oo2 con prueba anual: PFD media según la fracción de fallos de causa común",
        "Línea en escala logarítmica con la PFD media de un 1oo2: 1,02 por diez a la menos cuatro sin causa común, 2,73 por diez a la menos cuatro con beta de 0,02, 5,30 por diez a la menos cuatro con 0,05, 9,59 por diez a la menos cuatro con 0,10 y 1,82 por diez a la menos tres con 0,20.",
        [("PFD media de 1oo2", list(zip(betas, pfd)), "teal")],
        x_label="Fracción de causa común (beta)", y_label="PFD media", log_y=True, x_ticks=[(b, f"{b:.2f}".replace(".", ",")) for b in betas],
        y_ticks=[1e-4, 1e-3, 1e-2], point_labels="all", decimals=5, plot_h=290, hlines=[(1e-3, "frontera 1e-3")],
        note="Con beta cero, duplicar el canal reduce la PFD a 1,02e-4; con beta 0,20 la deja en 1,82e-3, un factor 18 peor, y cruza la frontera de la banda. La redundancia no protege de lo que comparten los dos canales: misma calibración, misma fuente, misma especificación errónea.",
        note_kind="coral", foot=MODELO)


def se566_prueba_imperfecta() -> Fig:
    cov = ["100 %", "99 %", "95 %", "90 %", "70 %"]
    vals = [8.76e-3, 9.99e-3, 1.49e-2, 2.10e-2, 4.56e-2]
    return grouped_bars(
        "Un canal 1oo1 de 15 años de vida con prueba anual: PFD media según la cobertura de la prueba",
        "Barras con la PFD media de un canal 1oo1 con prueba anual y vida de 15 años: 8,76 por diez a la menos tres con cobertura de prueba del 100 por ciento, 9,99 por diez a la menos tres con el 99, 1,49 por diez a la menos dos con el 95, 2,10 por diez a la menos dos con el 90 y 4,56 por diez a la menos dos con el 70.",
        cov, [("PFD media", vals, "navy")], unit="PFD media", value_fmt=_sci, ref_lines=[(1e-2, "frontera 1e-2")], plot_h=260,
        note="Una prueba que no detecta el 5 % de los fallos deja que esos fallos se acumulen hasta el final de la vida útil: la PFD sube un 70 % y el canal baja de banda. La cobertura de la prueba periódica es un supuesto del modelo que hay que justificar y vigilar, no un dato.",
        note_kind="gold", foot=MODELO)


# ---------------------------------------------------------------- SE-447
def se567_metrica() -> Fig:
    return grouped_bars(
        "Métrica de fallo único de dos diseños del Horno de curado frente a tres valores de referencia no verificados",
        "Barras con la métrica de fallo único: 60,7 por ciento con diagnóstico mínimo y 98,1 con diagnóstico por componente, con líneas de referencia en 90, 97 y 99 por ciento.",
        ["A: diagnóstico mínimo", "B: diagnóstico por componente"], [("Métrica de fallo único (%)", [60.7, 98.1], "teal")],
        unit="Por ciento", decimals=1, ref_lines=[(90, "90 %"), (97, "97 %"), (99, "99 %")], plot_h=250,
        note="Los fallos peligrosos sin cubrir son 78,5 FIT en el diseño A y 3,9 FIT en el B sobre un total de 200 FIT: el diseño B supera el umbral de 97 % pero no el de 99 %. Las tasas de fallo y las coberturas por componente las fijó el autor; los tres umbrales son valores que circulan en la literatura técnica y no se verificaron contra la norma, que es de pago.",
        note_kind="gold", foot=MODELO)


def se567_cobertura_medida() -> Fig:
    return grouped_bars(
        "Inyección de 20 000 fallos de un bit en un cálculo de par: cobertura medida de cuatro esquemas de diagnóstico",
        "Barras con la cobertura medida sobre 15 422 fallos peligrosos: sin diagnóstico 0 por ciento, comprobación de rango de la entrada 57,0, doble cálculo con comparación 67,3 y doble cálculo con relectura de la salida 100.",
        ["Sin diagnóstico", "Rango de la entrada", "Doble cálculo y comparación", "Doble cálculo y relectura de la salida"],
        [("Cobertura medida (%)", [0.0, 57.0, 67.3, 100.0], "teal")], unit="Por ciento de fallos peligrosos detectados", decimals=1, plot_h=270,
        note="El doble cálculo no ve un fallo que ocurre después de la comparación (en la salida), por eso se queda en 67,3 %; la relectura de la salida lo cierra. Los fallos se inyectan en la entrada, en un valor intermedio y en la salida del canal A, con el canal B sano; solo se prueba un fallo a la vez. El 100 % vale para este modelo de fallos, no para fallos de causa común.",
        note_kind="coral", foot=EJEC)


def se567_diagnostico() -> Fig:
    return flow("Diagnóstico del cálculo de par: dónde se coloca cada comprobación y qué fallos no ve",
                "Diagrama de cuatro cajas encadenadas: entrada del pedal con comprobación de rango, canal A y canal B de cálculo, comparador que ve los fallos de los canales pero no los posteriores, y salida con relectura que cierra el último tramo.",
                [[("Entrada\nRango: ve solo valores imposibles", "gold"), ("Canales A y B\nDoble cálculo: ve fallos de un canal", "teal"),
                  ("Comparador\nNo ve lo que ocurre después de él", "coral"), ("Salida y relectura\nCierra el último tramo", "teal")]],
                note="Cada diagnóstico cubre un tramo del camino del dato. La cobertura de un esquema es la unión de los tramos que cubren sus comprobaciones, y los fallos de causa común (el mismo error en ambos canales) no los ve ninguno de los tres.",
                note_kind="teal", box_h=112, foot=MODELO)


# ---------------------------------------------------------------- SE-448
def se568_cobertura_acumulada() -> Fig:
    ks = [("R1", 6), ("R2", 6), ("R3", 8), ("R4", 9), ("R0", 10), ("R5", 11)]
    return line_chart(
        "Sentencias ejecutadas del limitador (13 en total) al ir añadiendo pruebas derivadas de requisitos, una a una",
        "Línea con las sentencias ejecutadas acumuladas: 6 con la prueba de R1, 6 con la de R2, 8 con R3, 9 con R4, 10 con R0 y 11 con R5, de un total de 13 sentencias.",
        [("Sentencias ejecutadas", [(i + 1, v) for i, (_, v) in enumerate(ks)], "teal")],
        x_label="Prueba añadida", y_label="Sentencias ejecutadas de 13", x_ticks=[(i + 1, n) for i, (n, _) in enumerate(ks)], y_ticks=[0, 4, 8, 12],
        point_labels="all", decimals=0, plot_h=280, hlines=[(13, "13 sentencias")],
        note="Seis pruebas, una por requisito, ejecutan 11 de 13 sentencias (84,6 %). Las dos restantes no las pide ningún requisito: una rama con un límite de temperatura imposible de alcanzar con la entrada acotada (código muerto) y una orden de depuración activada por el valor 42 (una función no prevista).",
        note_kind="gold", foot=EJEC)


def se568_causas() -> Fig:
    return flow("Tres lecturas de una sentencia que ningún requisito ejecuta, y qué hace la persona que revisa",
                "Diagrama de tres cajas con las explicaciones posibles de código sin cubrir por pruebas de requisitos: falta una prueba, falta un requisito derivado, o el código es muerto o no previsto y se elimina o se justifica.",
                [[("Falta una prueba\nEl requisito existe: se escribe la prueba", "teal"), ("Falta un requisito\nLa conducta es deseable: se deriva y se prueba", "gold"),
                  ("Código muerto o no previsto\nSe elimina o se justifica por escrito", "coral")]],
                note="La cobertura estructural no busca llegar a un número: busca las sentencias que nadie pidió. Es una comprobación de que las pruebas basadas en requisitos fueron suficientes, y su hallazgo es una de estas tres decisiones.",
                note_kind="teal", box_h=100, foot=EJEC)


def se568_tras_r5() -> Fig:
    return grouped_bars(
        "El limitador con y sin el requisito del sensor sin lectura: sentencias sin ejecutar tras las pruebas de requisitos",
        "Barras con las sentencias sin ejecutar del limitador: 3 con las pruebas de los requisitos R0 a R4 y 2 tras añadir el requisito R5 de sensor sin lectura; las 2 restantes son la rama imposible y la orden de depuración.",
        ["Pruebas de R0 a R4", "Tras añadir R5 (sensor sin lectura)"], [("Sentencias sin ejecutar", [3, 2], "coral")],
        unit="Sentencias sin ejecutar de 13", decimals=0, plot_h=240,
        note="La sentencia que se cubrió al añadir R5 era una conducta defensiva (devolver el estado seguro sin lectura) que existía en el código sin requisito: una conducta derivada que hasta entonces nadie había escrito. Las otras dos siguen siendo hallazgos abiertos.",
        note_kind="teal", foot=EJEC)


# ---------------------------------------------------------------- SE-449
def se569_clases() -> Fig:
    return stacked_bars(
        "Doce módulos de un software de bomba de infusión: clases de seguridad con y sin segregación documentada",
        "Barras apiladas con el número de módulos de clase A, B y C: sin segregación, 2 de clase A, 4 de B y 6 de C; con segregación documentada, 4 de A, 4 de B y 4 de C.",
        ["Sin segregación", "Con segregación documentada"],
        [("Clase A", [2, 4], "teal"), ("Clase B", [4, 4], "gold"), ("Clase C", [6, 4], "coral")],
        unit="Módulos", horizontal=True, decimals=0, label_w=190,
        note="Sin segregación, todo lo que sirve a un módulo de clase C hereda la clase: pantalla, registro y almacén suben. Las actividades de verificación pasan de 90 a 76 con los pesos del autor (3, 6 y 10 por módulo de clase A, B y C). La segregación solo vale si está argumentada y verificada, no si se declara.",
        note_kind="gold", foot=MODELO)


def se569_topes() -> Fig:
    return grouped_bars(
        "20 000 órdenes de velocidad con un 2 % de deslizamientos del punto decimal: órdenes peligrosas que llegan a la bomba",
        "Barras con las órdenes peligrosas que pasan: sin control 398, con un tope global de 100 mililitros por hora 266 y con un tope por perfil de fármaco de tres veces la velocidad habitual 0.",
        ["Sin control", "Tope global de 100 ml/h", "Tope por perfil de fármaco"], [("Órdenes peligrosas que pasan", [398, 266, 0], "coral")],
        unit="Órdenes de 20 000", decimals=0, plot_h=250,
        note="Un tope fijo no sabe qué se prescribió: deja pasar 266 de 398 órdenes diez veces mayores que lo prescrito. El tope por perfil las detiene todas en este modelo, a costa de mantener y verificar la biblioteca de perfiles, que pasa a ser un componente crítico. El modelo supone un solo tipo de error de tecleo.",
        note_kind="teal", foot=MODELO)


def se569_ciclo() -> Fig:
    return flow("Del peligro al control de software en la lógica de un ciclo de vida de dispositivo médico: lo que se encadena",
                "Diagrama de cuatro cajas: peligro y situación peligrosa, riesgo estimado, medida de control incluida en el software o fuera de él, y clase de seguridad del módulo que determina el rigor de verificación.",
                [[("Peligro\nSobreinfusión por una orden mal tecleada", "coral"), ("Riesgo\nGravedad y probabilidad estimadas con supuestos", "gold"),
                  ("Control\nTope por perfil en el software o límite mecánico fuera", "teal"), ("Clase del módulo\nSegún lo que el software contribuye al peligro", "teal")]],
                note="La clase de seguridad del software no se elige por el tamaño del módulo sino por si su fallo puede contribuir a una situación peligrosa y por qué controles externos reducen ese riesgo. Un control fuera del software puede bajar la clase; solo si es independiente y verificado.",
                note_kind="teal", box_h=118, foot=MODELO)


# ---------------------------------------------------------------- SE-450
def se570_apoyo() -> Fig:
    return grouped_bars(
        "Cuatro afirmaciones de un argumento de seguridad: evidencias que respaldan a cada una",
        "Barras con las evidencias por afirmación del argumento: G1 con 2, G2 con 1, G3 con 3 y G4 con 1 una vez desarrollada; G2 y G4 dependen de una sola evidencia y su retirada rompe la afirmación principal.",
        ["G1 peligros identificados", "G2 requisitos verificados", "G3 verificación estructural", "G4 desarrollada con una evidencia"], [("Evidencias", [2, 1, 3, 1], "navy")],
        unit="Evidencias por afirmación", decimals=0, horizontal=True, label_w=270, ref_lines=[(2, "2 evidencias")],
        note="Al retirar una evidencia por vez, solo E3 (única de G2) y E7 (única de G4) rompen la afirmación principal G0. Antes de desarrollar G4, el argumento ni siquiera cierra: una afirmación sin desarrollar no es una afirmación apoyada. Además, E7 y E8 estaban en la carpeta sin que ninguna afirmación las usara.",
        note_kind="gold", foot=MODELO)


def se570_trazabilidad() -> Fig:
    return grouped_bars(
        "Trazabilidad de 30 requisitos y 45 pruebas: huecos, enlaces sin destino y enlaces sospechosos tras un cambio",
        "Barras con los huecos de trazabilidad: 9 requisitos sin ninguna prueba, 2 pruebas sin requisito y, tras cambiar el texto de 3 requisitos, 3 enlaces sospechosos que obligan a revisar 4 pruebas.",
        ["Requisitos sin prueba", "Pruebas sin requisito", "Enlaces sospechosos tras cambiar 3 requisitos", "Pruebas que hay que revisar"], [("Elementos", [9, 2, 3, 4], "coral")],
        unit="Elementos", decimals=0, horizontal=True, label_w=330, plot_h=260,
        note="Los enlaces se comparan por el resumen SHA-256 del texto del requisito: si el texto cambia después de enlazar la prueba, el enlace queda marcado como sospechoso. La cobertura de enlaces mide que existe un enlace, no que la prueba compruebe el requisito. Los datos son sintéticos con semilla 47.",
        note_kind="teal", foot=MODELO)


def se570_estructura() -> Fig:
    return flow("Estructura de un caso de seguridad: de la afirmación principal a la evidencia, con el contexto y las suposiciones",
                "Diagrama de cuatro cajas: afirmación principal de que el sistema es aceptablemente seguro en un contexto, estrategia de argumento por peligros, subafirmaciones y evidencias, y suposiciones y contexto que acotan el argumento.",
                [[("Afirmación\nEl sistema es aceptablemente seguro en este contexto", "teal"), ("Estrategia\nArgumento por peligros y por controles", "gold"),
                  ("Evidencia\nPruebas, análisis y revisiones con versión", "teal"), ("Contexto y supuestos\nLo que no se prueba pero se asume", "coral")]],
                note="Un caso de seguridad es un argumento estructurado con evidencia que lo respalda: el argumento sin evidencia es opinión y la evidencia sin argumento es una carpeta. Los supuestos también son parte del argumento y también se desafían.",
                note_kind="teal", box_h=118, foot=MODELO)


FIGURES = {
    "se-445-causa-comun.svg": se565_causa_comun,
    "se-445-rpn-contra-gravedad.svg": se565_rpn_contra_gravedad,
    "se-445-sin-fallo.svg": se565_sin_fallo,
    "se-446-arquitecturas.svg": se566_arquitecturas,
    "se-446-beta.svg": se566_beta,
    "se-446-prueba-imperfecta.svg": se566_prueba_imperfecta,
    "se-447-metrica.svg": se567_metrica,
    "se-447-cobertura-medida.svg": se567_cobertura_medida,
    "se-447-diagnostico.svg": se567_diagnostico,
    "se-448-cobertura-acumulada.svg": se568_cobertura_acumulada,
    "se-448-causas.svg": se568_causas,
    "se-448-tras-r5.svg": se568_tras_r5,
    "se-449-clases.svg": se569_clases,
    "se-449-topes.svg": se569_topes,
    "se-449-ciclo.svg": se569_ciclo,
    "se-450-apoyo.svg": se570_apoyo,
    "se-450-trazabilidad.svg": se570_trazabilidad,
    "se-450-estructura.svg": se570_estructura,
}
