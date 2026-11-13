"""Figures for SE-133 to SE-138 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab
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
    rows = [["Por alumno (1,5 por alumno y mes)", "2 %", "4", "−17 516", "+1 287 537"],
            ["Por alumno (1,5 por alumno y mes)", "5 %", "5", "−21 094", "+755 245"],
            ["Plano por centro (600 al mes)", "2 %", "15", "−70 760", "+21 759"],
            ["Plano por centro (600 al mes)", "5 %", "22", "−102 685", "−61 514"],
            ["Gratuito con 10 % de conversión (900)", "3 %", "nunca", "−657 924", "−657 924"],
            ["Gratuito con 52 % de conversión (900)", "3 %", "14", "−79 085", "+30 208"]]
    return tab("Tres modelos de precio sobre los mismos centros: cuándo se equilibra la caja",
               "Tabla de seis simulaciones de 36 meses con seis centros nuevos por mes: el precio por alumno equilibra la operación en el mes 4 o 5 y acumula más de 750 000 unidades; el precio plano equilibra en el mes 15 o 22 y con abandono de 5 por ciento no recupera la caja en 36 meses; el gratuito con 10 por ciento de conversión nunca la equilibra y con 52 por ciento tarda 14 meses.",
               ["Modelo de precio", "Abandono mensual", "Mes en que el flujo mensual es positivo", "Caja mínima", "Caja al mes 36"],
               rows, [300, 110, 170, 130, 150], row_h=48, size=12,
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
    rows = [["Punto (valores centrales)", "655", "30,5 %"],
            ["Mediana de 20 000 sorteos", "845", "28,0 %"],
            ["Intervalo p5–p95", "609 a 1 136", "20,7 % a 36,2 %"],
            ["Sorteos en que construir pesa más de la mitad", "0 de 20 000", "—"]]
    return tab("Costo a cinco años: construir es la parte menor",
               "Tabla: con valores centrales el costo de cinco años es 655 mil unidades y construir pesa 30,5 por ciento; en 20 000 sorteos la mediana del total es 845 mil, el intervalo del 5 al 95 por ciento va de 609 a 1136 y construir pesa entre 20,7 y 36,2 por ciento; nunca pesa más de la mitad.",
               ["Estimación", "Costo total a 5 años (miles)", "Construcción sobre el total"], rows, [420, 230, 230], row_h=50, size=13,
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
    rows = [["0 %", "84,0", "120,0", "B"], ["5 %", "73,5", "94,1", "B"], ["10 %", "64,0", "71,1", "B"],
            ["13,0 % (cruce)", "58,8", "58,8", "empate"], ["20 %", "47,6", "32,8", "A"], ["30 %", "34,2", "2,3", "A"], ["40 %", "23,1", "−21,9", "A"]]
    return tab("Una misma pareja de opciones cambia de ganadora según la tasa de descuento",
               "Tabla de valor presente neto de dos opciones: A cuesta 60 hoy y rinde 4 al mes durante 36 meses; B cuesta 150 hoy y rinde 7,5 al mes desde el mes 7. B gana con tasas hasta 10 por ciento anual, ambas empatan cerca de 13 por ciento y A gana con tasas mayores.",
               ["Tasa anual", "VPN de A (barata, ya)", "VPN de B (cara, desde el mes 7)", "Mejor"], rows, [200, 230, 300, 150], row_h=40, size=13,
               note="El cruce está en 12,97 % anual. Quien descuenta alto (capital escaso, incertidumbre) prefiere lo que rinde antes. La tasa es un juicio sobre el costo de oportunidad, no un dato: se declara y se prueba el cruce.", note_kind="gold", foot="Cálculo determinista; cifras en unidades monetarias ficticias.")


# ---------------------------------------------------------------- SE-135
def se135_goodhart() -> Fig:
    rows = [["Semana 4, antes de anunciar la meta", "50", "45", "10 %"],
            ["Semanas 5 a 12, meta «tickets cerrados»", "760 en 12 semanas", "512", "41,2 %"],
            ["Semanas 5 a 12, meta «resueltos sin reabrir»", "600 en 12 semanas", "560", "5,7 %"]]
    return tab("Premiar lo cerrado: el número sube y lo resuelto baja",
               "Tabla de diez agentes durante doce semanas: con la meta de tickets cerrados se cierran 760 tickets y se resuelven 512, y el 41,2 por ciento de lo cerrado se reabre; con la meta de resueltos sin reabrir se cierran 600 y se resuelven 560, con 5,7 por ciento de reapertura.",
               ["Situación", "Cerrados", "Resueltos (no reabiertos)", "Reabiertos de lo cerrado"], rows, [420, 190, 190, 190], row_h=48, size=13,
               note="La métrica premiada subió 26,7 % (600 a 760) y el resultado que importa bajó 8,6 % (560 a 512). Es un modelo con supuestos del autor (cerrar rápido eleva de 5 a 7 los cierres por agente y la reapertura de 8 % a 45 %): muestra el mecanismo, no mide a ningún equipo.", note_kind="coral", foot=SINT)


def se135_acumulado() -> Fig:
    rows = [["6", "1 800", "1 121", "ambos suben"], ["9", "2 700", "1 383", "ambos suben"],
            ["10", "2 955", "1 405", "pico de activos"], ["12", "3 330", "1 324", "los activos ya caen"],
            ["15", "3 555", "976", "última alta; el acumulado deja de subir"], ["18", "3 555", "599", "el acumulado se queda plano"],
            ["24", "3 555", "226", "dos años: 3 555 registros, 226 activos"]]
    return tab("Registros acumulados frente a usuarios activos",
               "Tabla de 24 meses: los registros acumulados crecen hasta 3555 y no bajan nunca, mientras los usuarios activos alcanzan un pico de 1405 en el mes 10, caen desde el mes 11 y llegan a 226 en el mes 24.",
               ["Mes", "Registros acumulados", "Usuarios activos", "Lectura"], rows, [90, 220, 200, 400], row_h=42, size=13,
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
    rows = [["1", "81,6 %", "97,0 %", "75,0 %"], ["4", "48,7 %", "88,5 %", "31,6 %"], ["8", "30,5 %", "78,4 %", "10,0 %"],
            ["12", "23,0 %", "69,4 %", "3,2 %"], ["26", "13,6 %", "45,3 %", "0,06 %"]]
    return tab("Una curva de retención agregada aplana mientras cada segmento decae por igual",
               "Tabla de retención por semana: la curva agregada cae de 81,6 a 13,6 por ciento en 26 semanas; el segmento de hábito baja de 97,0 a 45,3 por ciento y el de visitas ocasionales de 75,0 a casi 0. Una tasa constante ajustada a las primeras cuatro semanas predice 0,9 por ciento en la semana 26 y el valor real es 13,6.",
               ["Semana", "Agregada (30 % hábito, 70 % ocasional)", "Segmento hábito", "Segmento ocasional"], rows, [110, 340, 200, 220], row_h=40, size=13,
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
    rows = [["Retención a 30 días real (la conoce el generador)", "34,2 %", "referencia"],
            ["Ingenua: todos los registrados, aunque tengan menos de 30 días", "27,0 %", "sesgo −7,2 puntos"],
            ["Solo quienes ya cumplieron 30 días (n = 1 632)", "34,6 %", "sesgo +0,4"],
            ["Intervalo de Wilson con n = 50", "22,4 % a 47,8 %", "ancho 25,4 puntos"],
            ["Intervalo de Wilson con n = 200", "27,8 % a 40,8 %", "ancho 13,0"],
            ["Intervalo de Wilson con n = 1 000", "31,1 % a 37,0 %", "ancho 5,9"],
            ["Intervalo de Wilson con n = 5 000", "32,7 % a 35,3 %", "ancho 2,6"]]
    return tab("Retención a 30 días: cohortes incompletas y cohortes pequeñas",
               "Tabla: con 34,2 por ciento de retención real, contar a las personas con menos de 30 días de observación como no retenidas da 27,0 por ciento; usar solo a quienes completaron los 30 días da 34,6. El intervalo de Wilson mide 25,4 puntos de ancho con 50 personas y 2,6 con 5000.",
               ["Estimación", "Valor", "Lectura"], rows, [520, 230, 190], row_h=44, size=13,
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
    rows = [["sistema operativo", "6", "0,0 %", "0,0 %"], ["+ versión de la aplicación", "72", "0,0 %", "0,0 %"],
            ["+ idioma regional", "489", "0,3 %", "3,4 %"], ["+ resolución de pantalla", "2 580", "9,8 %", "42,9 %"],
            ["+ zona horaria", "5 575", "38,3 %", "71,1 %"], ["+ identificador del centro (300)", "9 969", "99,4 %", "100,0 %"]]
    return tab("Cada campo de telemetría estrecha el grupo hasta señalar a una persona",
               "Tabla de 10 000 dispositivos sintéticos: con sistema operativo y versión ninguno es único; con idioma regional 0,3 por ciento; con resolución 9,8; con zona horaria 38,3; y con el identificador del centro 99,4 por ciento son únicos y el 100 por ciento queda en grupos de menos de cinco.",
               ["Campos acumulados", "Grupos distintos", "Dispositivos únicos", "En grupos con menos de 5"], rows, [330, 170, 190, 220], row_h=44, size=13,
               note="Ningún campo es un dato personal por sí solo. La combinación sí lo es en la práctica. Quitar el centro y la zona horaria deja sistema operativo + idioma: 42 grupos y 0 % en grupos de menos de 5. El diseño del evento decide qué campos se recogen; el consentimiento no los vuelve inocuos.", note_kind="coral", foot=SINT)


def se137_mutantes() -> Fig:
    rows = [["M1 el estado denegado envía", "mata", "mata"], ["M2 el estado desconocido envía de inmediato", "mata", "mata"],
            ["M3 negar no vacía el búfer", "sobrevive", "mata"], ["M4 retirar el consentimiento no frena el envío", "sobrevive", "mata"],
            ["M5 deja pasar el correo", "sobrevive", "mata"], ["M6 acepta eventos no declarados", "sobrevive", "mata"],
            ["M7 búfer sin tope", "sobrevive", "mata"], ["M8 al conceder no vacía el búfer", "sobrevive", "mata"],
            ["M9 invierte el orden al vaciar", "sobrevive", "mata"], ["M10 conserva user_id", "sobrevive", "mata"],
            ["M11 borra una variable sin uso (equivalente)", "sobrevive", "sobrevive"]]
    return tab("Control de consentimiento: 3 pruebas del camino feliz frente a 9 pruebas dirigidas",
               "Tabla de once mutantes de un rastreador con consentimiento: las tres primeras pruebas matan 2 y las nueve pruebas completas matan 10; el undécimo es equivalente y ninguna prueba puede distinguirlo.",
               ["Mutante", "3 pruebas", "9 pruebas"], rows, [540, 150, 150], row_h=34, size=12,
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
