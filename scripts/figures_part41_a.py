"""Figures for SE-493 to SE-498 (harness and agentic engineering: a stdlib mini-harness with a scripted policy, real files and Git repositories in temporary directories; Windows 11, CPython 3.12.9; no language model was invoked)."""
from __future__ import annotations

from figure_flow_rows import chain_rows
from figure_kit import Fig, grouped_bars, line_chart, scatter, stacked_bars

from figures_part40_a import bars, flow

EJEC = "Código ejecutado de verdad en Windows 11 con CPython 3.12.9; ninguna cifra viene de un modelo de lenguaje."
SIM = "Simulación con semilla fija (parámetros del autor) ejecutada en Windows 11 con CPython 3.12.9; no mide ningún modelo real."


# ---------------------------------------------------------------- SE-493
def se493_ablacion() -> Fig:
    return stacked_bars(
        "Quitar un componente del harness cambia el fallo: siete configuraciones sobre seis tareas",
        "Barras apiladas horizontales con el destino de seis tareas de corrección de errores en siete configuraciones del harness: el completo resuelve 6 de 6 con 5 pasos de media; sin contexto, sin herramienta de escritura o con un solo paso resuelve 0 de 6; sin criterio de parada resuelve las seis pero consume 12 pasos; sin comprobación de pruebas o sin instrucciones resuelve 3 de 6 y declara terminadas en falso otras 3.",
        ["Harness completo (5,0 pasos)", "Sin contexto entre pasos (12,0)", "Sin herramienta de escritura (12,0)", "Sin bucle, un solo paso (1,0)", "Sin criterio de parada (12,0)",
         "Sin comprobación de pruebas (3,0)", "Sin instrucciones (3,0)"],
        [("Resueltas", [6, 0, 0, 0, 6, 3, 3], "teal"), ("Terminadas en falso", [0, 0, 0, 0, 0, 3, 3], "coral"), ("Sin resolver", [0, 6, 6, 6, 0, 0, 0], "grey")],
        unit="Tareas de 6 (entre paréntesis, pasos medios)", horizontal=True, label_w=270,
        note="Cada componente falla de una manera distinta: unos impiden resolver, uno solo desperdicia pasos y dos producen el peor fallo, declarar terminada una tarea que no pasa. La política es un guion, así que el gráfico mide el harness, no a un modelo.",
        note_kind="gold", foot=EJEC)


def se493_anatomia() -> Fig:
    return flow('Anatomía de un harness: lo que rodea al modelo en cada vuelta del bucle',
                'Diagrama con dos filas de cajas: el modelo recibe instrucciones y contexto, propone una acción, el harness comprueba el permiso y la ejecuta con una herramienta, la observación vuelve al contexto, y el harness decide si repetir, verificar o parar.',
                [[('Instrucciones y contexto visible', 'gold'), ('Modelo propone una acción', 'navy'), ('Permiso y herramienta ejecutan', 'teal')],
                 [('Observación vuelve al contexto', 'plain'), ('Verificación con pruebas', 'teal'), ('Criterio de parada o nueva vuelta', 'coral')]],
                note='El modelo ocupa una caja de seis. Todo lo demás lo decide el harness, y por eso un fallo del conjunto puede no ser del modelo.',
                note_kind='gold', foot=EJEC, box_h=76)


def se493_resueltas() -> Fig:
    return bars('Tareas resueltas de seis según el componente que se quita',
                'Gráfico de barras con las tareas resueltas de seis: harness completo 6, sin criterio de parada 6, sin comprobación de pruebas 3, sin instrucciones 3, sin contexto 0, sin escritura 0 y sin bucle 0.',
                [('Harness completo', 6, 'teal', '6'), ('Sin criterio de parada', 6, 'gold', '6'), ('Sin comprobación de pruebas', 3, 'coral', '3'),
                 ('Sin instrucciones', 3, 'coral', '3'), ('Sin contexto', 0, 'coral', '0'), ('Sin escritura', 0, 'coral', '0'), ('Sin bucle', 0, 'coral', '0')],
                scale=100, note='Resolver las seis no basta: la configuración sin parada llega al mismo resultado con 12 pasos en vez de 5. La eficiencia es una propiedad del harness.',
                note_kind='gold', foot=EJEC, label_w=330)


