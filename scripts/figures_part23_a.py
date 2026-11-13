"""Figures for SE-277 to SE-280 (synthetic simulations, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Simulación sintética con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-277
def se277_orden() -> Fig:
    rows = [
        ["Suma ingenua, 1000 órdenes aleatorios", "205", "mediana 6,4·10⁻⁶; máximo 4,4·10⁻⁵"],
        ["Suma ingenua ordenada por magnitud", "1", "0 en esta muestra"],
        ["Suma por pares (recursiva)", "1", "2,4·10⁻⁷"],
        ["math.fsum (referencia exacta)", "1", "—"],
    ]
    return tab("Sumar 20 000 números de magnitudes muy distintas: el orden cambia el resultado",
               "Tabla: al sumar veinte mil números de magnitudes entre diez a la menos seis y diez a la ocho en mil órdenes aleatorios, la suma ingenua da 205 resultados distintos con un error mediano de 6,4 por diez a la menos seis; ordenada por magnitud o por pares da un solo resultado.",
               ["Estrategia", "Resultados distintos", "Error absoluto frente a fsum"], rows, [400, 190, 340], row_h=44, size=13,
               note="Sumar en coma flotante no es asociativo: el mismo conjunto de datos produce 205 totales distintos según el orden en que lo recorre un procesador, un hilo o una partición. Cambiar el número de núcleos puede cambiar la última cifra publicada. El error absoluto es pequeño frente a un total de unos 2·10⁹, pero basta para que una comparación exacta entre ejecuciones falle.",
               note_kind="gold", foot=SINT)


def se277_semillas() -> Fig:
    rows = [
        ["1 000", "0,0490", "15,0 %", "2,988 a 3,292"],
        ["10 000", "0,0161", "46,5 %", "3,090 a 3,183"],
        ["100 000", "0,0048", "95,5 %", "3,128 a 3,158"],
    ]
    return tab("Estimar π con 200 semillas: lo que una sola ejecución no dice",
               "Tabla: con mil puntos la desviación de la estimación de pi entre doscientas semillas es 0,049 y solo el 15 por ciento queda a menos de 0,01 del valor; con cien mil puntos la desviación es 0,0048 y el 95,5 por ciento queda dentro de 0,01.",
               ["Puntos por ejecución", "Desviación entre semillas", "Dentro de ±0,01 de π", "Rango observado"], rows, [220, 260, 240, 220], row_h=44, size=13,
               note="Con una semilla fija la misma ejecución da siempre el mismo número, y eso es reproducibilidad exacta. No es evidencia de que el resultado sea estable: con mil puntos, otra semilla da cualquier valor entre 2,99 y 3,29. Publicar la semilla permite repetir; variar las semillas permite saber cuánto vale la cifra.",
               note_kind="teal", foot=SINT)


def se277_caos() -> Fig:
    rows = [
        ["10⁻⁶", "23", "20 a 29"],
        ["10⁻⁹", "37", "33 a 45"],
        ["10⁻¹²", "50", "46 a 59"],
        ["10⁻¹⁵", "65", "59 a 75"],
        ["Control estable (r = 2,8), 10⁻¹²", "no diverge en 500", "—"],
    ]
    return tab("Pasos hasta que dos trayectorias casi idénticas se separan en 0,1 (mapa logístico, r = 3,9)",
               "Tabla: en un mapa logístico caótico, dos trayectorias con diferencia inicial de diez a la menos seis se separan en 23 pasos de mediana y con diferencia de diez a la menos quince en 65; en un régimen estable la diferencia no crece en quinientos pasos.",
               ["Diferencia inicial", "Pasos hasta separarse (mediana)", "Percentiles 10 a 90"], rows, [380, 290, 240], row_h=44, size=13,
               note="Cada mil millonésima de diferencia compra apenas unos 14 pasos: la divergencia crece de forma exponencial, así que mejorar la precisión de la máquina retrasa el desacuerdo pero no lo elimina. Si el modelo es caótico, reproducir bit a bit una trayectoria larga en otra plataforma no es un objetivo realista; hay que reproducir estadísticos.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-278
def se278_reintentos() -> Fig:
    rows = [
        ["0 %", "10 000 (0)", "10 000"],
        ["5 %", "10 442 (442)", "10 000"],
        ["20 %", "10 867 (867)", "10 000"],
    ]
    return tab("Cargar 10 000 filas en lotes de 100 con fallos a mitad de lote y reintentos",
               "Tabla: al reintentar lotes que fallaron a la mitad, añadir al final deja 10442 filas con 442 duplicadas si falla el 5 por ciento de los lotes y 10867 con 867 duplicadas si falla el 20 por ciento; escribir por clave deja siempre 10000 filas.",
               ["Lotes que fallan", "Añadir al final: filas (duplicadas)", "Escribir por clave (upsert)"], rows, [220, 400, 300], row_h=44, size=13,
               note="El reintento es correcto solo si repetir la escritura no cambia el resultado. Añadir al final no es repetible: cada reintento duplica lo que ya se había escrito antes del corte. La escritura por clave es idempotente. Simulación con cortes en un punto aleatorio del lote y hasta diez intentos.",
               note_kind="coral", foot=SINT)


def se278_tardios() -> Fig:
    items = [
        ("Espera de 5 s", 50.17, "coral", "50,2 % descartado"),
        ("15 s", 13.57, "coral", "13,6 %"),
        ("30 s", 3.55, "gold", "3,6 %"),
        ("60 s", 0.66, "gold", "0,66 %"),
        ("120 s", 0.06, "teal", "0,06 %"),
        ("300 s", 0.0, "teal", "0 %"),
    ]
    return bars("Eventos que llegan después de cerrar su ventana según la tolerancia de retraso",
                "Barras: con retraso lognormal de mediana 5 segundos, una tolerancia de 5 segundos descarta el 50,2 por ciento de los eventos, 15 segundos el 13,6, 30 segundos el 3,6, 60 segundos el 0,66, 120 segundos el 0,06 y 300 segundos ninguno.",
                items, 11, "Retraso de llegada lognormal (mediana 5 s, p99 51 s, máximo 351 s) sobre 100 000 eventos. Cada tolerancia compra completitud a costa de latencia: esperar 120 s deja los resultados abiertos dos minutos. El 0 % exacto depende de esta muestra, no de la física.",
                label_w=190, width=960, note_kind="gold", foot=SINT)


def se278_sesgo() -> Fig:
    rows = [
        ["0,0 (uniforme)", "1,01", "1,01"],
        ["0,8", "1,35", "1,01"],
        ["1,1", "2,03", "1,01"],
        ["1,5", "3,43", "1,01"],
    ]
    return tab("Carga de la partición más cargada frente a la media (8 particiones, 200 000 filas, 1 000 claves)",
               "Tabla: con claves repartidas de forma uniforme la partición más cargada tiene 1,01 veces la media; con una distribución de Zipf de exponente 1,1 tiene 2,03 veces y con 1,5 tiene 3,43; añadir un sufijo aleatorio a la clave la devuelve a 1,01.",
               ["Exponente de Zipf", "Máxima / media sin sal", "Máxima / media con sal de 8"], rows, [250, 340, 340], row_h=44, size=13,
               note="El reparto por clave es equilibrado solo si las claves lo son: una sola partición con 3,4 veces la media fija el tiempo total del trabajo. Salar la clave reparte la carga a cambio de un paso más para recombinar los resultados parciales. Las claves y los exponentes son sintéticos.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-279
def se279_fuga() -> Fig:
    rows = [
        ["Señal real (x), sin fuga", "0,742", "0,755"],
        ["Copia ruidosa de la etiqueta (z), con fuga", "0,899", "0,515"],
    ]
    return tab("Exactitud de un umbral sobre una variable con y sin fuga de la etiqueta (4 000 casos por conjunto)",
               "Tabla: un clasificador por umbral sobre la señal real obtiene 0,742 en prueba y 0,755 en producción; sobre una variable que es una copia ruidosa de la etiqueta obtiene 0,899 en prueba pero 0,515 en producción, donde esa copia no existe.",
               ["Variable usada", "Exactitud en prueba", "Exactitud en producción"], rows, [430, 230, 270], row_h=48, size=13,
               note="La métrica de prueba subió 16 puntos justo cuando el modelo dejó de aprender el fenómeno y empezó a leer la respuesta. Una exactitud sorprendentemente alta es una pista para buscar fuga, no para celebrar. La fuga se detecta preguntando, variable por variable, si existiría en el momento de predecir.",
               note_kind="coral", foot=SINT)


def se279_prevalencia() -> Fig:
    rows = [
        ["50 %", "0,925", "0,947", "0,500"],
        ["10 %", "0,945", "0,667", "0,900"],
        ["1 %", "0,950", "0,154", "0,990"],
        ["0,1 %", "0,950", "0,018", "0,999"],
    ]
    return tab("Un detector con sensibilidad 0,90 y especificidad 0,95 según la prevalencia del evento",
               "Tabla: con sensibilidad 0,90 y especificidad 0,95 la exactitud casi no cambia con la prevalencia, pero el valor predictivo positivo baja de 0,947 con prevalencia del 50 por ciento a 0,154 con el 1 por ciento y 0,018 con el 0,1 por ciento; responder siempre no obtiene 0,99 de exactitud con el 1 por ciento.",
               ["Prevalencia", "Exactitud", "De cada aviso, proporción real", "Exactitud de «siempre no»"], rows, [190, 190, 330, 260], row_h=48, size=13,
               note="Con el 1 % de casos, 85 de cada 100 avisos son falsos aunque el detector parezca bueno (0,95 de exactitud). Y la regla que nunca avisa saca 0,99. La exactitud no sirve con eventos raros: hay que reportar sensibilidad, valor predictivo y coste de cada tipo de error. Comprobado con 500 000 casos simulados.",
               note_kind="gold", foot=SINT)


def se279_deriva() -> Fig:
    rows = [
        ["0,0 (sin cambio)", "4 %", "0 %", "0 %"],
        ["0,1", "6 %", "0 %", "0 %"],
        ["0,3", "37 %", "0 %", "0 %"],
        ["0,5", "92 %", "92 %", "100 %"],
    ]
    return tab("Alarmas de deriva (PSI > 0,2) según el desplazamiento de la media y el tamaño de la ventana",
               "Tabla: con ventanas de 100 observaciones la alarma de deriva suena el 4 por ciento de las veces sin cambio y el 37 por ciento con un desplazamiento de 0,3 desviaciones; con ventanas de 500 o 5000 no suena con ese desplazamiento y suena el 92 y el 100 por ciento con 0,5.",
               ["Desplazamiento (desviaciones típicas)", "Ventana de 100", "Ventana de 500", "Ventana de 5 000"], rows, [310, 200, 200, 210], row_h=44, size=13,
               note="Con ventanas pequeñas el índice se infla por azar: a 0,3 desviaciones la alarma de n = 100 suena 37 veces de 100 y la de n ≥ 500 ninguna, porque el valor real del índice (alrededor de 0,09) queda bajo el umbral. El umbral de 0,2 es una convención, no una ley; 200 ventanas por celda.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-280
def se280_determinismo() -> Fig:
    rows = [
        ["Paso variable, 30 fps medios", "0,0637", "1,4·10⁻²"],
        ["Paso variable, 60 fps medios", "0,0687", "9,1·10⁻³"],
        ["Paso variable, 144 fps medios", "0,0744", "3,4·10⁻³"],
        ["Paso fijo de 1/60 s", "0,0697", "8,1·10⁻³"],
        ["Referencia (paso de 1/10 000 s)", "0,0778", "—"],
    ]
    return tab("Posición de un resorte amortiguado a los 10 s según la política de paso de tiempo",
               "Tabla: la posición de un resorte tras diez segundos es 0,0637, 0,0687 y 0,0744 con paso variable a 30, 60 y 144 fotogramas por segundo, 0,0697 con paso fijo de 1/60 y 0,0778 de referencia; con paso variable cada una de 20 ejecuciones da un resultado distinto y con paso fijo todas dan el mismo.",
               ["Política de paso", "Posición a los 10 s", "Error frente a la referencia"], rows, [430, 250, 250], row_h=44, size=13,
               note="El paso variable no es necesariamente menos exacto en una corrida: es irrepetible. Con una fluctuación del 25 % en el tiempo de cada fotograma, 20 ejecuciones dieron 20 resultados distintos; con paso fijo, uno. Reproducir un fallo, grabar una repetición o sincronizar una partida exige el paso fijo.",
               note_kind="gold", foot=SINT)


def se280_tunel() -> Fig:
    rows = [
        ["5", "0,08", "8,2 %", "8,2 %"],
        ["12", "0,20", "20,5 %", "20,5 %"],
        ["30", "0,50", "19,2 %", "49,4 %"],
        ["60", "1,00", "20,0 %", "100 %"],
        ["120", "2,00", "0 %", "100 %"],
    ]
    return tab("Una bala contra una pared de 0,2 unidades de grosor: choques detectados por la prueba discreta y por la barrida",
               "Tabla: con velocidad 5 y 12 unidades por segundo ambos métodos detectan el mismo porcentaje de choques; a 30 la prueba discreta detecta el 19,2 por ciento y la barrida el 49,4; a 60 detecta el 20 y la barrida el 100; a 120 la discreta no detecta ninguno.",
               ["Velocidad (u/s)", "Paso por fotograma (u)", "Prueba discreta", "Prueba barrida"], rows, [220, 280, 220, 220], row_h=44, size=13,
               note="Cuando el desplazamiento por fotograma supera el grosor de la pared, la bala aparece a un lado y luego al otro sin estar nunca dentro: el choque desaparece. La prueba barrida revisa el segmento recorrido. Mide cada trayectoria de tres lados: pared, bala y paso del fotograma. 2 000 lanzamientos por celda.",
               note_kind="coral", foot=SINT)


def se280_espiral() -> Fig:
    rows = [
        ["4", "59,9 · 18", "59,9 · 18 · 1,00"],
        ["12", "52,4 · 122", "52,5 · 122 · 1,00"],
        ["15", "18,7 · 302", "26,7 · 167 · 0,98"],
        ["17", "1,0 · 5 357", "10,9 · 189 · 0,90"],
        ["20", "0,5 · 13 322", "9,3 · 282 · 0,77"],
    ]
    return tab("Espiral de la muerte: coste de cada actualización fija de 16,7 ms (fotogramas por segundo · peor fotograma en ms)",
               "Tabla: con actualizaciones de 4 milisegundos el juego sostiene 60 fotogramas por segundo; con 17 milisegundos, más que el paso de 16,7, sin tope de pasos cae a 1 fotograma por segundo con un fotograma de 5357 milisegundos y con un tope de 5 pasos sostiene 10,9 fotogramas por segundo con el juego al 90 por ciento de la velocidad.",
               ["Coste de una actualización (ms)", "Sin tope de pasos", "Tope de 5 pasos (fps · peor · juego/real)"], rows, [270, 290, 370], row_h=44, size=13,
               note="Si actualizar cuesta más que el paso, cada fotograma debe recuperar más pasos, tarda más, acumula más tiempo y el sistema colapsa. El tope de pasos evita el bloqueo a cambio de que el juego corra más lento que el reloj (0,90 a 17 ms). Picos del 2 % con coste cuádruple; 60 s simulados.",
               note_kind="coral", foot=SINT)


FIGURES = {
    "se-277-orden-de-la-suma.svg": se277_orden,
    "se-277-semillas-y-repeticiones.svg": se277_semillas,
    "se-277-horizonte-del-caos.svg": se277_caos,
    "se-278-reintentos-y-duplicados.svg": se278_reintentos,
    "se-278-eventos-tardios.svg": se278_tardios,
    "se-278-asimetria-de-claves.svg": se278_sesgo,
    "se-279-fuga-de-la-etiqueta.svg": se279_fuga,
    "se-279-prevalencia-y-avisos.svg": se279_prevalencia,
    "se-279-alarmas-de-deriva.svg": se279_deriva,
    "se-280-paso-de-tiempo-fijo.svg": se280_determinismo,
    "se-280-atravesar-la-pared.svg": se280_tunel,
    "se-280-espiral-de-la-muerte.svg": se280_espiral,
}
