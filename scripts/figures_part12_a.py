"""Figures for SE-145 to SE-150 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3 unless a timing is shown)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab
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
    rows = [["1", "39,1 %", "39,2 %", "0,1"], ["2", "62,9 %", "55,8 %", "−7,1"], ["3", "77,4 %", "64,7 %", "−12,7"],
            ["4", "86,2 %", "70,4 %", "−15,8"], ["5", "91,6 %", "74,1 %", "−17,5"], ["6", "94,9 %", "77,1 %", "−17,8"]]
    return tab("Revisar con más personas: modelo independiente frente a defectos de dificultad desigual",
               "Tabla de la fracción de 30 defectos hallada por 1 a 6 revisores: el modelo de independencia predice 39,1, 62,9, 77,4, 86,2, 91,6 y 94,9 por ciento; la simulación con dificultad desigual da 39,2, 55,8, 64,7, 70,4, 74,1 y 77,1.",
               ["Revisores", "Predicción 1−(1−p)^k", "Simulación (5 000 corridas)", "Diferencia (puntos)"], rows, [140, 280, 300, 200], row_h=40, size=13,
               note="El modelo independiente usa la probabilidad media (0,391) para todos los defectos. Cuando algunos son difíciles para todos, los revisores adicionales repiten los mismos aciertos: con seis personas la simulación se queda 17,8 puntos por debajo.", note_kind="gold", foot=SINT)


def se145_conflictos() -> Fig:
    rows = [["Retención (días)", "≥ 730 (Auditoría)", "≤ 365 (Privacidad)", "Conflicto"],
            ["Cupo por entrega (MB)", "≥ 50 (Docencia)", "≤ 25 (Operaciones)", "Conflicto"],
            ["Intentos de acceso", "≥ 8 (Estudiantes)", "≤ 5 (Seguridad)", "Conflicto"],
            ["Tiempo de respuesta (ms)", "≥ 800 (Seguridad)", "≤ 1 500 (Estudiantes)", "Factible: 800–1 500"],
            ["Ventana de edición (h)", "≥ 48 (Estudiantes)", "≤ 48 (Auditoría)", "Factible: solo 48"]]
    return tab("Restricciones de cinco interesados sobre cinco parámetros: intersección de intervalos",
               "Tabla de cinco parámetros con cotas inferior y superior de distintos interesados: retención, cupo e intentos de acceso tienen intersección vacía; tiempo de respuesta admite 800 a 1500 milisegundos y la ventana de edición exactamente 48 horas.",
               ["Parámetro", "Cota inferior más alta", "Cota superior más baja", "Resultado"], rows, [250, 250, 260, 190], row_h=44, size=13,
               kinds=["plain", "plain", "plain", ("coral", "coral", "coral", "teal", "gold")],
               note="Tres de cinco parámetros no tienen valor posible: ninguna negociación de redacción los arregla, hay que cambiar una de las dos cotas o separar casos (por ejemplo, archivo legal frente a datos de operación). El caso «solo 48 h» es factible pero frágil.", note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-146
def se146_tabla() -> Fig:
    rows = [["En gracia, sin prórroga, sin adaptación", "R2", "−10 % de nota", "Una regla: correcto"],
            ["En gracia, con prórroga, sin reentrega ni adaptación", "ninguna", "—", "Hueco: ¿qué pasa?"],
            ["En gracia, con prórroga, con reentrega, sin adaptación", "ninguna", "—", "Hueco: ¿qué pasa?"],
            ["En gracia, sin prórroga, con adaptación", "R2 y R5", "−10 % y sin penalización", "Conflicto de resultado"],
            ["En gracia, sin prórroga, con reentrega y adaptación", "R2 y R5", "−10 % y sin penalización", "Conflicto de resultado"]]
    return tab("Tabla de decisión de la penalización por entrega tardía: 24 combinaciones, 4 defectuosas",
               "Tabla con cinco de las 24 combinaciones de estado, prórroga, reentrega y adaptación: dos no tienen regla aplicable y dos activan a la vez R2 y R5 con resultados distintos; las otras 20 combinaciones se resuelven con una sola regla.",
               ["Combinación", "Reglas aplicables", "Resultado", "Diagnóstico"], rows, [380, 150, 210, 210], row_h=48, size=13,
               kinds=["plain", "plain", "plain", ("teal", "coral", "coral", "coral", "coral")],
               note="Cinco reglas redactadas con sentido común dejan 2 de 24 combinaciones sin respuesta y 2 con respuestas contradictorias. Ninguna regla es incorrecta por separado: el defecto está en la combinación, y solo la enumeración lo muestra.", note_kind="coral", foot=SINT)


def se146_medianoche() -> Fig:
    rows = [["Santiago de Chile", "00:00", "364", "0", "1 (6 sep)"], ["Santiago de Chile", "23:59", "364", "1 (4 abr)", "0"],
            ["Nueva York", "02:30", "364", "0", "1 (8 mar)"], ["Nueva York", "00:00", "365", "0", "0"],
            ["UTC", "cualquiera", "365", "0", "0"]]
    return tab("Una hora local de plazo en 2026: cuántos días existe, se repite o no existe",
               "Tabla de 365 días de 2026 por zona y hora local: medianoche en Santiago no existe una vez; 23:59 se repite una vez; 02:30 en Nueva York no existe una vez; en UTC siempre existe una sola vez.",
               ["Zona", "Hora local", "Días normales", "Días en que se repite", "Días en que no existe"], rows, [220, 140, 160, 220, 200], row_h=40, size=13,
               note="El día calendario local de Santiago midió 24 h en 363 días, 25 h en uno y 23 h en otro. «Hasta la medianoche» y «dentro de 24 horas» no son el mismo plazo esos dos días; el requisito debe fijar zona y regla.", note_kind="gold", foot="Calculado con zoneinfo (CPython 3.12.9 en Windows y 3.12.3 en Ubuntu); el resultado depende de la versión de la base de zonas.")


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
    rows = [["99 %", "432 min", "87,6 h"], ["99,5 %", "216 min", "43,8 h"], ["99,9 %", "43,2 min", "8,76 h"],
            ["99,95 %", "21,6 min", "4,38 h"], ["99,99 %", "4,3 min", "0,88 h"], ["3 servicios en serie de 99,9 %", "≈ 130 min", "99,70 % conjunto"]]
    return tab("Disponibilidad: cuánta caída permite cada objetivo y cómo se compone",
               "Tabla de tiempo de caída permitido por mes de 30 días y por año según el objetivo de disponibilidad, de 99 a 99,99 por ciento, más el caso de tres servicios en serie de 99,9 por ciento que dan 99,70 por ciento.",
               ["Objetivo", "Caída permitida por mes (30 días)", "Caída permitida por año"], rows, [310, 330, 270], row_h=38, size=13,
               note="Con los mismos incidentes simulados (semilla 1473), 85,8 % de los meses cumplió 99,9 % mensual, pero 99,8 % de los años cumplió 99,9 % anual. El objetivo no es completo sin su ventana de medición.", note_kind="gold", foot=SINT)


def se147_pbkdf2() -> Fig:
    items = [("1 000 iteraciones", 0.9, "teal", "0,9 ms"), ("10 000 iteraciones", 8.4, "teal", "8,4 ms"),
             ("100 000 iteraciones", 99.6, "gold", "99,6 ms"), ("600 000 iteraciones", 570.3, "coral", "570 ms")]
    return bars("Costo de PBKDF2-HMAC-SHA-256 al verificar una contraseña (Windows 11, una corrida)",
                "Barras con el tiempo de una derivación PBKDF2 con SHA-256: 0,9 milisegundos con mil iteraciones, 8,4 con diez mil, 99,6 con cien mil y 570 con seiscientas mil; en Ubuntu fueron 0,7, 10,4, 85,8 y 544.",
                items, 0.85, "El valor de 600 000 iteraciones que recomienda OWASP para este algoritmo cuesta unos 570 ms por intento en este equipo; un requisito de «login en menos de 300 ms» y otro de «seguir la guía de OWASP» no pueden cumplirse a la vez sin cambiar algoritmo, hardware o umbral.",
                label_w=250, width=940, note_kind="coral", foot=MEDIDO)


# ---------------------------------------------------------------- SE-148
def se148_caminos() -> Fig:
    rows = [["Solo el flujo principal (8 pasos)", "—", "1"], ["Tras añadir «guardar»: sesión expirada (vuelve), almacenamiento caído (termina)", "2", "3"],
            ["Tras añadir «revisar plazo»: en gracia (vuelve), vencido (termina)", "2", "7"],
            ["Tras añadir «validar tamaño»: comprimible (vuelve), demasiado grande (termina)", "2", "15"],
            ["Tras añadir «validar formato»: no admitido (termina)", "1", "16"]]
    return tab("Escenarios de un caso de uso de entrega: de 1 flujo a 16 caminos con 7 alternativas",
               "Tabla acumulada del caso de uso entregar una tarea: al añadir cuatro puntos de decisión con siete alternativas, el número de caminos completos pasa de 1 a 3, 7, 15 y 16.",
               ["Decisión añadida", "Alternativas", "Caminos completos"], rows, [560, 150, 200], row_h=46, size=13,
               note="Las alternativas que vuelven al flujo multiplican los caminos; las que terminan solo los suman. Cubrir cada alternativa una vez exige 5 escenarios; cubrir todas las combinaciones exige 16. El requisito debe decir cuál se promete.", note_kind="gold", foot=SINT)


def se148_valor() -> Fig:
    rows = [["Por capas (datos, reglas, interfaz)", "0", "0", "5"], ["Por rebanadas verticales (una historia completa)", "1", "3", "5"]]
    return tab("Historias completas disponibles al final de cada iteración (5 historias, 3 capas, 5 unidades por iteración)",
               "Tabla de historias entregadas con valor visible tras cada una de tres iteraciones: cortar por capas da 0, 0 y 5; cortar por rebanadas verticales da 1, 3 y 5.",
               ["Estrategia de corte", "Iteración 1", "Iteración 2", "Iteración 3"], rows, [450, 150, 150, 150], row_h=52, size=13,
               note="Las dos estrategias cuestan lo mismo y terminan igual. La diferencia es cuándo se puede mostrar algo a quien lo usará y, por tanto, cuándo se puede descubrir un error de requisito. Es un modelo aritmético, no una medición de equipos reales.", note_kind="teal", foot=SINT)


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
    rows = [["Todas las combinaciones", "1 296", "100 % (por definición)", "100 % (por definición)"],
            ["Pairwise voraz (cubre 166 de 166 pares)", "18", "100 %", "47,6 % (cubre 45,4 % de 732 tercias)"],
            ["18 casos elegidos al azar", "18", "81,6 %", "39,8 %"]]
    return tab("Seis parámetros de prueba: 1 296 combinaciones frente a 18 casos que cubren todos los pares",
               "Tabla con 6 parámetros de prueba: el producto completo tiene 1296 combinaciones; una suite voraz de 18 casos cubre los 166 pares y el 45,4 por ciento de las 732 tercias; detecta 100 por ciento de fallas de dos factores y 47,6 de tres.",
               ["Suite", "Casos", "Detecta fallas de 2 factores", "Detecta fallas de 3 factores"], rows, [310, 100, 260, 300], row_h=52, size=13,
               note="Cubrir pares reduce 72 veces el número de casos, pero una falla que exige tres valores a la vez se detecta menos de la mitad de las veces. Los ejemplos de aceptación deben elegirse por riesgo, no solo por combinatoria.", note_kind="gold", foot=SINT)


def se149_redondeo() -> Fig:
    rows = [["2,5", "2 (round de Python)", "3 (mitad hacia arriba)", "Difiere"], ["4,5", "4", "5", "Difiere"], ["6,5", "6", "7", "Difiere"],
            ["3,5", "4", "4", "Igual"], ["5,5", "6", "6", "Igual"], ["1,5", "2", "2", "Igual"]]
    return tab("Redondear una nota a entero: dos implementaciones razonables, tres notas de 61 que difieren",
               "Tabla de redondeo de notas a entero: con 2,5, 4,5 y 6,5 la función round de Python da 2, 4 y 6 y la regla de mitad hacia arriba da 3, 5 y 7; con 1,5, 3,5 y 5,5 coinciden; de las 61 notas de 1,0 a 7,0 con un decimal difieren 3.",
               ["Nota", "Implementación A", "Implementación B", "Resultado"], rows, [130, 280, 290, 200], row_h=38, size=13,
               kinds=["plain", "plain", "plain", ("coral", "coral", "coral", "teal", "teal", "teal")],
               note="Un criterio de aceptación con ejemplos como 6,4 → 6 y 6,6 → 7 lo cumplen ambas implementaciones. Solo un ejemplo en el empate (6,5) distingue la regla. Entre 61 notas, 3 dependen de ese ejemplo.", note_kind="coral", foot="Calculado con round y decimal.ROUND_HALF_UP; idéntico en Windows y Ubuntu.")


# ---------------------------------------------------------------- SE-150
def se150_dependencias() -> Fig:
    rows = [["3", "A, C, F", "F necesita D", "No entregable"], ["4", "A, C, E, F", "E necesita B; F necesita D", "No entregable"],
            ["5", "A, C, E, F, H", "E, F y H necesitan B, D, G", "No entregable"], ["6", "A, C, E, F, H, J", "las mismas", "No entregable"]]
    return tab("Los k primeros por valor/costo no forman un conjunto entregable",
               "Tabla de diez requisitos con dependencias: los 3, 4, 5 y 6 primeros por valor sobre costo violan dependencias; entre 3 628 800 ordenaciones solo 1000 respetan el grafo y el óptimo con presupuesto 12 entrega valor 27 mientras el voraz promete 33 sin poder entregarlo.",
               ["k", "Conjunto", "Dependencias que faltan", "Estado"], rows, [80, 250, 380, 200], row_h=40, size=13,
               kinds=["plain", "plain", "plain", "coral"],
               note="De 3 628 800 ordenaciones de 10 requisitos solo 1 000 respetan las dependencias. Con presupuesto 12, el voraz ignora el grafo y promete valor 33 (A, C, E, F, H) que no puede entregarse; el mejor conjunto cerrado vale 27 (A, B, C, J).", note_kind="gold", foot=SINT)


def se150_must() -> Fig:
    items = [("Interesado sin sesgo", 12, "teal", "12 de 40"), ("Sesgo 0,1", 16, "teal", "16"), ("Sesgo 0,2", 21, "gold", "21"), ("Sesgo 0,3", 22, "gold", "22"), ("Sesgo 0,4", 26, "coral", "26"),
             ("«Must» si alguien lo pide", 27, "coral", "27"), ("«Must» por mayoría (≥3 de 5)", 22, "gold", "22"), ("«Must» por unanimidad", 10, "teal", "10")]
    return bars("Cinco interesados clasifican 40 requisitos: la inflación de «Must»",
                "Barras con el número de requisitos marcados Must por cinco interesados con sesgos crecientes de 12, 16, 21, 22 y 26 de 40; si basta que alguien lo pida son 27, por mayoría 22 y por unanimidad 10.",
                items, 18, "El mismo mundo produce entre 10 y 27 «Must» según la regla de agregación. Con presupuesto para 12 requisitos, solo un ranking forzado o una regla de corte decide; MoSCoW por sí solo no pone un límite.",
                label_w=310, width=940, note_kind="gold", foot=SINT + " Los sesgos son supuestos del autor.")


def se150_mayoria() -> Fig:
    rows = [["3 votantes, 3 alternativas: perfiles con ciclo de mayoría", "12 de 216", "5,56 %"],
            ["3 votantes, 3 alternativas: pluralidad y Borda eligen distinto", "54 de 216", "25,0 %"],
            ["5 votantes, 3 alternativas (100 000 perfiles al azar): ciclo", "—", "6,87 %"],
            ["5 votantes, 4 alternativas (100 000 perfiles): sin ganador de Condorcet", "—", "13,99 %"]]
    return tab("Decidir por mayoría entre alternativas: ciclos y reglas que discrepan",
               "Tabla de frecuencia de ciclos de mayoría: con 3 votantes y 3 alternativas ocurren en 12 de 216 perfiles, 5,56 por ciento; pluralidad y Borda discrepan en 25 por ciento; con 5 votantes sube a 6,87 por ciento y con 4 alternativas el 13,99 por ciento no tiene ganador de Condorcet.",
               ["Situación", "Casos", "Frecuencia"], rows, [610, 150, 150], row_h=48, size=13,
               note="Que A venza a B, B a C y C a A no es un error de cómputo: es una propiedad de las preferencias agregadas. Una negociación que pide «lo que apoye la mayoría» puede no tener respuesta, o tener una distinta según el método.", note_kind="coral", foot="Perfiles de preferencias sintéticos con todas las permutaciones equiprobables (semillas 1502 y 1503); supuesto de cultura imparcial.")


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