# ---------------------------------------------------------------- SE-494
def se494_casos() -> Fig:
    from figure_kit import grouped_bars as gb
    return gb(
        "Un comprobador de reglas del repositorio: dónde acierta y dónde se equivoca (17 casos)",
        "Barras horizontales con los 17 casos de un comprobador determinista de reglas: 9 aciertos al detectar una infracción, 4 omisiones, como la ruta temporal armada por concatenación, el token partido en dos cadenas, la llamada a eval por un nombre armado y la prueba vacía, 1 falsa alarma ante un comentario que menciona la ruta y 3 casos sin infracción que no se marcan.",
        ["Infracciones detectadas (aciertos)", "Infracciones que se escapan (omisiones)", "Falsas alarmas", "Casos sin infracción que no se marcan"],
        [("Casos", [9, 4, 1, 3], "gold")],
        unit="Casos de 17", horizontal=True, label_w=290, ticks=[0, 3, 6, 9, 12],
        note="Con 17 casos: 9 aciertos, 1 falsa alarma y 4 omisiones (precisión 90 %, cobertura 69 %). Una regla mecánica es barata y exacta en lo que escribe, y ciega a lo que se escribe de otra forma.",
        note_kind="coral", foot=EJEC)


def se494_donde_aplicar() -> Fig:
    return flow('Dónde vive una regla del repositorio según cuánto se puede mecanizar',
                'Diagrama con tres cajas en una fila: la regla escrita como prosa en el archivo de instrucciones guía al modelo pero nadie la comprueba; la misma regla como hook antes de escribir bloquea la acción; la misma regla como compuerta de integración continua rechaza el cambio.',
                [[('Prosa en el archivo de instrucciones\nGuía, no obliga', 'gold'), ('Hook antes de escribir\nBloquea la acción', 'teal'), ('Compuerta en integración continua\nRechaza el cambio', 'navy')]],
                note='Seis de diez reglas del ejemplo se pueden mecanizar. Las cuatro semánticas (claridad, honestidad de las fuentes) solo pueden vivir como prosa y como revisión.',
                note_kind='gold', foot=EJEC, box_h=96)


def se494_resultados() -> Fig:
    return bars('Resultado del comprobador sobre 17 casos con 13 infracciones reales',
                'Gráfico de barras: 9 infracciones detectadas, 4 omitidas y 1 falsa alarma sobre diecisiete casos.',
                [('Infracciones detectadas', 9, 'teal', '9'), ('Infracciones omitidas', 4, 'coral', '4'), ('Falsas alarmas', 1, 'gold', '1')],
                scale=60, note='Las omisiones son más caras que la falsa alarma: la alarma cuesta una revisión, la omisión cuesta un defecto que pasa con apariencia de comprobado.',
                note_kind='coral', foot=EJEC, label_w=330)


# ---------------------------------------------------------------- SE-495
def se495_comandos() -> Fig:
    return grouped_bars(
        "Treinta comandos frente a dos políticas: prefijos permitidos y análisis del comando",
        "Barras agrupadas con los errores de dos políticas sobre treinta comandos: de 18 comandos inseguros, la lista de prefijos permite 13 y el análisis del comando 0; de 12 comandos seguros, los prefijos deniegan 0 y el análisis 1, un comando benigno con una tubería; ambos deniegan el empuje forzado.",
        ["Inseguros permitidos (de 18)", "Seguros denegados (de 12)"],
        [("Lista de prefijos", [13, 0], "coral"), ("Análisis del comando", [0, 1], "teal")],
        unit="Comandos", plot_h=230, ticks=[0, 4, 8, 12, 16],
        note="De 18 comandos inseguros, los prefijos dejan pasar 13 y el análisis, 0. De 12 seguros, los prefijos deniegan 0 y el análisis, 1. El análisis compra seguridad con una falsa denegación.",
        note_kind="gold", foot=EJEC)


