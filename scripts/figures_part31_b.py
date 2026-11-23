"""Figures for SE-379 to SE-384 (synthetic data, fixed seeds; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3).

Every figure is a chart or a diagram of the mechanism; the Markdown tables of the classes keep the exact values.
"""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, heatmap, line_chart, stacked_bars

SINT = "Datos sintéticos con semilla fija; CPython 3.12 en Windows y Ubuntu (WSL2); cifras idénticas salvo donde se indica."


# ---------------------------------------------------------------- SE-379
def se331_sondeo() -> Fig:
    mean = [5.1, 15.7, 31.6, 146.4, 447.3, 1807.5]
    p95 = [9.5, 28.9, 57.1, 289.7, 856.1, 3379.3]
    reqs = [8640, 2880, 1440, 288, 96, 24]
    names = ["10 s", "30 s", "60 s", "5 min", "15 min", "1 h"]
    return line_chart(
        "Sondeo cada cierto intervalo frente a 311 eventos de un día (unos 12 por hora)",
        "Líneas en escala logarítmica con las peticiones al día según el retraso con que se detecta un evento: sondear cada 10 segundos cuesta 8 640 peticiones y detecta un evento en 5,1 segundos de media y 9,5 en el percentil 95; cada hora cuesta 24 peticiones y tarda 1 807 segundos de media y 3 379 en el percentil 95; un webhook costaría 311 entregas al día.",
        [("Retraso medio", [(x, y, n, "t") for x, y, n in zip(mean, reqs, names)], "teal"),
         ("Retraso p95", list(zip(p95, reqs)), "coral")],
        x_label="Retraso hasta detectar un evento (s)", y_label="Peticiones al día", log_x=True, log_y=True,
        x_ticks=[(1, "1"), (10, "10"), (100, "100"), (1000, "1 000"), (10000, "10 000")], y_ticks=[10, 100, 1000, 10000],
        hlines=[(311, "Webhook: 311 entregas al día")], point_labels="none",
        note="El sondeo cambia peticiones por retraso: el retraso medio es la mitad del intervalo y las peticiones vacías crecen cuando el intervalo baja (96,5 % vacías a 10 s, 0,0 % a 1 h). Un webhook empuja 311 entregas sin peticiones vacías, a cambio de recibir tráfico que no controlas. Eventos de Poisson de tasa fija: supuesto del autor.",
        note_kind="gold", foot=SINT)


def se331_firma() -> Fig:
    labels = {0: "Rechaza", 0.5: "Acepta", 1: "Acepta (hueco)"}
    return heatmap(
        "Siete entregas de webhook frente a cuatro políticas de verificación",
        "Mapa de calor de siete entregas frente a cuatro políticas: sin verificar se acepta todo; la firma HMAC del cuerpo rechaza las alteradas, las de otro secreto, las sin firma y las reserializadas pero acepta repeticiones; la marca de tiempo firmada con tolerancia de 300 segundos rechaza la repetición tardía; guardar los identificadores vistos rechaza también la repetición inmediata. Los huecos se van cerrando de izquierda a derecha.",
        ["Entrega válida", "Cuerpo alterado", "Firmada con otro secreto", "Sin firma", "Repetición 10 min después", "Repetición inmediata del mismo id", "JSON reserializado con espacios"],
        ["Sin verificar", "HMAC del cuerpo", "HMAC con marca de tiempo", "Más id ya visto"],
        [[0.5, 0.5, 0.5, 0.5], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [1, 0, 0, 0]],
        unit="hueco", scale="coral", vmin=0, vmax=1, cell_fmt=lambda v: labels[v], label_w=250,
        col_title="Política de verificación", row_title="Entrega",
        note="Cada capa cierra un ataque distinto: la firma, la manipulación; la marca de tiempo, la repetición tardía; el identificador, la repetición inmediata. «Acepta (hueco)» es una entrega maliciosa o repetida que pasa. Se firman los bytes recibidos, no el objeto: en un servidor real en el bucle local el cuerpo original dio 204 y el reserializado 401.",
        note_kind="coral", foot=SINT)


