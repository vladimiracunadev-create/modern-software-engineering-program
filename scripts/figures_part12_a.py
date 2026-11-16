"""Figures for SE-145 to SE-150 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3 unless a timing is shown)."""
from __future__ import annotations

from figure_cases import case_cards
from figure_kit import Fig, dumbbell, fmt_es, grouped_bars, line_chart, scatter
from figures_part07_a import bars
from figures_part10_a import SINT, intervals

MEDIDO = "Tiempos medidos con CPython 3.12.9 en Windows 11 y 3.12.3 en Ubuntu (WSL2); dependen del equipo y se leen como razones."


# ---------------------------------------------------------------- SE-145
def se145_cobertura() -> Fig:
    items = []
    for k, solo, mixto in ((1, 17.7, 32.1), (2, 32.9, 47.1), (4, 55.2, 68.5), (8, 77.2, 90.3)):
        etiqueta = f"{k} entrevista" + ("s" if k > 1 else "")
        items.append((f"{etiqueta}, solo entrevistas", solo, "coral", f"{solo:g} %"))
        items.append((f"{etiqueta} + 3 observaciones", mixto, "teal", f"{mixto:g} %"))
    return bars("Cobertura de 40 requisitos sintéticos según la técnica de elicitación",
                "Barras de cobertura media de 40 requisitos, 8 de ellos tácitos, con 1, 2, 4 y 8 entrevistas: solo entrevistas llegan a 17,7, 32,9, 55,2 y 77,2 por ciento; con tres observaciones añadidas, a 32,1, 47,1, 68,5 y 90,3.",
                items, 5.0, "Con ocho entrevistas la cobertura se detiene en 77,2 % porque los 8 requisitos tácitos casi nunca se enuncian (5 % de probabilidad por persona que los conoce). Tres sesiones de observación suben el techo a 90,3 %.",
                label_w=330, width=1000, note_kind="teal", foot=SINT)


def se145_revision() -> Fig:
    ks = [1, 2, 3, 4, 5, 6]
    return line_chart("Revisar con más personas: modelo independiente frente a defectos de dificultad desigual",
                      "Líneas con la fracción de 30 defectos hallada por 1 a 6 revisores: el modelo de independencia sube a 39,1, 62,9, 77,4, 86,2, 91,6 y 94,9 por ciento y la simulación con dificultad desigual solo a 39,2, 55,8, 64,7, 70,4, 74,1 y 77,1; la brecha llega a 17,8 puntos con seis revisores.",
                      [("Predicción 1−(1−p)^k (independiente)", [(k, v, fmt_es(v, 1), "t") for k, v in zip(ks, [39.1, 62.9, 77.4, 86.2, 91.6, 94.9])], "gold"),
                       ("Simulación con dificultad desigual (5 000 corridas)", [(k, v, fmt_es(v, 1), "b") for k, v in zip(ks, [39.2, 55.8, 64.7, 70.4, 74.1, 77.1])], "coral")],
                      x_label="Revisores", y_label="Defectos hallados (%)", x_ticks=[(k, str(k)) for k in ks], y_ticks=[0, 20, 40, 60, 80, 100],
                      note="El modelo independiente usa la probabilidad media (0,391) para todos los defectos. Cuando algunos son difíciles para todos, los revisores adicionales repiten los mismos aciertos: con seis personas la simulación se queda 17,8 puntos por debajo (diferencias: 0,1; −7,1; −12,7; −15,8; −17,5; −17,8).",
                      note_kind="gold", foot=SINT)


