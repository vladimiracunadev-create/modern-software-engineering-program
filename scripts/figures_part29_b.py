"""Figures for SE-355 to SE-360 (synthetic models with fixed seeds; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig, dumbbell, fmt_exact, grouped_bars, heatmap, line_chart, percentile_intervals, scatter, stacked_bars
from figures_part07_a import bars
from figures_part40_a import flow

SINT = "Modelo sintético con semilla fija; Windows y Ubuntu (WSL2) con cifras idénticas. Los parámetros son supuestos del autor."


# ---------------------------------------------------------------- SE-355
def se355_radio() -> Fig:
    return scatter(
        "Un error cometido en desarrollo o preproducción (20 000 ensayos): ¿llega a producción y cuánto daña?",
        "Dispersión con tres estructuras de cuentas, con el porcentaje de errores que tocan producción en el eje vertical y los recursos afectados por error en el horizontal: una sola cuenta, 5,54 por ciento y 2,28 recursos; una cuenta por entorno, 0 y 1,39; una por entorno y servicio, 0 y 1,06. Separar cuentas baja ambos.",
        [("Una sola cuenta", [(2.28, 5.54, "5,54 %", "l")], "coral"),
         ("Una cuenta por entorno", [(1.39, 0, "0 %", "t")], "gold"),
         ("Una cuenta por entorno y servicio", [(1.06, 0, "0 %", "t")], "teal")],
        x_label="Recursos afectados por error (media)", y_label="Errores que tocan producción (%)",
        x_ticks=[(1, "1,0"), (1.5, "1,5"), (2, "2,0"), (2.5, "2,5")], y_ticks=[0, 2, 4, 6], y_zero=True, point_labels="none",
        note="La frontera de la cuenta no evita el error, acota su alcance: con una cuenta por entorno el comodín destruye más en desarrollo, pero ya no cruza. Los 24 recursos (3 entornos, 4 servicios, 2 clases), el 5 % de acciones comodín y la intención uniforme son supuestos del autor.",
        note_kind="teal", foot=SINT)


def se355_divergencia() -> Fig:
    return line_chart(
        "Semanas con divergencia entre preproducción y producción en 52 semanas, según las ediciones manuales por semana",
        "Líneas con las semanas con divergencia de 52 según las ediciones manuales por semana (0,1, 0,3 y 0,6): sin promoción son 38,0, 48,3 y 50,5; con una promoción que copia la configuración cada 4 semanas son 5,0, 13,7 y 24,1. Sin promoción, además, quedan 3,34, 9,32 y 17,39 claves distintas al final; con ella, 0.",
        [("Sin promoción", [(0.1, 38.0, "38,0", "t"), (0.3, 48.3, "48,3", "t"), (0.6, 50.5, "50,5", "t")], "coral"),
         ("Con promoción cada 4 semanas", [(0.1, 5.0, "5,0", "t"), (0.3, 13.7, "13,7", "t"), (0.6, 24.1, "24,1", "t")], "teal")],
        x_label="Ediciones manuales por semana", y_label="Semanas con divergencia (de 52)",
        x_ticks=[(0.1, "0,1"), (0.3, "0,3"), (0.6, "0,6")], y_ticks=[0, 13, 26, 39, 52], hlines=[(52, "52 semanas: todo el año")], point_labels="none",
        note="La promoción no impide la divergencia, la acota en el tiempo: dura hasta la siguiente copia. Sin ella las diferencias se acumulan, la probabilidad de la edición manual es un supuesto del autor, y la experiencia de «en preproducción funcionaba» deja de significar nada tras unas semanas.",
        note_kind="gold", foot=SINT)


def se355_toxicas() -> Fig:
    items = [
        ("1 rol", 27.1, "teal", "27,1 %"),
        ("2 roles", 61.8, "gold", "61,8 %"),
        ("3 roles", 82.7, "coral", "82,7 %"),
        ("4 roles", 92.3, "coral", "92,3 %"),
    ]
    return bars("Personas con una combinación tóxica de permisos según cuántos roles se les asignan (40 roles, 6 pares prohibidos)",
                "Barras: con 40 roles de 2 a 4 permisos entre 12 y seis pares de permisos incompatibles, el 27,1 por ciento de las personas con un solo rol ya tiene una combinación tóxica; con dos roles el 61,8, con tres el 82,7 y con cuatro el 92,3.",
                items, 7.5, "Once de los 40 roles ya contienen un par tóxico dentro de sí mismos; los demás se vuelven tóxicos al sumarse. Revisar cada rol por separado no detecta el problema: el riesgo está en la unión de los roles de una persona. Los 12 permisos, los 6 pares y los 40 roles son sintéticos.",
                label_w=120, width=900, note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-356
def se356_politicas() -> Fig:
    return scatter(
        "Siete días de tráfico con picos: demanda sin atender frente a instancias-hora, según la política",
        "Dispersión con seis políticas de escalado, con las instancias-hora en el eje horizontal y el porcentaje de demanda sin atender en el vertical: 12 instancias fijas, 2 016 y 1,64; 30 fijas, 5 040 y 0; reactivo inmediato, 1 910 y 0; reactivo con arranque de 2 y 5 minutos, 1 866 y 0,34 y 1 813 y 0,84; programado, 1 762 y 1,85. Reservar para el pico cuesta 2,6 veces más.",
        [("Fijo", [(2016, 1.64, "12 fijas", "r"), (5040, 0, "30 fijas", "t")], "coral"),
         ("Reactivo", [(1910, 0, "Inmediato", "r"), (1866, 0.34, "2 min", "l"), (1813, 0.84, "5 min", "l")], "teal"),
         ("Programado", [(1762, 1.85, "Programado", "t")], "gold")],
        x_label="Instancias-hora en siete días", y_label="Demanda sin atender (%)",
        x_ticks=[(1500, "1 500"), (2500, "2 500"), (3500, "3 500"), (4500, "4 500"), (5500, "5 500")], y_ticks=[0, 0.5, 1.0, 1.5, 2.0], y_zero=True, point_labels="none",
        note="El arranque tarda y eso se paga en demanda perdida: cada minuto de retardo añade unos 0,17 puntos porcentuales de demanda perdida en este tráfico. Reservar para el peor pico cuesta 2,6 veces más que escalar con reacción. Capacidad de 20 solicitudes por segundo por instancia, objetivo del 60 % y picos de 2,5 a 4 veces son supuestos del autor.",
        note_kind="gold", foot=SINT)


def se356_cola() -> Fig:
    return line_chart(
        "Una cola de un servidor: tiempo en el sistema según la utilización, en unidades del tiempo de servicio",
        "Líneas con el tiempo medio y el percentil 99 en el sistema, en unidades del tiempo de servicio, según la utilización del 50, 70, 80, 90 y 95 por ciento: la media simulada va de 2,00 a 20,7 y el percentil 99 de 9,3 a 103; las curvas teóricas (2 a 20 y 9,2 a 92) casi las cubren. El tiempo se dispara pasado el 80 por ciento.",
        [("Media simulada", [(50, 2.00, "", "t"), (70, 3.35, "", "t"), (80, 5.07, "5,07", "t"), (90, 10.1, "10,1", "t"), (95, 20.7, "20,7", "t")], "teal"),
         ("Media teórica", [(50, 2.0, "", "t"), (70, 3.33, "", "t"), (80, 5.0, "", "t"), (90, 10.0, "", "t"), (95, 20.0, "", "t")], "navy"),
         ("Percentil 99 simulado", [(50, 9.3, "9,3", "t"), (70, 15.6, "15,6", "t"), (80, 23.7, "23,7", "t"), (90, 48.3, "48,3", "t"), (95, 103, "103", "l")], "coral"),
         ("Percentil 99 teórico", [(50, 9.2, "", "t"), (70, 15.4, "", "t"), (80, 23.0, "", "t"), (90, 46.1, "", "t"), (95, 92, "", "t")], "gold")],
        x_label="Utilización del servidor (%)", y_label="Tiempo en el sistema (veces el de servicio)",
        x_ticks=[(50, "50"), (70, "70"), (80, "80"), (90, "90"), (95, "95")], y_ticks=[0, 25, 50, 75, 100, 125], point_labels="none",
        note="De 80 a 95 % de utilización el tiempo medio se cuadruplica: ese es el codo que el escalado debe evitar. La simulación de 200 000 clientes de Poisson con servicio exponencial coincide con la fórmula 1 ÷ (μ − λ); no representa colas con ráfagas, prioridades ni varios servidores.",
        note_kind="coral", foot=SINT)


def se356_compromiso() -> Fig:
    items = [
        ("Todo bajo demanda", 1124.0, "gold", "1 124 (0 comprometidas)"),
        ("Compromiso de 4", 862.0, "teal", "862"),
        ("Compromiso de 7 (mediana)", 854.0, "teal", "854 (el mínimo)"),
        ("Compromiso de 9", 943.0, "gold", "943"),
        ("Compromiso de 14", 1426.0, "coral", "1 426"),
        ("Compromiso de 30 (el máximo)", 3024.0, "coral", "3 024"),
    ]
    return bars("Coste de siete días de demanda según cuántas instancias se compromete (precio comprometido 0,6; bajo demanda 1,0)",
                "Barras: pagar todo bajo demanda cuesta 1 124 unidades; comprometer 4 instancias baja a 862, 7 (la mediana de lo necesario) a 854, el mínimo; 9 sube a 943, 14 a 1 426 y 30, el máximo, a 3 024.",
                items, 0.2, "El compromiso óptimo está en torno a la mediana de la demanda, no en el promedio ni en el máximo: comprometer de más cuesta más que no comprometer. Los precios son unidades inventadas con una rebaja del 40 %; no son tarifas de ningún proveedor, y el óptimo depende de que el patrón se repita durante la duración del compromiso.",
                label_w=290, width=960, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-357
def se357_disponibilidad() -> Fig:
    return grouped_bars(
        "Minutos de caída al año al combinar dos proveedores que fallan de forma independiente",
        "Barras horizontales en escala logarítmica con los minutos de caída al año: un proveedor de 99,95 por ciento pierde 262,8; dos con conmutación perfecta, 0,1; dos con conmutación que acierta el 90 por ciento, 26,4; dos con un DNS compartido de 99,95 por ciento, 262,9; dos exigiendo ambos a la vez, 525,5.",
        ["Un proveedor (99,95 %)", "Dos, conmutación perfecta (99,99998 %)", "Dos, conmutación acierta el 90 % (99,995 %)", "Dos con un DNS compartido (99,95 %)", "Dos, exigiendo ambos a la vez (99,90 %)"],
        [("Minutos de caída al año", [262.8, 0.1, 26.4, 262.9, 525.5], "coral")],
        unit="Minutos de caída al año", horizontal=True, log=True, ticks=[0.1, 1, 10, 100, 1000], label_w=330,
        note="Redundancia en paralelo ayuda mucho solo si la conmutación funciona y nada se comparte; una dependencia en serie con el mismo 99,95 % anula el beneficio, y exigir ambos lo empeora al doble. El cálculo se verificó con 35 millones de horas simuladas. La independencia de fallos y los 99,95 % son supuestos del autor, no medidas de un proveedor.",
        note_kind="coral", foot=SINT)


def se357_interseccion() -> Fig:
    return dumbbell(
        "Funciones que ofrecen a la vez tres proveedores ficticios, frente a las que ofrece cada uno (media de 2 000 sorteos)",
        "Mancuernas con las funciones que ofrece cada proveedor y las que ofrecen los tres a la vez: de 20 básicas, 18 y 14,6; de 20 avanzadas, 12 y 4,3; de las 40, 30 y 18,8. La intersección pierde más en las avanzadas, donde cae de 12 a 4,3.",
        [("20 funciones básicas", 18, 14.6), ("20 funciones avanzadas", 12, 4.3), ("Las 40 funciones", 30, 18.8)],
        unit="Funciones (de 20 o de 40)", names=("Cada proveedor ofrece", "Los tres a la vez"), lower_is_better=False, label_w=220,
        note="El mínimo común denominador se lleva más de la mitad de las funciones: 21 de 40 quedan fuera por no estar en alguno. Portabilidad total sale a costa de no usar lo que justificó elegir el proveedor. Probar las 40 en cada uno son 120 casos frente a 56 si se limita a lo común. Los proveedores son ficticios y las probabilidades supuestos del autor; no se comparó ninguna oferta real.",
        note_kind="gold", foot=SINT)


def se357_gravedad() -> Fig:
    return line_chart(
        "Tiempo de mover datos entre proveedores según el volumen y el enlace (70 % de eficiencia)",
        "Líneas en escala logarítmica con las horas para mover 0,1, 1, 10 y 100 terabytes: por un enlace de 100 megabits por segundo, 3,2, 31,7, 317,5 y 3 175 horas; por uno de 1 gigabit, 0,3, 3,2, 31,7 y 317,5. La línea de un día queda superada a partir de 1 terabyte con 100 megabits. El coste de salida crece de 8 a 8 000 unidades.",
        [("Enlace de 100 Mbps", [(0.1, 3.2, "3,2", "t"), (1, 31.7, "31,7", "t"), (10, 317.5, "317,5", "t"), (100, 3175, "3 175", "l")], "coral"),
         ("Enlace de 1 Gbps", [(0.1, 0.3, "0,3", "b"), (1, 3.2, "3,2", "b"), (10, 31.7, "31,7", "b"), (100, 317.5, "317,5", "b")], "teal")],
        x_label="Volumen a mover (TB)", y_label="Horas para moverlo",
        x_ticks=[(0.1, "0,1"), (1, "1"), (10, "10"), (100, "100")], log_x=True, log_y=True, hlines=[(24, "1 día")], point_labels="none",
        note="Los datos no se mueven tan rápido como el código: 100 TB tardan 13 días incluso a 1 Gbps. Además la luz limita la latencia: 8 000 km imponen al menos 80 ms de ida y vuelta por la fibra, 20 ms con 2 000 km. El coste de salida (8, 80, 800 y 8 000 unidades) está en la tabla; el precio de 0,08 por GB es una unidad inventada y la eficiencia del 70 % un supuesto.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-358
def se358_camino() -> Fig:
    return percentile_intervals(
        "Crear un primer servicio listo para producción: horas hasta terminar, mediana y percentil 90 (20 000 ensayos por fila)",
        "Intervalos con la mediana y el percentil 90 de las horas hasta crear el servicio: a mano con 23 pasos y 2 por ciento de error por paso, 5,5 y 6,8 horas y el 62,6 por ciento sin retrabajo; camino dorado de 5 pasos con 2 por ciento, 0,28 y 0,50 horas y 90,5 por ciento; con 1 por ciento, 0,28 y 0,40 horas y 95,0 por ciento.",
        [("A mano, 23 pasos, error 2 % (62,6 % sin retrabajo)", [5.5, 6.8]),
         ("Camino dorado, 5 pasos, error 2 % (90,5 %)", [0.28, 0.50]),
         ("Camino dorado, 5 pasos, error 1 % (95,0 %)", [0.28, 0.40])],
        unit="Horas hasta tener el servicio listo", marks=("Mediana", "Percentil 90"), label_w=330,
        note="El camino dorado gana porque tiene menos pasos que equivocarse, no porque las personas acierten más: lo que se elimina es la oportunidad de error. El porcentaje entre paréntesis es el éxito sin ningún error (62,8 % teórico para el manual). Los 23 y 5 pasos, el 2 % y los tiempos son supuestos del autor, no medidas de personas ni de un equipo real.",
        note_kind="teal", foot=SINT)


def se358_cola() -> Fig:
    return line_chart(
        "Equipo de plataforma de 4 personas y 100 servicios: espera por soporte según cuántos usan el camino dorado",
        "Líneas con la espera media y el percentil 90 de la espera por soporte, en días hábiles, según el porcentaje de servicios que usan el camino dorado: con 20 por ciento, 0,50 y 1,40; con 50, 0,06 y 0,23; con 80, 0,01 y 0,00; con 95, 0,00 y 0,00. El equipo pasa de trabajar al 83 por ciento a hacerlo al 19.",
        [("Espera media", [(20, 0.50, "0,50", "t"), (50, 0.06, "0,06", "t"), (80, 0.01, "0,01", "t"), (95, 0.0, "0,00", "t")], "teal"),
         ("Percentil 90", [(20, 1.40, "1,40", "t"), (50, 0.23, "0,23", "t"), (80, 0.0, "", "t"), (95, 0.0, "", "t")], "coral")],
        x_label="Servicios que usan el camino dorado (%)", y_label="Espera por soporte (días hábiles)",
        x_ticks=[(20, "20"), (50, "50"), (80, "80"), (95, "95")], y_ticks=[0, 0.5, 1.0, 1.5], point_labels="none",
        annotations=[(20, 1.40, "Con 20 %: 166 solicitudes al mes y el equipo al 83 %", 30, 8)],
        note="La espera no baja de forma lineal: de 20 a 50 % se divide por ocho y de 50 a 95 % ya es casi cero, porque el equipo sale de la zona de saturación (de 83 % a 58, 32 y 19 % de uso). Las 0,3 y 2,0 solicitudes por servicio al mes y el 0,4 días por solicitud son supuestos del autor.",
        note_kind="gold", foot=SINT)


def se358_verificador() -> Fig:
    return stacked_bars(
        "Un verificador de ocho reglas sobre 150 descriptores de servicio sintéticos: qué señala y qué no",
        "Barras apiladas horizontales al 100 por ciento: de 100 servicios generados desde la plantilla señala 5 con alguna violación y deja 95 sin señalar; de 50 escritos a mano señala 49 (135 violaciones) y deja 1; de 5 defectos semánticos, como un límite de 1 000 núcleos o una ruta de sonda inexistente, no señala ninguno.",
        ["Servicios de la plantilla (100)", "Servicios escritos a mano (50)", "Defectos semánticos (5)"],
        [("Señalados por el verificador", [5, 49, 0], "teal"), ("Sin señalar", [95, 1, 5], "grey")],
        unit="Elementos de cada conjunto", horizontal=True, percent=True, label_w=250, plot_h=200,
        note="Las ocho reglas detectaron las 25 mutaciones de cada una, y por eso el verificador es útil y a la vez ciego a lo que no es una regla. La plantilla no elimina las violaciones, las reduce al 4 % de ediciones manuales. Las 5 y 135 violaciones señaladas en los dos primeros conjuntos están en la tabla. Las reglas y los defectos los escribí yo: la exactitud sobre código real es desconocida.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-359
def se359_cortes() -> Fig:
    return heatmap(
        "Una creación de 12 recursos interrumpida en cada paso: restos sin rastro y conflictos al reintentar",
        "Mapa de calor con restos sin rastro y conflictos al reintentar según la estrategia de estado y el punto del corte: si el estado se guarda solo al final, 66 y 66 con corte antes de crear y 78 y 78 con corte tras crear y antes de anotar; si se guarda tras cada recurso, 0 y 0 y 12 y 12; con intención previa, 0 y 0, y 0 restos (12 sospechosos) y 12 conflictos.",
        ["Estado solo al final", "Estado tras cada recurso", "Intención antes, confirmación después"],
        ["Antes de crear: restos", "Antes de crear: conflictos", "Tras crear: restos", "Tras crear: conflictos"],
        [[66, 66, 78, 78], [0, 0, 12, 12], [0, 0, 0, 12]],
        unit="restos o conflictos", scale="coral", cell_fmt=fmt_exact, row_title="Estrategia", col_title="Punto del corte y qué se cuenta",
        highlight=[(2, 2)], label_w=230,
        note="Guardar el estado tras cada recurso elimina el caso fácil y deja el difícil: el recurso creado cuyo registro no llegó. Anotar la intención antes de crear lo vuelve un sospechoso que se puede reconciliar (el recuadro marca los 0 restos, pero con 12 sospechosos), aunque el reintento sigue chocando con él hasta que se reconcilia. Los recursos son carpetas locales, no recursos de una nube.",
        note_kind="coral", foot=SINT)


def se359_destruccion() -> Fig:
    return grouped_bars(
        "Destruir 12 recursos con dependencias: intentos rechazados y pasadas necesarias según el orden",
        "Barras agrupadas con los rechazos medios y las pasadas medias al destruir los 12 recursos: en un orden al azar (5 000 órdenes) son 13,73 rechazos y 3,88 pasadas; en el inverso del orden de dependencias, 0 rechazos y 1 pasada. Ningún orden al azar sale sin algún rechazo.",
        ["Rechazos medios", "Pasadas medias"],
        [("Orden al azar (5 000 órdenes)", [13.73, 3.88], "coral"), ("Inverso del orden de dependencias", [0, 1], "teal")],
        unit="Intentos rechazados o pasadas (media)", decimals=2, plot_h=260,
        note="Un bucle que reintenta hasta que no quede nada oculta el orden equivocado: termina, con casi cuatro pasadas y trece rechazos. Pero sin una señal de qué falló no se distingue ese caso de un recurso atascado. Con orden al azar el 0 % de las órdenes sale sin ningún rechazo; con el inverso, el 100 %. El grafo de 12 recursos y sus dependencias es del autor y la destrucción es de carpetas locales.",
        note_kind="gold", foot=SINT)


def se359_barrido() -> Fig:
    return stacked_bars(
        "Barrido por etiqueta de 12 recursos por entorno (2 000 entornos): entornos que quedan limpios",
        "Barras apiladas horizontales al 100 por ciento con los entornos limpios y los que dejan algún resto según el porcentaje de recursos etiquetados: con 100 por ciento, todos limpios; con 95 por ciento, 54,0 limpios y 46,0 con restos; con 80 por ciento, 7,3 y 92,7.",
        ["100 % de los recursos etiquetados", "95 % etiquetados", "80 % etiquetados"],
        [("Entornos sin restos", [100, 54.0, 7.3], "teal"), ("Entornos con algún resto", [0, 46.0, 92.7], "coral")],
        unit="Entornos", horizontal=True, percent=True, label_w=230, plot_h=200,
        note="Un barrido por etiqueta solo limpia lo que se dejó etiquetar: con un 95 % de cobertura casi la mitad de los entornos deja algo. Quedan 0, 0,61 y 2,42 restos por entorno, y 100 entornos cuestan 0, 915 y 3 630 unidades en 30 días (tabla). Al medio por día por resto, el coste de un resto olvidado es pequeño y el de un resto con datos o con una credencial no se mide en unidades. La cobertura y el coste son supuestos del autor.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-360
def se360_hashes() -> Fig:
    return flow(
        "SHA-256 del mismo paquete de 12 archivos construido en Windows y en Ubuntu, cada vez con más normalización",
        "Diagrama de cinco construcciones con los primeros 8 caracteres de la suma en Windows y en Ubuntu: sin normalizar, 0bc289f3 y 740aafa8; con fechas y orden fijos, cf351096 y 765d27f7; al fijar además el sistema que crea el archivo, ambas 765d27f7; con deflate de nivel 6 y de nivel 9, ambas c3d29a42. Coinciden la tercera, la cuarta y la quinta construcción.",
        [[("Sin normalizar, sin compresión. Windows 0bc289f3, Ubuntu 740aafa8: distintas", "coral"),
          ("Fechas y orden fijos. Windows cf351096, Ubuntu 765d27f7: distintas", "coral"),
          ("Además se fija el sistema que crea el archivo. Ambas 765d27f7: iguales", "teal")],
         [("Normalizado con deflate, nivel 6. Ambas c3d29a42: iguales", "teal"),
          ("Normalizado con deflate, nivel 9. Ambas c3d29a42: iguales", "teal")]],
        note="El campo «versión creada por» del formato ZIP dice 0 en Windows y 3 en Linux: un detalle invisible que cambia la suma. Con zlib 1.3.1 y 1.3 la compresión dio bytes idénticos para este contenido; no se garantiza con otro contenido ni otra versión de zlib. El paquete se generó con semilla, no con archivos del repositorio.",
        note_kind="gold", foot=SINT, box_h=96)


def se360_validador() -> Fig:
    return stacked_bars(
        "Un validador de paquetes frente a 208 mutaciones: las que detecta y las que no",
        "Barras apiladas horizontales con las mutaciones detectadas y no detectadas: de las 128 de ocho familias estructurales (sección faltante, módulo duplicado, hash alterado, secreto literal y otras) detecta las 128; de las 80 de cinco familias que exigen interpretar el contenido, como una prueba de destrucción caducada o un gasto muy superior al tope, no detecta ninguna.",
        ["Ocho familias estructurales (16 mutaciones cada una)", "Cinco familias de contenido (16 cada una)"],
        [("Detectadas", [128, 0], "teal"), ("No detectadas", [0, 80], "coral")],
        unit="Mutaciones sembradas", horizontal=True, label_w=270, plot_h=180,
        note="El validador ve la forma y las coincidencias exactas; no ve la verdad de lo que el paquete afirma. Que apruebe un paquete solo significa que está completo y coherente en forma. Cada familia detectó 16 de 16 o 0 de 16, y la tabla las nombra una por una. Las mutaciones y las reglas las escribí yo, así que 16 de 16 describe estas reglas contra estos defectos, no una cobertura general.",
        note_kind="coral", foot=SINT)


def se360_olvidados() -> Fig:
    return grouped_bars(
        "Gasto de un mes con entornos de laboratorio de 5 unidades por día y un 15 % que se olvida (500 meses)",
        "Barras horizontales agrupadas con el gasto mediano y el percentil 90 del mes: sin plazo, 340 y 570 unidades; con plazo de 24 horas y barrido diario, 110 y 110, el mínimo sin olvidos; con el mismo plazo pero un barrido que falla el 20 por ciento de los días, 110 y 120.",
        ["A mano, sin plazo", "Plazo de 24 h con barrido diario", "Plazo de 24 h, el barrido falla el 20 % de los días"],
        [("Gasto mediano del mes", [340, 110, 110], "teal"), ("Percentil 90", [570, 110, 120], "coral")],
        unit="Unidades de gasto en un mes", horizontal=True, label_w=270,
        note="El plazo convierte un coste abierto en uno acotado: el olvido pasa de costar hasta 30 días a costar uno o dos. Los 110 son 22 días hábiles por 5 unidades. El precio, la tasa de olvido del 15 % y el fallo del barrido son supuestos del autor, no medidas de un equipo.",
        note_kind="teal", foot=SINT)


FIGURES = {
    "se-355-radio-de-un-error-segun-las-cuentas.svg": se355_radio,
    "se-355-divergencia-entre-entornos.svg": se355_divergencia,
    "se-355-combinaciones-toxicas-de-permisos.svg": se355_toxicas,
    "se-356-politicas-de-escalado.svg": se356_politicas,
    "se-356-latencia-segun-la-utilizacion.svg": se356_cola,
    "se-356-nivel-de-compromiso-y-coste.svg": se356_compromiso,
    "se-357-disponibilidad-segun-la-composicion.svg": se357_disponibilidad,
    "se-357-interseccion-de-funciones.svg": se357_interseccion,
    "se-357-tiempo-y-coste-de-mover-datos.svg": se357_gravedad,
    "se-358-camino-dorado-frente-a-pasos-manuales.svg": se358_camino,
    "se-358-cola-del-equipo-de-plataforma.svg": se358_cola,
    "se-358-lo-que-el-verificador-ve-y-no-ve.svg": se358_verificador,
    "se-359-cortes-y-huerfanos.svg": se359_cortes,
    "se-359-orden-de-destruccion.svg": se359_destruccion,
    "se-359-barrido-por-etiquetas.svg": se359_barrido,
    "se-360-hashes-entre-sistemas.svg": se360_hashes,
    "se-360-validador-del-paquete.svg": se360_validador,
    "se-360-entornos-olvidados.svg": se360_olvidados,
}