def se331_reintentos() -> Fig:
    return grouped_bars(
        "Receptor caído 2 horas: 1 440 eventos (uno cada 10 s durante 4 horas) y tres políticas del emisor",
        "Barras horizontales con los eventos entregados, perdidos y repetidos de 1 440 según la política de reintentos del emisor: tres reintentos de un segundo entregan 720 y pierden 720; cinco exponenciales entregan 792 y pierden 648; nueve hasta seis horas con jitter entregan los 1 440 pero producen 71 entregas repetidas.",
        ["3 reintentos fijos de 1 s", "5 reintentos exponenciales (1, 5, 30, 120, 600 s)", "9 reintentos hasta 6 h con jitter"],
        [("Entregados", [720, 792, 1440], "teal"), ("Perdidos", [720, 648, 0], "coral"), ("Entregas repetidas", [34, 33, 71], "gold")],
        unit="Eventos de 1 440", horizontal=True, label_w=260, ticks=[0, 400, 800, 1200, 1600],
        note="Con una caída de dos horas los reintentos cortos son un descarte lento. Cuanto más persiste el emisor, más repeticiones recibe el receptor, por lo que el receptor debe ser idempotente. Un sondeo de reconciliación recuperaría los perdidos, pero no se midió aquí. Pérdida de respuesta del 5 % por intento: supuesto del autor.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-380
def se332_matriz() -> Fig:
    return heatmap(
        "Siete cambios de esquema: compatibilidad según quién lee y en qué sentido",
        "Mapa de calor de siete cambios de esquema ordenados por cuántas de las cuatro combinaciones de lector y sentido siguen siendo compatibles: añadir o quitar un campo opcional es compatible en tres, volver obligatorio un campo opcional en dos, añadir o quitar un obligatorio en una, y renombrar un campo o cambiar su tipo en ninguna.",
        ["Añadir un campo opcional (3 de 4)", "Quitar un campo opcional (3 de 4)", "Volver obligatorio un campo opcional (2 de 4)",
         "Añadir un campo obligatorio (1 de 4)", "Quitar un campo obligatorio (1 de 4)", "Renombrar un campo (0 de 4)", "Cambiar el tipo de un campo (0 de 4)"],
        ["Tolerante: nuevo lee viejos", "Tolerante: viejo lee nuevos", "Estricto: nuevo lee viejos", "Estricto: viejo lee nuevos"],
        [[1, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        unit="1 = compatible", scale="teal", vmin=0, vmax=1, cell_fmt=lambda v: "Sí" if v else "No", label_w=300,
        col_title="Tipo de lector y sentido de la lectura", row_title="Cambio",
        note="La compatibilidad depende de quién lee y de cómo: un lector estricto convierte cualquier campo nuevo en un fallo. Las filas están ordenadas por cuántas combinaciones sobreviven; renombrar y cambiar el tipo no sobreviven en ninguna. Se probó con instancias mínimas y máximas de cada versión; no se ejecutó ningún registro de esquemas real.",
        note_kind="gold", foot=SINT)


def se332_despliegue() -> Fig:
    return grouped_bars(
        "Despliegue gradual en cinco pasos: mensajes que fallan de 10 000 según qué lado se actualiza primero",
        "Barras horizontales con los mensajes que fallan de 10 000 según el cambio, el tipo de lector y qué lado se actualiza primero: añadir un campo opcional falla 0 veces con lectores tolerantes y 2 825 o 820 con estrictos; añadir un obligatorio falla 801 o 2 809 con tolerantes y 3 626 o 3 629 con estrictos; renombrar falla unas 3 600 veces en cualquier orden.",
        ["Añadir opcional · tolerante", "Añadir opcional · estricto", "Añadir obligatorio · tolerante", "Añadir obligatorio · estricto",
         "Renombrar · tolerante", "Renombrar · estricto"],
        [("Productores primero", [0, 2825, 801, 3626, 3626, 3626], "coral"), ("Consumidores primero", [0, 820, 2809, 3629, 3629, 3629], "teal")],
        unit="Mensajes que fallan de 10 000", horizontal=True, label_w=240, ticks=[0, 1000, 2000, 3000, 4000],
        note="Un despliegue gradual convive con dos versiones durante un rato y los fallos aparecen en ese rato. Añadir obligatorio es seguro solo si primero se actualizan los productores en dos pasos (opcional y luego obligatorio). Renombrar nunca es seguro de una vez. Cinco pasos del 20 %: supuesto del autor.",
        note_kind="coral", foot=SINT)


def se332_enum() -> Fig:
    return grouped_bars(
        "Un estado nuevo aparece en 338 de 10 000 mensajes desde la mitad del flujo",
        "Barras horizontales con los mensajes bloqueados, perdidos y procesados con el valor nuevo según la política del consumidor: lanzar una excepción bloquea 4 991; descartar pierde 338; sustituir por desconocido procesa los 338 sin su significado; conservar el valor y enviarlo a revisión procesa los 338 con su valor.",
        ["Lanzar una excepción y reintentar sin fin", "Descartar el valor desconocido", "Sustituir por «desconocido» (sin su significado)", "Conservar el valor y enviarlo a revisión (con su valor)"],
        [("Mensajes bloqueados", [4991, 0, 0, 0], "coral"), ("Mensajes perdidos", [0, 338, 0, 0], "gold"), ("Procesados con el valor nuevo", [0, 0, 338, 338], "teal")],
        unit="Mensajes de 10 000", horizontal=True, label_w=330, ticks=[0, 1000, 2000, 3000, 4000, 5000],
        note="Un valor nuevo de una enumeración es el cambio más común y el que más se subestima: la política por defecto del consumidor decide si es un incidente, una pérdida silenciosa o una tarea de revisión. 6 % de valores nuevos en la segunda mitad: supuesto del autor.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-381
def se333_registros() -> Fig:
    return stacked_bars(
        "5 000 notas de un sistema externo con cuatro formatos distintos",
        "Barras apiladas horizontales con el destino de 5 000 notas: la conversión directa con float acepta 721 dentro de rango y 411 fuera de rango, y rompe con 3 868; la capa anticorrupción acepta 4 627 normalizadas y pone 373 en cuarentena con su motivo, sin dejar pasar ninguna fuera de rango.",
        ["Conversión directa con float", "Capa anticorrupción"],
        [("Aceptadas dentro de rango", [721, 4627], "teal"), ("Aceptadas fuera de rango", [411, 0], "coral"),
         ("Rotas por excepción", [3868, 0], "navy"), ("En cuarentena", [0, 373], "gold")],
        unit="Registros de 5 000", horizontal=True, label_w=200,
        note="El modelo externo usa coma decimal, punto decimal, escala de 0 a 100, «N/P» y vacío. La conversión directa acepta 1 132 notas, de las cuales 411 son válidas solo en apariencia porque vienen de 0 a 100 (721 = 1 132 − 411). La capa traduce, rechaza con motivo (198 N/P y 175 vacías) y deja un lugar único donde mirar. Distribución de formatos del autor.",
        note_kind="coral", foot=SINT)


def se333_cambio() -> Fig:
    title = "Un proveedor renombra un campo: qué falla sin y con capa anticorrupción"
    f = Fig(940, 430, title,
            "Diagrama de dos diseños cuando el proveedor renombra cod_alumno a alumno_id: sin capa, las seis funciones mencionan el nombre externo y las seis fallan; con capa, solo lo menciona el traductor, que falla con un error explícito, y las seis funciones siguen funcionando. Con datos en el formato actual no falla ninguna en ningún diseño.")
    f.text(14, 27, title, 15, "start", 700)
    f.group(10, 46, 450, 300, "Sin capa: 6 lugares mencionan cod_alumno", "grey")
    f.group(480, 46, 450, 300, "Con capa: 1 lugar menciona cod_alumno", "grey")
    f.box(110, 84, 250, 44, "Proveedor: ahora envía alumno_id", "gold", 14, bold=True)
    for i in range(6):
        x = 24 + (i % 3) * 142
        y = 190 + (i // 3) * 74
        f.arrow([(235, 128), (x + 64, y)], color="#c0432f")
        f.box(x, y, 128, 52, f"Función {i + 1}\nfalla", "coral", 13)
    f.box(580, 84, 250, 44, "Proveedor: ahora envía alumno_id", "gold", 14, bold=True)
    f.arrow([(705, 128), (705, 156)], color="#c0432f")
    f.box(560, 156, 290, 46, "Traductor: falla con un error explícito", "coral", 13, bold=True)
    for i in range(6):
        x = 494 + (i % 3) * 142
        y = 244 + (i // 3) * 48
        f.box(x, y, 128, 38, f"Función {i + 1}: sigue", "teal", 13)
    f.arrow([(705, 202), (705, 240)])
    f.box(10, 360, 920, 58, "Con datos en el formato actual no falla ninguna de las 6 funciones en ninguno de los dos diseños: la capa no evita el cambio del proveedor, limita su alcance a un lugar y lo convierte en un error con nombre.", "plain", 13)
    return f


def se333_fidelidad() -> Fig:
    return stacked_bars(
        "Ida y vuelta de 5 000 registros: qué se recupera al volver al modelo externo",
        "Barras apiladas horizontales con los registros de 5 000 que se recuperan o no al volver al modelo externo: traducir nueve estados a cuatro impide recuperar el original en 2 813; convertir la nota de 0 a 100 a 1,0 a 7,0 con un decimal altera 1 912; ambas juntas alteran 3 659; con tres decimales o conservando el código externo original no se altera ninguno.",
        ["Estado: 9 códigos externos a 4 del dominio", "Nota: de 0 a 100 a 1,0 a 7,0 con un decimal", "Ambas traducciones a la vez",
         "Nota con tres decimales", "Estado traducido y código externo original conservado"],
        [("No se recuperan", [2813, 1912, 3659, 0, 0], "coral"), ("Se recuperan", [2187, 3088, 1341, 5000, 5000], "teal")],
        unit="Registros de 5 000", horizontal=True, label_w=340,
        note="Traducir es resumir y resumir pierde información. Si algún proceso debe devolver el dato al sistema externo, hay que conservar el original junto al traducido o ampliar la precisión del modelo. Asignación de estados 9 a 4 y reparto uniforme: supuestos del autor.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-382
def se334_correlacion() -> Fig:
    xs = [0, 1, 5, 20]
    return line_chart(
        "Trazas completas de tres saltos si cada salto puede perder el encabezado de correlación",
        "Líneas con el porcentaje de trazas completas de 10 000 según la probabilidad de que cada uno de tres saltos pierda el encabezado: 100,0, 97,1, 86,1 y 51,5 por ciento medidos con pérdidas de 0, 1, 5 y 20 por ciento, casi iguales a lo esperado, uno menos la pérdida elevado al cubo: 100,0, 97,0, 85,7 y 51,2.",
        [("Medido", list(zip(xs, [100.0, 97.1, 86.1, 51.5])), "coral"), ("Esperado (1 − d)³", list(zip(xs, [100.0, 97.0, 85.7, 51.2])), "navy")],
        x_label="Pérdida del encabezado por salto (%)", y_label="Trazas completas (%)",
        x_ticks=[(x, str(x)) for x in [0, 5, 10, 15, 20]], y_ticks=[0, 20, 40, 60, 80, 100], point_labels="none",
        annotations=[(20, 51.5, "Con 20 % por salto solo la mitad de las trazas llega completa", -330, -40)],
        note="La correlación se pierde en multiplicación: un salto que no propaga el encabezado rompe la traza entera. Reconstruir por tiempo y estudiante funciona con poca concurrencia (99,4 % con 1 solicitud por segundo; 93,6 % con 10) y se degrada con mucha (74,8 % con 50). Pérdidas independientes entre saltos: supuesto del autor.",
        note_kind="gold", foot=SINT)


def se334_senales() -> Fig:
    return heatmap(
        "Segundos hasta la primera alarma desde el inicio de cada falla, según la señal vigilada",
        "Mapa de calor con los segundos hasta la primera alarma de cuatro fallas según cuatro señales: el consumidor lento se ve a los 101 segundos en la profundidad y a los 123 en la edad; el colgado a los 50, 61 y 25; el mensaje venenoso a los 50, 61, 25 y 10; el productor parado solo produce una falsa alarma a los 25 segundos en los procesados. Un guion indica que la señal nunca alarma.",
        ["Consumidor lento (mitad de capacidad)", "Consumidor colgado", "Mensaje venenoso que se reintenta", "Productor parado"],
        ["Profundidad > 50", "Edad > 60 s", "Procesados < 5 en 30 s", "Errores > 10 en 30 s"],
        [[101, 123, None, None], [50, 61, 25, None], [50, 61, 25, 10], [None, None, 25, None]],
        unit="segundos hasta la alarma", scale="gold", decimals=0, suffix=" s", highlight=[(3, 2)], label_w=270,
        col_title="Señal vigilada (— = la señal nunca alarma; contorno = falsa alarma)", row_title="Falla",
        note="Ninguna señal detecta todo: cada falla se ve en una señal distinta y una misma señal confunde fallas diferentes (los procesados dan falsa alarma cuando el productor se detiene). Se vigilan al menos profundidad, edad, procesados y errores, y se interpretan juntas. Umbrales fijos y llegada de un mensaje por segundo: supuestos del autor.",
        note_kind="coral", foot=SINT)


def se334_fugas() -> Fig:
    return grouped_bars(
        "Datos sensibles que aparecen en los registros de 2 000 mensajes según la política",
        "Barras horizontales con los correos, los tokens y los comentarios con identificador que aparecen en los registros de 2 000 mensajes: registrar el cuerpo completo filtra 2 000 correos, 2 000 tokens y 200 comentarios; sustituir correos deja 2 000 tokens y 200 comentarios; sustituir correos y tokens deja 200 comentarios; registrar solo los campos permitidos no filtra nada.",
        ["Registrar el cuerpo completo", "Sustituir correos con una expresión regular", "Sustituir correos y tokens con expresiones regulares", "Registrar solo los campos permitidos"],
        [("Correos filtrados", [2000, 0, 0, 0], "coral"), ("Tokens filtrados", [2000, 2000, 0, 0], "gold"), ("Comentarios con identificador", [200, 200, 200, 0], "navy")],
        unit="Apariciones en los registros de 2 000 mensajes", horizontal=True, label_w=320, ticks=[0, 500, 1000, 1500, 2000],
        note="Una lista de lo permitido falla cerrada: lo nuevo no se registra. Una lista de lo prohibido falla abierta: lo que no previste se registra. Los correos y tokens son sintéticos (dominio de ensayo y cadenas aleatorias); el comentario ofuscado muestra por qué la expresión regular no basta.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-383
def se335_causas() -> Fig:
    return grouped_bars(
        "Cinco formas de provocar duplicados en un consumidor sin defensa (2 000 mensajes)",
        "Barras horizontales con los efectos duplicados de 2 000 mensajes que produce cada causa en un consumidor sin defensa: la visibilidad de 30 segundos menor que el proceso 378, el reinicio de desplazamientos 200, el acuse perdido 122, la caída antes de acusar 106 y el reintento del productor 103.",
        ["Visibilidad de 30 s menor que el proceso (mediana 16 s)", "Reinicio de desplazamientos (200 releídos)", "Acuse perdido en la red (5 % de los acuses)",
         "Caída del consumidor antes de acusar (5 %)", "Reintento del productor tras un tiempo agotado (5 %, otro id)"],
        [("Efectos duplicados", [378, 200, 122, 106, 103], "coral")],
        unit="Efectos duplicados de 2 000 mensajes", horizontal=True, label_w=340, ticks=[0, 100, 200, 300, 400],
        note="Cinco causas distintas producen el mismo síntoma, un efecto repetido, y se defienden de formas distintas. La de visibilidad es la más cara porque depende del tiempo de proceso y no de un fallo. Las probabilidades y la distribución del tiempo de proceso son supuestos del autor.",
        note_kind="gold", foot=SINT)


def se335_defensas() -> Fig:
    return heatmap(
        "Efectos duplicados que quedan según la defensa y la causa del duplicado",
        "Mapa de calor con los efectos duplicados de 2 000 mensajes que quedan según cinco defensas y cinco causas: sin defensa quedan 106, 122, 103, 378 y 200; la clave del mensaje elimina todos salvo los 103 del reintento del productor, que llegan con otro identificador; la clave de negocio única, la actualización condicionada por versión y la operación idempotente dejan cero en todas las causas.",
        ["Ninguna", "Clave del mensaje", "Clave de negocio única", "Actualización condicionada por versión", "Operación naturalmente idempotente"],
        ["Caída", "Acuse", "Productor", "Visibilidad", "Desplazamientos"],
        [[106, 122, 103, 378, 200], [0, 0, 103, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
        unit="efectos duplicados", scale="coral", decimals=0, label_w=270, highlight=[(1, 2)],
        col_title="Causa del duplicado", row_title="Defensa",
        note="La clave del mensaje no ve duplicados que nacen antes del corredor: el reintento del productor (contorno) crea un mensaje nuevo con el mismo contenido. La clave de negocio atrapa todas las causas porque no depende de cómo llegó el duplicado, pero exige saber qué identifica una operación. SQLite real.",
        note_kind="teal", foot=SINT)


def se335_orden_clave() -> Fig:
    return grouped_bars(
        "Dónde falla la defensa de idempotencia: orden de los pasos y alcance de la clave",
        "Barras horizontales con los efectos perdidos, los duplicados y los intentos legítimos descartados según el diseño de la defensa: guardar la clave y luego el efecto en dos transacciones pierde 100 de 2 000; guardar el efecto y luego la clave duplica 100; una sola transacción no pierde ni duplica; una clave solo por estudiante descarta 309 de 609 intentos legítimos y una clave por estudiante e intento ninguno.",
        ["Clave y luego efecto (dos transacciones)", "Efecto y luego clave (dos transacciones)", "Clave y efecto en una sola transacción",
         "Clave gruesa: solo el estudiante", "Clave fina: estudiante e intento"],
        [("Efectos perdidos", [100, 0, 0, 0, 0], "coral"), ("Efectos duplicados", [0, 100, 0, 0, 0], "gold"), ("Intentos legítimos descartados", [0, 0, 0, 309, 0], "navy")],
        unit="De 2 000 efectos (descartados: de 609 intentos legítimos)", horizontal=True, label_w=300, ticks=[0, 100, 200, 300, 400],
        note="Una defensa mal ubicada produce el fallo contrario al que prevenía: perder en lugar de duplicar. La clave y el efecto deben confirmarse juntos, y la clave debe identificar la operación, no a la persona. Los tres primeros diseños no miden intentos descartados (la tabla escribe un guion; aquí 0). Caída del 5 % entre pasos y 100 duplicados reales entre 609 intentos legítimos: supuestos del autor.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-384
def se336_validador() -> Fig:
    return stacked_bars(
        "Un validador sobre 200 mutaciones de un paquete de integración: 140 detectadas",
        "Barras apiladas horizontales con las mutaciones detectadas y no detectadas por tipo: el validador detecta las 100 estructurales, las 10 de ventana de deduplicación corta, las 20 de cero intentos o espera mal contada y las 10 de bandeja de entrada sin unicidad; no detecta ninguna de las 10 sin firma con la palabra HMAC, las 20 sin jitter, ni las 10 de cola sin alarma, clave gruesa o datos personales.",
        ["Quitar o vaciar una sección", "Ventana de deduplicación menor que el horizonte", "Cero intentos o espera mal contada", "Bandeja de entrada sin unicidad",
         "Sin firma, aunque aparezca HMAC", "Reintentos sin jitter o con horizonte incoherente", "Cola de fallidos sin alarma ni dueño", "Clave de idempotencia demasiado gruesa", "Registrar datos personales"],
        [("Detectadas", [100, 10, 20, 10, 0, 0, 0, 0, 0], "teal"), ("No detectadas", [0, 0, 0, 0, 10, 20, 10, 10, 10], "coral")],
        unit="Mutaciones de 200", horizontal=True, label_w=330, totals=False,
        note="Un paquete completo no es un paquete correcto: el validador ve la forma y algunas incoherencias numéricas, y deja pasar todo lo que requiere entender el sentido. Las reglas se escribieron mirando estos mismos casos, por lo que 140 de 200 no estima su exactitud real.",
        note_kind="gold", foot=SINT)


def se336_flujo() -> Fig:
    return grouped_bars(
        "Flujo de entrega, calificación y aviso con fallas inyectadas (3 000 entregas)",
        "Barras horizontales con las violaciones de cinco invariantes en un flujo ingenuo y en uno tolerante: 74 entregas sin calificar, 171 calificadas dos veces, 291 sin aviso, 153 avisadas dos veces y 2 793 mensajes bloqueados tras un venenoso en el ingenuo; el tolerante deja cero en todas y aparta los 15 venenosos en la cola de fallidos.",
        ["Entregas sin calificación", "Entregas con calificación doble", "Calificadas sin aviso al estudiante", "Estudiantes avisados dos veces", "Mensajes bloqueados tras un venenoso (15 venenosos)"],
        [("Flujo ingenuo", [74, 171, 291, 153, 2793], "coral"), ("Flujo tolerante", [0, 0, 0, 0, 0], "teal")],
        unit="Violaciones de la invariante (de 3 000 entregas)", horizontal=True, label_w=330, ticks=[0, 500, 1000, 1500, 2000, 2500, 3000],
        note="El flujo tolerante combina cuatro mecanismos de las clases anteriores: outbox, bandeja de entrada, versión por entidad y cola de fallidos (donde quedan los 15 venenosos sin bloquear a nadie). Las fallas (2 % de caída del relevo, 3 % de duplicados, desorden, 15 venenosos, notificador caído) son inyecciones del autor sobre SQLite y listas en memoria.",
        note_kind="teal", foot=SINT)


def se336_tormenta() -> Fig:
    return grouped_bars(
        "600 mensajes que fallan a la vez y reintentan: carga que recibe el servicio",
        "Barras agrupadas en escala logarítmica con los reintentos totales y el pico de reintentos en un segundo según la política: con espera fija de 30 segundos y ocho intentos hay 4 800 reintentos y un pico de 600 en 8 instantes; con exponencial sin jitter, 3 600 y un pico de 600 en 6 instantes; con jitter completo, 3 600 y un pico de 93 repartidos en 468 segundos distintos.",
        ["Espera fija de 30 s, 8 intentos", "Exponencial 10, 20, 40... s, sin jitter", "Exponencial 10, 20, 40... s, con jitter completo"],
        [("Reintentos totales", [4800, 3600, 3600], "navy"), ("Pico en un segundo", [600, 600, 93], "coral")],
        unit="Reintentos", log=True, ticks=[10, 100, 1000, 10000],
        note="El retardo exponencial espacia los reintentos de un mensaje pero no los desincroniza entre mensajes: 600 mensajes que fallaron a la vez vuelven a la vez (en 8, 6 y 468 segundos distintos con reintentos). El jitter reparte la carga y no cambia cuántos reintentos hay. Fallo simultáneo de todos los mensajes: supuesto del autor.",
        note_kind="coral", foot=SINT)


FIGURES = {
    "se-379-sondeo-y-latencia.svg": se331_sondeo,
    "se-379-firmas-y-repeticiones.svg": se331_firma,
    "se-379-reintentos-del-emisor.svg": se331_reintentos,
    "se-380-matriz-de-compatibilidad.svg": se332_matriz,
    "se-380-fallos-en-un-despliegue-gradual.svg": se332_despliegue,
    "se-380-valor-nuevo-de-un-enum.svg": se332_enum,
    "se-381-registros-del-sistema-externo.svg": se333_registros,
    "se-381-cambio-del-proveedor.svg": se333_cambio,
    "se-381-traduccion-con-perdida.svg": se333_fidelidad,
    "se-382-propagar-la-correlacion.svg": se334_correlacion,
    "se-382-senales-de-un-consumidor.svg": se334_senales,
    "se-382-fugas-en-los-registros.svg": se334_fugas,
    "se-383-cinco-causas-de-duplicados.svg": se335_causas,
    "se-383-defensas-contra-causas.svg": se335_defensas,
    "se-383-orden-de-clave-y-efecto.svg": se335_orden_clave,
    "se-384-validador-del-paquete.svg": se336_validador,
    "se-384-flujo-ingenuo-frente-a-tolerante.svg": se336_flujo,
    "se-384-tormenta-de-reintentos.svg": se336_tormenta,
}