def se495_inseguros() -> Fig:
    return bars('Comandos inseguros permitidos de 18 según la política',
                'Gráfico de barras: la lista de prefijos permite 13 de 18 comandos inseguros y el análisis del comando permite 0; entre los 12 comandos seguros, los prefijos deniegan 0 y el análisis deniega 1.',
                [('Lista de prefijos: inseguros permitidos', 13, 'coral', '13 de 18'), ('Análisis: inseguros permitidos', 0, 'teal', '0 de 18'),
                 ('Lista de prefijos: seguros denegados', 0, 'teal', '0 de 12'), ('Análisis: seguros denegados', 1, 'gold', '1 de 12')],
                scale=50, note='Un permiso por prefijo describe cómo empieza un comando, no qué hace. Los operadores de shell convierten un comando permitido en dos.',
                note_kind='coral', foot=EJEC, label_w=380)


def se495_capas() -> Fig:
    return flow('Capas de control de una llamada a herramienta, de la más barata a la más estricta',
                'Diagrama con cuatro cajas: la herramienta debe estar ofrecida al modelo; el análisis de argumentos permite o deniega; el confinamiento resuelve rutas dentro de la raíz; la aprobación humana decide lo irreversible.',
                [[('Herramienta ofrecida', 'plain'), ('Análisis de argumentos', 'teal'), ('Confinamiento de rutas', 'teal'), ('Aprobación humana', 'gold')]],
                note='Cada capa cubre lo que la anterior no ve. Ninguna sustituye a la última para lo irreversible, y la última deja de valer si se concede por costumbre.',
                note_kind='gold', foot=EJEC, box_h=80)


# ---------------------------------------------------------------- SE-496
def se496_estrategias() -> Fig:
    sizes = [6000, 12000, 24000, 48000]
    return line_chart(
        "Hechos recordables tras 120 turnos según la estrategia de contexto y el tamaño de la ventana",
        "Líneas con los hechos recordables, de 10, tras 120 turnos según el tamaño de la ventana: truncar conserva 0, 1, 4 y 10 con 6 000, 12 000, 24 000 y 48 000 fichas; resumir lo declarado 6, 6, 8 y 10; un archivo de notas del harness 8, 8, 9 y 10; con 48 000 fichas cabe toda la sesión.",
        [("Truncar lo antiguo", list(zip(sizes, [0, 1, 4, 10])), "coral"), ("Resumir lo declarado", list(zip(sizes, [6, 6, 8, 10])), "gold"),
         ("Archivo de notas del harness", list(zip(sizes, [8, 8, 9, 10])), "teal")],
        x_label="Ventana de contexto (fichas)", y_label="Hechos recordables (de 10)", x_ticks=[(s, f"{s // 1000} 000") for s in sizes], y_ticks=[0, 2, 4, 6, 8, 10], point_labels="none",
        note="Modelo determinista de 120 turnos de 400 fichas con 10 hechos en puntos fijos. Describe el mecanismo de pérdida de cada estrategia con supuestos explícitos; no mide la compactación de ningún producto.",
        note_kind="gold", foot=EJEC)


def se496_ciclo() -> Fig:
    return flow('Ciclo de contexto con relevo: escribir fuera de la ventana lo que debe sobrevivir',
                'Diagrama con dos filas de cajas: la sesión trabaja y el harness registra decisiones y restricciones en un archivo de notas; cuando la ventana se acerca al límite se compacta o se abre una sesión nueva; la sesión siguiente arranca leyendo las notas y el estado del repositorio y comprueba el estado antes de seguir.',
                [[('Sesión trabaja y deja notas', 'teal'), ('Ventana cerca del límite', 'coral'), ('Compactar o abrir sesión nueva', 'gold')],
                 [('Leer notas y estado del repositorio', 'teal'), ('Comprobar que el estado coincide', 'navy'), ('Continuar con una tarea pequeña', 'plain')]],
                note='Lo que importa es lo que está en disco al cierre: notas, commit y pruebas. Una sesión nueva no hereda nada que no se haya escrito.',
                note_kind='gold', foot=EJEC, box_h=76)


