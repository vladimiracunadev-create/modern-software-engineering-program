"""Figures for SE-133 to SE-138 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig, dumbbell, grouped_bars, line_chart, percentile_intervals, stacked_bars
from figures_part07_a import bars
from figures_part10_a import SINT, intervals


# ---------------------------------------------------------------- SE-133
def se133_ltv() -> Fig:
    items = [("Punto (valores centrales)", 11.48, 11.48, 11.48, "gold", "11,5 veces"),
             ("Intervalo p5–p95 (20 000 sorteos)", 1.15, 10.96, 50.26, "teal", "mediana 11,0 veces")]
    return intervals("Valor de vida del centro sobre costo de adquirirlo: un punto o un rango",
                     "Gráfico de intervalos: con valores centrales la razón entre valor de vida y costo de adquisición es 11,5; con rangos triangulares para tamaño, precio, costos, abandono y adquisición el intervalo del 5 al 95 por ciento va de 1,15 a 50,3 y la mediana es 11,0.",
                     items, 55, "veces",
                     note="La probabilidad de que un centro no recupere su costo de adquisición (razón menor que 1) es 4,4 %; de que no llegue a 3 veces, 12,8 %; y en 1,9 % de los sorteos el margen mensual del centro ya es negativo. Una razón de 11,5 «sobra» solo si los rangos son correctos.",
                     label_w=345)


def se133_precios() -> Fig:
    return dumbbell(
        "Tres modelos de precio sobre los mismos centros: de la caja mínima a la caja al mes 36",
        "Mancuernas con la caja mínima y la caja al mes 36 de seis simulaciones: el precio por alumno sube de −17 516 a +1 287 537 con abandono de 2 por ciento y de −21 094 a +755 245 con 5; el precio plano termina en +21 759 o en −61 514; el gratuito con 10 por ciento de conversión termina en −657 924 y con 52 por ciento en +30 208.",
        [("Por alumno, abandono 2 % (equilibrio mes 4)", -17516, 1287537), ("Por alumno, abandono 5 % (mes 5)", -21094, 755245),
         ("Plano, abandono 2 % (mes 15)", -70760, 21759), ("Plano, abandono 5 % (mes 22)", -102685, -61514),
         ("Gratuito, 10 % de conversión (nunca)", -657924, -657924), ("Gratuito, 52 % de conversión (mes 14)", -79085, 30208)],
        unit="Caja acumulada (unidades monetarias ficticias)", names=("Caja mínima", "Caja al mes 36"), lower_is_better=False,
        label_w=330,
        note="Mismos centros (150–1 500 alumnos, moda 400), mismos costos (0,6 por alumno, 50 por centro, 12 000 fijos al mes). Cambia solo cómo se cobra: el precio plano deja de cubrir a los centros grandes y el gratuito paga el servicio de todos con la conversión de unos pocos. Unidades monetarias ficticias.", note_kind="gold", foot=SINT)


def se133_concentracion() -> Fig:
    items = [("Dispersión baja: mayor cliente", 3.1, "teal", "3,1 %"),
             ("Dispersión baja: 5 mayores", 11.5, "teal", "11,5 %"),
             ("Dispersión baja: 10 mayores", 19.2, "teal", "19,2 %"),
             ("Dispersión alta: mayor cliente", 13.1, "coral", "13,1 %"),
             ("Dispersión alta: 5 mayores", 33.5, "coral", "33,5 %"),
             ("Dispersión alta: 10 mayores", 45.8, "coral", "45,8 %")]
    return bars("Cuánto del ingreso concentran los mayores clientes entre 120 centros",
                "Barras con la parte del ingreso mensual de los mayores clientes: con dispersión baja el mayor cliente aporta 3,1 por ciento y los diez mayores 19,2; con dispersión alta el mayor aporta 13,1 por ciento y los diez mayores 45,8.",
                items, 6.5, "Índice de concentración (HHI): 105 con dispersión baja y 352 con alta. Perder al mayor cliente baja el margen mensual 4,3 % en el primer caso (31 541 a 30 190) y 15,6 % en el segundo (62 380 a 52 656). Con ingreso total casi el doble, el negocio es más frágil.",
                label_w=300, width=940, note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-134
def se134_tco() -> Fig:
    return percentile_intervals(
        "Costo total a cinco años: el valor central frente a 20 000 sorteos (miles)",
        "Intervalos con el costo total a cinco años: el valor central da 655 mil; en 20 000 sorteos el percentil 5 es 609 mil, la mediana 845 mil y el percentil 95 1 136 mil. Construir pesa 30,5 por ciento en el punto y entre 20,7 y 36,2 en el intervalo, y en ningún sorteo supera la mitad.",
        [("Valor central (un punto)", [655, 655, 655]), ("20 000 sorteos de los rangos", [609, 845, 1136])],
        unit="Costo total a cinco años (miles)", marks=("p5", "mediana", "p95"), label_w=250,
        note="Construcción 120–400 (moda 200), mantenimiento 10–30 % de la construcción al año, infraestructura 10–60 y soporte 15–90 al año. El punto subestima la mediana en 190 mil porque los rangos de operación son asimétricos hacia arriba: el costo que más se omite en la propuesta es el que más pesa.", note_kind="gold", foot=SINT)


def se134_suma() -> Fig:
    items = [("5 tareas, σ 0,6, independientes", 32.1, "gold", "32,1 %"),
             ("20 tareas, σ 0,6, independientes", 11.7, "coral", "11,7 %"),
             ("20 tareas, σ 0,6, correlación 0,5", 43.7, "gold", "43,7 %"),
             ("20 tareas, σ 0,3, independientes", 26.1, "gold", "26,1 %")]
    return bars("Probabilidad de terminar dentro de la suma de las medianas",
                "Barras con la probabilidad de que el total real no supere la suma de las medianas: 32,1 por ciento con cinco tareas, 11,7 con veinte tareas independientes, 43,7 con veinte tareas correlacionadas y 26,1 con veinte tareas de menor dispersión.",
                items, 6.0, "Con 20 tareas de mediana 5 días (suma 100), el total tiene mediana 118,5, percentil 80 de 134,3 y percentil 95 de 150,8. Sumar medianas no da una mediana: promete un plazo que se cumple una de cada ocho veces. Con correlación 0,5 la probabilidad sube, pero el percentil 95 salta a 224,3.",
                label_w=330, width=940, note_kind="coral", foot=SINT)


def se134_descuento() -> Fig:
    return line_chart(
        "Valor presente de dos opciones según la tasa de descuento anual",
        "Líneas con el valor presente neto de la opción A (barata y ya) y de la opción B (cara, desde el mes 7) según la tasa anual: B gana con 0, 5 y 10 por ciento (120,0, 94,1 y 71,1 frente a 84,0, 73,5 y 64,0), se cruzan en 13,0 por ciento con 58,8 cada una y A gana con 20, 30 y 40 por ciento.",
        [("Opción A (60 hoy, 4 al mes)", [(0, 84.0), (5, 73.5), (10, 64.0, "", "b"), (13, 58.8), (20, 47.6, "", "t"), (30, 34.2, "", "t"), (40, 23.1, "", "t")], "teal"),
         ("Opción B (150 hoy, 7,5 al mes desde el mes 7)", [(0, 120.0), (5, 94.1), (10, 71.1), (13, 58.8), (20, 32.8, "", "b"), (30, 2.3, "", "b"), (40, -21.9, "", "b")], "coral")],
        x_label="Tasa de descuento anual (%)", y_label="Valor presente neto (unidades ficticias)",
        x_ticks=[(0, "0"), (5, "5"), (10, "10"), (13, "13"), (20, "20"), (30, "30"), (40, "40")], y_zero=False,
        annotations=[(13, 58.8, "Cruce en 12,97 %: empatan", 60, -50)],
        note="El cruce está en 12,97 % anual. Quien descuenta alto (capital escaso, incertidumbre) prefiere lo que rinde antes. La tasa es un juicio sobre el costo de oportunidad, no un dato: se declara y se prueba el cruce.", note_kind="gold", foot="Cálculo determinista; cifras en unidades monetarias ficticias.")


# ---------------------------------------------------------------- SE-135
def se135_goodhart() -> Fig:
    return grouped_bars(
        "Premiar lo cerrado: el número sube y lo resuelto baja (diez agentes, doce semanas)",
        "Barras agrupadas con los tickets cerrados y los resueltos sin reabrir según la meta: con la meta de tickets cerrados se cierran 760 y se resuelven 512 y se reabre el 41,2 por ciento; con la meta de resueltos sin reabrir se cierran 600 y se resuelven 560 y se reabre el 5,7 por ciento.",
        ["Meta «tickets cerrados» (41,2 % reabiertos)", "Meta «resueltos sin reabrir» (5,7 % reabiertos)"],
        [("Cerrados", [760, 600], "gold"), ("Resueltos (no reabiertos)", [512, 560], "teal")],
        unit="Tickets en doce semanas", horizontal=True, label_w=300,
        note="La métrica premiada subió 26,7 % (600 a 760) y el resultado que importa bajó 8,6 % (560 a 512). Es un modelo con supuestos del autor (cerrar rápido eleva de 5 a 7 los cierres por agente y la reapertura de 8 % a 45 %): muestra el mecanismo, no mide a ningún equipo.", note_kind="coral", foot=SINT)


def se135_acumulado() -> Fig:
    return line_chart(
        "Registros acumulados frente a usuarios activos en 24 meses",
        "Líneas con los registros acumulados y los usuarios activos: los registros suben hasta 3 555 en el mes 15 y se quedan planos; los activos alcanzan un pico de 1 405 en el mes 10, ya caen en el mes 12 (1 324) y llegan a 226 en el mes 24.",
        [("Registros acumulados", [(6, 1800), (9, 2700), (10, 2955), (12, 3330), (15, 3555), (18, 3555), (24, 3555)], "gold"),
         ("Usuarios activos", [(6, 1121), (9, 1383), (10, 1405, "", "t"), (12, 1324, "", "t"), (15, 976), (18, 599), (24, 226)], "teal")],
        x_label="Mes", y_label="Personas", x_ticks=[(6, "6"), (9, "9"), (10, "10"), (12, "12"), (15, "15"), (18, "18"), (24, "24")],
        annotations=[(10, 1405, "Pico de activos (mes 10)", 80, 80)],
        note="Altas de 300 al mes hasta el mes 9 y luego decrecientes; 85 % de los activos permanece cada mes. Una métrica acumulada solo puede subir: no puede avisar de que el producto se vacía.", note_kind="gold", foot=SINT)


def se135_actividad() -> Fig:
    items = [("Actividad (producción) con resultado", 0.20, "coral", "0,20"),
             ("Calidad con resultado", 0.90, "teal", "0,90")]
    return bars("Correlación de rango con el resultado en 300 equipos sintéticos",
                "Barras con la correlación de Spearman: la actividad medida como producción se asocia con el resultado en 0,20; la calidad subyacente, en 0,90.",
                items, 400, "El decil de equipos con más producción tiene resultado medio 1,32 frente a 0,23 de la población: hay algo de señal, pero se fabrica con la parte de la producción que sí depende de la calidad (peso 2 de 12 en el generador). Premiar la producción mueve sobre todo la actividad pura, que no aporta resultado.",
                label_w=330, width=940, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-136
def se136_curva() -> Fig:
    return line_chart(
        "Retención por semana: la curva agregada aplana mientras cada segmento decae por igual",
        "Líneas con la retención de la curva agregada (30 por ciento hábito y 70 ocasional) y de cada segmento: la agregada cae de 81,6 a 13,6 por ciento en 26 semanas; el segmento de hábito de 97,0 a 45,3; el ocasional de 75,0 a 0,06.",
        [("Agregada (30 % hábito, 70 % ocasional)", [(1, 81.6), (4, 48.7), (8, 30.5), (12, 23.0), (26, 13.6)], "navy"),
         ("Segmento hábito", [(1, 97.0), (4, 88.5), (8, 78.4), (12, 69.4), (26, 45.3)], "teal"),
         ("Segmento ocasional", [(1, 75.0, "", "b"), (4, 31.6), (8, 10.0), (12, 3.2), (26, 0.06, "0,06", "t")], "coral")],
        x_label="Semana desde el registro", y_label="Retención (%)", decimals=1, x_ticks=[(1, "1"), (4, "4"), (8, "8"), (12, "12"), (26, "26")],
        note="Cada segmento pierde una fracción constante por semana (3 % y 25 %); la mezcla produce una curva que decae cada vez más despacio. Extrapolar con la tasa de las primeras semanas subestima la retención a 26 semanas por 15 veces. Una simulación de 2 000 personas da 47,3 %, 22,2 % y 13,8 % en las semanas 4, 12 y 26.", note_kind="gold", foot=SINT)


def se136_activo() -> Fig:
    items = [("Cualquier evento o acceso (1 737 al mes)", 28.2, "gold", "28,2 %"),
             ("Vio una entrega (1 688 al mes)", 23.2, "gold", "23,2 %"),
             ("Envió una entrega (1 215 al mes)", 8.1, "teal", "8,1 %")]
    return bars("DAU/MAU de las mismas 2 000 personas según qué cuenta como activo",
                "Barras del cociente entre activos diarios y mensuales con la misma población: 28,2 por ciento si basta un acceso, 23,2 si se vio una entrega y 8,1 si se envió una entrega.",
                items, 12, "Ningún valor es el verdadero: responden a preguntas distintas. 28,2 % mide hábito de abrir la aplicación; 8,1 % mide hábito de hacer la tarea útil. Compararse con «un DAU/MAU de 25 %» publicado por otro equipo exige saber qué evento cuenta.",
                label_w=360, width=980, note_kind="gold", foot=SINT)


def se136_censura() -> Fig:
    return percentile_intervals(
        "Intervalo de Wilson de la retención a 30 días según el tamaño de la cohorte",
        "Intervalos de Wilson de la retención a 30 días: con 50 personas va de 22,4 a 47,8 por ciento, con 200 de 27,8 a 40,8, con 1 000 de 31,1 a 37,0 y con 5 000 de 32,7 a 35,3; la retención real es 34,2 y la cuenta ingenua que incluye a quienes no cumplieron 30 días da 27,0, fuera de los dos intervalos mayores.",
        [("n = 50", [22.4, 47.8]), ("n = 200", [27.8, 40.8]), ("n = 1 000", [31.1, 37.0]), ("n = 5 000", [32.7, 35.3])],
        unit="Retención a 30 días (%)", marks=("inferior", "superior"), decimals=1, ref_lines=[(34.2, "real 34,2 %"), (27.0, "ingenua 27,0 %")], label_w=130,
        note="Se simularon 3 000 personas registradas a lo largo de 60 días; la devolución a 30 días tiene probabilidad real 0,34. Las cohortes recientes parecen peores solo porque aún no pasó el tiempo. Un intervalo estrecho no corrige un sesgo de medición: solo mide el azar de muestrear.", note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-137
def se137_consentimiento() -> Fig:
    items = [("Consiente 42 % de las personas", 15.7, "coral", "+15,7 %"),
             ("Consiente 54 %", 9.8, "coral", "+9,8 %"),
             ("Consiente 67 %", 5.1, "gold", "+5,1 %")]
    return bars("Sesgo de la métrica medida solo con quienes aceptan",
                "Barras con el sesgo relativo de las entregas semanales por persona estimadas solo con quienes consienten: 15,7 por ciento de sobreestimación si consiente el 42 por ciento, 9,8 con 54 y 5,1 con 67.",
                items, 14, "La probabilidad de aceptar crece con el compromiso, de modo que quienes aceptan usan más el producto. Reponderar por el plan (una variable que sí se conoce) deja el sesgo casi igual (15,7 / 9,7 / 5,0 %): corrige lo que explica el plan, no el compromiso. Más consentimiento reduce el sesgo, pero no lo elimina.",
                label_w=300, width=940, note_kind="coral", foot=SINT)


def se137_identifica() -> Fig:
    return grouped_bars(
        "Cada campo de telemetría estrecha el grupo hasta señalar a una persona (10 000 dispositivos)",
        "Barras horizontales con el porcentaje de dispositivos únicos y de dispositivos en grupos de menos de cinco al sumar campos: con sistema operativo y versión ninguno es único; con idioma regional 0,3 y 3,4 por ciento; con resolución 9,8 y 42,9; con zona horaria 38,3 y 71,1; y con el identificador del centro 99,4 y 100,0.",
        ["Sistema operativo (6 grupos)", "+ versión de la aplicación (72)", "+ idioma regional (489)", "+ resolución de pantalla (2 580)",
         "+ zona horaria (5 575)", "+ identificador del centro (9 969)"],
        [("Únicos", [0.0, 0.0, 0.3, 9.8, 38.3, 99.4], "coral"), ("En grupos con menos de 5", [0.0, 0.0, 3.4, 42.9, 71.1, 100.0], "gold")],
        unit="Dispositivos (%)", horizontal=True, label_w=270, decimals=1,
        note="Ningún campo es un dato personal por sí solo. La combinación sí lo es en la práctica. Quitar el centro y la zona horaria deja sistema operativo + idioma: 42 grupos y 0 % en grupos de menos de 5. El diseño del evento decide qué campos se recogen; el consentimiento no los vuelve inocuos.", note_kind="coral", foot=SINT)


def se137_mutantes() -> Fig:
    return stacked_bars(
        "Control de consentimiento: mutantes que matan 3 pruebas del camino feliz frente a 9 dirigidas",
        "Barras apiladas de los once mutantes del rastreador con consentimiento: las tres pruebas del camino feliz matan 2 y dejan 9 vivos; las nueve pruebas completas matan 10 y solo sobrevive el equivalente.",
        ["3 pruebas del camino feliz", "9 pruebas dirigidas"],
        [("Muertos", [2, 10], "teal"), ("Sobreviven", [9, 1], "coral")],
        unit="Mutantes", horizontal=True, label_w=230,
        note="Puntaje de mutación: 2 de 11 con las pruebas del camino feliz y 10 de 11 con las completas. El mutante equivalente sobrevive con razón: el código resultante se comporta igual. Un 100 % no se espera; hay que revisar cada superviviente y decidir.", note_kind="gold", foot="Código y pruebas reales ejecutados; idénticos en Windows y Ubuntu (WSL2).")


# ---------------------------------------------------------------- SE-138
def se138_seleccion() -> Fig:
    items = [("Efecto verdadero", 0.50, "navy", "0,50"), ("Aleatorizado", 0.48, "teal", "0,48"),
             ("Estratificado con un indicador ruidoso", 1.80, "gold", "1,80"), ("Comparación ingenua de quienes adoptan", 2.62, "coral", "2,62")]
    return bars("Efecto estimado de una función: observar frente a asignar al azar",
                "Barras del efecto estimado en entregas por semana: el efecto verdadero es 0,50; la asignación al azar estima 0,48; estratificar por un indicador ruidoso del compromiso estima 1,80; comparar a quienes adoptan con quienes no estima 2,62.",
                items, 130, "Quienes adoptan la función ya eran más comprometidos (adopción 41 % con 20 000 personas). Controlar por un indicador ruidoso reduce el sesgo pero deja 3,6 veces el efecto real. Solo la asignación al azar rompe el vínculo entre compromiso y adopción.",
                label_w=360, width=980, note_kind="coral", foot=SINT)


def se138_srm() -> Fig:
    items = [("Pérdida de 0,5 % del grupo tratado", 0.2, "coral", "0,2 %"), ("Pérdida de 1 %", 0.9, "coral", "0,9 %"),
             ("Pérdida de 2 %", 10.7, "gold", "10,7 %"), ("Pérdida de 5 %", 95.8, "teal", "95,8 %")]
    return bars("Con qué frecuencia el control de proporciones detecta una asignación rota",
                "Barras con la fracción de 1000 experimentos en que el control de proporción de muestra da alarma: 0,2 por ciento si se pierde el 0,5 por ciento del grupo tratado, 0,9 con 1, 10,7 con 2 y 95,8 con 5.",
                items, 3.6, "Con 10 000 personas y asignación correcta, el control (p < 0,001) dio 0 alarmas falsas en 1 000 experimentos. Pero una pérdida de 2 % pasa inadvertida el 89 % de las veces, y eliminar al 3 % menos comprometido del grupo tratado ya desplaza la diferencia 0,046 desviaciones típicas, del orden de un efecto real pequeño.",
                label_w=320, width=940, note_kind="gold", foot=SINT)


def se138_regresion() -> Fig:
    items = [("Ruido 2 (fiabilidad 0,94)", 0.91, "teal", "+0,91 puntos"), ("Ruido 5 (fiabilidad 0,72)", 4.0, "gold", "+4,00 puntos"),
             ("Ruido 8 (fiabilidad 0,50)", 12.64, "coral", "+12,64 puntos")]
    return bars("Mejora de los centros peores sin ninguna intervención",
                "Barras con la mejora media del 10 por ciento de centros con peor primera medición al medirlos de nuevo sin intervención: 0,91 puntos con fiabilidad 0,94, 4,00 con 0,72 y 12,64 con 0,50.",
                items, 30, "500 centros con valor verdadero de media 60 y desviación 8; se elige el 10 % peor en la primera medición. Con ruido 5, el 80 % de ellos «mejora» solo por azar. Un programa dirigido al peor decil que mide antes y después atribuiría esa mejora al programa.",
                label_w=300, width=940, note_kind="coral", foot=SINT)


FIGURES = {
    "se-133-valor-de-vida-sobre-costo-de-adquisicion.svg": se133_ltv,
    "se-133-modelos-de-precio-y-caja.svg": se133_precios,
    "se-133-concentracion-de-ingresos.svg": se133_concentracion,
    "se-134-construir-es-la-parte-menor.svg": se134_tco,
    "se-134-suma-de-medianas.svg": se134_suma,
    "se-134-tasa-de-descuento-y-ranking.svg": se134_descuento,
    "se-135-premiar-lo-cerrado.svg": se135_goodhart,
    "se-135-acumulado-frente-a-activos.svg": se135_acumulado,
    "se-135-actividad-y-resultado.svg": se135_actividad,
    "se-136-curva-agregada-y-segmentos.svg": se136_curva,
    "se-136-definicion-de-activo.svg": se136_activo,
    "se-136-cohortes-incompletas-y-pequenas.svg": se136_censura,
    "se-137-sesgo-por-consentimiento.svg": se137_consentimiento,
    "se-137-campos-que-identifican.svg": se137_identifica,
    "se-137-mutantes-del-control-de-consentimiento.svg": se137_mutantes,
    "se-138-sesgo-de-seleccion.svg": se138_seleccion,
    "se-138-desajuste-de-proporcion-de-muestra.svg": se138_srm,
    "se-138-regresion-a-la-media.svg": se138_regresion,
}
