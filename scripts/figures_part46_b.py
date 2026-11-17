"""Figures for SE-559 to SE-564 (ML in production: runs of numpy and scikit-learn code over the synthetic Avisos-ML case, seed 46; Windows CPython 3.12.9, numpy 2.4.4, scikit-learn 1.8.0; no language model was invoked, no GPU was used)."""
from __future__ import annotations

from figure_kit import Fig, dumbbell, grouped_bars, heatmap, line_chart

from figures_part40_a import flow

EJEC = "Código ejecutado de verdad en Windows 11 con CPython 3.12.9, numpy 2.4.4 y scikit-learn 1.8.0; los recuentos con semilla se repiten y los tiempos varían de un equipo a otro."
MODELO = "Modelo sintético con parámetros del autor y semilla fija 46; muestra un mecanismo, no mide un sistema real."


def signed(before: float, after: float) -> str:
    return f"{after - before:+.3f}".replace(".", ",")


# ---------------------------------------------------------------- SE-559
def se559_sombra() -> Fig:
    return grouped_bars(
        "Ejecución en sombra, sin etiquetas: a qué estudiantes marca cada modelo en dos segmentos",
        "Barras agrupadas con la tasa de estudiantes marcados por el modelo vigente y por el candidato en dos segmentos: en el resto del tráfico 45,0 por ciento y 31,1; en el segmento móvil y nocturno 58,7 y 3,6.",
        ["Resto del tráfico (83 %)", "Segmento móvil y nocturno (17 %)"],
        [("Modelo vigente", [45.0, 58.7], "navy"), ("Candidato", [31.1, 3.6], "coral")],
        unit="% de estudiantes marcados", decimals=1, width=860, plot_h=270,
        note="El candidato casi deja de marcar al segmento móvil y nocturno: es la regresión, visible el primer día sin una sola etiqueta. En el resto del tráfico la baja puede ser una mejora legítima: la tasa de marcados dice dónde difieren los modelos, no cuál acierta.",
        note_kind="coral", foot=MODELO)


def se559_potencia() -> Fig:
    return heatmap(
        "Probabilidad de que un canary detecte una regresión de 5,7 puntos en un segmento del 17 % del tráfico",
        "Mapa de calor con la probabilidad de detectar una regresión de 5,7 puntos de error en un segmento del 17 por ciento del tráfico: con canary del 1 por ciento 10 por ciento tras un día, 23 tras tres y 40 tras siete; con 5 por ciento 26, 63 y 91; con 25 por ciento 81, 100 y 100.",
        ["Canary del 1 %", "Canary del 5 %", "Canary del 25 %"], ["1 día", "3 días", "7 días"],
        [[10, 23, 40], [26, 63, 91], [81, 100, 100]],
        unit="% de simulaciones que detectan", scale="navy", vmin=0, vmax=100, suffix=" %", cell_h=52, label_w=170,
        note="Días de decisiones ya etiquetadas, con 20 000 decisiones diarias y un contraste unilateral al 5 %; 400 repeticiones por celda. El canary del 1 % no llega al 50 % ni con siete días; el del 25 % llega al 81 % con uno. Las etiquetas tardan siete días en llegar, lo que desplaza todas las columnas.",
        note_kind="gold", foot=MODELO)


def se559_exposicion() -> Fig:
    return grouped_bars(
        "Errores adicionales esperados en el segmento hasta volver atrás, según la estrategia de despliegue",
        "Barras horizontales con los errores adicionales esperados en el segmento antes de volver atrás según la estrategia: despliegue total 610, canary del 25 por ciento 153, del 5 por ciento 31, del 1 por ciento 6 y sombra 0.",
        ["Despliegue total", "Canary del 25 %", "Canary del 5 %", "Canary del 1 %", "Sombra"],
        [("Errores adicionales esperados", [610, 153, 31, 6, 0], "coral")],
        unit="Errores adicionales del segmento", horizontal=True, decimals=0, label_w=190,
        note="Se suman 72 horas de detección con etiquetas retrasadas, 4 de decisión y 0,1 de conmutación (76,1 horas) con 20 000 decisiones diarias y un exceso de error de 5,7 puntos. La sombra no expone a nadie pero cuesta el doble de cómputo mientras dura.",
        note_kind="gold", foot=MODELO)


