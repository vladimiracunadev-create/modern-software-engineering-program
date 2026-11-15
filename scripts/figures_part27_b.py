"""Figures for SE-331 to SE-336 (synthetic data, fixed seeds; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import tab

SINT = "Datos sintéticos con semilla fija; CPython 3.12 en Windows y Ubuntu (WSL2); cifras idénticas salvo donde se indica."


# ---------------------------------------------------------------- SE-331
def se331_sondeo() -> Fig:
    rows = [
        ["10 s", "8 640", "96,5 %", "5,1 s", "9,5 s"],
        ["30 s", "2 880", "89,9 %", "15,7 s", "28,9 s"],
        ["60 s", "1 440", "81,3 %", "31,6 s", "57,1 s"],
        ["5 min", "288", "34,4 %", "146,4 s", "289,7 s"],
        ["15 min", "96", "2,1 %", "447,3 s", "856,1 s"],
        ["1 h", "24", "0,0 %", "1 807,5 s", "3 379,3 s"],
    ]
    return tab("Sondeo cada cierto intervalo frente a 311 eventos de un día (unos 12 por hora)",
               "Tabla: sondear cada 10 segundos cuesta 8 640 peticiones al día, el 96,5 por ciento vacías, y detecta un evento en 5,1 segundos de media; sondear cada hora cuesta 24 peticiones sin ninguna vacía pero tarda 1 807 segundos de media y 3 379 en el percentil 95; un webhook costaría una entrega por evento, 311 al día.",
               ["Intervalo", "Peticiones al día", "Peticiones vacías", "Retraso medio", "Retraso p95"], rows, [150, 190, 190, 190, 190], row_h=44, size=13,
               note="El sondeo cambia peticiones por retraso: el retraso medio es la mitad del intervalo y las peticiones vacías crecen cuando el intervalo baja. Un webhook empuja 311 entregas sin peticiones vacías, a cambio de recibir tráfico que no controlas. Eventos de Poisson de tasa fija: supuesto del autor.",
               note_kind="gold", foot=SINT)


def se331_firma() -> Fig:
    rows = [
        ["Válido", "Acepta", "Acepta", "Acepta", "Acepta"],
        ["Cuerpo alterado", "Acepta", "Rechaza", "Rechaza", "Rechaza"],
        ["Firmado con otro secreto", "Acepta", "Rechaza", "Rechaza", "Rechaza"],
        ["Sin firma", "Acepta", "Rechaza", "Rechaza", "Rechaza"],
        ["Repetición 10 min después", "Acepta", "Acepta", "Rechaza", "Rechaza"],
        ["Repetición inmediata del mismo id", "Acepta", "Acepta", "Acepta", "Rechaza"],
        ["JSON reserializado con espacios", "Acepta", "Rechaza", "Rechaza", "Rechaza"],
    ]
    return tab("Siete entregas de webhook frente a cuatro políticas de verificación",
               "Tabla: sin verificar se acepta cualquier entrega; una firma HMAC del cuerpo rechaza las alteradas, las de otro secreto, las sin firma y las reserializadas pero acepta repeticiones; añadir una marca de tiempo firmada con tolerancia de 300 segundos rechaza la repetición tardía; solo guardar los identificadores vistos rechaza la repetición inmediata.",
               ["Caso", "Sin verificar", "HMAC del cuerpo", "HMAC con marca de tiempo", "Más id ya visto"], rows, [330, 140, 150, 160, 140], row_h=44, size=13,
               note="Cada capa cierra un ataque distinto: la firma, la manipulación; la marca de tiempo, la repetición tardía; el identificador, la repetición inmediata. Se firman los bytes recibidos, no el objeto: en un servidor real en el bucle local el cuerpo original dio 204 y el reserializado 401.",
               note_kind="coral", foot=SINT)


def se331_reintentos() -> Fig:
    rows = [
        ["3 reintentos fijos de 1 s", "720", "720", "34"],
        ["5 reintentos exponenciales (1, 5, 30, 120, 600 s)", "792", "648", "33"],
        ["9 reintentos hasta 6 h con jitter", "1 440", "0", "71"],
    ]
    return tab("Receptor caído 2 horas: 1 440 eventos (uno cada 10 s durante 4 horas) y tres políticas del emisor",
               "Tabla: tres reintentos de un segundo entregan 720 de 1 440 eventos y pierden 720; cinco reintentos exponenciales entregan 792 y pierden 648; nueve reintentos hasta seis horas entregan los 1 440 pero producen 71 entregas repetidas porque algunas respuestas se perdieron después de procesar.",
               ["Política de reintentos del emisor", "Entregados", "Perdidos", "Entregas repetidas"], rows, [450, 150, 150, 180], row_h=52, size=13,
               note="Con una caída de dos horas los reintentos cortos son un descarte lento. Cuanto más persiste el emisor, más repeticiones recibe el receptor, por lo que el receptor debe ser idempotente. Un sondeo de reconciliación recuperaría los perdidos, pero no se midió aquí. Pérdida de respuesta del 5 % por intento: supuesto del autor.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-332
def se332_matriz() -> Fig:
    rows = [
        ["Añadir un campo opcional", "Sí", "Sí", "Sí", "No"],
        ["Añadir un campo obligatorio", "No", "Sí", "No", "No"],
        ["Quitar un campo opcional", "Sí", "Sí", "No", "Sí"],
        ["Quitar un campo obligatorio", "Sí", "No", "No", "No"],
        ["Renombrar un campo", "No", "No", "No", "No"],
        ["Cambiar el tipo de un campo", "No", "No", "No", "No"],
        ["Volver obligatorio un campo opcional", "No", "Sí", "No", "Sí"],
    ]
    return tab("Siete cambios de esquema: si el lector nuevo lee datos viejos y el lector viejo lee datos nuevos",
               "Tabla: añadir un campo opcional es compatible en ambos sentidos con un lector tolerante y solo hacia atrás con uno estricto; renombrar un campo o cambiar su tipo no es compatible en ningún sentido ni con ningún lector; añadir un campo obligatorio rompe a los lectores nuevos con datos viejos; quitar un obligatorio rompe a los lectores viejos con datos nuevos.",
               ["Cambio", "Tolerante: nuevo lee viejos", "Tolerante: viejo lee nuevos", "Estricto: nuevo lee viejos", "Estricto: viejo lee nuevos"], rows, [250, 170, 170, 170, 170], row_h=44, size=13,
               note="La compatibilidad depende de quién lee y de cómo: un lector estricto convierte cualquier campo nuevo en un fallo. Se probó con instancias mínimas y máximas de cada versión. Solo se modelan campos simples y tipos primitivos; no se ejecutó ningún registro de esquemas real.",
               note_kind="gold", foot=SINT)


def se332_despliegue() -> Fig:
    rows = [
        ["Añadir campo opcional", "Tolerante", "0", "0"],
        ["Añadir campo opcional", "Estricto", "2 825", "820"],
        ["Añadir campo obligatorio", "Tolerante", "801", "2 809"],
        ["Añadir campo obligatorio", "Estricto", "3 626", "3 629"],
        ["Renombrar campo", "Tolerante", "3 626", "3 629"],
        ["Renombrar campo", "Estricto", "3 626", "3 629"],
    ]
    return tab("Despliegue gradual en cinco pasos: mensajes que fallan de 10 000 según qué lado se actualiza primero",
               "Tabla: añadir un campo opcional no falla con lectores tolerantes en ningún orden pero falla 2 825 veces con lectores estrictos si los productores se actualizan primero y 820 si lo hacen los consumidores; añadir un campo obligatorio falla 801 o 2 809 veces con lectores tolerantes; renombrar un campo falla unas 3 600 veces en cualquier orden.",
               ["Cambio", "Lector", "Productores primero", "Consumidores primero"], rows, [300, 160, 220, 240], row_h=44, size=13,
               note="Un despliegue gradual convive con dos versiones durante un rato y los fallos aparecen en ese rato. Añadir obligatorio es seguro solo si primero se actualizan los productores en dos pasos (opcional y luego obligatorio). Renombrar nunca es seguro de una vez. Cinco pasos del 20 %: supuesto del autor.",
               note_kind="coral", foot=SINT)


def se332_enum() -> Fig:
    rows = [
        ["Lanzar una excepción y reintentar sin fin", "4 991", "0", "0"],
        ["Descartar el valor desconocido", "0", "338", "0"],
        ["Sustituir por «desconocido»", "0", "0", "338 sin su significado"],
        ["Conservar el valor y enviarlo a revisión", "0", "0", "338 con su valor"],
    ]
    return tab("Un estado nuevo aparece en 338 de 10 000 mensajes desde la mitad del flujo",
               "Tabla: un consumidor que lanza una excepción con un valor desconocido bloquea 4 991 mensajes, desde el primero con el valor nuevo; uno que descarta pierde 338 mensajes; uno que sustituye por desconocido conserva los 338 pero sin su significado; uno que conserva el valor y lo envía a revisión los conserva con su valor.",
               ["Política del consumidor", "Mensajes bloqueados", "Mensajes perdidos", "Mensajes con el valor nuevo procesados"], rows, [380, 160, 160, 220], row_h=52, size=13,
               note="Un valor nuevo de una enumeración es el cambio más común y el que más se subestima: la política por defecto del consumidor decide si es un incidente, una pérdida silenciosa o una tarea de revisión. 6 % de valores nuevos en la segunda mitad: supuesto del autor.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-333
def se333_registros() -> Fig:
    rows = [
        ["Conversión directa con float", "1 132", "3 868", "411", "0"],
        ["Capa anticorrupción", "4 627", "0", "0", "373 (198 N/P, 175 vacías)"],
    ]
    return tab("5 000 notas de un sistema externo con cuatro formatos distintos",
               "Tabla: convertir la nota con float acepta 1 132 de 5 000 registros, rompe con 3 868 y deja pasar 411 notas fuera del rango de 1,0 a 7,0 porque vienen en escala de 0 a 100; una capa anticorrupción acepta 4 627 normalizados, no deja pasar ninguna fuera de rango y pone 373 en cuarentena con su motivo.",
               ["Adaptador", "Aceptadas", "Rotas por excepción", "Aceptadas fuera de rango", "En cuarentena"], rows, [250, 120, 170, 170, 210], row_h=52, size=13,
               note="El modelo externo usa coma decimal, punto decimal, escala de 0 a 100, «N/P» y vacío. La conversión directa no solo rompe: acepta como válidas 411 notas que significan otra cosa. La capa traduce, rechaza con motivo y deja un lugar único donde mirar. Distribución de formatos del autor.",
               note_kind="coral", foot=SINT)


def se333_cambio() -> Fig:
    rows = [
        ["Datos con el formato actual", "0 de 6 funciones fallan", "0 de 6 funciones fallan"],
        ["El proveedor renombra cod_alumno a alumno_id", "6 de 6 funciones fallan", "1 falla: el traductor, con error explícito"],
        ["Lugares del código que mencionan cod_alumno", "6", "1"],
    ]
    return tab("Un proveedor renombra un campo: qué falla sin y con capa anticorrupción",
               "Tabla: con datos en el formato actual nada falla en ninguno de los dos diseños; cuando el proveedor renombra un campo, seis de seis funciones del diseño sin capa fallan y solo falla el traductor, con un error explícito, en el diseño con capa; el nombre externo aparece en seis lugares sin capa y en uno con ella.",
               ["Situación", "Sin capa anticorrupción", "Con capa anticorrupción"], rows, [370, 260, 290], row_h=52, size=13,
               note="La capa no evita el cambio del proveedor; limita su alcance a un lugar y lo convierte en un error con nombre. El código de seis funciones lo escribió el autor para el ejercicio, ejecutado de verdad con el campo original y con el renombrado; no es una medida de ningún proyecto real.",
               note_kind="teal", foot=SINT)


def se333_fidelidad() -> Fig:
    rows = [
        ["Estado: 9 códigos externos a 4 del dominio", "2 813", "2 187"],
        ["Nota: de 0 a 100 a 1,0 a 7,0 con un decimal", "1 912", "3 088"],
        ["Ambas traducciones a la vez", "3 659", "1 341"],
        ["Nota con tres decimales", "0", "5 000"],
        ["Estado traducido y código externo original conservado", "0", "5 000"],
    ]
    return tab("Ida y vuelta de 5 000 registros: qué se recupera al volver al modelo externo",
               "Tabla: traducir nueve códigos de estado externos a cuatro del dominio impide recuperar el original en 2 813 de 5 000 registros; convertir la nota de 0 a 100 a una escala de 1,0 a 7,0 con un decimal altera 1 912; ambas juntas alteran 3 659; con tres decimales o conservando el código externo original no se altera ninguno.",
               ["Traducción", "No se recuperan", "Se recuperan"], rows, [520, 180, 180], row_h=48, size=13,
               note="Traducir es resumir y resumir pierde información. Si algún proceso debe devolver el dato al sistema externo, hay que conservar el original junto al traducido o ampliar la precisión del modelo. Asignación de estados 9 a 4 y reparto uniforme: supuestos del autor.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-334
def se334_correlacion() -> Fig:
    rows = [
        ["0 %", "10 000", "100,0 %", "100,0 %"],
        ["1 %", "9 712", "97,1 %", "97,0 %"],
        ["5 %", "8 610", "86,1 %", "85,7 %"],
        ["20 %", "5 154", "51,5 %", "51,2 %"],
    ]
    return tab("Trazas completas de tres saltos si cada salto puede perder el encabezado de correlación",
               "Tabla: si cada uno de tres saltos pierde el encabezado de correlación con probabilidad 0, 1, 5 y 20 por ciento, quedan completas 10 000, 9 712, 8 610 y 5 154 trazas de 10 000, muy cerca de uno menos la pérdida elevado al cubo; la reconstrucción por estudiante y ventana de dos segundos acierta el 99,4, 93,6 y 74,8 por ciento con 1, 10 y 50 solicitudes por segundo.",
               ["Pérdida por salto", "Trazas completas de 10 000", "Porcentaje medido", "Esperado (1 − d)³"], rows, [200, 270, 200, 220], row_h=44, size=13,
               note="La correlación se pierde en multiplicación: un salto que no propaga el encabezado rompe la traza entera. Reconstruir por tiempo y estudiante funciona con poca concurrencia (99,4 %) y se degrada con mucha (74,8 %). Pérdidas independientes entre saltos: supuesto del autor.",
               note_kind="gold", foot=SINT)


def se334_senales() -> Fig:
    rows = [
        ["Consumidor lento (mitad de capacidad)", "101 s", "123 s", "nunca", "nunca"],
        ["Consumidor colgado", "50 s", "61 s", "25 s", "nunca"],
        ["Mensaje venenoso que se reintenta", "50 s", "61 s", "25 s", "10 s"],
        ["Productor parado", "nunca", "nunca", "25 s (falsa alarma)", "nunca"],
    ]
    return tab("Segundos hasta la primera alarma desde el inicio de cada falla, según la señal vigilada",
               "Tabla: la profundidad de la cola detecta al consumidor lento a los 101 segundos pero nunca al productor parado; la edad del mensaje más viejo es más lenta que la profundidad; la tasa de procesados detecta consumidores colgados y venenosos a los 25 segundos pero da una falsa alarma cuando el productor se detiene; la tasa de errores solo detecta el mensaje venenoso, a los 10 segundos.",
               ["Falla", "Profundidad > 50", "Edad > 60 s", "Procesados < 5 en 30 s", "Errores > 10 en 30 s"], rows, [330, 140, 120, 200, 130], row_h=52, size=13,
               note="Ninguna señal detecta todo: cada falla se ve en una señal distinta y una misma señal confunde fallas diferentes. Se vigilan al menos profundidad, edad, procesados y errores, y se interpretan juntas. Umbrales fijos y llegada de un mensaje por segundo: supuestos del autor.",
               note_kind="coral", foot=SINT)


def se334_fugas() -> Fig:
    rows = [
        ["Registrar el cuerpo completo", "2 000", "2 000", "200"],
        ["Sustituir correos con una expresión regular", "0", "2 000", "200"],
        ["Sustituir correos y tokens con expresiones regulares", "0", "0", "200"],
        ["Registrar solo los campos permitidos", "0", "0", "0"],
    ]
    return tab("Datos sensibles que aparecen en los registros de 2 000 mensajes según la política",
               "Tabla: registrar el cuerpo completo filtra 2 000 correos y 2 000 tokens; sustituir correos con una expresión regular deja salir 2 000 tokens; sustituir ambos aún deja 200 comentarios con el identificador del estudiante escrito de otra forma; registrar solo campos permitidos no filtra nada de lo medido.",
               ["Política de registro", "Correos filtrados", "Tokens filtrados", "Comentarios con identificador"], rows, [420, 150, 150, 200], row_h=52, size=13,
               note="Una lista de lo permitido falla cerrada: lo nuevo no se registra. Una lista de lo prohibido falla abierta: lo que no previste se registra. Los correos y tokens son sintéticos (dominio de ensayo y cadenas aleatorias); el comentario ofuscado muestra por qué la expresión regular no basta.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-335
def se335_causas() -> Fig:
    rows = [
        ["Caída del consumidor antes de acusar", "5 % de los mensajes", "106"],
        ["Acuse perdido en la red", "5 % de los acuses", "122"],
        ["Reintento del productor tras un tiempo agotado", "5 % de los envíos, con otro id", "103"],
        ["Visibilidad de 30 s menor que el proceso", "Proceso lognormal, mediana 16 s", "378"],
        ["Reinicio de desplazamientos", "200 mensajes releídos", "200"],
    ]
    return tab("Cinco formas de provocar duplicados en un consumidor sin defensa (2 000 mensajes)",
               "Tabla: sin ninguna defensa, la caída antes de acusar produce 106 efectos duplicados de 2 000, el acuse perdido 122, el reintento del productor 103, una visibilidad de 30 segundos menor que el tiempo de proceso 378 y reiniciar los desplazamientos de 200 mensajes produce 200.",
               ["Causa provocada", "Parámetro", "Efectos duplicados"], rows, [430, 330, 160], row_h=48, size=13,
               note="Cinco causas distintas producen el mismo síntoma, un efecto repetido, y se defienden de formas distintas. La de visibilidad es la más cara porque depende del tiempo de proceso y no de un fallo. Las probabilidades y la distribución del tiempo de proceso son supuestos del autor.",
               note_kind="gold", foot=SINT)


def se335_defensas() -> Fig:
    rows = [
        ["Ninguna", "106", "122", "103", "378", "200"],
        ["Clave del mensaje", "0", "0", "103", "0", "0"],
        ["Clave de negocio única", "0", "0", "0", "0", "0"],
        ["Actualización condicionada por versión", "0", "0", "0", "0", "0"],
        ["Operación naturalmente idempotente", "0", "0", "0", "0", "0"],
    ]
    return tab("Efectos duplicados que quedan según la defensa y la causa del duplicado",
               "Tabla: sin defensa quedan 106, 122, 103, 378 y 200 duplicados según la causa; una clave del identificador del mensaje elimina todos salvo los 103 del reintento del productor, que llegan con otro identificador; una clave de negocio única, una actualización condicionada por versión y una operación idempotente dejan cero en todas las causas.",
               ["Defensa", "Caída", "Acuse", "Productor", "Visibilidad", "Desplazamientos"], rows, [310, 100, 100, 120, 130, 160], row_h=48, size=13,
               note="La clave del mensaje no ve duplicados que nacen antes del corredor: el reintento del productor crea un mensaje nuevo con el mismo contenido. La clave de negocio atrapa todas las causas porque no depende de cómo llegó el duplicado, pero exige saber qué identifica una operación. SQLite real.",
               note_kind="teal", foot=SINT)


def se335_orden_clave() -> Fig:
    rows = [
        ["Guardar la clave y luego el efecto (dos transacciones)", "100", "0", "—"],
        ["Guardar el efecto y luego la clave (dos transacciones)", "0", "100", "—"],
        ["Clave y efecto en una sola transacción", "0", "0", "—"],
        ["Clave gruesa: solo el estudiante", "0", "0", "309"],
        ["Clave fina: estudiante e intento", "0", "0", "0"],
    ]
    return tab("Dónde falla la defensa de idempotencia: orden de los pasos y alcance de la clave",
               "Tabla: guardar la clave de idempotencia y después el efecto en dos transacciones pierde 100 efectos de 2 000 cuando hay una caída entre ambos; guardar primero el efecto duplica 100; hacerlo en una sola transacción no pierde ni duplica; una clave solo por estudiante descarta 309 intentos legítimos de 609 y una clave por estudiante e intento no descarta ninguno.",
               ["Diseño de la defensa", "Efectos perdidos", "Efectos duplicados", "Intentos legítimos descartados"], rows, [430, 150, 150, 180], row_h=52, size=13,
               note="Una defensa mal ubicada produce el fallo contrario al que prevenía: perder en lugar de duplicar. La clave y el efecto deben confirmarse juntos, y la clave debe identificar la operación, no a la persona. Caída del 5 % entre pasos y 100 duplicados reales entre 609 intentos legítimos: supuestos del autor.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-336
def se336_validador() -> Fig:
    rows = [
        ["Quitar o vaciar una sección", "100", "100"],
        ["Ventana de deduplicación menor que el horizonte de reintentos", "10", "10"],
        ["Cero intentos o espera mal contada", "20", "20"],
        ["Bandeja de entrada sin restricción de unicidad", "10", "10"],
        ["Sin firma, aunque aparezca la palabra HMAC", "10", "0"],
        ["Reintentos sin jitter o con horizonte incoherente", "20", "0"],
        ["Cola de fallidos sin alarma ni dueño", "10", "0"],
        ["Clave de idempotencia demasiado gruesa", "10", "0"],
        ["Registrar datos personales", "10", "0"],
    ]
    return tab("Un validador sobre 200 mutaciones de un paquete de integración: 140 detectadas",
               "Tabla: el validador detecta las 100 mutaciones estructurales, las 10 de ventana de deduplicación demasiado corta, las 20 de cero intentos o espera mal contada y las 10 de bandeja de entrada sin unicidad; no detecta ninguna de las 10 sin firma con la palabra HMAC presente, las 20 sin jitter o con horizonte incoherente, ni las de cola sin alarma, clave gruesa o datos personales.",
               ["Tipo de mutación", "Mutaciones", "Detectadas"], rows, [560, 160, 160], row_h=38, size=13,
               note="Un paquete completo no es un paquete correcto: el validador ve la forma y algunas incoherencias numéricas, y deja pasar todo lo que requiere entender el sentido. Las reglas se escribieron mirando estos mismos casos, por lo que 140 de 200 no estima su exactitud real.",
               note_kind="gold", foot=SINT)


def se336_flujo() -> Fig:
    rows = [
        ["Entregas sin calificación", "74", "0"],
        ["Entregas con calificación doble", "171", "0"],
        ["Calificadas sin aviso al estudiante", "291", "0"],
        ["Estudiantes avisados dos veces", "153", "0"],
        ["15 mensajes venenosos", "Bloquean 2 793 mensajes tras el primero", "15 en la cola de fallidos; nadie bloqueado"],
    ]
    return tab("Flujo de entrega, calificación y aviso con fallas inyectadas (3 000 entregas)",
               "Tabla: sin outbox, bandeja de entrada ni cola de fallidos el flujo deja 74 entregas sin calificar, 171 calificadas dos veces, 291 sin aviso, 153 avisadas dos veces y un mensaje venenoso que bloquea los 2 793 que le siguen; el flujo tolerante deja cero en todas las invariantes y aparta los 15 venenosos.",
               ["Invariante", "Flujo ingenuo", "Flujo tolerante"], rows, [350, 290, 280], row_h=52, size=13,
               note="El flujo tolerante combina cuatro mecanismos de las clases anteriores: outbox, bandeja de entrada, versión por entidad y cola de fallidos. Las fallas (2 % de caída del relevo, 3 % de duplicados, desorden, 15 venenosos, notificador caído) son inyecciones del autor sobre SQLite y listas en memoria.",
               note_kind="teal", foot=SINT)


def se336_tormenta() -> Fig:
    rows = [
        ["Espera fija de 30 s, 8 intentos", "4 800", "600", "8"],
        ["Exponencial 10, 20, 40... s, sin jitter", "3 600", "600", "6"],
        ["Exponencial 10, 20, 40... s, con jitter completo", "3 600", "93", "468"],
    ]
    return tab("600 mensajes que fallan a la vez y reintentan: carga que recibe el servicio por segundo",
               "Tabla: con espera fija o exponencial sin jitter los 600 mensajes reintentan juntos y el servicio recibe un pico de 600 reintentos en un segundo, en 8 y 6 instantes; con jitter completo el pico baja a 93 y los reintentos se reparten en 468 segundos distintos.",
               ["Política de reintentos", "Reintentos totales", "Pico por segundo", "Segundos con reintentos"], rows, [430, 160, 150, 180], row_h=52, size=13,
               note="El retardo exponencial espacia los reintentos de un mensaje pero no los desincroniza entre mensajes: 600 mensajes que fallaron a la vez vuelven a la vez. El jitter reparte la carga y no cambia cuántos reintentos hay. Fallo simultáneo de todos los mensajes: supuesto del autor.",
               note_kind="coral", foot=SINT)


FIGURES = {
    "se-331-sondeo-y-latencia.svg": se331_sondeo,
    "se-331-firmas-y-repeticiones.svg": se331_firma,
    "se-331-reintentos-del-emisor.svg": se331_reintentos,
    "se-332-matriz-de-compatibilidad.svg": se332_matriz,
    "se-332-fallos-en-un-despliegue-gradual.svg": se332_despliegue,
    "se-332-valor-nuevo-de-un-enum.svg": se332_enum,
    "se-333-registros-del-sistema-externo.svg": se333_registros,
    "se-333-cambio-del-proveedor.svg": se333_cambio,
    "se-333-traduccion-con-perdida.svg": se333_fidelidad,
    "se-334-propagar-la-correlacion.svg": se334_correlacion,
    "se-334-senales-de-un-consumidor.svg": se334_senales,
    "se-334-fugas-en-los-registros.svg": se334_fugas,
    "se-335-cinco-causas-de-duplicados.svg": se335_causas,
    "se-335-defensas-contra-causas.svg": se335_defensas,
    "se-335-orden-de-clave-y-efecto.svg": se335_orden_clave,
    "se-336-validador-del-paquete.svg": se336_validador,
    "se-336-flujo-ingenuo-frente-a-tolerante.svg": se336_flujo,
    "se-336-tormenta-de-reintentos.svg": se336_tormenta,
}
