"""Figures for SE-271 to SE-276 (synthetic simulations, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Simulación sintética con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-271
def se271_cortes() -> Fig:
    rows = [
        ["Una sola ranura (sobrescribe)", "19", "1", "1", "17 (inutilizable)"],
        ["Dos ranuras, indicador atómico", "19", "18", "1", "0"],
        ["Dos ranuras, indicador de 2 bytes sin validar", "20", "18", "1", "1 (indicador inválido)"],
        ["Dos ranuras, indicador de 2 bytes validado", "20", "19", "1", "0"],
    ]
    return tab("Corte de energía en cada paso posible de una actualización (enumeración exhaustiva)",
               "Tabla: al cortar la energía en cada uno de los pasos de una actualización, una sola ranura que sobrescribe deja el dispositivo inutilizable en 17 de 19 puntos de corte; con dos ranuras y un indicador atómico ninguno, y con un indicador de dos bytes sin validar queda un punto de corte inválido que desaparece al validarlo.",
               ["Estrategia", "Puntos de corte", "Queda la antigua", "Queda la nueva", "Queda inservible"], rows, [400, 150, 180, 160, 230], row_h=52, size=13,
               note="La enumeración prueba todos los cortes posibles, no una muestra: el defecto del indicador de dos bytes existe en un solo punto de veinte y una prueba con cortes al azar lo vería pocas veces. Es un modelo de pasos, no de una memoria flash concreta con su orden de programación.",
               note_kind="coral", foot=SINT)


def se271_delta() -> Fig:
    rows = [
        ["50 bytes cambiados al azar", "13 200", "13 512"],
        ["500 bytes cambiados al azar", "106 128", "106 936"],
        ["Inserción de 100 bytes a mitad", "135 168", "288"],
        ["Inserción de 1 byte a mitad", "135 168", "288"],
    ]
    return tab("Bytes de una actualización diferencial de una imagen de 256 KiB (imagen completa: 262 144)",
               "Tabla: con una imagen de 262 144 bytes, comparar bloques de 256 bytes por posición transmite 13 200 bytes si cambian 50 bytes al azar y 135 168 si se inserta un solo byte a mitad de la imagen; buscar los bloques en cualquier posición transmite 288 bytes en ese caso, y la imagen nueva comprimida ocupa unos 184 000.",
               ["Cambio", "Bloques por posición", "Bloques en cualquier posición"], rows, [400, 220, 300], row_h=40, size=13,
               note="Una inserción desplaza todo lo que sigue y la comparación por posición lo trata como un cambio total; la búsqueda de bloques lo reduce a 288 bytes. Con cambios dispersos ambos métodos se parecen. Firmware sintético de 50 % de estructura y 50 % de bytes aleatorios: uno real se comprime de otro modo.",
               note_kind="gold", foot=SINT)


def se271_etapas() -> Fig:
    rows = [
        ["0,1 %", "10 · 0 %", "10 · 5 %", "10 · 5 %"],
        ["0,5 %", "50 · 0 %", "15 · 78 %", "15 · 77 %"],
        ["2 %", "200 · 0 %", "15 · 100 %", "16 · 100 %"],
        ["10 %", "1 002 · 0 %", "11 · 100 %", "10 · 100 %"],
    ]
    return tab("Dispositivos dañados · porcentaje de despliegues detenidos antes del 100 %, de 10 000",
               "Tabla: con una versión que falla en el 2 por ciento de los dispositivos, publicar a todos daña 200 sin posibilidad de detenerse, y las etapas de 1 por ciento, 10 por ciento y 100 por ciento dañan 15 y siempre se detienen; con un fallo del 0,1 por ciento las etapas dañan los mismos 10 y casi nunca detectan el problema antes del final.",
               ["Fallo de la versión", "Todos a la vez", "Etapas 1 %, 10 %, 100 %", "Etapas 0,1 %, 1 %, 10 %, 100 %"], rows, [220, 220, 270, 330], row_h=44, size=13,
               note="Las etapas protegen cuando el fallo es lo bastante frecuente como para dar tres informes en la etapa pequeña. Con un fallo del 0,1 % la etapa de 100 dispositivos espera 0,1 fallos y el defecto llega a toda la flota: el tamaño de la primera etapa fija qué fallos se ven. Probabilidad de informe 0,9; 600 despliegues por celda.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-272
def se272_radio() -> Fig:
    rows = [
        ["1", "10 000", "1", "10 000"],
        ["10", "10 000", "10", "10 000"],
        ["100", "10 000", "100", "10 000"],
    ]
    return tab("Dispositivos suplantables tras extraer k claves de una flota de 10 000",
               "Tabla: si toda la flota comparte una clave, extraer una sola clave de un dispositivo permite suplantar a los 10 000; con claves distintas por dispositivo, extraer 1, 10 o 100 claves permite suplantar exactamente 1, 10 o 100, y si la clave maestra de derivación sale del dispositivo, vuelven a ser 10 000.",
               ["Claves extraídas", "Una clave de flota", "Claves por dispositivo", "Derivadas, con la maestra extraída"], rows, [230, 230, 260, 330], row_h=44, size=13,
               note="La clave por dispositivo limita el daño de una extracción a un dispositivo, siempre que la clave maestra nunca esté en ninguno. Las firmas son HMAC-SHA256 reales; la flota, la extracción y los números son sintéticos y no se atacó ningún chip.",
               note_kind="teal", foot=SINT)


def se272_reloj() -> Fig:
    rows = [
        ["1 s", "0,0 %", "0,0 %", "0,0 %"],
        ["5 s", "31,56 %", "0,0 %", "0,0 %"],
        ["30 s", "86,71 %", "31,56 %", "0,01 %"],
    ]
    return tab("Mensajes legítimos rechazados por una ventana de tiempo según el desfase del reloj",
               "Tabla: con un desfase típico de reloj de 5 segundos, una ventana de más o menos 5 segundos rechaza el 31,56 por ciento de los mensajes legítimos, y con 30 segundos de desfase una de más o menos 30 rechaza el 31,56 y una de 5 el 86,71; un contador que se reinicia en cada arranque acepta una reproducción en el 50,8 por ciento de los casos.",
               ["Desfase típico (σ)", "Ventana ±5 s", "Ventana ±30 s", "Ventana ±120 s"], rows, [270, 210, 210, 210], row_h=44, size=13,
               note="Ensanchar la ventana evita rechazos y deja más tiempo para reproducir un mensaje capturado. Un contador estricto no depende del reloj, pero si se reinicia sin memoria persistente acepta el 50,8 % de las reproducciones del modelo. Desfase gaussiano supuesto; no se midió ningún reloj.",
               note_kind="coral", foot=SINT)


def se272_semilla() -> Fig:
    rows = [
        ["Segundo de arranque en 1 hora (3 600)", "2 279", "5 000 (100 %)"],
        ["Segundo de arranque en 1 día (86 400)", "149", "197 (3,94 %)"],
        ["Semilla de 32 bits", "0", "0 (0 %)"],
    ]
    return tab("Claves de 64 bits generadas con una semilla débil (5000 dispositivos)",
               "Tabla: si 5000 dispositivos generan una clave de 64 bits con el segundo de arranque como semilla, con una ventana de una hora hay 2279 claves repetidas y quien enumere las 3600 semillas recupera las 5000 claves; con un día quedan 149 repetidas y se recupera el 3,94 por ciento; con una semilla de 32 bits no hay repetidas ni recuperadas.",
               ["Origen de la semilla", "Claves repetidas", "Recuperadas enumerando 3 600 semillas"], rows, [430, 190, 360], row_h=44, size=13,
               note="Una clave de 64 bits con una semilla de 3600 posibilidades tiene la seguridad de 12 bits: la longitud de la clave no importa si la semilla es predecible. Se usó el generador estándar de Python solo para ilustrar el mecanismo; no es un generador criptográfico y ningún dispositivo real lo hace así.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-273
def se273_reporte() -> Fig:
    rows = [
        ["Cada segundo", "691 200", "8", "0", "0,00"],
        ["Media por minuto", "11 520", "8", "22", "0,089"],
        ["Máximo por minuto", "11 520", "8", "22", "0,250"],
        ["Banda muerta de 0,5", "1 250", "8", "0", "0,140"],
        ["Media por minuto y evento", "11 608", "8", "22", "0,100"],
    ]
    return tab("Estrategias de reporte de una señal de 1 Hz durante un día (86 400 muestras, 8 eventos)",
               "Tabla: enviar cada segundo cuesta 691 200 bytes por día; la media por minuto, 11 520, con un retraso mediano de aviso de 22 segundos; la banda muerta de 0,5, solo 1250 bytes con aviso inmediato, y todas detectan los ocho eventos, pero el pico notificado queda 0,28 por debajo del real con la media por minuto y 0,01 con el máximo por minuto.",
               ["Estrategia", "Bytes al día", "Eventos detectados", "Retraso mediano (s)", "Error medio"], rows, [330, 160, 210, 220, 140], row_h=40, size=13,
               note="La banda muerta reduce los bytes 550 veces y avisa de inmediato, pero reconstruye peor la señal lenta. La media por minuto la reconstruye mejor y retrasa el aviso. No hay estrategia que gane en todo: se elige según lo que se decide con los datos. Señal sintética con ocho picos de 3 °C.",
               note_kind="gold", foot=SINT)


def se273_plazo() -> Fig:
    items = [
        ("Decisión local", 100.0, "teal", "100,0 %"),
        ("Decisión solo en la nube", 61.41, "coral", "61,41 %"),
        ("Nube con respaldo local", 100.0, "teal", "100,0 %"),
    ]
    return bars("Decisiones de control que cumplen un plazo de 100 ms (100 000 decisiones)",
                "Barras: con un plazo de 100 milisegundos, una decisión local lo cumple el 100 por ciento de las veces, una que depende de la nube el 61,41 por ciento, con un percentil 99 de ida y vuelta de 256,7 milisegundos y la nube caída el 5 por ciento del tiempo, y una nube con respaldo local el 100 por ciento.",
                items, 5, "La nube incumple por la latencia (mediana de 80 ms con cola larga) y por las caídas; el respaldo local cumple siempre, pero decide con menos información. Latencias lognormales y caídas del 5 % supuestas, no medidas en ninguna red.",
                label_w=300, width=950, note_kind="gold", foot=SINT)


def se273_carga() -> Fig:
    rows = [
        ["1 muestra", "85,0", "13,0", "83,0", "21,0"],
        ["10 muestras", "84,9", "13,0", "23,0", "13,0"],
        ["60 muestras", "84,7", "13,0", "14,9", "10,5"],
    ]
    return tab("Bytes por muestra según la codificación y el tamaño del lote",
               "Tabla: una lectura de cinco magnitudes ocupa 85 bytes en JSON y 13 en binario por muestra; comprimir un lote de 60 muestras reduce el JSON a 14,9 y el binario a 10,5 bytes por muestra, pero con una sola muestra comprimir casi no ayuda al JSON, 83,0, y empeora el binario, 21,0.",
               ["Lote", "JSON", "Binario", "JSON comprimido", "Binario comprimido"], rows, [200, 160, 160, 260, 250], row_h=44, size=13,
               note="El formato compacto ahorra más que comprimir cuando el lote es pequeño; comprimir ayuda cuando hay muchas muestras parecidas y a cambio exige memoria y energía en el dispositivo. Lecturas sintéticas con ruido gaussiano; la compresión es zlib en el nivel 9.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-274
def se274_voto() -> Fig:
    rows = [
        ["0 %", "0,0998", "0,0278", "0,0300", "3,6"],
        ["5 %", "0,0997", "0,0303", "0,0321", "3,3"],
        ["20 %", "0,0988", "0,0380", "0,0392", "2,6"],
    ]
    return tab("Fallo peligroso no detectado en una misión: un sensor frente a votación 2 de 3",
               "Tabla: con una probabilidad de fallo de 0,1 por sensor, un sensor falla peligrosamente con 0,0998 y una votación de dos de tres con 0,0278 si los fallos son independientes, 3,6 veces menos; si el 20 por ciento de los fallos tiene causa común, la votación llega a 0,0380 y la mejora baja a 2,6 veces.",
               ["Fracción de causa común", "Un sensor", "2 de 3 simulado", "2 de 3 analítico", "Mejora (veces)"], rows, [260, 160, 220, 220, 150], row_h=44, size=13,
               note="La redundancia no triplica la seguridad: con p = 0,1 solo la divide por 3,6, y la causa común (misma fuente de alimentación, mismo error de calibración, mismo software) se come la mejora. Un millón de misiones por fila; p = 0,1 es alto a propósito para poder medirlo.",
               note_kind="coral", foot=SINT)


def se274_vigilancia() -> Fig:
    rows = [
        ["0,1 s", "17,289", "5,1 s", "8,78"],
        ["0,5 s", "6,086", "5,5 s", "3,10"],
        ["1 s", "2,268", "6,0 s", "1,17"],
        ["2 s", "0,581", "7,0 s", "0,32"],
        ["5 s", "0,047", "10,0 s", "0,06"],
        ["10 s", "0,003", "15,0 s", "0,05"],
    ]
    return tab("Plazo del temporizador de vigilancia: reinicios falsos y horas perdidas por año",
               "Tabla: con operaciones largas de mediana 0,3 segundos y cola larga, un plazo de vigilancia de 0,1 segundos produce 17,3 reinicios falsos por día y 8,78 horas perdidas por año; con 5 segundos, 0,047 reinicios y 0,06 horas, pero un cuelgue tarda 10 segundos en resolverse; la operación más larga observada fue de 35,3 segundos.",
               ["Plazo", "Reinicios falsos por día", "Indisponibilidad por cuelgue", "Horas perdidas por año"], rows, [150, 290, 320, 250], row_h=40, size=13,
               note="Un plazo corto reacciona rápido y reinicia sin motivo las operaciones largas legítimas; uno largo casi no se equivoca y tarda en actuar. El percentil 99,9 de las operaciones es 6,6 s: un plazo de 5 s aún reinicia una de cada mil. Un cuelgue al mes y 20 operaciones largas al día son supuestos.",
               note_kind="gold", foot=SINT)


def se274_vuelta() -> Fig:
    rows = [
        ["Comparación directa de tiempos", "66 703 de 200 000 (33,35 %)"],
        ["Resta sin signo en 32 bits", "0 de 200 000"],
        ["Vuelta del contador de milisegundos", "49,71 días"],
        ["Desbordamiento de segundos con signo", "19 de enero de 2038, 03:14:07 UTC"],
    ]
    return tab("Temporizadores armados en los dos minutos previos a la vuelta de un contador de 32 bits",
               "Tabla: entre temporizadores armados en los dos minutos previos a la vuelta de un contador de milisegundos de 32 bits, la comparación directa decide mal el 33,35 por ciento, 66 703 de 200 000, y la resta sin signo ninguno; el contador da la vuelta a los 49,71 días y los segundos con signo de 32 bits se desbordan el 19 de enero de 2038.",
               ["Medida", "Resultado"], rows, [430, 420], row_h=40, size=13,
               note="El defecto no aparece nunca en las pruebas de un día y llega a los 49,7 días en todos los dispositivos a la vez si arrancaron juntos. Se cura con una comparación escrita para la vuelta, no con un contador más grande. Un dispositivo de 15 años instalado en 2026 pasa por 2038.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-275
def se275_inyeccion() -> Fig:
    rows = [
        ["Solo rango", "0", "0", "0", "0", "0", "0", "0"],
        ["Rango y variación", "0", "0", "100", "98", "100", "0", "298"],
        ["Más congelado y ausencia", "100", "0", "100", "98", "100", "100", "498"],
        ["Más dispersión", "100", "0", "100", "100", "100", "100", "500"],
        ["Más referencia independiente", "100", "100", "100", "100", "100", "100", "600"],
    ]
    return tab("Fallos detectados de 100 inyectados por tipo según las comprobaciones activas",
               "Tabla: una campaña de 600 fallos inyectados en un nodo sensor, 100 de cada uno de seis tipos, detecta 0 con solo una comprobación de rango, 298 al añadir la variación máxima, 498 con detección de valor congelado y ausencia de lectura, 500 con dispersión y 600 al añadir una referencia independiente, que es la única que ve la deriva.",
               ["Comprobaciones", "Congelado", "Deriva", "Pico", "Ruido ×10", "Bit alto", "Ausencia", "Total"], rows, [270, 110, 90, 80, 110, 100, 110, 80], row_h=40, size=12,
               note="La deriva lenta pasa todas las comprobaciones que miran solo el propio sensor: cada lectura parece plausible con respecto a la anterior. Solo una referencia independiente la ve. Cada celda son 100 fallos con instante de aparición aleatorio; los fallos y las comprobaciones son modelos del autor.",
               note_kind="gold", foot=SINT)


def se275_escritura() -> Fig:
    rows = [
        ["Sobrescribir en el mismo sitio", "10", "1", "1", "8"],
        ["Una copia con CRC", "12", "1", "1", "10"],
        ["Dos copias alternadas con CRC", "12", "11", "1", "0"],
    ]
    return tab("Corte de energía en cada punto de la escritura de una configuración de 8 bytes",
               "Tabla: al cortar la energía en cada punto posible de la escritura de una configuración, sobrescribir en el mismo sitio deja una configuración inválida en 8 de 10 puntos, una sola copia con CRC en 10 de 12, y dos copias alternadas con CRC en ninguno de 12, quedando siempre la antigua o la nueva.",
               ["Estrategia", "Puntos de corte", "Antigua válida", "Nueva válida", "Inválida"], rows, [400, 160, 190, 170, 140], row_h=44, size=13,
               note="Una sola copia con CRC detecta la corrupción, pero no la repara: sin la copia anterior no hay a qué volver. La alternancia de dos copias convierte cualquier corte en «antigua o nueva». Modelo de escritura byte a byte; una flash real programa páginas y puede dejar bits a medias.",
               note_kind="teal", foot=SINT)


def se275_amfe() -> Fig:
    items = [
        ("Se conserva el mismo primer modo de fallo", 86.3, "gold", "86,3 %"),
        ("Se conservan los mismos tres peores modos", 27.2, "coral", "27,2 %"),
        ("Correlación de rangos media (×100)", 83.4, "gold", "0,834"),
    ]
    return bars("Estabilidad de un AMFE de 12 modos de fallo si dos evaluadoras difieren en ±1 punto",
                "Barras: al perturbar cada puntuación de gravedad, ocurrencia y detección en más o menos un punto en 2000 repeticiones, el primer modo de fallo se conserva el 86,3 por ciento de las veces, el conjunto de los tres peores solo el 27,2 y la correlación de rangos media es 0,834, con un mínimo de 0,427.",
                items, 5, "El número de prioridad de riesgo mezcla tres escalas ordinales: un punto de desacuerdo mueve el ranking. Sirve para empezar una conversación, no para ordenar con precisión. Las puntuaciones de los doce modos son sintéticas, con semilla fija.",
                label_w=470, width=1010, note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-276
def se276_mes() -> Fig:
    rows = [
        ["Básico (sin vigilancia, sin cola, sobrescribe)", "86,3 %", "51,5", "22"],
        ["Con temporizador de vigilancia", "91,8 %", "9,5", "20"],
        ["Y cola de almacenar y reenviar", "98,6 %", "9,5", "20"],
        ["Y dos ranuras con reversión", "99,9 %", "0,1", "0"],
    ]
    return tab("Un mes de 1000 dispositivos simulados con cortes de red, cuelgues y una actualización",
               "Tabla: en un mes simulado con cortes de red, cuelgues y una actualización el día 10, un dispositivo básico entrega el 86,3 por ciento de los datos esperados con 51,5 horas fuera de servicio y deja 22 de 1000 inutilizados; con vigilancia, cola y dos ranuras entrega el 99,9 por ciento con 0,1 horas y ninguno inutilizado.",
               ["Configuración", "Datos recibidos", "Horas fuera de servicio", "Inutilizados de 1000"], rows, [450, 190, 250, 200], row_h=48, size=13,
               note="Cada mecanismo cura un problema distinto: la vigilancia el tiempo caído, la cola los datos perdidos, las dos ranuras los dispositivos inutilizados. Probabilidades de cuelgue, cortes y fallo de actualización supuestas por el autor; no se simuló ningún componente real.",
               note_kind="teal", foot=SINT)


def se276_validador() -> Fig:
    rows = [
        ["Campo ausente", "17 de 17"],
        ["Sin identidad individual", "12 de 12"],
        ["Sin plan de reversión", "12 de 12"],
        ["Sin rotación con plazo", "15 de 15"],
        ["Reintentos sin jitter", "25 de 25"],
        ["Despliegue sin etapas", "20 de 20"],
        ["Fecha de revisión sin formato", "17 de 17"],
        ["Responsable colectivo", "24 de 24"],
        ["Plazo del temporizador menor que la operación más larga", "0 de 15"],
        ["Etapas de despliegue en orden inverso", "0 de 16"],
        ["Umbral invertido (40 a 5 °C)", "0 de 17"],
        ["Clave maestra almacenada en el dispositivo", "0 de 10"],
    ]
    return tab("Validador de paquetes de dispositivo sobre 200 mutaciones: 142 detectadas",
               "Tabla: un verificador de forma detecta 142 de 200 mutaciones de un paquete de dispositivo y ninguna de las 58 que cambian el sentido: un plazo de vigilancia menor que la operación más larga, etapas de despliegue en orden inverso, un umbral invertido o una clave maestra almacenada en el dispositivo.",
               ["Mutación", "Detectadas"], rows, [640, 200], row_h=32, size=12,
               note="Las cuatro mutaciones que no ve son justo las que rompen el dispositivo: tienen forma correcta y sentido contrario. Las reglas se escribieron conociendo las mutaciones, así que el 100 % por tipo es optimista.",
               note_kind="gold", foot=SINT)


def se276_flota() -> Fig:
    rows = [
        ["Publicar a todos el día 1", "30,0", "30,0", "1", "0 %"],
        ["Etapas sin reversión automática", "18,0", "18,0", "7,7", "44,2 %"],
        ["Etapas con reversión y umbral de 3 informes", "18,0", "1,8", "7,7", "44,2 %"],
    ]
    return tab("Mil dispositivos y una versión defectuosa (3 % fallan; informe con probabilidad 0,9)",
               "Tabla: con una versión defectuosa que daña al 3 por ciento de 1000 dispositivos, publicar a todos daña 30 sin posibilidad de detenerse, las etapas dañan 18 y detienen el despliegue a tiempo en el 44,2 por ciento, y con reversión automática solo 1,8 dispositivos siguen dañados al final.",
               ["Estrategia", "Dañados", "Siguen dañados", "Días", "Detenidos a tiempo"], rows, [430, 130, 190, 90, 220], row_h=48, size=13,
               note="Las etapas reducen el daño inicial; la reversión lo repara. Con el 3 % de fallo, 55,8 % de los despliegues llegan a toda la flota antes de detectar el problema, porque la primera etapa de 10 dispositivos espera 0,3 fallos. 2000 despliegues; la reparación al 90 % es un supuesto.",
               note_kind="teal", foot=SINT)


FIGURES = {
    "se-271-cortes-de-energia-en-una-actualizacion.svg": se271_cortes,
    "se-271-actualizacion-diferencial.svg": se271_delta,
    "se-271-despliegue-por-etapas.svg": se271_etapas,
    "se-272-claves-extraidas-de-una-flota.svg": se272_radio,
    "se-272-ventana-de-tiempo-y-desfase.svg": se272_reloj,
    "se-272-semillas-debiles.svg": se272_semilla,
    "se-273-estrategias-de-reporte.svg": se273_reporte,
    "se-273-decision-local-o-en-la-nube.svg": se273_plazo,
    "se-273-codificacion-de-la-carga.svg": se273_carga,
    "se-274-votacion-y-causa-comun.svg": se274_voto,
    "se-274-plazo-de-vigilancia.svg": se274_vigilancia,
    "se-274-vuelta-del-contador.svg": se274_vuelta,
    "se-275-inyeccion-de-fallos.svg": se275_inyeccion,
    "se-275-corte-durante-la-escritura.svg": se275_escritura,
    "se-275-estabilidad-de-un-amfe.svg": se275_amfe,
    "se-276-un-mes-de-flota-simulada.svg": se276_mes,
    "se-276-validador-de-paquetes.svg": se276_validador,
    "se-276-flota-y-version-defectuosa.svg": se276_flota,
}