def se496_doce_mil() -> Fig:
    return bars('Hechos recordados de 10 con una ventana de 12 000 fichas',
                'Gráfico de barras con una ventana de 12 000 fichas: truncar lo antiguo conserva 1 de 10 hechos, resumir lo declarado 6 y el archivo de notas del harness 8.',
                [('Truncar lo antiguo', 1, 'coral', '1 de 10'), ('Resumir lo declarado', 6, 'gold', '6 de 10'), ('Archivo de notas del harness', 8, 'teal', '8 de 10')],
                scale=60, note='Los 2 hechos que ninguna estrategia conserva aparecieron solo dentro de la salida de una herramienta, nunca en un mensaje de la persona: nadie los declaró ni los anotó.',
                note_kind='coral', foot=EJEC, label_w=330)


# ---------------------------------------------------------------- SE-497
def se497_reglas() -> Fig:
    return scatter(
        "Cinco reglas de parada sobre 4 000 tareas sintéticas: resueltas frente a costo",
        "Dispersión de las tareas resueltas frente a las iteraciones medias de cinco reglas de parada: sin tope resuelve 69,9 por ciento con 20,1 iteraciones de media; el tope de 10 resuelve 68,8 con 5,0; el tope de 30 resuelve 69,2 con 11,2; el detector de falta de progreso resuelve 77,0 con 3,5, igual que combinado con el tope de 10.",
        [("Reglas de parada", [(20.1, 69.9, "Sin tope (60 en las inviables)", "l"), (5.0, 68.8, "Tope de 10", "b"), (11.2, 69.2, "Tope de 30", "r"),
                              (3.5, 77.0, "Detector de falta de progreso, solo o con tope de 10 (6 en las inviables)", "r")], "coral")],
        x_label="Iteraciones medias por tarea", y_label="Tareas resueltas (%)", y_zero=False, x_ticks=[(0, "0"), (5, "5"), (10, "10"), (15, "15"), (20, "20"), (25, "25")],
        y_ticks=[60, 65, 70, 75, 80], point_labels="none",
        note="Mezcla del autor: 70 % de tareas reintentables, 15 % que exigen cambiar de plan y 15 % inviables. Un tope solo limita el daño; cambiar de plan al detectar que no hay progreso añade 7 puntos.",
        note_kind="gold", foot=SIM)


def se497_inviables() -> Fig:
    return bars('Iteraciones gastadas en las tareas inviables según la regla de parada',
                'Gráfico de barras con las iteraciones gastadas en tareas inviables: sin tope 60, tope de 30 iteraciones 30, tope de 10 iteraciones 10 y detector de falta de progreso 6.',
                [('Sin tope', 60, 'coral', '60'), ('Tope de 30', 30, 'coral', '30'), ('Tope de 10', 10, 'gold', '10'), ('Detector de falta de progreso', 6, 'teal', '6')],
                scale=11, note='El costo de una tarea inviable es proporcional a la regla de parada, no a la tarea. Una tarea inviable sin tope gasta 10 veces más que con el detector.',
                note_kind='gold', foot=SIM, label_w=330)


def se497_bucle() -> Fig:
    return flow('Bucle de un agente con tres salidas distintas de «seguir intentando»',
                'Diagrama con dos filas: el agente actúa y observa; el harness compara con el intento anterior; si el resultado se repite tres veces cambia de plan una vez; si vuelve a repetirse o se agota el tope, escala a una persona con el rastro.',
                [[('Actuar y observar', 'plain'), ('Comparar con el intento anterior', 'teal'), ('Repetido tres veces: cambiar de plan', 'gold')],
                 [('Verificar con pruebas', 'teal'), ('Éxito: parar', 'navy'), ('Repetido otra vez o tope: escalar', 'coral')]],
                note='Parar bien tiene tres salidas: éxito verificado, cambio de plan y escalada con evidencia. Un tope sin escalada solo esconde el fallo.',
                note_kind='gold', foot=EJEC, box_h=76)


