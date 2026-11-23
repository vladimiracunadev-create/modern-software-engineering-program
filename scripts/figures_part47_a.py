"""Figures for SE-565 to SE-570 (SPEC, agents and agentic life cycle: synthetic data with fixed seeds, plus runs of real CPython/SQLite code on Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, heatmap, line_chart, percentile_intervals, stacked_bars


SINT = "Datos sintéticos con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
EJEC = "Código ejecutado de verdad en Windows 11 y Ubuntu (WSL2) con datos sintéticos; los recuentos son idénticos en ambos."
REAL = "Medido en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); los tiempos de reloj cambian de equipo en equipo."

# ---------------------------------------------------------------- SE-565
def se469_vocabulario_vago() -> Fig:
    return grouped_bars(
        "Cuatro detectores de vaguedad sobre 125 frases de requisitos: 60 vagas y 65 comprobables",
        "Barras agrupadas con las vagas halladas, las falsas alarmas y las vagas que pasan de cuatro detectores sobre 125 frases, 60 vagas y 65 comprobables: la lista de palabras halla 40 con 10 falsas alarmas, la falta de medida halla 56 con 5, la combinación con y halla 40 sin falsas alarmas y deja pasar 20, y con o halla 56 con 15 y deja pasar 4.",
        ["Lista de palabras vagas", "Falta de medida o estado", "Palabra vaga y sin medida", "Palabra vaga o sin medida"],
        [("Vagas halladas", [40, 56, 40, 56], "teal"), ("Falsas alarmas", [10, 5, 0, 15], "coral"), ("Vagas que pasan", [20, 4, 20, 4], "gold")],
        unit="Frases", decimals=0, plot_h=260,
        note="Frases marcadas por cada detector: 50, 61, 40 y 71. Ninguno gana en todo: exigir las dos señales elimina las falsas alarmas y deja pasar 20 frases vagas; exigir una u otra deja pasar 4 a cambio de 15 falsas alarmas. Las frases y los detectores fueron escritos por el autor sabiendo qué buscan.",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-565
def se469_espacio_de_interpretaciones() -> Fig:
    xs = [0, 2, 4, 6, 8]
    return line_chart(
        "Ocho decisiones abiertas de dos o tres lecturas: comportamientos posibles y observados en 200 implementaciones",
        "Líneas en escala logarítmica con los comportamientos posibles y los distintos observados en 200 implementaciones según las decisiones resueltas: con 0 hay 864 posibles y 184 distintos; con 2, 144 y 107; con 4, 36 y 36; con 6, 6 y 6; con 8, 1 y 1; las implementaciones que coinciden con la intención son 0, 1, 5, 53 y 200.",
        [("Comportamientos posibles", list(zip(xs, [864, 144, 36, 6, 1])), "grey"), ("Distintos en 200 implementaciones", list(zip(xs, [184, 107, 36, 6, 1])), "coral")],
        x_label="Decisiones resueltas (de 8)", y_label="Comportamientos", log_y=True, x_ticks=[(x, str(x)) for x in xs], y_ticks=[1, 10, 100, 1000],
        point_labels="all", decimals=0, plot_h=280,
        note="Implementaciones que coinciden con la intención (de 200): 0, 1, 5, 53 y 200 con 0, 2, 4, 6 y 8 decisiones resueltas. Cada decisión resuelta divide el espacio por su número de lecturas. Con las ocho abiertas, ninguna de 200 implementaciones coincide con la intención. El modelo supone decisiones independientes y lecturas igual de probables.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-565
def se469_trazabilidad_y_vacias() -> Fig:
    return stacked_bars(
        "Doce defectos inyectados entre 25 entradas de especificación y 24 pruebas: qué comprobación encuentra cada uno",
        "Barras apiladas horizontales con los defectos inyectados que encuentra cada comprobación: identificadores y criterios encuentran 8 (3 requisitos sin prueba, 2 pruebas huérfanas, 1 identificador repetido, 2 requisitos sin criterio), el árbol sintáctico añade las 3 pruebas sin aserción y llega a 11, y queda sin ver una prueba que cita el requisito RF-02 pero afirma que dos más dos son cuatro.",
        ["Requisito sin prueba", "Prueba huérfana", "Identificador repetido", "Requisito sin criterio", "Prueba sin aserción", "Prueba que afirma algo irrelevante"],
        [("Encontrados por identificadores y criterios", [3, 2, 1, 2, 0, 0], "teal"), ("Añadidos por el árbol sintáctico", [0, 0, 0, 0, 3, 0], "navy"), ("No encontrados", [0, 0, 0, 0, 0, 1], "coral")],
        unit="Defectos inyectados", horizontal=True, decimals=0, label_w=280,
        note="La comprobación formal encuentra 8 de 12 y el árbol sintáctico llega a 11. Queda sin ver una prueba con forma correcta que comprueba otra cosa. Los defectos los inyectó el autor y la comprobación se escribió para encontrarlos.",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-566
def se470_incoherencias_entre_artefactos() -> Fig:
    return grouped_bars(
        "Hallazgos de un analizador de texto sobre constitución, plan y tareas con incoherencias inyectadas",
        "Barras horizontales con los 18 hallazgos de un analizador de texto sobre tres artefactos de un servicio de avisos: tres requisitos sin tarea, dos decisiones del plan que violan la constitución, tres dependencias hacia tareas posteriores y tres tareas de código antes de su prueba, y un hallazgo en cada uno de los demás tipos.",
        ["Requisito sin tarea", "Identificador de tarea duplicado", "Tarea con requisito inexistente", "Tarea sin requisito", "Plan que viola la constitución", "Plan que cita un requisito inexistente",
         "Conflicto numérico entre decisiones (24 frente a 48 horas)", "Dependencia de una tarea posterior", "Ciclo de dependencias", "Tareas en paralelo sobre el mismo archivo", "Código planificado antes de su prueba"],
        [("Hallazgos", [3, 1, 1, 1, 2, 1, 1, 3, 1, 1, 3], "navy")],
        unit="Hallazgos (18 en total)", horizontal=True, decimals=0, label_w=330,
        note="El analizador emite 18 hallazgos; 17 son incoherencias reales y uno es discutible. No ve dos problemas inyectados que exigen entender el significado: un canal distinto entre requisito y plan y un requisito sin mecanismo.",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-566
def se470_presupuesto_de_preguntas() -> Fig:
    xs = [0, 3, 5, 8, 14]
    return line_chart(
        "Fracción del costo esperado de 14 ambigüedades que queda sin resolver según el número de preguntas (2 000 especificaciones)",
        "Líneas con la fracción del costo esperado de catorce ambigüedades que queda sin resolver según las preguntas de clarificación y la estrategia: con cinco preguntas el orden del documento deja 64,3 por ciento, el azar 64,5, el mayor impacto 29,8 y el mayor costo esperado 29,3.",
        [("Orden del documento", list(zip(xs, [100.0, 78.7, 64.3, 42.8, 0.0])), "grey"), ("Al azar", list(zip(xs, [100.0, 78.5, 64.5, 43.1, 0.0])), "gold"),
         ("Mayor impacto", list(zip(xs, [100.0, 46.4, 29.8, 14.0, 0.0])), "teal"), ("Mayor costo esperado", list(zip(xs, [100.0, 45.8, 29.3, 13.6, 0.0])), "navy")],
        x_label="Preguntas de clarificación", y_label="Costo esperado sin resolver (%)", x_ticks=[(x, str(x)) for x in xs], y_ticks=[0, 20, 40, 60, 80, 100],
        point_labels="none", decimals=1, plot_h=300,
        note="El orden del documento rinde igual que el azar: no contiene información sobre cuánto importa cada ambigüedad (las dos líneas casi se superponen). Ordenar por impacto o por costo esperado reduce a menos de la mitad lo que queda con cinco preguntas. Los impactos son supuestos del autor.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-566
def se470_tareas_y_ruta_critica() -> Fig:
    return grouped_bars(
        "Cuarenta tareas con 53 dependencias: duración con distinto número de trabajadores y orden del archivo",
        "Barras horizontales con la duración de 40 tareas con 53 dependencias: 52,3 con un trabajador, 27,6 con dos, 14,4 con cuatro y 10,8 con ocho, frente a una ruta crítica de 10,4; si se ejecutan en el orden del archivo desordenado dentro de cada fase, 8 de 53 dependencias se violan.",
        ["1 trabajador", "2 trabajadores", "4 trabajadores", "8 trabajadores", "Ruta crítica (mínimo con cualquier número)"],
        [("Duración", [52.3, 27.6, 14.4, 10.8, 10.4], "navy")],
        unit="Duración", horizontal=True, decimals=1, label_w=270,
        note="Fracción del trabajo total: 100,0 %, 52,7 %, 27,5 %, 20,6 % y 19,9 %. Hay siete olas de hasta 13 tareas. La ruta crítica es un suelo: ocho trabajadores ya están a un 4 % de ella. Si el agente ejecuta las tareas en un orden de archivo desordenado dentro de cada fase, 8 de 53 dependencias se violan. Duraciones y dependencias son sintéticas.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-567
def se471_bucle_y_regresion() -> Fig:
    return grouped_bars(
        "Bucle implementar y converger con 40 criterios y 20 abiertos: pasadas según la tasa de regresión (5 000 corridas por fila)",
        "Barras agrupadas con las pasadas del bucle según la regresión por pasada: sin regresión la mediana es de 3 y el percentil 90 de 5; con 2 por ciento, 5 y 10; con 5 por ciento, 10 y 10; con 10 por ciento, 10 y 10, con un máximo de 10 pasadas.",
        ["0 %", "2 %", "5 %", "10 %"],
        [("Pasadas (mediana)", [3, 5, 10, 10], "teal"), ("Percentil 90", [5, 10, 10, 10], "coral")],
        unit="Pasadas", decimals=0, ref_lines=[(10, "máximo de 10 pasadas")], plot_h=260,
        note="Corridas que topan el máximo de 10: 0,0 %, 9,4 %, 62,4 % y 96,3 %; criterios abiertos al parar (media): 0,00, 0,17, 1,84 y 4,88. Una regresión del 5 % por pasada deja sin converger al 62,4 % de las corridas: de 20 criterios cumplidos, uno se rompe en cada pasada. La tasa de corrección de 0,7 y la independencia entre criterios son supuestos del autor.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-567
def se471_verificador_parcial() -> Fig:
    return grouped_bars(
        "Declaración de convergencia de un agente según la cobertura de su verificador (40 criterios, 5 000 corridas)",
        "Barras agrupadas con el porcentaje de corridas que declaran convergencia y de las que lo hacen con criterios abiertos según la cobertura del verificador: con 100 por ciento declara el 90,7 y ninguna con criterios abiertos; con 80, el 94,5 y el 93,7; con 50, el 98,9 y el 98,9; con 30, el 99,9 y el 99,9.",
        ["Cobertura del 100 %", "Cobertura del 80 %", "Cobertura del 50 %", "Cobertura del 30 %"],
        [("Declara convergido", [90.7, 94.5, 98.9, 99.9], "gold"), ("Con criterios aún abiertos", [0.0, 93.7, 98.9, 99.9], "coral")],
        unit="Corridas (%)", decimals=1, plot_h=260,
        note="Criterios abiertos reales al declarar (media): 0,0, 4,4, 10,7 y 14,8. Cuanto peor es el verificador, antes declara convergencia, porque tiene menos que corregir. Los criterios que no ve nunca se corrigen. La segunda barra es la fracción de todas las corridas que declaran con criterios abiertos.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-567
def se471_criterios_y_variantes() -> Fig:
    return grouped_bars(
        "Tres conjuntos de criterios ejecutables frente a diez variantes defectuosas de la regla de avisos",
        "Barras agrupadas con los casos y las variantes defectuosas detectadas de diez por tres conjuntos de criterios: tres casos del camino feliz detectan 3, nueve casos con bordes detectan 6 y diecisiete casos completos detectan las 10.",
        ["Camino feliz", "Camino feliz y bordes", "Criterios completos"],
        [("Casos", [3, 9, 17], "grey"), ("Variantes detectadas (de 10)", [3, 6, 10], "teal")],
        unit="Casos o variantes", decimals=0, ref_lines=[(10, "10 variantes")], plot_h=260,
        note="Quedan vivas con el camino feliz: ignora entregada, ignora silencio, repite, envía todos, avisa tras vencer, elige el más lejano y solo bloquea el idéntico; con bordes: ignora entregada, ignora silencio, envía todos y elige el más lejano. Esas variantes dependen de combinaciones de estado que un caso de borde de un solo valor no ejercita. Las diez variantes y los 17 casos son del autor: el 10 de 10 es consecuencia de haberlos escrito sabiéndolo.",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-568
def se472_leer_un_repositorio_ajeno() -> Fig:
    return grouped_bars(
        "Cinco estrategias para encontrar los usos de una función en un repositorio sintético de 300 módulos y 1 004 KB",
        "Barras horizontales en escala logarítmica con los módulos y los kilobytes leídos por cinco estrategias: leer todo lee 300 módulos y 1004 kilobytes y encuentra 5 de 5; buscar el nombre lee 4 y 11,8 y encuentra 4; buscar el nombre y el módulo que la define lee 9 y 27,2 y encuentra 5; un mapa vigente lee 5 y 15,3 y encuentra 5; un mapa desactualizado lee 4 y 11,8 y encuentra 4.",
        ["Leer todo (5 de 5)", "Buscar el nombre y leer los que lo contienen (4 de 5)", "Buscar el nombre y el módulo que lo define (5 de 5)", "Mapa de arquitectura vigente (5 de 5)", "Mapa de hace un trimestre (4 de 5)"],
        [("Módulos leídos", [300, 4, 9, 5, 4], "navy"), ("KB leídos", [1004.0, 11.8, 27.2, 15.3, 11.8], "coral")],
        unit="Módulos o KB leídos", horizontal=True, log=True, decimals=1, label_w=300,
        note="Entre paréntesis, los cambios hallados de 5. La búsqueda por nombre cuesta el 1,2 % de la lectura total y no ve el uso por cadena de texto. Un mapa vale lo que valga su mantenimiento. El repositorio es sintético, con módulos pequeños y un solo uso dinámico.",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-568
def se472_verificar_una_correccion() -> Fig:
    return heatmap(
        "Cinco errores y cuatro candidatos de arreglo: cuántos acepta cada política de verificación",
        "Mapa de calor con los arreglos aceptados de cinco por cada política de verificación y candidato: la batería existente acepta el código sin corregir en 5 de 5 casos; la reproducción lo rechaza pero acepta el arreglo del síntoma en 5; batería y reproducción aceptan el síntoma y rechazan dos arreglos que rompen otro caso; con casos vecinos solo se aceptan los arreglos de la causa, más uno que rompe otro caso.",
        ["Solo la batería existente", "Solo la reproducción", "Batería y reproducción", "Batería, reproducción y casos vecinos"],
        ["Sin corregir", "Arregla el síntoma", "Arregla y rompe otro caso", "Arregla la causa"],
        [[5, 5, 3, 5], [0, 5, 5, 5], [0, 5, 3, 5], [0, 0, 1, 5]],
        unit="Arreglos aceptados de 5", scale="coral", vmin=0, vmax=5, decimals=0, label_w=290,
        note="La batería existente acepta el código sin corregir en los cinco casos: por eso el error existía. Solo los casos vecinos rechazan el arreglo del síntoma. Los errores, las baterías y los arreglos son del autor.",
        note_kind="coral", foot=EJEC)


# ---------------------------------------------------------------- SE-568
def se472_cuando_evaluar_una_idea() -> Fig:
    xs = [5, 10, 25, 50, 75]
    return line_chart(
        "Valor esperado de tres políticas según la proporción de ideas buenas (construir 10, valor 40, evaluar 1)",
        "Líneas con el valor esperado de tres políticas según la proporción de ideas buenas: con 5 por ciento construir todo da menos 8,12, evaluar y construir si procede menos 2,18 y no construir 0; con 25 por ciento evaluar da 3,38 frente a menos 0,19; con 50 por ciento 10,33 frente a 9,68; con 75 por ciento construir todo da 19,74 frente a 17,29.",
        [("Construir todo", list(zip(xs, [-8.12, -6.21, -0.19, 9.68, 19.74])), "coral"), ("Evaluar y construir si procede", list(zip(xs, [-2.18, -0.84, 3.38, 10.33, 17.29])), "teal"),
         ("No construir", list(zip(xs, [0.0, 0.0, 0.0, 0.0, 0.0])), "grey")],
        x_label="Ideas buenas (%)", y_label="Valor esperado", x_ticks=[(x, f"{x} %") for x in xs], y_ticks=[-10, -5, 0, 5, 10, 15, 20],
        point_labels="none", decimals=2, plot_h=300,
        note="Mejor opción: no construir con 5 % y 10 %; evaluar con 25 % y 50 %; construir todo con 75 %. Evaluar compensa en un rango intermedio: con pocas ideas buenas conviene no construir y con casi todas buenas, construir sin evaluar. Los valores y la señal de evaluación son supuestos del autor.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-569
def se473_reglas_de_permiso() -> Fig:
    return grouped_bars(
        "Cuatro políticas de permisos frente a 30 órdenes de shell (16 peligrosas y 14 inocuas), sin ejecutar ninguna",
        "Barras horizontales con las órdenes que permite o frena cada política: permitirlo todo deja pasar las 16 peligrosas; la lista por prefijo deja pasar 13 y frena una inocua; el análisis de segmentos deja pasar 4 y frena una inocua; los segmentos con confinamiento de rutas frenan las 16 y ninguna inocua.",
        ["Permitirlo todo", "Lista por prefijo", "Lista con análisis de segmentos", "Segmentos y confinamiento de rutas"],
        [("Peligrosas permitidas (de 16)", [16, 13, 4, 0], "coral"), ("Peligrosas frenadas (de 16)", [0, 3, 12, 16], "teal"), ("Inocuas frenadas (de 14)", [0, 1, 1, 0], "gold")],
        unit="Órdenes", horizontal=True, decimals=0, label_w=260,
        note="El prefijo deja pasar las órdenes compuestas; el análisis de segmentos deja pasar cuatro lecturas fuera del espacio de trabajo. Las treinta órdenes se escribieron sabiendo qué reglas las evaluarían: el cero de la última fila es mérito de la construcción.",
        note_kind="coral", foot=EJEC)


# ---------------------------------------------------------------- SE-569
def se473_radio_de_dano() -> Fig:
    return grouped_bars(
        "Sesiones de 20 acciones con un 5 % de desvíos y 12 herramientas: sesiones con algún daño según la configuración (5 000 sesiones)",
        "Barras horizontales con el porcentaje de sesiones con algún daño en 5000 sesiones de 20 acciones con un 5 por ciento de desvíos: con todas las herramientas y alcance completo 41,6; con solo las seis de la tarea 21,3; con escritura confinada 3,2; con aprobación humana para lo destructivo 0,0.",
        ["Todas las herramientas, alcance completo (0,53 daños por sesión)", "Solo las herramientas de la tarea (0,24)", "…y escritura confinada al espacio de trabajo (0,03)", "…y lo destructivo exige aprobación humana (0,00)"],
        [("Sesiones con algún daño", [41.6, 21.3, 3.2, 0.0], "coral")],
        unit="Sesiones con algún daño (%)", horizontal=True, decimals=1, label_w=330,
        note="Entre paréntesis, las acciones dañinas por sesión. Cada restricción reduce el daño por una razón distinta y se acumulan. El cero de la última fila supone una aprobación humana perfecta, la suposición más débil. El 5 % de desvíos y la elección uniforme de herramienta son del autor.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-569
def se473_reglas_que_se_acumulan() -> Fig:
    return grouped_bars(
        "Reglas «permitir siempre» tras 24 semanas con 6 solicitudes semanales (500 equipos por fila)",
        "Barras agrupadas con las reglas de permitir siempre acumuladas en 24 semanas en 500 equipos: sin revisión la mediana es de 57 reglas, 20 amplias; con revisión cada 12 semanas 38 y 4; con revisión cada 4 semanas 13 y 1.",
        ["Nunca se revisan", "Se revisan cada 12 semanas", "Se revisan cada 4 semanas"],
        [("Reglas (mediana)", [57, 38, 13], "navy"), ("Reglas amplias (mediana)", [20, 4, 1], "coral")],
        unit="Reglas", decimals=0, plot_h=260,
        note="Equipos con alguna regla amplia: 100 %, 98 % y 75 %. Sin revisión se acumulan 57 reglas y todos los equipos tienen alguna amplia; revisar cada cuatro semanas mantiene el conjunto acotado sin eliminar el problema. El 40 % de aprobaciones permanentes y el 35 % de reglas amplias son supuestos del autor.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-570
def se474_gancho_y_modo_de_fallo() -> Fig:
    return grouped_bars(
        "Un gancho de política ejecutado como proceso sobre 58 eventos (18 peligrosos): salidas y modo de fallo",
        "Barras horizontales con las salidas de 58 eventos ejecutados como procesos reales: 40 con éxito, 12 con bloqueo, 4 con error y 2 con tiempo agotado; si solo el código 2 bloquea, 6 de las 18 acciones peligrosas se ejecutan; si todo lo que no sea éxito bloquea, ninguna.",
        ["Éxito (código 0)", "Bloqueo (código 2)", "Error (otro código)", "Tiempo agotado", "Peligrosas ejecutadas si solo el código 2 bloquea (de 18)", "Peligrosas ejecutadas si todo lo que no sea éxito bloquea (de 18)"],
        [("Eventos o acciones", [40, 12, 4, 2, 6, 0], "navy")],
        unit="Eventos o acciones", horizontal=True, decimals=0, label_w=330,
        note="Con todo lo que no sea éxito bloqueando, ninguna acción inocua se bloquea. El diseño por defecto de estos controles falla abierto: una caída o un tiempo agotado no bloquean. El gancho imita un contrato documentado, no es la herramienta; el arranque de un proceso cuesta decenas de milisegundos y cambia de equipo en equipo.",
        note_kind="coral", foot=REAL)


# ---------------------------------------------------------------- SE-570
def se474_cargar_habilidades() -> Fig:
    return grouped_bars(
        "Cuarenta habilidades y cien peticiones: selección según el estilo de descripción y costo de contexto de tres formas de cargar",
        "Barras horizontales en escala logarítmica con los tokens de contexto de tres formas de cargar 40 habilidades: cargar los 40 cuerpos cuesta unos 30496, las 40 descripciones 778 y las descripciones más un cuerpo 1541; con frases de activación se activa la habilidad correcta en 45 de 60 peticiones y con descripción genérica en 29.",
        ["Cargar los 40 cuerpos al arrancar", "Cargar solo las 40 descripciones", "Descripciones y un cuerpo cargado (media)"],
        [("Tokens de contexto", [30496, 778, 1541], "navy")],
        unit="Tokens de contexto", horizontal=True, log=True, decimals=0, label_w=270,
        note="Selección de 60 peticiones con habilidad: con frases de activación, 45 correctas, 15 incorrectas y 0 sin activar; con descripción genérica, 29 correctas, 15 incorrectas y 16 sin activar. Una buena descripción previene la falta de activación; el solape entre habilidades, que da las 15 activaciones incorrectas, es un defecto del conjunto. El selector es una coincidencia de palabras clave y los textos son sintéticos.",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-570
def se474_confinar_rutas() -> Fig:
    return grouped_bars(
        "Cuatro comprobaciones de confinamiento al directorio de trabajo sobre 22 intentos (10 legítimos y 12 de escape)",
        "Barras agrupadas con los escapes que pasan, de 12, y los legítimos rechazados, de 10, por cuatro comprobaciones: comparar el prefijo de texto deja pasar 3 escapes y rechaza 7 legítimos; el prefijo con separador sin normalizar deja pasar 7 y rechaza 1; normalizar deja pasar 1 y no rechaza ninguno; normalizar y rechazar el byte nulo deja pasar 0 y no rechaza ninguno.",
        ["Prefijo de texto", "Prefijo con separador, sin normalizar", "Normalizar y luego comparar", "Normalizar y rechazar el nulo"],
        [("Escapes que pasan (de 12)", [3, 7, 1, 0], "coral"), ("Legítimos rechazados (de 10)", [7, 1, 0, 0], "gold")],
        unit="Intentos", decimals=0, plot_h=260,
        note="La barra invertida cambia de significado entre sistemas: queda dentro con las reglas de POSIX y fuera con las de Windows. Los enlaces simbólicos no se probaron. Pasar esta batería no demuestra que la comprobación sea correcta.",
        note_kind="gold", foot=EJEC)


FIGURES = {
    "se-565-vocabulario-vago.svg": se469_vocabulario_vago,
    "se-565-espacio-de-interpretaciones.svg": se469_espacio_de_interpretaciones,
    "se-565-trazabilidad-y-vacias.svg": se469_trazabilidad_y_vacias,
    "se-566-incoherencias-entre-artefactos.svg": se470_incoherencias_entre_artefactos,
    "se-566-presupuesto-de-preguntas.svg": se470_presupuesto_de_preguntas,
    "se-566-tareas-y-ruta-critica.svg": se470_tareas_y_ruta_critica,
    "se-567-bucle-y-regresion.svg": se471_bucle_y_regresion,
    "se-567-verificador-parcial.svg": se471_verificador_parcial,
    "se-567-criterios-y-variantes.svg": se471_criterios_y_variantes,
    "se-568-leer-un-repositorio-ajeno.svg": se472_leer_un_repositorio_ajeno,
    "se-568-verificar-una-correccion.svg": se472_verificar_una_correccion,
    "se-568-cuando-evaluar-una-idea.svg": se472_cuando_evaluar_una_idea,
    "se-569-reglas-de-permiso.svg": se473_reglas_de_permiso,
    "se-569-radio-de-dano.svg": se473_radio_de_dano,
    "se-569-reglas-que-se-acumulan.svg": se473_reglas_que_se_acumulan,
    "se-570-gancho-y-modo-de-fallo.svg": se474_gancho_y_modo_de_fallo,
    "se-570-cargar-habilidades.svg": se474_cargar_habilidades,
    "se-570-confinar-rutas.svg": se474_confinar_rutas,
}