def se145_conflictos() -> Fig:
    return case_cards("Restricciones de cinco interesados sobre cinco parámetros: intersección de intervalos",
                      "Cinco parámetros con la cota inferior más alta y la superior más baja de distintos interesados: retención, cupo e intentos de acceso tienen intersección vacía; el tiempo de respuesta admite de 800 a 1500 milisegundos y la ventana de edición exactamente 48 horas.",
                      [("Retención (días): ≥ 730 (Auditoría) y ≤ 365 (Privacidad)", "Conflicto: ningún valor cumple las dos cotas", "El mayor mínimo está por encima del menor máximo.", "coral"),
                       ("Cupo por entrega (MB): ≥ 50 (Docencia) y ≤ 25 (Operaciones)", "Conflicto: ningún valor", "Las cotas se cruzan.", "coral"),
                       ("Intentos de acceso: ≥ 8 (Estudiantes) y ≤ 5 (Seguridad)", "Conflicto: ningún valor", "Las cotas se cruzan.", "coral"),
                       ("Tiempo de respuesta (ms): ≥ 800 (Seguridad) y ≤ 1 500 (Estudiantes)", "Factible: 800–1 500", "Hay un intervalo no vacío.", "teal"),
                       ("Ventana de edición (h): ≥ 48 (Estudiantes) y ≤ 48 (Auditoría)", "Factible: solo 48", "El intervalo es un punto: frágil.", "gold")],
                      note="Tres de cinco parámetros no tienen valor posible: ninguna negociación de redacción los arregla, hay que cambiar una de las dos cotas o separar casos (por ejemplo, archivo legal frente a datos de operación). El caso «solo 48 h» es factible pero frágil.",
                      note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-146
def se146_tabla() -> Fig:
    return case_cards("Tabla de decisión de la penalización por entrega tardía: 24 combinaciones, 4 defectuosas",
                      "Cinco de las 24 combinaciones de estado, prórroga, reentrega y adaptación como tarjetas: dos no tienen regla aplicable y dos activan a la vez R2 y R5 con resultados distintos; las otras 20 combinaciones se resuelven con una sola regla, como la primera.",
                      [("En gracia, sin prórroga, sin adaptación", "R2: −10 % de nota (una regla)", "Correcto.", "teal"),
                       ("En gracia, con prórroga, sin reentrega ni adaptación", "Ninguna regla aplicable", "Hueco: ¿qué pasa?", "coral"),
                       ("En gracia, con prórroga, con reentrega, sin adaptación", "Ninguna regla aplicable", "Hueco: ¿qué pasa?", "coral"),
                       ("En gracia, sin prórroga, con adaptación", "R2 y R5: −10 % y sin penalización", "Conflicto de resultado.", "gold"),
                       ("En gracia, sin prórroga, con reentrega y adaptación", "R2 y R5: −10 % y sin penalización", "Conflicto de resultado.", "gold")],
                      note="Cinco reglas redactadas con sentido común dejan 2 de 24 combinaciones sin respuesta y 2 con respuestas contradictorias. Ninguna regla es incorrecta por separado: el defecto está en la combinación, y solo la enumeración lo muestra.",
                      note_kind="coral", foot=SINT)


def se146_medianoche() -> Fig:
    return scatter("Una hora local de plazo en 2026: cuántos días existe, se repite o no existe",
                   "Puntos con los días de 2026 en que una hora local no ocurre exactamente una vez: la medianoche de Santiago no existe el 6 de septiembre, las 23:59 de Santiago se repiten el 4 de abril y las 02:30 de Nueva York no existen el 8 de marzo; los otros 364 días la hora ocurre una vez y en UTC o a la medianoche de Nueva York siempre.",
                   [("00:00 en Santiago: no existe", [(249, 0, "6 sep", "r")], "coral"), ("23:59 en Santiago: se repite", [(94, 2, "4 abr", "r")], "gold"),
                    ("02:30 en Nueva York: no existe", [(67, 0, "8 mar", "r")], "navy")],
                   x_label="Día de 2026", y_label="Veces que ocurre la hora ese día", x_ticks=[(1, "1 ene"), (91, "1 abr"), (182, "1 jul"), (274, "1 oct"), (365, "31 dic")],
                   y_ticks=[0, 1, 2], hlines=[(1, "día normal: existe una vez")],
                   note="Los otros 364 días la hora ocurre una vez. En UTC y a las 00:00 de Nueva York (365 días normales) no hay excepciones. El día calendario local de Santiago midió 24 h en 363 días, 25 h en uno y 23 h en otro. «Hasta la medianoche» y «dentro de 24 horas» no son el mismo plazo esos dos días; el requisito debe fijar zona y regla.",
                   note_kind="gold", foot="Calculado con zoneinfo (CPython 3.12.9 en Windows y 3.12.3 en Ubuntu); el resultado depende de la versión de la base de zonas.")


def se146_mutantes() -> Fig:
    items = [("3 ejemplos típicos", 4, "coral", "4 de 12"), ("10 casos en las fronteras", 10, "gold", "10 de 12"), ("Todo el dominio (12 800 casos)", 11, "teal", "11 de 12")]
    return bars("Mutantes de la regla de penalización detectados según la suite de pruebas",
                "Barras con 12 mutantes de una regla de penalización por tardanza: tres ejemplos típicos detectan 4, diez casos en las fronteras detectan 10 y recorrer todo el dominio detecta 11; el mutante restante es equivalente.",
                items, 40, "Los 6 mutantes que sobreviven a los ejemplos típicos son cambios de un minuto en los límites (60 → 59, 1440 → 1441) o la omisión de la prórroga. El único que sobrevive a todo el dominio, quitar max(0, …), es equivalente: no cambia ningún resultado.",
                label_w=330, width=980, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-147
def se147_percentil() -> Fig:
    items = [("Mediana (p50)", 406, "teal", "406 ms"), ("Media", 535, "teal", "535 ms"), ("Percentil 95", 1023, "gold", "1 023 ms"),
             ("Percentil 99", 4490, "coral", "4 490 ms"), ("Máximo observado", 7576, "coral", "7 576 ms")]
    return bars("Cien mil latencias sintéticas: cada resumen cuenta una historia distinta",
                "Barras con mediana 406, media 535, percentil 95 1023, percentil 99 4490 y máximo 7576 milisegundos de cien mil latencias sintéticas con una cola lenta del 2 por ciento; el umbral de 2000 ms lo cumplen la media y el p95 pero no el p99.",
                items, 0.075, "«Responde en menos de 2 s» se cumple con la media y con p95 y se incumple con p99; el 2,1 % de las peticiones supera los 2 s. Con muestras de 200 peticiones el p99 observado varió entre 1 303 y 5 711 ms (p5–p95 de 1 000 muestras).",
                label_w=250, width=940, note_kind="gold", foot=SINT)


def se147_disponibilidad() -> Fig:
    return grouped_bars("Disponibilidad: cuánta caída permite cada objetivo y cómo se compone",
                        "Barras horizontales con los minutos de caída permitidos por mes de 30 días: 432 con 99 por ciento, 216 con 99,5, 43,2 con 99,9, 21,6 con 99,95 y 4,3 con 99,99, y unos 130 minutos para tres servicios en serie de 99,9 por ciento que dan 99,70 por ciento conjunto.",
                        ["99 % (87,6 h al año)", "99,5 % (43,8 h al año)", "99,9 % (8,76 h al año)", "99,95 % (4,38 h al año)", "99,99 % (0,88 h al año)", "3 servicios en serie de 99,9 % (99,70 % conjunto)"],
                        [("Caída permitida por mes", [432, 216, 43.2, 21.6, 4.3, 130], "teal")],
                        unit="minutos de caída por mes de 30 días", horizontal=True, label_w=300,
                        note="Con los mismos incidentes simulados (semilla 1473), 85,8 % de los meses cumplió 99,9 % mensual, pero 99,8 % de los años cumplió 99,9 % anual. El objetivo no es completo sin su ventana de medición.",
                        note_kind="gold", foot=SINT)


def se147_pbkdf2() -> Fig:
    items = [("1 000 iteraciones", 0.9, "teal", "0,9 ms"), ("10 000 iteraciones", 8.4, "teal", "8,4 ms"),
             ("100 000 iteraciones", 99.6, "gold", "99,6 ms"), ("600 000 iteraciones", 570.3, "coral", "570 ms")]
    return bars("Costo de PBKDF2-HMAC-SHA-256 al verificar una contraseña (Windows 11, una corrida)",
                "Barras con el tiempo de una derivación PBKDF2 con SHA-256: 0,9 milisegundos con mil iteraciones, 8,4 con diez mil, 99,6 con cien mil y 570 con seiscientas mil; en Ubuntu fueron 0,7, 10,4, 85,8 y 544.",
                items, 0.85, "El valor de 600 000 iteraciones que recomienda OWASP para este algoritmo cuesta unos 570 ms por intento en este equipo; un requisito de «login en menos de 300 ms» y otro de «seguir la guía de OWASP» no pueden cumplirse a la vez sin cambiar algoritmo, hardware o umbral.",
                label_w=250, width=940, note_kind="coral", foot=MEDIDO)


# ---------------------------------------------------------------- SE-148
def se148_caminos() -> Fig:
    return grouped_bars("Escenarios de un caso de uso de entrega: de 1 flujo a 16 caminos con 7 alternativas",
                        "Barras agrupadas con los caminos completos del caso de uso entregar una tarea al añadir cuatro puntos de decisión con siete alternativas: 1, 3, 7, 15 y 16 caminos, con 0, 2, 2, 2 y 1 alternativas añadidas en cada paso.",
                        ["Solo el flujo principal (8 pasos)", "+ «guardar»", "+ «revisar plazo»", "+ «validar tamaño»", "+ «validar formato»"],
                        [("Alternativas añadidas en el paso", [0, 2, 2, 2, 1], "gold"), ("Caminos completos acumulados", [1, 3, 7, 15, 16], "teal")],
                        unit="cantidad",
                        note="Guardar: sesión expirada (vuelve) y almacenamiento caído (termina). Revisar plazo: en gracia (vuelve) y vencido (termina). Validar tamaño: comprimible (vuelve) y demasiado grande (termina). Validar formato: no admitido (termina). Las alternativas que vuelven al flujo multiplican los caminos; las que terminan solo los suman. Cubrir cada alternativa una vez exige 5 escenarios; cubrir todas las combinaciones exige 16.",
                        note_kind="gold", foot=SINT)


def se148_valor() -> Fig:
    return grouped_bars("Historias completas disponibles al final de cada iteración (5 historias, 3 capas, 5 unidades por iteración)",
                        "Barras agrupadas con las historias entregadas con valor visible tras cada una de tres iteraciones: cortar por capas da 0, 0 y 5, y cortar por rebanadas verticales da 1, 3 y 5; las dos terminan igual pero solo la vertical muestra algo antes.",
                        ["Iteración 1", "Iteración 2", "Iteración 3"],
                        [("Por capas (datos, reglas, interfaz)", [0, 0, 5], "coral"), ("Por rebanadas verticales (una historia completa)", [1, 3, 5], "teal")],
                        unit="historias completas",
                        note="Las dos estrategias cuestan lo mismo y terminan igual. La diferencia es cuándo se puede mostrar algo a quien lo usará y, por tanto, cuándo se puede descubrir un error de requisito. Es un modelo aritmético, no una medición de equipos reales.",
                        note_kind="teal", foot=SINT)


def se148_actores() -> Fig:
    items = [("Estudiante", 7, "teal", "7"), ("Docente", 6, "teal", "6"), ("Soporte", 4, "teal", "4"), ("Administrador (no está en el catálogo)", 3, "coral", "3"),
             ("Coordinación", 2, "teal", "2"), ("Sistema de correo", 2, "teal", "2"), ("Auditoría (sin historias)", 0, "gold", "0"), ("Familia (sin historias)", 0, "gold", "0")]
    return bars("Historias por actor en un backlog sintético de 24 historias",
                "Barras de historias por actor: Estudiante 7, Docente 6, Soporte 4, Administrador 3 aunque no figura en el catálogo, Coordinación 2, Sistema de correo 2, y Auditoría y Familia sin ninguna.",
                items, 40, "Tres historias nombran a un actor que no existe en el catálogo y dos actores del catálogo no tienen historia. Ambos defectos se ven al cruzar la lista de actores con el backlog; ninguno se ve leyendo las historias de una en una.",
                label_w=370, width=980, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-149
def se149_mutantes() -> Fig:
    items = [("1 ejemplo feliz", 0, "coral", "0 de 10"), ("4 clases de equivalencia", 4, "gold", "4 de 10"),
             ("13 casos con fronteras", 10, "teal", "10 de 10"), ("240 casos del dominio", 10, "teal", "10 de 10")]
    return bars("Mutantes de una regla de validación de archivos detectados por cada suite de ejemplos",
                "Barras con 10 mutantes de una validación de subida de archivos: un ejemplo feliz detecta 0, cuatro clases de equivalencia detectan 4 y trece casos con fronteras detectan los 10, igual que 240 casos del dominio.",
                items, 40, "Un ejemplo que pasa no prueba nada sobre los límites. Los 6 mutantes que sobreviven a las clases de equivalencia son errores de «≤» frente a «<», de 10 frente a 11 MB o de mayúsculas en la extensión: solo los ejemplos de frontera los matan.",
                label_w=300, width=940, note_kind="teal", foot=SINT)


def se149_pairwise() -> Fig:
    return grouped_bars("Seis parámetros de prueba: 1 296 combinaciones frente a 18 casos que cubren todos los pares",
                        "Barras agrupadas con el porcentaje de fallas detectadas por tres suites: todas las combinaciones (1296 casos) detectan 100 por ciento de las de dos y de tres factores; una suite voraz de 18 casos cubre los 166 pares y detecta 100 y 47,6 por ciento; 18 casos al azar detectan 81,6 y 39,8.",
                        ["Todas (1 296 casos)", "Pairwise voraz (18 casos)", "18 casos al azar"],
                        [("Fallas de 2 factores", [100, 100, 81.6], "teal"), ("Fallas de 3 factores", [100, 47.6, 39.8], "coral")],
                        unit="% de fallas detectadas",
                        note="La suite voraz cubre 166 de 166 pares y 45,4 % de 732 tercias. Cubrir pares reduce 72 veces el número de casos, pero una falla que exige tres valores a la vez se detecta menos de la mitad de las veces. Los ejemplos de aceptación deben elegirse por riesgo, no solo por combinatoria.",
                        note_kind="gold", foot=SINT)


def se149_redondeo() -> Fig:
    return dumbbell("Redondear una nota a entero: dos implementaciones razonables, tres notas de 61 que difieren",
                    "Puntos unidos con el redondeo de seis notas por dos implementaciones: con 2,5, 4,5 y 6,5 la función round de Python da 2, 4 y 6 y la regla de mitad hacia arriba da 3, 5 y 7, y con 1,5, 3,5 y 5,5 coinciden en 2, 4 y 6; de las 61 notas de 1,0 a 7,0 con un decimal difieren 3.",
                    [("2,5", 2, 3), ("4,5", 4, 5), ("6,5", 6, 7), ("1,5", 2, 2), ("3,5", 4, 4), ("5,5", 6, 6)],
                    unit="nota redondeada", names=("round de Python", "Mitad hacia arriba"), decimals=0,
                    delta=lambda a, b: "difiere" if a != b else "igual", lower_is_better=True,
                    note="Un criterio de aceptación con ejemplos como 6,4 → 6 y 6,6 → 7 lo cumplen ambas implementaciones. Solo un ejemplo en el empate (6,5) distingue la regla. Entre 61 notas, 3 dependen de ese ejemplo.",
                    note_kind="coral", foot="Calculado con round y decimal.ROUND_HALF_UP; idéntico en Windows y Ubuntu.")


# ---------------------------------------------------------------- SE-150
def se150_dependencias() -> Fig:
    return case_cards("Los k primeros por valor/costo no forman un conjunto entregable",
                      "Cuatro conjuntos de los k primeros por valor sobre costo en diez requisitos con dependencias, todos no entregables porque violan dependencias; entre 3 628 800 ordenaciones solo 1000 respetan el grafo y el óptimo con presupuesto 12 entrega valor 27 mientras el voraz promete 33.",
                      [("k = 3: A, C, F", "No entregable: F necesita D", "Falta una dependencia.", "coral"),
                       ("k = 4: A, C, E, F", "No entregable: E necesita B; F necesita D", "Faltan dos dependencias.", "coral"),
                       ("k = 5: A, C, E, F, H", "No entregable: E, F y H necesitan B, D, G", "Faltan tres dependencias.", "coral"),
                       ("k = 6: A, C, E, F, H, J", "No entregable: las mismas dependencias", "Añadir J no resuelve ninguna.", "coral")],
                      note="De 3 628 800 ordenaciones de 10 requisitos solo 1 000 respetan las dependencias. Con presupuesto 12, el voraz ignora el grafo y promete valor 33 (A, C, E, F, H) que no puede entregarse; el mejor conjunto cerrado vale 27 (A, B, C, J).",
                      note_kind="gold", foot=SINT)


def se150_must() -> Fig:
    items = [("Interesado sin sesgo", 12, "teal", "12 de 40"), ("Sesgo 0,1", 16, "teal", "16"), ("Sesgo 0,2", 21, "gold", "21"), ("Sesgo 0,3", 22, "gold", "22"), ("Sesgo 0,4", 26, "coral", "26"),
             ("«Must» si alguien lo pide", 27, "coral", "27"), ("«Must» por mayoría (≥3 de 5)", 22, "gold", "22"), ("«Must» por unanimidad", 10, "teal", "10")]
    return bars("Cinco interesados clasifican 40 requisitos: la inflación de «Must»",
                "Barras con el número de requisitos marcados Must por cinco interesados con sesgos crecientes de 12, 16, 21, 22 y 26 de 40; si basta que alguien lo pida son 27, por mayoría 22 y por unanimidad 10.",
                items, 18, "El mismo mundo produce entre 10 y 27 «Must» según la regla de agregación. Con presupuesto para 12 requisitos, solo un ranking forzado o una regla de corte decide; MoSCoW por sí solo no pone un límite.",
                label_w=310, width=940, note_kind="gold", foot=SINT + " Los sesgos son supuestos del autor.")


def se150_mayoria() -> Fig:
    return grouped_bars("Decidir por mayoría entre alternativas: ciclos y reglas que discrepan",
                        "Barras horizontales con la frecuencia de ciclos de mayoría y desacuerdos: 5,56 por ciento de los perfiles con 3 votantes y 3 alternativas tienen ciclo, pluralidad y Borda discrepan en 25 por ciento, con 5 votantes el ciclo es 6,87 por ciento y con 4 alternativas el 13,99 por ciento no tiene ganador de Condorcet.",
                        ["3 votantes, 3 alternativas: ciclo de mayoría (12 de 216)", "3 votantes, 3 alternativas: pluralidad y Borda eligen distinto (54 de 216)",
                         "5 votantes, 3 alternativas: ciclo (100 000 perfiles)", "5 votantes, 4 alternativas: sin ganador de Condorcet (100 000 perfiles)"],
                        [("Frecuencia", [5.56, 25.0, 6.87, 13.99], "coral")],
                        unit="% de los perfiles", horizontal=True, label_w=340, decimals=2,
                        note="Que A venza a B, B a C y C a A no es un error de cómputo: es una propiedad de las preferencias agregadas. Una negociación que pide «lo que apoye la mayoría» puede no tener respuesta, o tener una distinta según el método.",
                        note_kind="coral", foot="Perfiles de preferencias sintéticos con todas las permutaciones equiprobables (semillas 1502 y 1503); supuesto de cultura imparcial.")


FIGURES = {
    "se-145-cobertura-de-elicitacion.svg": se145_cobertura,
    "se-145-revision-independiente-o-desigual.svg": se145_revision,
    "se-145-restricciones-en-conflicto.svg": se145_conflictos,
    "se-146-tabla-de-decision-con-huecos.svg": se146_tabla,
    "se-146-medianoche-que-no-existe.svg": se146_medianoche,
    "se-146-mutantes-ejemplos-o-fronteras.svg": se146_mutantes,
    "se-147-media-frente-a-percentil.svg": se147_percentil,
    "se-147-disponibilidad-y-ventana.svg": se147_disponibilidad,
    "se-147-costo-de-pbkdf2.svg": se147_pbkdf2,
    "se-148-caminos-de-un-caso-de-uso.svg": se148_caminos,
    "se-148-valor-por-iteracion.svg": se148_valor,
    "se-148-actores-sin-historia.svg": se148_actores,
    "se-149-mutantes-segun-la-suite.svg": se149_mutantes,
    "se-149-pairwise-frente-a-completo.svg": se149_pairwise,
    "se-149-redondeo-mitad-arriba.svg": se149_redondeo,
    "se-150-dependencias-y-top-k.svg": se150_dependencias,
    "se-150-inflacion-de-must.svg": se150_must,
    "se-150-ciclos-de-mayoria.svg": se150_mayoria,
}
