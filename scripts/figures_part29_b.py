"""Figures for SE-355 to SE-360 (synthetic models with fixed seeds; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Modelo sintético con semilla fija; Windows y Ubuntu (WSL2) con cifras idénticas. Los parámetros son supuestos del autor."


# ---------------------------------------------------------------- SE-355
def se355_radio() -> Fig:
    rows = [
        ["Una sola cuenta", "5,54 %", "2,28"],
        ["Una cuenta por entorno", "0 %", "1,39"],
        ["Una cuenta por entorno y servicio", "0 %", "1,06"],
    ]
    return tab("Un error cometido en desarrollo o preproducción (20 000 ensayos): ¿llega a producción?",
               "Tabla: si el 5 por ciento de las acciones son comodines que afectan a todo lo que la credencial alcanza, en una sola cuenta el 5,54 por ciento de los errores hechos en desarrollo o preproducción toca producción y afecta en promedio 2,28 recursos; con una cuenta por entorno ninguno toca producción y afecta 1,39; con una por entorno y servicio, 1,06.",
               ["Estructura de cuentas", "Errores que tocan producción", "Recursos afectados por error"], rows, [380, 280, 260], row_h=44, size=13,
               note="La frontera de la cuenta no evita el error, acota su alcance: con una cuenta por entorno el comodín destruye más en desarrollo, pero ya no cruza. Los 24 recursos (3 entornos, 4 servicios, 2 clases), el 5 % de acciones comodín y la intención uniforme son supuestos del autor.",
               note_kind="teal", foot=SINT)


def se355_divergencia() -> Fig:
    rows = [
        ["Sin promoción", "0,1", "38,0", "3,34"],
        ["Sin promoción", "0,3", "48,3", "9,32"],
        ["Sin promoción", "0,6", "50,5", "17,39"],
        ["Con promoción cada 4 semanas", "0,1", "5,0", "0"],
        ["Con promoción cada 4 semanas", "0,3", "13,7", "0"],
        ["Con promoción cada 4 semanas", "0,6", "24,1", "0"],
    ]
    return tab("Divergencia entre preproducción y producción en 52 semanas (72 claves que deberían coincidir; media de 300 años)",
               "Tabla: sin una promoción que copie la configuración, con una edición manual cada diez semanas hay divergencia en 38 de 52 semanas y quedan 3,34 claves distintas al final; con una edición cada dos semanas y media, 50,5 semanas y 17,39 claves; con una promoción cada cuatro semanas, las claves distintas al final son 0 y las semanas con divergencia bajan a 5,0, 13,7 y 24,1.",
               ["Proceso", "Ediciones manuales por semana", "Semanas con divergencia", "Claves distintas al final"], rows, [300, 230, 210, 190], row_h=40, size=12,
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
    rows = [
        ["Fijo en el pico diurno (12 instancias)", "1,64 %", "2 016"],
        ["Fijo en el pico de los picos (30)", "0 %", "5 040"],
        ["Reactivo, arranque inmediato", "0 %", "1 910"],
        ["Reactivo, arranque de 2 minutos", "0,34 %", "1 866"],
        ["Reactivo, arranque de 5 minutos", "0,84 %", "1 813"],
        ["Programado (solo la curva diaria)", "1,85 %", "1 762"],
    ]
    return tab("Siete días de tráfico con picos: demanda sin atender e instancias-hora según la política",
               "Tabla: con 12 instancias fijas queda sin atender el 1,64 por ciento de la demanda y se gastan 2 016 instancias-hora; con 30 fijas no queda nada y se gastan 5 040; un escalado reactivo sin retardo no deja nada con 1 910, y con arranques de 2 y 5 minutos deja 0,34 y 0,84 por ciento con 1 866 y 1 813; el programado deja 1,85 con 1 762.",
               ["Política", "Demanda sin atender", "Instancias-hora"], rows, [450, 230, 190], row_h=44, size=13,
               note="El arranque tarda y eso se paga en demanda perdida: cada minuto de retardo añade unos 0,17 puntos porcentuales de demanda perdida en este tráfico. Reservar para el peor pico cuesta 2,6 veces más que escalar con reacción. Capacidad de 20 solicitudes por segundo por instancia, objetivo del 60 % y picos de 2,5 a 4 veces son supuestos del autor.",
               note_kind="gold", foot=SINT)


def se356_cola() -> Fig:
    rows = [
        ["50 %", "2,00 / 2,00", "9,3 / 9,2"],
        ["70 %", "3,35 / 3,33", "15,6 / 15,4"],
        ["80 %", "5,07 / 5,00", "23,7 / 23,0"],
        ["90 %", "10,1 / 10,0", "48,3 / 46,1"],
        ["95 %", "20,7 / 20,0", "103 / 92"],
    ]
    return tab("Una cola de un servidor: tiempo en el sistema, en unidades del tiempo de servicio, simulado / teórico",
               "Tabla: con utilización del 50 por ciento el tiempo medio en el sistema es 2 veces el de servicio y el percentil 99 es 9,3; con 80 por ciento es 5,1 y 23,7; con 90 por ciento es 10,1 y 48,3; con 95 por ciento es 20,7 y 103. La teoría da 2, 5, 10 y 20 para la media.",
               ["Utilización", "Media simulada / teórica", "Percentil 99 simulado / teórico"], rows, [260, 320, 340], row_h=44, size=13,
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
    rows = [
        ["Un proveedor (99,95 %)", "99,95 %", "262,8"],
        ["Dos, conmutación perfecta e instantánea", "99,99998 %", "0,1"],
        ["Dos, la conmutación acierta el 90 % de las veces", "99,995 %", "26,4"],
        ["Dos, pero con un DNS compartido de 99,95 %", "99,95 %", "262,9"],
        ["Dos, exigiendo ambos a la vez (réplica síncrona)", "99,90 %", "525,5"],
    ]
    return tab("Disponibilidad anual al combinar dos proveedores que fallan de forma independiente",
               "Tabla: un proveedor con 99,95 por ciento de disponibilidad pierde 262,8 minutos al año; dos proveedores con conmutación perfecta pierden 0,1; si la conmutación acierta el 90 por ciento de las veces, 26,4; si hay un servicio compartido de 99,95 por ciento, 262,9; y si el servicio necesita ambos a la vez, 525,5.",
               ["Composición", "Disponibilidad", "Minutos de caída al año"], rows, [490, 200, 220], row_h=44, size=13,
               note="Redundancia en paralelo ayuda mucho solo si la conmutación funciona y nada se comparte; una dependencia en serie con el mismo 99,95 % anula el beneficio, y exigir ambos lo empeora al doble. El cálculo se verificó con 35 millones de horas simuladas. La independencia de fallos y los 99,95 % son supuestos del autor, no medidas de un proveedor.",
               note_kind="coral", foot=SINT)


def se357_interseccion() -> Fig:
    rows = [
        ["20 funciones básicas (cada proveedor ofrece 18)", "14,6 de 20"],
        ["20 funciones avanzadas (cada proveedor ofrece 12)", "4,3 de 20"],
        ["Las 40 funciones", "18,8 de 40"],
        ["Casos de prueba: 40 en un proveedor; 3 proveedores × 40", "120 frente a 56 con el común"],
    ]
    return tab("Funciones que ofrecen a la vez tres proveedores ficticios (media de 2 000 sorteos)",
               "Tabla: con tres proveedores que ofrecen cada función básica con probabilidad 0,9 y cada avanzada con 0,6, a la vez ofrecen 14,6 de 20 básicas y 4,3 de 20 avanzadas, 18,8 de 40; probar las 40 funciones en cada uno son 120 casos frente a 56 si se limita a lo común.",
               ["Conjunto", "Funciones que ofrecen los tres"], rows, [560, 360], row_h=44, size=13,
               note="El mínimo común denominador se lleva más de la mitad de las funciones: 21 de 40 quedan fuera por no estar en alguno. Portabilidad total sale a costa de no usar lo que justificó elegir el proveedor. Los proveedores son ficticios y las probabilidades supuestos del autor; no se comparó ninguna oferta real.",
               note_kind="gold", foot=SINT)


def se357_gravedad() -> Fig:
    rows = [
        ["0,1 TB", "3,2 h", "0,3 h", "8"],
        ["1 TB", "31,7 h", "3,2 h", "80"],
        ["10 TB", "317,5 h (13 días)", "31,7 h", "800"],
        ["100 TB", "3 175 h (132 días)", "317,5 h (13 días)", "8 000"],
    ]
    return tab("Mover datos entre proveedores: tiempo con 70 % de eficiencia y coste de salida (0,08 por GB)",
               "Tabla: mover 0,1 terabytes por un enlace de 100 megabits por segundo toma 3,2 horas y por uno de 1 gigabit 0,3; 10 terabytes toman 317,5 horas con 100 megabits y 31,7 con 1 gigabit; 100 terabytes toman 3 175 horas con 100 megabits y 317,5 con 1 gigabit; el coste de salida crece de 8 a 8 000 unidades.",
               ["Volumen", "A 100 Mbps", "A 1 Gbps", "Salida (u.m.)"], rows, [210, 300, 250, 160], row_h=44, size=13,
               note="Los datos no se mueven tan rápido como el código: 100 TB tardan 13 días incluso a 1 Gbps. Además la luz limita la latencia: 8 000 km imponen al menos 80 ms de ida y vuelta por la fibra, 20 ms con 2 000 km. El precio de 0,08 por GB es una unidad inventada y la eficiencia del 70 % un supuesto.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-358
def se358_camino() -> Fig:
    rows = [
        ["A mano, 23 pasos (2 % de error por paso)", "62,6 % (62,8 % teórico)", "5,5 h", "6,8 h"],
        ["Camino dorado, 5 pasos (2 %)", "90,5 % (90,4 %)", "0,28 h", "0,50 h"],
        ["Camino dorado, 5 pasos (1 %)", "95,0 % (95,1 %)", "0,28 h", "0,40 h"],
    ]
    return tab("Crear un primer servicio listo para producción: éxito sin retrabajo y tiempo (20 000 ensayos por fila)",
               "Tabla: con 23 pasos manuales y un 2 por ciento de error por paso, el 62,6 por ciento llega sin retrabajo y la mediana es 5,5 horas; con un camino dorado de 5 pasos y el mismo error, el 90,5 por ciento y 0,28 horas; con 1 por ciento, el 95,0.",
               ["Camino", "Sin ningún error", "Mediana", "Percentil 90"], rows, [430, 220, 120, 130], row_h=52, size=13,
               note="El camino dorado gana porque tiene menos pasos que equivocarse, no porque las personas acierten más: lo que se elimina es la oportunidad de error. Los 23 y 5 pasos, el 2 % y los tiempos son supuestos del autor, no medidas de personas ni de un equipo real.",
               note_kind="teal", foot=SINT)


def se358_cola() -> Fig:
    rows = [
        ["20 %", "166", "83 %", "0,50", "1,40"],
        ["50 %", "115", "58 %", "0,06", "0,23"],
        ["80 %", "64", "32 %", "0,01", "0,00"],
        ["95 %", "38,5", "19 %", "0,00", "0,00"],
    ]
    return tab("Equipo de plataforma de 4 personas y 100 servicios: espera por soporte según cuántos usan el camino dorado",
               "Tabla: si el 20 por ciento de los servicios usa el camino dorado llegan 166 solicitudes al mes, el equipo trabaja al 83 por ciento y la espera media es 0,50 días hábiles con percentil 90 de 1,40; con el 50 por ciento llegan 115, 58 por ciento y 0,06 días; con 80 por ciento, 64 y 0,01; con 95 por ciento, 38,5.",
               ["Servicios en el camino", "Solicitudes al mes", "Uso del equipo", "Espera media (días)", "Percentil 90"], rows, [260, 190, 170, 170, 130], row_h=44, size=13,
               note="La espera no baja de forma lineal: de 20 a 50 % se divide por ocho y de 50 a 95 % ya es casi cero, porque el equipo sale de la zona de saturación. Las 0,3 y 2,0 solicitudes por servicio al mes y el 0,4 días por solicitud son supuestos del autor.",
               note_kind="gold", foot=SINT)


def se358_verificador() -> Fig:
    rows = [
        ["100 servicios de la plantilla", "5", "5"],
        ["50 servicios escritos a mano", "49", "135"],
        ["5 defectos semánticos (1 000 núcleos, ruta de sonda inexistente, imagen de otro registro, propietario «x», secreto corto)", "0", "0"],
    ]
    return tab("Un verificador de ocho reglas sobre 150 descriptores de servicio sintéticos",
               "Tabla: el verificador de ocho reglas señala 5 violaciones en 5 de los 100 servicios generados desde la plantilla y 135 violaciones en 49 de los 50 escritos a mano; de cinco defectos semánticos, entre ellos un límite de 1 000 núcleos y una sonda con una ruta inexistente, no señala ninguno.",
               ["Conjunto", "Servicios con alguna violación", "Violaciones señaladas"], rows, [560, 190, 170], row_h=92, size=12,
               note="Las ocho reglas detectaron las 25 mutaciones de cada una, y por eso el verificador es útil y a la vez ciego a lo que no es una regla. La plantilla no elimina las violaciones, las reduce al 4 % de ediciones manuales. Las reglas y los defectos los escribí yo: la exactitud sobre código real es desconocida.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-359
def se359_cortes() -> Fig:
    rows = [
        ["Estado solo al final", "66", "66", "78", "78"],
        ["Estado tras cada recurso", "0", "0", "12", "12"],
        ["Intención antes, confirmación después", "0", "0", "0 (12 sospechosos)", "12"],
    ]
    return tab("Una creación de 12 recursos interrumpida en cada paso: restos sin rastro y conflictos al reintentar",
               "Tabla: interrumpir 12 veces la creación de 12 recursos antes de crear el recurso fallido deja 66 restos sin rastro y 66 conflictos al reintentar si el estado se guarda solo al final, y 0 y 0 si se guarda tras cada recurso o con intención previa; interrumpir después de crear y antes de anotar deja 78 y 78, 12 y 12, y 0 con 12 sospechosos y 12 conflictos.",
               ["Estrategia de estado", "Corte antes de crear: restos", "conflictos", "Corte tras crear y antes de anotar: restos", "conflictos"], rows, [250, 150, 120, 230, 120], row_h=60, size=12,
               note="Guardar el estado tras cada recurso elimina el caso fácil y deja el difícil: el recurso creado cuyo registro no llegó. Anotar la intención antes de crear lo vuelve un sospechoso que se puede reconciliar, aunque el reintento sigue chocando con él hasta que se reconcilia. Los recursos son carpetas locales, no recursos de una nube.",
               note_kind="coral", foot=SINT)


def se359_destruccion() -> Fig:
    rows = [
        ["Orden al azar (5 000 órdenes)", "13,73", "3,88", "0 %"],
        ["Inverso del orden de dependencias", "0", "1", "100 %"],
    ]
    return tab("Destruir 12 recursos con dependencias: intentos rechazados y pasadas necesarias",
               "Tabla: destruir los 12 recursos en un orden al azar provoca en promedio 13,73 intentos rechazados por dependientes que siguen vivos, necesita 3,88 pasadas y nunca sale sin fallos en 5 000 órdenes; destruir en el inverso del orden de dependencias no provoca ninguno y necesita una pasada.",
               ["Orden de destrucción", "Rechazos medios", "Pasadas medias", "Órdenes sin ningún rechazo"], rows, [380, 190, 190, 190], row_h=52, size=13,
               note="Un bucle que reintenta hasta que no quede nada oculta el orden equivocado: termina, con casi cuatro pasadas y trece rechazos. Pero sin una señal de qué falló no se distingue ese caso de un recurso atascado. El grafo de 12 recursos y sus dependencias es del autor y la destrucción es de carpetas locales.",
               note_kind="gold", foot=SINT)


def se359_barrido() -> Fig:
    rows = [
        ["100 %", "0", "100 %", "0"],
        ["95 %", "0,61", "54,0 %", "915"],
        ["80 %", "2,42", "7,3 %", "3 630"],
    ]
    return tab("Barrido por etiqueta de 12 recursos por entorno (2 000 entornos): lo que queda sin etiqueta",
               "Tabla: si todos los recursos llevan la etiqueta del entorno el barrido no deja restos; con el 95 por ciento etiquetados quedan 0,61 recursos por entorno, solo el 54 por ciento de los entornos queda limpio y 100 entornos cuestan 915 unidades en 30 días; con el 80 por ciento quedan 2,42 y 3 630.",
               ["Recursos con la etiqueta", "Restos por entorno", "Entornos sin restos", "Coste de 100 entornos en 30 días (u.m.)"], rows, [230, 200, 220, 270], row_h=52, size=13,
               note="Un barrido por etiqueta solo limpia lo que se dejó etiquetar: con un 95 % de cobertura casi la mitad de los entornos deja algo. Al medio por día por resto, el coste de un resto olvidado es pequeño y el de un resto con datos o con una credencial no se mide en unidades. La cobertura y el coste son supuestos del autor.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-360
def se360_hashes() -> Fig:
    rows = [
        ["Sin normalizar, sin compresión", "0bc289f3", "740aafa8", "No"],
        ["Fechas y orden fijos, sin fijar el sistema", "cf351096", "765d27f7", "No"],
        ["Además se fija el sistema que crea el archivo", "765d27f7", "765d27f7", "Sí"],
        ["Normalizado con deflate, nivel 6", "c3d29a42", "c3d29a42", "Sí"],
        ["Normalizado con deflate, nivel 9", "c3d29a42", "c3d29a42", "Sí"],
    ]
    return tab("SHA-256 del mismo paquete (12 archivos) construido en Windows y en Ubuntu: primeros 8 caracteres",
               "Tabla: construir el mismo paquete de 12 archivos en Windows y en Ubuntu da sumas distintas sin normalizar y también al fijar fechas y orden pero no el sistema que crea el archivo; al fijar además ese campo coinciden, y también coinciden con compresión deflate en los niveles 6 y 9.",
               ["Variante de construcción", "Windows 11", "Ubuntu (WSL2)", "¿Igual?"], rows, [430, 150, 150, 100], row_h=44, size=13,
               note="El campo «versión creada por» del formato ZIP dice 0 en Windows y 3 en Linux: un detalle invisible que cambia la suma. Con zlib 1.3.1 y 1.3 la compresión dio bytes idénticos para este contenido; no se garantiza con otro contenido ni otra versión de zlib. El paquete se generó con semilla, no con archivos del repositorio.",
               note_kind="gold", foot=SINT)


def se360_validador() -> Fig:
    rows = [
        ["Falta una sección, sección vacía, módulo duplicado", "16 de 16 cada uno"],
        ["Hash alterado, tope de gasto no positivo, TTL en cero", "16 de 16 cada uno"],
        ["Versión sin fijar, secreto literal", "16 de 16 cada uno"],
        ["Prueba de destrucción de 2019 (caducada)", "0 de 16"],
        ["Gasto de 10^6 sobre un tope de 100", "0 de 16"],
        ["Evidencia copiada de otro paquete", "0 de 16"],
        ["Límites que dicen «sin límites»", "0 de 16"],
        ["Estado que no corresponde al plan", "0 de 16"],
    ]
    return tab("Un validador de paquetes frente a 208 mutaciones: ocho familias que ve y cinco que no",
               "Tabla: el validador detecta 16 de 16 mutaciones de cada una de ocho familias estructurales, entre ellas sección faltante, hash alterado y secreto literal, y 0 de 16 de cada una de cinco familias que exigen interpretar el contenido, como una prueba de destrucción caducada o un gasto muy superior al tope.",
               ["Defecto sembrado", "Detectado"], rows, [640, 270], row_h=44, size=12,
               note="El validador ve la forma y las coincidencias exactas; no ve la verdad de lo que el paquete afirma. Que apruebe un paquete solo significa que está completo y coherente en forma. Las mutaciones y las reglas las escribí yo, así que 16 de 16 describe estas reglas contra estos defectos, no una cobertura general.",
               note_kind="coral", foot=SINT)


def se360_olvidados() -> Fig:
    rows = [
        ["A mano, sin plazo", "340", "570"],
        ["Plazo de 24 h con barrido diario", "110", "110"],
        ["Plazo de 24 h, el barrido falla el 20 % de los días", "110", "120"],
    ]
    return tab("Gasto de un mes con entornos de laboratorio de 5 unidades por día y un 15 % que se olvida (500 meses)",
               "Tabla: si el 15 por ciento de los entornos se olvida y no hay plazo, el gasto mediano del mes es 340 unidades y el percentil 90 es 570; con un plazo de 24 horas y barrido diario es 110 y 110, que es el mínimo sin olvidos; si el barrido falla el 20 por ciento de los días, 110 y 120.",
               ["Proceso", "Gasto mediano del mes", "Percentil 90"], rows, [500, 230, 190], row_h=52, size=13,
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