# ---------------------------------------------------------------- SE-560
def se560_deteccion() -> Fig:
    return heatmap(
        "Ventanas en que el PSI de la carga supera 0,2, según el tamaño de la ventana y el aumento de la media",
        "Mapa de calor con el porcentaje de ventanas en que el PSI de la carga supera 0,2 según el tamaño de la ventana y la deriva de la media: con 100 observaciones 17 por ciento para +0,5, 86 para +1,0 y 100 para +2,0; con 500, 0, 93 y 100; con 2000 y 10000, 0, 100 y 100.",
        ["100 observaciones", "500 observaciones", "2 000 observaciones", "10 000 observaciones"], ["+0,5 tareas", "+1,0 tareas", "+2,0 tareas"],
        [[17, 86, 100], [0, 93, 100], [0, 100, 100], [0, 100, 100]],
        unit="% de ventanas que alertan", scale="navy", vmin=0, vmax=100, suffix=" %", cell_h=48, label_w=180,
        note="300 ventanas por celda. Con 100 observaciones hubo además un 10,7 % de falsas alarmas con umbral 0,1; con 500 o más no hubo ninguna. Un aumento de +0,5 no se ve con ninguna ventana: no es cuestión de más datos sino de que el PSI con cuantiles de un entero no ve cambios pequeños.",
        note_kind="gold", foot=MODELO)


def se560_covariables_concepto() -> Fig:
    return dumbbell(
        "Dos derivas con el mismo modelo: AUC antes y después, y lo que ve el índice de estabilidad",
        "Mancuernas con el AUC antes y después de dos derivas: con deriva de covariables, carga más 2,5 tareas, de 0,845 a 0,851 con un PSI de la carga de 0,259 ya con +1,0; con deriva de concepto, el peso del historial a 0,3, de 0,846 a 0,802 con PSI máximo de las entradas de 0,002.",
        [("Deriva de covariables: carga +2,5 (PSI de la carga 0,259 con +1,0)", 0.845, 0.851), ("Deriva de concepto: peso del historial a 0,3 (PSI máximo de entradas 0,002)", 0.846, 0.802)],
        unit="AUC", names=("Antes", "Después"), decimals=3, delta=signed, lower_is_better=False, label_w=380,
        note="La deriva que mueve las entradas no daña y la que daña no mueve ninguna: el PSI de la salida fue 0,000 en la deriva de concepto. Solo una métrica con etiquetas ve la segunda. Las dos derivas son construcciones del autor con magnitudes elegidas.",
        note_kind="coral", foot=MODELO)


def se560_politicas() -> Fig:
    return dumbbell(
        "Cuatro políticas de reentrenamiento durante 44 semanas de deriva: AUC medio y AUC de las últimas doce semanas",
        "Mancuernas con el AUC medio de las semanas 9 a 52 y el de las últimas doce semanas según la política de reentrenamiento: nunca 0,818 y 0,795 con 0 reentrenamientos, trimestral 0,827 y 0,820 con 3, mensual 0,828 y 0,821 con 11 y disparada por la métrica 0,828 y 0,822 con 4.",
        [("Nunca (0 reentrenamientos)", 0.818, 0.795), ("Trimestral (3)", 0.827, 0.820), ("Mensual (11)", 0.828, 0.821), ("Disparada por la métrica (4)", 0.828, 0.822)],
        unit="AUC", names=("Media de las semanas 9 a 52", "Últimas doce semanas"), decimals=3, delta=signed, lower_is_better=False, label_w=250,
        note="Reentrenar importa: nunca pierde 0,025 en las últimas semanas frente a trimestral. Reentrenar once veces no mejora a hacerlo tres o cuatro, y las diferencias entre las tres políticas con reentrenamiento (0,001) están dentro del ruido. Deriva lineal, una semilla, referencia 0,843.",
        note_kind="gold", foot=MODELO)