# ---------------------------------------------------------------- SE-498
def se498_proteccion() -> Fig:
    return grouped_bars(
        "Cinco acciones destructivas contra 15 archivos: qué sobrevive y qué se recupera",
        "Barras horizontales con los archivos intactos, de 15, tras cinco acciones destructivas, 13 en el proyecto y 2 fuera: sin protección sobreviven 0 y se recuperan 0; con solo confinamiento sobreviven 2 y se recuperan 2; con confinamiento y copia previa sobreviven 2 y se recuperan los 15; sin confinar y con Git sobreviven 0 y se recuperan 10.",
        ["Sin protección (0 acciones bloqueadas)", "Solo confinamiento (2 acciones bloqueadas)", "Confinamiento + copia previa (2)", "Sin confinar + Git (0)"],
        [("Intactos tras el agente", [0, 2, 2, 0], "coral"), ("Intactos tras recuperar", [0, 2, 15, 10], "teal")],
        unit="Archivos intactos (de 15)", horizontal=True, label_w=290, ticks=[0, 5, 10, 15],
        note="El confinamiento impide el daño fuera de la raíz y no deshace el de dentro; la copia deshace lo de dentro y no impide nada. Git recupera 10 de 15: los archivos no versionados y los de fuera no vuelven.",
        note_kind="coral", foot=EJEC)


def se498_capas() -> Fig:
    return flow('Control de daño en capas: impedir, acotar y deshacer',
                'Diagrama con cuatro cajas en una fila: confinar rutas a la raíz del proyecto, tomar una copia o un commit antes de actuar, ejecutar la acción con permisos mínimos y restaurar desde la copia si la verificación falla.',
                [[('Confinar a la raíz', 'teal'), ('Copiar o confirmar antes', 'gold'), ('Ejecutar con permisos mínimos', 'plain'), ('Restaurar si falla', 'navy')]],
                note='Impedir y deshacer son controles distintos y complementarios. Lo que no se puede deshacer (un envío, un pago, un borrado remoto) solo se controla impidiendo o aprobando.',
                note_kind='gold', foot=EJEC, box_h=80)


def se498_intactos() -> Fig:
    return bars('Archivos intactos de 15 después de recuperar',
                'Gráfico de barras con los archivos intactos de 15 tras recuperar: sin protección 0, solo confinamiento 2, Git sin confinar 10 y confinamiento con copia previa 15.',
                [('Sin protección', 0, 'coral', '0'), ('Solo confinamiento', 2, 'coral', '2'), ('Sin confinar + Git', 10, 'gold', '10'), ('Confinamiento + copia previa', 15, 'teal', '15')],
                scale=50, note='Ninguna capa alcanza sola: las dos juntas llegan a 15 en un caso donde cada una por separado deja huecos.',
                note_kind='gold', foot=EJEC, label_w=330)


FIGURES = {
    "se-493-ablacion-del-harness.svg": se493_ablacion,
    "se-493-anatomia-del-harness.svg": se493_anatomia,
    "se-493-tareas-resueltas.svg": se493_resueltas,
    "se-494-casos-del-comprobador.svg": se494_casos,
    "se-494-donde-aplicar-una-regla.svg": se494_donde_aplicar,
    "se-494-resultados-del-comprobador.svg": se494_resultados,
    "se-495-comandos-y-politicas.svg": se495_comandos,
    "se-495-inseguros-permitidos.svg": se495_inseguros,
    "se-495-capas-de-permiso.svg": se495_capas,
    "se-496-estrategias-de-contexto.svg": se496_estrategias,
    "se-496-ciclo-con-relevo.svg": se496_ciclo,
    "se-496-hechos-con-doce-mil.svg": se496_doce_mil,
    "se-497-reglas-de-parada.svg": se497_reglas,
    "se-497-iteraciones-inviables.svg": se497_inviables,
    "se-497-bucle-con-salidas.svg": se497_bucle,
    "se-498-proteccion-y-recuperacion.svg": se498_proteccion,
    "se-498-capas-de-control-de-dano.svg": se498_capas,
    "se-498-archivos-intactos.svg": se498_intactos,
}
