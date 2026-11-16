"""Figures for SE-439 to SE-444 (modernization of a legacy grading module: synthetic data with fixed seeds, plus runs of real CPython/SQLite code on Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_flow_rows import chain_rows
from figure_kit import Fig, dumbbell, fmt_es, grouped_bars, heatmap, line_chart, percentile_intervals, scatter, stacked_bars
from figures_part07_a import bars


SINT = "Datos sintéticos con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
EJEC = "Código ejecutado de verdad en Windows 11 y Ubuntu (WSL2) con datos sintéticos; los recuentos son idénticos en ambos."
REAL = "Medido en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); los tiempos de reloj cambian de equipo en equipo."

# ---------------------------------------------------------------- SE-439
def se439_tamano_de_lote() -> Fig:
    return line_chart(
        "Relleno de 200 000 filas con 50 escrituras por segundo concurrentes: duración del relleno frente a espera de una escritura",
        "Línea en escala logarítmica con la duración del relleno y la espera en el percentil 99 de una escritura concurrente según el tamaño de lote: con 200 000 filas dura 4,0 segundos y la escritura espera 3 969 milisegundos; con 20 000, 4,2 s y 400 ms; con 2 000, 6,5 s y 44 ms; con 200, 29,0 s y 8,7 ms; con 20, 254,0 s y 5,1 ms.",
        [("Tamaño de lote", [(4.0, 3969, "200 000", "t"), (4.2, 400, "20 000", "r"), (6.5, 44, "2 000", "r"), (29.0, 8.7, "200", "r"), (254.0, 5.1, "20", "t")], "coral")],
        x_label="Duración del relleno (s)", y_label="Espera p99 de una escritura (ms)", log_x=True, log_y=True,
        x_ticks=[(1, "1"), (10, "10"), (100, "100"), (1000, "1000")], y_ticks=[1, 10, 100, 1000, 10000], point_labels="none",
        note="Un lote pequeño casi no hace esperar a las escrituras y alarga el relleno por el costo fijo de cada lote (el bloqueo por lote va de 4 005 ms a 5,4 ms). Los costos de 0,02 ms por fila y 5 ms por lote, la pausa de 20 ms y las llegadas Poisson son supuestos del autor.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-439
def se439_relleno_que_pisa() -> Fig:
    return grouped_bars(
        "Relleno de 20 000 filas en lotes de 1 000 con un 2 % de filas modificadas por la aplicación entre lectura y escritura",
        "Barras horizontales con las filas con la columna nueva distinta del texto tras cuatro estrategias de relleno: el relleno ingenuo deja 389, el condicional por versión 0, el condicional con la aplicación escribiendo en ambas columnas 0 y el ingenuo con la aplicación escribiendo en ambas columnas también 389.",
        ["Relleno ingenuo", "Condicional por versión (y pasada final)", "Condicional con la aplicación escribiendo en ambas columnas", "Ingenuo con la aplicación escribiendo en ambas columnas"],
        [("Filas con la columna nueva distinta del texto", [389, 0, 0, 389], "coral")],
        unit="Filas con la columna nueva distinta del texto", horizontal=True, label_w=330, ticks=[0, 100, 200, 300, 400],
        note="Los recuentos coinciden en las cuatro; el contenido, no. Escribir en ambas columnas no corrige un relleno ingenuo, que sobrescribe lo que la aplicación acaba de poner. La intercalación es determinista y no hay concurrencia real.",
        note_kind="coral", foot=EJEC)


# ---------------------------------------------------------------- SE-439
def se439_metadatos_y_reconstruccion() -> Fig:
    return grouped_bars(
        "Costo de cambios de esquema sobre 200 000 filas en SQLite",
        "Barras horizontales en escala logarítmica con el tiempo de cuatro cambios de esquema sobre 200 000 filas en SQLite, en Windows y en Ubuntu: añadir una columna nula 0,37 y 0,34 milisegundos, reconstruir la tabla 74 y 92, rellenar con una sentencia 57 y 62, y rellenar por lotes de 2 000 60 y 151.",
        ["Añadir una columna nula", "Reconstruir la tabla (copiar)", "Rellenar con una sola sentencia", "Rellenar por lotes de 2 000"],
        [("Windows 11 (SQLite 3.45.3)", [0.37, 74, 57, 60], "gold"), ("Ubuntu bajo WSL2 (SQLite 3.45.1)", [0.34, 92, 62, 151], "teal")],
        unit="Tiempo (ms)", horizontal=True, log=True, label_w=250, ticks=[0.1, 1, 10, 100, 1000],
        note="Añadir una columna es un cambio de metadatos y reconstruir la tabla cuesta cientos de veces más (200 y 267 veces). Rellenar por lotes cuesta 1,05 y 2,44 veces la sentencia única. SQLite es una base embebida en memoria; otros motores tienen reglas distintas. Los tiempos de reloj cambian de equipo en equipo.",
        note_kind="gold", foot=REAL)


# ---------------------------------------------------------------- SE-440
def se440_tres_formas_de_escribir_dos_veces() -> Fig:
    return line_chart(
        "Claves distintas entre dos almacenes tras 100 000 escrituras sobre 20 000 claves, según la tasa de fallo del segundo",
        "Líneas en escala logarítmica horizontal con las claves distintas entre dos almacenes según la tasa de fallo del segundo: el mejor esfuerzo deja 110, 292 y 1 069 con fallos del 0,1, 1 y 5 por ciento; tres intentos dejan 88, 84 y 76 por el desorden de las escrituras; la bandeja de salida con número de secuencia deja 0 en los tres casos.",
        [("Mejor esfuerzo (sin reintento)", [(0.1, 110), (1, 292), (5, 1069)], "coral"), ("Hasta tres intentos", [(0.1, 88), (1, 84), (5, 76)], "gold"),
         ("Bandeja de salida con secuencia", [(0.1, 0), (1, 0), (5, 0)], "teal")],
        x_label="Tasa de fallo del segundo almacén (%)", y_label="Claves distintas entre los dos almacenes", log_x=True,
        x_ticks=[(0.1, "0,1"), (1, "1"), (5, "5")], y_ticks=[0, 250, 500, 750, 1000, 1250], point_labels="all",
        note="Los reintentos arreglan los fallos pero no el desorden (0,5 % de escrituras cruzadas); la bandeja con número de secuencia arregla ambos. Las tasas y el desorden son supuestos del autor y la bandeja reintenta sin límite.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-440
def se440_costo_de_detectar() -> Fig:
    return line_chart(
        "Filas leídas hasta detectar divergencias entre 100 000 filas (media de 300 corridas)",
        "Líneas en escala logarítmica con las filas leídas hasta detectar divergencias según cuántas hay: con una divergencia el muestreo del 1 por ciento lee 108 490, el del 10 por ciento 105 400 y las sumas por rangos 1 100; con diez, 10 947, 14 867 y 9 667; con cien, 1 583, 10 000 y 63 483.",
        [("Muestra del 1 %", [(1, 108490), (10, 10947), (100, 1583)], "coral"), ("Muestra del 10 %", [(1, 105400), (10, 14867), (100, 10000)], "gold"),
         ("Sumas por rangos", [(1, 1100), (10, 9667), (100, 63483)], "teal")],
        x_label="Filas divergentes", y_label="Filas leídas", log_x=True, log_y=True, x_ticks=[(1, "1"), (10, "10"), (100, "100")], y_ticks=[1000, 10000, 100000, 1000000],
        point_labels="all",
        note="Con una divergencia las sumas por rangos ganan (1 ciclo frente a 108,5 y 10,5); con cien, el muestreo del 1 % lee menos. Las divergencias se reparten al azar y de forma uniforme, cosa que rara vez ocurre: suelen agruparse.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-440
def se440_matriz_de_compatibilidad() -> Fig:
    changes = ["Añadir campo opcional", "Añadir campo obligatorio", "Quitar campo", "Renombrar campo", "Cambiar el tipo", "Ampliar valores permitidos"]
    values = [[1, 0, 1, 0], [1, 0, 1, 1], [1, 0, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1], [1, 0, 0, 0]]
    return heatmap(
        "Seis cambios de esquema y cuatro lecturas: lector viejo o nuevo, estricto o tolerante",
        "Mapa de calor de seis cambios de esquema frente a cuatro lecturas: un lector estricto falla en 11 de 12 casos y uno tolerante en 4 de 12; cambiar el tipo falla en las cuatro lecturas y renombrar un campo pasa con un lector tolerante nuevo que lee un dato viejo pero deja la nota ausente.",
        changes, ["Viejo lee dato nuevo, estricto", "Viejo lee dato nuevo, tolerante", "Nuevo lee dato viejo, estricto", "Nuevo lee dato viejo, tolerante"], values,
        unit="falla = excepción", row_title="Cambio", col_title="Quién lee y cómo",
        scale="coral", vmin=0, vmax=1, cell_fmt=lambda v: "falla" if v else "pasa", cell_h=40, label_w=210,
        note="El lector estricto falla en 11 de 12 celdas; el tolerante, en 4. «Pasa» solo dice que no hubo excepción: un lector tolerante que lee un dato viejo tras renombrar la nota la deja ausente sin avisar. El registro de tres campos es del autor.",
        note_kind="coral", foot=EJEC)


# ---------------------------------------------------------------- SE-441
def se441_ventana_de_observacion() -> Fig:
    return grouped_bars(
        "200 consumidores (194 reales) observados con distintas ventanas: cuántos reales se declararían «sin uso»",
        "Barras con los consumidores reales, de 194, que se declararían sin uso según la ventana de observación: 54,9 con 7 días, 26,2 con 30, 10,5 con 91, 7,1 con 180 y ninguno con 365 y 400 días.",
        ["7 días", "30 días", "91 días", "180 días", "365 días", "400 días"],
        [("Reales declarados «sin uso» (media)", [54.9, 26.2, 10.5, 7.1, 0.0, 0.0], "coral")],
        unit="Consumidores reales declarados «sin uso»", plot_h=250, ticks=[0, 20, 40, 60],
        note="La fracción de los 194 va del 28 % (7 días) al 14, 5, 4 y 0 %. Solo una ventana que cubra el ciclo más largo conocido ve a todos; un consumidor bianual que no esté en el inventario no lo vería ni la de 400 días. La mezcla de periodicidades es un supuesto del autor.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-441
def se441_retencion_por_reglas() -> Fig:
    return grouped_bars(
        "50 000 registros sintéticos de cuatro tipos: un corte único a cinco años frente a reglas por tipo",
        "Barras agrupadas con los errores de retención sobre 50 000 registros de cuatro tipos: un corte único a cinco años borra 5 479 registros antes de tiempo o en litigio y conserva 7 368 más de lo permitido, mientras que las reglas por tipo con retención legal dan 0 y 0 por construcción del experimento.",
        ["Corte único a 5 años", "Reglas por tipo con retención legal"],
        [("Borrados antes de tiempo o en litigio", [5479, 0], "coral"), ("Conservados más de lo permitido", [7368, 0], "gold")],
        unit="Registros de 50 000", plot_h=240,
        note="Las reglas dan cero porque definen la verdad del experimento: no prueban que los plazos sean correctos. Los plazos son ilustrativos del autor y no son asesoría legal.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-441
def se441_formatos_de_archivo() -> Fig:
    return stacked_bars(
        "100 000 filas archivadas en tres formatos y leídas de vuelta: filas que vuelven idénticas",
        "Barras apiladas horizontales con las filas de 100 000 que vuelven idénticas tras archivarlas: con CSV ninguna vuelve idéntica, porque cambian los tipos, 10 080 códigos pierden ceros y 19 851 textos vacíos se vuelven nulos; con líneas JSON y con SQLite vuelven las 100 000.",
        ["CSV (tipos inferidos al leer; 2,68 MB)", "Líneas JSON (3,42 MB)", "SQLite (3,31 MB)"],
        [("Vuelven idénticas", [0, 100000, 100000], "teal"), ("No vuelven idénticas", [100000, 0, 0], "coral")],
        unit="Filas de 100 000", horizontal=True, label_w=250,
        note="El CSV solo guarda texto: sin un esquema que declare los tipos, los pierde. Un bit cambiado en un dígito del JSON deja un archivo válido que el lector acepta; solo la suma SHA-256 lo delata. Los datos son sintéticos.",
        note_kind="coral", foot=EJEC)


# ---------------------------------------------------------------- SE-442
def se442_tres_opciones() -> Fig:
    return percentile_intervals(
        "Costo acumulado a diez años de tres opciones en 20 000 escenarios (múltiplos del costo anual actual)",
        "Intervalos con el costo acumulado a diez años de tres opciones, en múltiplos del costo anual actual: no hacer nada tiene percentil 10 de 12,1, mediana de 15,2 y percentil 90 de 19,1; evolucionar 12,1, 13,5 y 15,1; reescribir 13,7, 19,1 y 27,6; reescribir es la opción más barata en el 9,4 por ciento de los escenarios.",
        [("No hacer nada", [12.1, 15.2, 19.1]), ("Evolucionar", [12.1, 13.5, 15.1]), ("Reescribir", [13.7, 19.1, 27.6])],
        unit="Costo acumulado (múltiplos del costo anual actual)", marks=("p10", "mediana", "p90"), label_w=150, decimals=1,
        note="Reescribir es la opción más barata en el 9,4 % de los escenarios frente a evolucionar y tiene el rango más ancho. Es una consecuencia de los supuestos del autor, no un hallazgo sobre reescrituras reales.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-442
def se442_sensibilidad() -> Fig:
    span = {(0.9, 13.4): "12,5", (3.2, 7.5): "4,3", (3.8, 8.0): "4,2", (4.0, 7.2): "3,2", (4.4, 6.9): "2,4", (6.2, 4.6): "1,6", (5.9, 4.9): "1,0"}
    rows = [("Costo de construir (3,0 → 12,0)", 0.9, 13.4), ("Costo anual del sistema nuevo (0,4 → 0,9)", 3.2, 7.5), ("Duración en años (1,5 → 4,0)", 3.8, 8.0),
            ("Deriva del alcance por año (0,05 → 0,25)", 4.0, 7.2), ("Probabilidad de abandono (0 → 0,4)", 4.4, 6.9), ("Crecimiento tras evolucionar (0,1 → 0,6)", 6.2, 4.6),
            ("Crecimiento del costo del legado (3 % → 15 %)", 5.9, 4.9)]
    return dumbbell(
        "Sensibilidad: diferencia de costo entre reescribir y evolucionar al mover un parámetro (positiva: reescribir cuesta más)",
        "Puntos unidos con la diferencia de costo entre reescribir y evolucionar con el valor bajo y alto de cada parámetro: el costo de construir tiene el mayor recorrido, de +0,9 a +13,4, 12,5; el costo anual del sistema nuevo 4,3, la duración 4,2, la deriva del alcance 3,2, el abandono 2,4, el crecimiento tras evolucionar 1,6 y el del legado 1,0.",
        rows, unit="Reescribir − evolucionar (unidades de costo)", names=("Valor bajo del parámetro", "Valor alto"), decimals=1,
        delta=lambda a, b: "recorrido " + span[(a, b)], label_w=300,
        note="El costo de construir domina; el crecimiento del costo del legado, el argumento más citado, es el de menor efecto. Con el valor bajo reescribir gana en el 37 % de los escenarios en el costo de construir y con el alto en 0 %. El análisis mueve un parámetro cada vez y no capta interacciones.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-442
def se442_horizonte_de_equilibrio() -> Fig:
    pts = [(4, 6.7, "6,7 · gana 0 %", "t"), (6, 6.3, "6,3 · 1 %", "t"), (8, 6.0, "6,0 · 4 %", "t"), (10, 5.7, "5,7 · 10 %", "t"), (15, 4.5, "4,5 · 25 %", "t"), (20, 3.4, "3,4 · 36 %", "t")]
    return line_chart(
        "Reescribir frente a evolucionar según el horizonte (6 000 escenarios por fila)",
        "Línea con la diferencia mediana de costo entre reescribir y evolucionar según el horizonte, con el porcentaje de escenarios en que reescribir gana: a 4 años +6,7 y 0 por ciento, a 6 años +6,3 y 1, a 8 años +6,0 y 4, a 10 años +5,7 y 10, a 15 años +4,5 y 25, y a 20 años +3,4 y 36.",
        [("Reescribir − evolucionar (mediana)", pts, "teal")],
        x_label="Horizonte (años)", y_label="Reescribir − evolucionar (mediana, unidades de costo)", x_ticks=[(4, "4"), (6, "6"), (8, "8"), (10, "10"), (15, "15"), (20, "20")],
        y_ticks=[0, 2, 4, 6, 8], point_labels="none",
        note="La ventaja de evolucionar se acorta con el plazo, pero no se invierte en este rango: la diferencia sigue siendo positiva a 20 años. El rótulo de cada punto añade el porcentaje de escenarios en que reescribir gana. El horizonte es una variable de negocio: un sistema con fecha de retiro conocida cambia la respuesta más que cualquier detalle técnico.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-443
def se443_ruido_y_reintentos() -> Fig:
    return scatter(
        "5 000 commits por configuración: falsos rojos y defectos intermitentes (30 %) que salen verdes",
        "Dispersión de cinco configuraciones de pruebas inestables y reintentos: con 20 inestables y sin reintentos el 64,3 por ciento de los commits sanos sale rojo y el 24,7 de los que tienen un defecto intermitente sale verde; con 20 y dos reintentos 26,5 y 58,2; con 5 y ninguno 23,2 y 53,8; con 5 y dos reintentos 1,4 y 90,3; sin inestables 0,0 y 70,7.",
        [("Configuraciones (inestables · reintentos)", [(64.3, 24.7, "20 · ninguno", "l"), (26.5, 58.2, "20 · dos reintentos", "r"), (23.2, 53.8, "5 · ninguno", "l"),
                                                      (1.4, 90.3, "5 · dos reintentos", "r"), (0.0, 70.7, "0 · ninguno", "r")], "coral")],
        x_label="Commits sanos que salen rojos (%)", y_label="Commits con defecto que salen verdes (%)", y_zero=True,
        x_ticks=[(0, "0"), (20, "20"), (40, "40"), (60, "60"), (80, "80")], y_ticks=[0, 25, 50, 75, 100], point_labels="none",
        note="Reintentar reduce los falsos rojos y esconde defectos reales: con cinco inestables y dos reintentos el 90,3 % de los commits con el defecto pasan. La salida es aislar y corregir las inestables. El 5 %, el 30 % y la independencia son supuestos del autor.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-443
def se443_construccion_reproducible() -> Fig:
    rows = [
        [("Bytecode", "plain"), ("Invalidación por marca de tiempo", "plain"), ("Distintas", "coral")],
        [("Bytecode", "plain"), ("Invalidación por hash comprobado", "plain"), ("Idénticas", "teal")],
        [("Archivo comprimido", "plain"), ("Fechas de los archivos, orden del sistema", "plain"), ("Distintas", "coral")],
        [("Archivo comprimido", "plain"), ("Fechas fijas, orden del sistema", "plain"), ("Idénticas", "teal")],
        [("Archivo comprimido", "plain"), ("Fechas fijas, nombres ordenados", "plain"), ("Idénticas", "teal")],
    ]
    return chain_rows(
        "Dos construcciones del mismo código con fechas de modificación distintas: ¿mismo artefacto?",
        "Diagrama de flujo de cinco configuraciones de construcción del mismo código con fechas de modificación distintas: el bytecode por marca de tiempo da artefactos distintos y por hash comprobado idénticos; el archivo comprimido con fechas del archivo da distintos, con fechas fijas idénticos y con fechas fijas y nombres ordenados idénticos.",
        ["Artefacto", "Configuración", "Resultado"], rows, [220, 420, 190],
        note="Fijar las fechas y el modo de invalidación basta aquí. Que el orden del sistema fuera estable en estas dos máquinas no está garantizado en general. Son treinta módulos de dos líneas: el experimento muestra el mecanismo, no la reproducibilidad de una cadena real.",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-443
def se443_linea_base_con_incertidumbre() -> Fig:
    return line_chart(
        "Semiancho del intervalo del 95 % de una tasa de cambios fallidos del 15 % según los cambios observados",
        "Línea en escala logarítmica con el semiancho mediano del intervalo de confianza del 95 por ciento de una tasa de cambios fallidos del 15 por ciento según los cambios observados: 19,3 puntos con 10 cambios, 15,4 con 20, 9,6 con 50, 4,9 con 200 y 2,2 con 1 000; el intervalo contiene la tasa real en cerca del 95 por ciento de 3 000 periodos.",
        [("Semiancho mediano", [(10, 19.3, "±19,3", "t"), (20, 15.4, "±15,4", "t"), (50, 9.6, "±9,6", "t"), (200, 4.9, "±4,9", "t"), (1000, 2.2, "±2,2", "t")], "teal")],
        x_label="Cambios observados", y_label="Semiancho del intervalo (puntos porcentuales)", log_x=True,
        x_ticks=[(10, "10"), (20, "20"), (50, "50"), (200, "200"), (1000, "1000")], y_ticks=[0, 5, 10, 15, 20, 25], point_labels="none",
        note="Con 20 cambios la tasa del 15 % queda entre el 0 % y el 30 %. Para distinguir 15 % de 10 % con potencia del 80 % hacen falta unos 686 cambios. Se supone independencia entre cambios, algo falso cuando hay rachas. El intervalo del 95 % contuvo la tasa real entre el 95 y el 98 % de las veces.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-444
def se444_fases_y_divergencia() -> Fig:
    return grouped_bars(
        "Filas que difieren entre el esquema antiguo y el nuevo en cada fase de una migración de 5 000 filas",
        "Barras horizontales con las filas que difieren entre el esquema antiguo y el nuevo en cinco fases de una migración de 5 000 filas, con y sin fallos del uno por ciento: 5 000 al expandir, 220 tras rellenar, 1 y 0 con doble escritura, 5 y 0 con lectura del nuevo, y 391 y 387 al escribir solo en el nuevo, donde son escrituras que el esquema antiguo no tiene.",
        ["0. Expandir (el nuevo está vacío)", "1. Rellenar (escrituras durante el relleno)", "2. Doble escritura", "3. Lectura del nuevo", "4. Solo escritura nueva (valores que el antiguo no tiene)"],
        [("Con 1 % de fallos", [5000, 220, 1, 5, 391], "coral"), ("Sin fallos", [5000, 220, 0, 0, 387], "teal")],
        unit="Filas que difieren (de 5 000)", horizontal=True, label_w=300, ticks=[0, 1000, 2000, 3000, 4000, 5000],
        note="La misma cuenta significa cosas distintas según la fase. En la fase 4 las diferencias son escrituras que solo existen en el esquema nuevo y que se perderían al volver sin reconstruir. SQLite en memoria, escrituras intercaladas de forma determinista.",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-444
def se444_costo_de_volver() -> Fig:
    return line_chart(
        "Filas que solo existen en el esquema nuevo según los días desde que se dejó de escribir en el antiguo (60 escrituras al día)",
        "Línea con las filas que solo existen en el esquema nuevo según los días desde que se dejó de escribir en el antiguo, con 60 escrituras diarias sobre 5 000 filas: 0 con cero días, 58 con uno, 177 con tres, 406 con siete y 779 con catorce, el 15,6 por ciento.",
        [("Filas solo en el esquema nuevo", [(0, 0, "0", "t"), (1, 58, "58 (1,2 %)", "t"), (3, 177, "177 (3,5 %)", "t"), (7, 406, "406 (8,1 %)", "t"), (14, 779, "779 (15,6 %)", "l")], "coral")],
        x_label="Días desde que se dejó de escribir en el antiguo", y_label="Filas solo en el esquema nuevo (de 5 000)", x_ticks=[(0, "0"), (1, "1"), (3, "3"), (7, "7"), (14, "14")],
        y_ticks=[0, 200, 400, 600, 800, 1000], point_labels="none",
        note="Volver atrás pasa de no costar nada a afectar casi una de cada seis filas en dos semanas. Las escrituras uniformes sobre claves al azar son un supuesto del autor; en un sistema real se concentran en pocas filas y en fechas de cierre.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-444
def se444_reposo_antes_de_contraer() -> Fig:
    items = [('3 días', 86.7, 'coral', '86,7 %'), ('7 días', 60.1, 'coral', '60,1 %'), ('14 días', 33.2, 'gold', '33,2 %'), ('30 días', 11.4, 'gold', '11,4 %'), ('60 días', 2.9, 'teal', '2,9 %'), ('90 días', 1.1, 'teal', '1,1 %')]
    return bars('Defectos latentes que aparecen después de contraer, según el reposo (descubrimiento lognormal de mediana 9 días)',
                'Barras con la fracción de defectos latentes que aparecen después de contraer según el reposo, con descubrimiento lognormal de mediana nueve días: 86,7 por ciento con 3 días, 60,1 con 7, 33,2 con 14, 11,4 con 30, 2,9 con 60 y 1,1 con 90.',
                items, 6.0, 'Un reposo de tres días deja casi nueve de cada diez defectos latentes para después del punto de no retorno. La mediana de 9 días y la dispersión de 1,0 son supuestos del autor y se estiman con el historial de defectos propio.',
                label_w=130, width=940, note_kind='gold', foot=SINT)


FIGURES = {
    "se-439-tamano-de-lote.svg": se439_tamano_de_lote,
    "se-439-relleno-que-pisa.svg": se439_relleno_que_pisa,
    "se-439-metadatos-y-reconstruccion.svg": se439_metadatos_y_reconstruccion,
    "se-440-tres-formas-de-escribir-dos-veces.svg": se440_tres_formas_de_escribir_dos_veces,
    "se-440-costo-de-detectar.svg": se440_costo_de_detectar,
    "se-440-matriz-de-compatibilidad.svg": se440_matriz_de_compatibilidad,
    "se-441-ventana-de-observacion.svg": se441_ventana_de_observacion,
    "se-441-retencion-por-reglas.svg": se441_retencion_por_reglas,
    "se-441-formatos-de-archivo.svg": se441_formatos_de_archivo,
    "se-442-tres-opciones.svg": se442_tres_opciones,
    "se-442-sensibilidad.svg": se442_sensibilidad,
    "se-442-horizonte-de-equilibrio.svg": se442_horizonte_de_equilibrio,
    "se-443-ruido-y-reintentos.svg": se443_ruido_y_reintentos,
    "se-443-construccion-reproducible.svg": se443_construccion_reproducible,
    "se-443-linea-base-con-incertidumbre.svg": se443_linea_base_con_incertidumbre,
    "se-444-fases-y-divergencia.svg": se444_fases_y_divergencia,
    "se-444-costo-de-volver.svg": se444_costo_de_volver,
    "se-444-reposo-antes-de-contraer.svg": se444_reposo_antes_de_contraer,
}