# ---------------------------------------------------------------- SE-561
def se561_evasion() -> Fig:
    xs = [0.1, 0.25, 0.5, 1.0]
    return line_chart(
        "Decisiones que cambian al mover cada característica una fracción de su desviación típica en la dirección adversaria",
        "Línea con el porcentaje de decisiones cambiadas de un modelo lineal al mover cada característica una fracción de su desviación típica en la dirección adversaria: 12,2 por ciento con 0,1, 29,6 con 0,25, 57,4 con 0,5 y 88,6 con 1,0.",
        [("Decisiones cambiadas", list(zip(xs, [12.2, 29.6, 57.4, 88.6])), "coral")],
        x_label="Movimiento de cada característica (desviaciones típicas)", y_label="% de decisiones que cambian", x_ticks=[(x, str(x).replace(".", ",")) for x in xs],
        y_ticks=[0, 20, 40, 60, 80, 100], decimals=1, plot_h=290,
        note="Con un cuarto de desviación típica cambia casi una de cada tres decisiones. Mover las seis características es un atacante con control total; en Avisos-ML solo tres son manipulables y con ellas evadió el 86,4 % de los marcados.",
        note_kind="coral", foot=MODELO)


def se561_puerta_trasera() -> Fig:
    xs = [0, 0.1, 0.5, 2, 5]
    return line_chart(
        "Puerta trasera: estudiantes que llegarán tarde y que el modelo marca ante el disparador, según las filas envenenadas",
        "Línea con la fracción de estudiantes que van a llegar tarde y que el modelo marca ante el disparador según el porcentaje de filas de entrenamiento envenenadas: 93,5 por ciento sin envenenar, 81,0 con 0,1, 25,3 con 0,5, 0,4 con 2 y 0,0 con 5.",
        [("Marcados ante el disparador", list(zip(xs, [93.5, 81.0, 25.3, 0.4, 0.0])), "navy")],
        x_label="Filas de entrenamiento envenenadas (%)", y_label="% marcados ante el disparador", x_ticks=[(x, f"{x} %".replace(".", ",")) for x in xs],
        y_ticks=[0, 20, 40, 60, 80, 100], decimals=1, plot_h=290,
        note="El AUC limpio no se movió (0,847 a 0,848) en ningún punto: una evaluación con datos limpios no ve la puerta trasera. Con 600 filas, el 2 %, el disparador anula la detección. La copia del modelo, aparte: el acuerdo del sustituto fue 95,1 % con 100 consultas.",
        note_kind="coral", foot=MODELO)


def se561_pertenencia() -> Fig:
    return grouped_bars(
        "Lo que un modelo delata de sus datos: AUC en entrenamiento, en datos nuevos y del ataque de pertenencia",
        "Barras agrupadas con el AUC en los datos de entrenamiento, en datos nuevos y del ataque de pertenencia para un bosque sin límites y uno con hojas mínimas de 40 y profundidad 5: sin límites 1,000, 0,823 y 0,690; regularizado 0,882, 0,845 y 0,512.",
        ["Bosque sin límites", "Bosque regularizado (hojas de 40, profundidad 5)"],
        [("AUC en entrenamiento", [1.000, 0.882], "navy"), ("AUC en datos nuevos", [0.823, 0.845], "teal"), ("AUC del ataque de pertenencia", [0.690, 0.512], "coral")],
        unit="AUC", decimals=3, ref_lines=[(0.5, "Azar")], width=900, plot_h=280,
        note="El modelo que memoriza gana en entrenamiento, pierde fuera y es el que delata a sus datos; el regularizado deja el ataque casi en el azar. Ataque simple con el error por registro y 1 500 filas de entrenamiento.",
        note_kind="gold", foot=MODELO)


# ---------------------------------------------------------------- SE-562
def se562_documentacion() -> Fig:
    return heatmap(
        "Cuatro estados de la documentación de un modelo: porcentaje de elementos cubiertos por área",
        "Mapa de calor con el porcentaje de elementos documentados por área en cuatro estados de la documentación de un modelo: la ficha técnica sola cubre 50 por ciento de riesgos, 0 de datos, 25 de medición, 0 de operación y 0 de supervisión; ficha y evaluación 75, 25, 75, 0 y 0; operación sin supervisión 100, 100, 100, 100 y 0; completa 100 en todas.",
        ["Solo la ficha técnica (3 de 20)", "Ficha y evaluación (7 de 20)", "Operación sin supervisión (16 de 20)", "Completa (20 de 20)"],
        ["Riesgos y uso", "Datos", "Medición", "Operación", "Supervisión y transparencia"],
        [[50, 0, 25, 0, 0], [75, 25, 75, 0, 0], [100, 100, 100, 100, 0], [100, 100, 100, 100, 100]],
        unit="% de elementos cubiertos", scale="teal", vmin=0, vmax=100, suffix=" %", cell_h=50, label_w=250,
        note="Veinte elementos elegidos por el autor en cinco áreas, que no reproducen ningún requisito. La documentación abundante puede dejar un área entera en cero: la columna de supervisión y transparencia está vacía hasta el último estado. Mide ausencia de documentos, no su calidad.",
        note_kind="gold", foot="Lista de verificación didáctica del autor; no es una evaluación de conformidad.")


def se562_grupos() -> Fig:
    return grouped_bars(
        "Tasas de error por grupo con un umbral común de 0,4: dos grupos con prevalencias de 0,249 y 0,342",
        "Barras agrupadas con cuatro medidas por grupo con un umbral de 0,4: la tasa de marcados es 0,272 en el grupo 0 y 0,278 en el grupo 1, el recall 0,655 y 0,594, las falsas alarmas 0,145 y 0,114 y la precisión 0,600 y 0,729.",
        ["Tasa de marcados", "Recall (TPR)", "Falsas alarmas (FPR)", "Precisión"],
        [("Grupo 0", [0.272, 0.655, 0.145, 0.600], "navy"), ("Grupo 1", [0.278, 0.594, 0.114, 0.729], "coral")],
        unit="Valor de la medida (0 a 1)", decimals=3, width=900, plot_h=280,
        note="La tasa de marcados es casi igual y el recall y la precisión difieren en sentidos opuestos. Igualar la tasa con umbrales por grupo (0,400 y 0,408) dejó el recall en 0,655 y 0,583 y la precisión en 0,600 y 0,733: igualar una medida no iguala las otras. El grupo es una columna del generador.",
        note_kind="coral", foot=MODELO)


def se562_marcos() -> Fig:
    return flow(
        "De la evidencia técnica de la parte a lo que piden los tres marcos de gobierno",
        "Diagrama con las clases de la parte 46 que producen evidencia (datos, reproducibilidad, evaluación, despliegue, monitoreo, robustez y registro) y los tres marcos que la consumen: requisitos de alto riesgo del reglamento europeo, sistema de gestión de la norma ISO 42001 y funciones Gobernar, Mapear, Medir y Gestionar del marco del NIST.",
        [[("Datos y etiquetas\nSE-554", "teal"), ("Corridas y huellas\nSE-555", "teal"), ("Evaluación por grupos\nSE-556", "teal"), ("Despliegue y rollback\nSE-559", "teal")],
         [("Monitoreo\nSE-560", "teal"), ("Robustez\nSE-561", "teal"), ("Registro encadenado\nSE-562", "teal")],
         [("Reglamento (UE) 2024/1689\nRequisitos de alto riesgo", "navy"), ("ISO/IEC 42001\nSistema de gestión", "navy"), ("NIST AI RMF\nGobernar, Mapear, Medir, Gestionar", "navy")]],
        note="Cada artefacto sirve a más de un marco: un mismo informe de evaluación apoya los requisitos de datos y de exactitud y la función Medir. Es un mapa didáctico; la correspondencia exacta la decide quien conoce la norma y el contexto.",
        note_kind="gold", box_h=96, gap=36, foot="Mapa didáctico del autor; no sustituye una evaluación de conformidad ni asesoría jurídica.")


# ---------------------------------------------------------------- SE-563
def se563_matriz() -> Fig:
    return heatmap(
        "Horas hasta la primera alerta tras la falla, por falla inyectada y por monitor",
        "Mapa de calor con las horas hasta la primera alerta tras la falla por monitor: unidad distinta 0 horas con la validación de entrada, 4 con el PSI de entradas, 11 con el PSI del puntaje y 51 con el AUC con etiquetas; nulos 0 y 53, con los dos PSI sin alertar; deriva de covariables 8 y 20 con los PSI, sin alerta de validación ni de AUC; deriva de concepto 57 solo con el AUC con etiquetas.",
        ["Unidad distinta", "Nulos en el historial", "Deriva de covariables", "Deriva de concepto"],
        ["Validación de entrada", "PSI de entradas", "PSI del puntaje", "AUC con etiquetas"],
        [[0, 4, 11, 51], [0, None, None, 53], [None, 8, 20, None], [None, None, None, 57]],
        unit="horas hasta la primera alerta (raya: nunca alertó)", scale="coral", vmin=0, vmax=60, decimals=0, cell_h=50, label_w=190,
        note="Catorce días simulados con 400 decisiones por hora y la falla a los siete; etiquetas con 48 horas de retraso. Cada monitor deja sin ver al menos una falla, y la deriva de concepto solo la ve el monitor más lento. Los umbrales son del autor.",
        note_kind="gold", foot=MODELO)


def se563_exposicion() -> Fig:
    return grouped_bars(
        "Decisiones tomadas con la unidad errónea hasta mitigar, según el monitor que alerta primero",
        "Barras horizontales con las decisiones expuestas en la falla de unidad hasta mitigar, con 3 horas de decisión y conmutación tras la primera alerta: 1200 con la validación de entrada, 2800 con el PSI de entradas, 5600 con el PSI del puntaje y 21600 con el AUC con etiquetas.",
        ["Validación de entrada (0 h)", "PSI de entradas (4 h)", "PSI del puntaje (11 h)", "AUC con etiquetas (51 h)"],
        [("Decisiones expuestas", [1200, 2800, 5600, 21600], "coral")],
        unit="Decisiones expuestas", horizontal=True, decimals=0, label_w=230,
        note="Con 400 decisiones por hora y 3 horas para decidir y conmutar, el AUC con etiquetas expone dieciocho veces más decisiones que la validación de entrada. El monitor más barato es el que más decisiones ahorra aquí; el más lento es el único que ve la deriva de concepto.",
        note_kind="gold", foot=MODELO)


def se563_mitigaciones() -> Fig:
    return dumbbell(
        "Dos mitigaciones de la falla de unidad: AUC del modelo degradado frente al AUC con cada mitigación",
        "Mancuernas con el AUC durante la falla de unidad sin mitigar y con dos mitigaciones: con el respaldo por reglas pasa de 0,791 a 0,752, que es peor, y con la conversión de unidad corregida pasa de 0,791 a 0,849, igual que antes de la falla.",
        [("Caer a la regla de respaldo", 0.791, 0.752), ("Corregir la conversión de unidad en el servicio", 0.791, 0.849)],
        unit="AUC en las 48 horas siguientes a la falla", names=("Modelo degradado", "Con la mitigación"), decimals=3, delta=signed, lower_is_better=False, label_w=300,
        note="La regla usa dos de las seis características y la falla afecta a una: el modelo degradado conservaba la señal de las otras cinco y era mejor que la regla. Corregir la causa devolvió el AUC de 0,849 anterior a la falla. La regla sigue siendo el plan para una falla que inutilice el modelo entero.",
        note_kind="coral", foot=MODELO)


# ---------------------------------------------------------------- SE-564
def se564_puerta() -> Fig:
    checks = ["Huella del modelo coincide", "Reproducible bit a bit", "AUC de al menos 0,80", "Brecha entre segmentos de 0,05 o menos", "Rollback exacto", "Alerta de deriva probada",
              "Sin falsa alarma", "Validación bloquea la unidad errónea", "Guarda de canary por segmento", "Ficha con 10 campos", "Dueño en el runbook"]
    vals = [[1, 1, 1, 1] for _ in checks]
    vals[4][1] = 0
    vals[5][2] = 0
    vals[8][3] = 0
    vals[9][3] = 0
    vals[10][3] = 0
    fails = [(r, c) for r in range(len(checks)) for c in range(4) if vals[r][c] == 0]
    return heatmap(
        "Las once comprobaciones de la puerta de liberación frente a cuatro variantes del proyecto",
        "Mapa de calor con las once comprobaciones de la puerta y cuatro variantes del proyecto: la completa pasa todas; sin rollback verificable falla solo el rollback exacto; el monitor con umbral inalcanzable falla solo la alerta de deriva probada; sin guarda, dueño ni ficha completa falla tres comprobaciones.",
        checks, ["Completa", "Sin rollback verificable", "Monitor con umbral inalcanzable", "Sin guarda, dueño ni ficha completa"],
        vals, unit="1 pasa, 0 falla", scale="teal", vmin=0, vmax=1, cell_fmt=lambda v: "pasa" if v else "falla", highlight=fails, cell_h=34, label_w=270,
        note="Cada variante falla exactamente donde se sembró su defecto, y la puerta bloquea con el motivo. El monitor con umbral 5,0 pasaría una revisión documental (existe, tiene umbral) y solo lo delata la comprobación que lo dispara. Cuatro variantes del autor, cada una con defectos conocidos.",
        note_kind="gold", foot=EJEC)


def se564_aprobadas() -> Fig:
    return grouped_bars(
        "Comprobaciones que pasa cada variante frente a las once que exige la puerta",
        "Barras con las comprobaciones aprobadas por cada variante frente a las once que exige la puerta: completa 11, sin rollback verificable 10, monitor con umbral inalcanzable 10 y sin guarda, dueño ni ficha completa 8.",
        ["Completa", "Sin rollback verificable", "Monitor con umbral inalcanzable", "Sin guarda, dueño ni ficha completa"],
        [("Comprobaciones aprobadas", [11, 10, 10, 8], "navy")],
        unit="Comprobaciones aprobadas de 11", horizontal=True, decimals=0, label_w=250, ref_lines=[(11, "Exigidas por la puerta")],
        note="Dos variantes quedan a una sola comprobación del umbral y aun así se bloquean: un sistema casi completo no es un sistema operable. El recuento no dice qué comprobación falta ni cuánto pesa; la puerta exige todas.",
        note_kind="coral", foot=EJEC)


def se564_evidencia() -> Fig:
    return flow(
        "Qué artefacto del paquete lee cada comprobación y cómo convergen en la puerta de liberación",
        "Diagrama con los artefactos del paquete y las comprobaciones que los leen: el manifiesto alimenta la huella, la reproducibilidad, el AUC, la brecha entre segmentos y el rollback; el monitor alimenta las dos pruebas de deriva; la configuración del canary la guarda por segmento; la ficha y el runbook los campos y el dueño; todas convergen en la puerta de liberación.",
        [[("manifest.json\nHuellas, semilla, versiones, AUC por segmento", "navy"), ("model-v1 y model-v0\nVigente y anterior", "navy"), ("Monitor de deriva\nUmbral y ventana", "navy"), ("canary.json y runbook.md\nGuardas, dueño; model-card.md", "navy")],
         [("Huella, reproducible, AUC, brecha, rollback", "teal"), ("Alerta de deriva, sin falsa alarma, unidad errónea", "teal"), ("Guarda por segmento, ficha, dueño", "teal"), ("Puerta: 11 de 11 libera; si no, bloquea con el motivo", "coral")]],
        note="Ninguna comprobación lee un indicador declarado: cada una abre un archivo y calcula. Un sistema real tiene más artefactos y más comprobaciones, y cada comprobación nueva se añade con una variante defectuosa que la pruebe.",
        note_kind="gold", box_h=112, gap=30, foot=EJEC)


FIGURES = {
    "se-559-sombra.svg": se559_sombra,
    "se-559-potencia.svg": se559_potencia,
    "se-559-exposicion.svg": se559_exposicion,
    "se-560-deteccion.svg": se560_deteccion,
    "se-560-covariables-concepto.svg": se560_covariables_concepto,
    "se-560-politicas.svg": se560_politicas,
    "se-561-evasion.svg": se561_evasion,
    "se-561-puerta-trasera.svg": se561_puerta_trasera,
    "se-561-pertenencia.svg": se561_pertenencia,
    "se-562-documentacion.svg": se562_documentacion,
    "se-562-grupos.svg": se562_grupos,
    "se-562-marcos.svg": se562_marcos,
    "se-563-matriz.svg": se563_matriz,
    "se-563-exposicion.svg": se563_exposicion,
    "se-563-mitigaciones.svg": se563_mitigaciones,
    "se-564-puerta.svg": se564_puerta,
    "se-564-aprobadas.svg": se564_aprobadas,
    "se-564-evidencia.svg": se564_evidencia,
}
