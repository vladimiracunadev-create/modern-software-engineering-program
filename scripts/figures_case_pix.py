"""Figuras del caso de estudio Pix (casos/exito/pix.md).

Contrato igual que scripts/figures_part*_a.py: ``FIGURES`` mapea nombre de archivo -> constructor.
Las cifras salen de documentos públicos del Banco Central do Brasil: los relatórios de gestão del Pix
(2020-2022 y 2023-2025), los relatórios anuais del SPI (2024 y 2025), el Manual de Tempos y el Manual
Operacional del DICT. Cada pie de figura nombra su fuente. Ninguna figura repite una tabla del caso.
"""
from __future__ import annotations

from case_diagrams import canvas, finish, lane_steps, sequence, years
from case_fig_helpers import hub, layer_stack
from figure_cases import case_cards
from figure_kit import grouped_bars, line_chart, timeline
from figures_part45_a import flow

RG = "Fuente: Banco Central do Brasil, Relatório de Gestão do Pix 2023-2025, consulta 2026-11-23."
RG23 = "Fuente: Banco Central do Brasil, Relatório de Gestão do Pix 2020-2022, consulta 2026-11-23."
SPI25 = "Fuente: Banco Central do Brasil, Relatório Anual do SPI 2025, consulta 2026-11-23."
DOCS = "Fuentes: documentos públicos del Banco Central do Brasil citados en el caso (consulta 2026-11-23). Esquema del autor."


def contexto():
    return hub(
        "El Pix entre pagadores, instituciones y el Banco Central",
        "Diagrama de contexto: el pagador inicia el pago desde la aplicación de su institución; la institución del pagador consulta el directorio de claves y envía la orden al sistema de liquidación del Banco Central; la institución del receptor acredita; el Banco Central regula el arreglo y opera el sistema de liquidación y el directorio; los iniciadores de pago y Open Finance se conectan a las instituciones.",
        ("Pix: arreglo de pagos instantáneos regulado y operado por el Banco Central", "navy"),
        [("Pagador: persona, empresa o gobierno con cuenta en un participante", "teal", "inicia"),
         ("Receptor: acredita en segundos, a cualquier hora", "teal", "recibe"),
         ("Participantes del Pix: 214 directos y 693 indirectos en 2025", "gold", "operan cuentas"),
         ("SPI: sistema de liquidación del Banco Central (24 horas, 7 días)", "plain", "liquida"),
         ("DICT: directorio de claves vinculadas a cuentas", "plain", "resuelve"),
         ("Iniciadores de pago y Open Finance", "gold", "inician"),
         ("Foro Pix: gobernanza con los agentes del mercado", "plain", "consulta"),
         ("Fraude y estafas: riesgo que el diseño debe contener", "coral", "amenaza")],
        "Documentado en los informes del Banco Central: el Banco Central definió las reglas y además desarrolla, opera y gestiona la infraestructura del Pix (SPI y DICT); los participantes proveen cuentas, y existen iniciadores de pago y liquidantes especiales. Dónde deja de valer: no muestra volúmenes por actor.",
        RG23)


def mensual():
    return grouped_bars(
        "Pix interbancarios liquidados por el SPI en cada mes de diciembre",
        "Barras en miles de millones de transacciones: 1,22 en diciembre de 2021, 2,42 en 2022, 4,21 en 2023, 5,71 en 2024 y 7,10 en 2025; el crecimiento de 2024 a 2025 fue de 24 por ciento.",
        ["Dic 2021", "Dic 2022", "Dic 2023", "Dic 2024", "Dic 2025"],
        [("Miles de millones de Pix interbancarios", [1.22, 2.42, 4.21, 5.71, 7.10], "teal")],
        unit="miles de millones de transacciones", decimals=2, plot_h=250,
        note="Son solo los Pix entre instituciones distintas, que son los que el SPI liquida; los Pix dentro de una misma institución se liquidan fuera del SPI. Diciembre supera el promedio por el aguinaldo y las fiestas. Dónde deja de valer: es un mes por año, no el promedio anual.",
        foot=SPI25)


def valor():
    return grouped_bars(
        "Valor liquidado por el SPI: 2024, 2025 y el acumulado desde el lanzamiento",
        "Barras en billones de reales: 22,12 en 2024, 29,61 en 2025 y un acumulado de 80,33 billones desde el lanzamiento; a fines de 2024 el acumulado era de 50,72 billones.",
        ["2024", "2025", "Acumulado a fines de 2024", "Acumulado a fines de 2025"],
        [("Billones de reales", [22.12, 29.61, 50.72, 80.33], "navy")],
        unit="billones de reales (R$ 10^12)", decimals=2, plot_h=250,
        note="Cálculo propio: 29,61 sobre 22,12 es un crecimiento de 33,9 % del valor liquidado por el SPI; 50,72 más 29,61 son 80,33. Dónde deja de valer: es solo lo liquidado por el SPI (interbancario); el Pix total de 2025 superó los 35 billones.",
        foot=SPI25)


def total_pix():
    return grouped_bars(
        "Transacciones del Pix, todos los canales, 2024 y 2025",
        "Barras en miles de millones: unas 63 en 2024 y casi 80 en 2025, un aumento de 25,7 por ciento; el valor de 2025 superó 35 billones de reales, 33,8 por ciento más.",
        ["2024 (cálculo propio)", "2025"],
        [("Miles de millones de transacciones", [63.5, 79.8], "teal")],
        unit="miles de millones de transacciones", decimals=1, plot_h=230,
        note="El informe da casi 80 mil millones en 2025 y un aumento de 25,7 %; la cifra de 2024 es el cálculo propio 79,8 entre 1,257. El récord diario fue de 313 339 328 transacciones el 5 de diciembre de 2025. Dónde deja de valer: la cifra de 2025 es «casi 80», no un recuento exacto.",
        foot=RG)


def tickets():
    return grouped_bars(
        "El Pix típico es pequeño: percentiles del valor en diciembre de 2025",
        "Barras en reales y escala logarítmica: la mitad de los Pix liquidados vale menos de 36 reales, el 90 por ciento menos de 400 y el 99 por ciento menos de 3 900; el valor medio fue de 443,29 reales y el mayor Pix individual liquidado fue de 3 500 millones.",
        ["Mediana (50 %)", "Percentil 90", "Valor medio", "Percentil 99"],
        [("Reales por Pix", [36, 400, 443.29, 3900], "gold")],
        unit="reales (escala logarítmica)", log=True, decimals=0, plot_h=240,
        note="El valor medio (443 reales) es mucho mayor que la mediana (36) porque unos pocos pagos grandes arrastran el promedio. Mire la distancia entre la primera y la última barra: más de 100 veces. Dónde deja de valer: son Pix interbancarios liquidados por el SPI en un mes.",
        foot=SPI25)


def usuarios():
    return grouped_bars(
        "Quién usó el Pix en diciembre de 2025 y cuántas claves hay",
        "Barras en millones: 148 millones de personas físicas y 12 millones de empresas hicieron o recibieron un Pix en diciembre de 2025, y había más de 920 millones de claves Pix registradas, 67 por ciento más que en diciembre de 2022.",
        ["Personas físicas activas", "Empresas activas", "Claves registradas"],
        [("Millones", [148, 12, 920], "teal")],
        unit="millones", decimals=0, plot_h=240,
        note="Una persona o empresa puede tener varias claves (hasta cinco por cuenta para personas físicas y hasta veinte para empresas), por eso hay más claves que usuarios. Dónde deja de valer: «más de 920 millones» es un mínimo.",
        foot=RG)


def participantes():
    return years(grouped_bars(
        "Participantes directos del SPI al cierre de cada año",
        "Barras con 111 participantes directos en diciembre de 2021, 124 en 2022, 150 en 2023, 176 en 2024 y 214 en 2025; los indirectos eran 693 a fines de 2025, el 76 por ciento del total.",
        ["2021", "2022", "2023", "2024", "2025"],
        [("Participantes directos", [111, 124, 150, 176, 214], "navy")],
        unit="participantes directos", decimals=0, plot_h=240,
        note="Un participante directo tiene cuenta de liquidación en el Banco Central y conexión directa al SPI; uno indirecto liquida a través de uno directo. A fines de 2025 había 214 directos (23,6 %) y 693 indirectos (76,4 %). Dónde deja de valer: solo cuenta instituciones del SPI, no usuarios.",
        foot=SPI25))


def disponibilidad():
    return grouped_bars(
        "Disponibilidad del SPI frente al mínimo normativo",
        "Barras en porcentaje: el mínimo normativo de disponibilidad es 99,90 por ciento y el índice del SPI cerró diciembre de 2025 en 99,98 por ciento; el sistema debe funcionar las 24 horas de todos los días del año.",
        ["Mínimo normativo", "Diciembre de 2025"],
        [("Disponibilidad (%)", [99.90, 99.98], "teal")],
        unit="% de disponibilidad", decimals=2, plot_h=220,
        note="Mire que la diferencia parece mínima: 0,08 puntos. Con 99,90 % se permite cerca de 8,8 horas de inactividad al año; con 99,98 %, unas 1,8 horas (cálculo propio sobre 8 760 horas). Dónde deja de valer: el índice se calcula sobre los tres últimos meses.",
        foot=SPI25)


def semana():
    return grouped_bars(
        "Cuántos Pix se liquidan por día según el tipo de día (2025)",
        "Barras en millones por día: 225,03 millones en promedio los viernes, 147,61 millones los domingos y 154,35 millones los feriados; los picos horarios están entre las 10 y las 14 horas y entre las 16 y las 19, y la franja de menos actividad va de las 2 a las 6.",
        ["Viernes", "Feriados", "Domingos"],
        [("Millones de Pix liquidados por día", [225.03, 154.35, 147.61], "teal")],
        unit="millones de Pix por día", decimals=2, plot_h=230,
        note="Hay actividad todas las horas del día: no hay momentos de inactividad. Mire que incluso el domingo, el día más bajo, mueve casi 148 millones. Dónde deja de valer: son promedios de Pix interbancarios; el récord de un día completo de 2025 fue mayor.",
        foot=SPI25)


def actores():
    return hub(
        "Quién obtiene qué en el ecosistema del Pix",
        "Diagrama de incentivos: las personas obtienen pagos gratuitos e instantáneos; los comercios un cobro barato; las instituciones un acceso común a todos los clientes del país; los gobiernos una forma de pagar y cobrar; el Banco Central competencia, inclusión y menos efectivo.",
        ("Pix: infraestructura pública con acceso abierto a todas las instituciones", "navy"),
        [("Persona: transfiere gratis, a cualquier hora", "teal", "gana"),
         ("Comercio y empresa: cobro rápido y de menor coste", "teal", "gana"),
         ("Institución grande: pierde parte del poder de su base cerrada", "gold", "compite"),
         ("Institución pequeña o fintech: acceso a toda la red", "gold", "gana"),
         ("Gobierno: pagos y cobros digitales", "plain", "usa"),
         ("Banco Central: regula, opera y recupera costes", "plain", "gestiona"),
         ("Estafador: busca engañar al pagador", "coral", "ataca"),
         ("Efectivo y otros medios: pierden uso", "grey", "ceden")],
        "Análisis propio sobre hechos documentados: el Banco Central lo creó para reducir el uso de efectivo, fomentar la competencia, incentivar la innovación, democratizar el acceso, reducir costes y dar una experiencia simple y segura, y el informe describe el Pix como «gratuito para las personas y de menor coste para las empresas». Dónde deja de valer: el efecto sobre cada institución no se publica.",
        RG23)


def recorridos():
    f = canvas("Cuatro recorridos en el Pix y su caso límite",
               "Cuatro filas de pasos: una persona que paga a un amigo con una clave, un comercio que cobra con un código QR, una empresa que cobra con débito automático y una víctima de una estafa; cada fila termina en un caso límite.")
    y = 56.0
    y = lane_steps(f, y, "Persona", [("Abre la app de su institución", "teal"), ("Escribe la clave del receptor", "teal"), ("Confirma el nombre y el valor", "teal"), ("Pago de noche con límite nocturno", "coral")])
    y = lane_steps(f, y, "Comercio", [("Genera un código QR", "gold"), ("El cliente lo lee con su app", "gold"), ("Confirma y paga", "gold"), ("Pago diferido o con vencimiento", "coral")])
    y = lane_steps(f, y, "Empresa recurrente", [("Pide autorización al pagador (Pix Automático)", "navy"), ("El pagador autoriza una vez", "navy"), ("Se programan cobros", "navy"), ("Cobro rechazado por saldo insuficiente", "coral")])
    y = lane_steps(f, y, "Víctima de estafa", [("Es engañada y paga", "plain"), ("Reclama a su institución", "plain"), ("Se bloquean los fondos (MED)", "plain"), ("Los fondos ya salieron de la cuenta", "coral")])
    return finish(f, y + 4, "Cada fila se lee de izquierda a derecha y la caja coral es el borde. El código QR, el Pix Automático, el límite nocturno y el MED son funciones descritas en los informes de gestión del Banco Central; los casos límite son escenarios del curso. Dónde deja de valer: no mide cuántos usuarios llegan a cada borde.", "Esquema del autor sobre los relatórios de gestão do Pix.")


def negocio():
    return flow(
        "Cómo se financia el Pix: sin comisión para el pagador, con recuperación de costes en el SPI",
        "Flujo del dinero: el pagador no paga por el Pix en el SPI; los participantes directos que reciben el crédito pagan al Banco Central un centavo de real por cada diez Pix liquidados; el Banco Central fija las tarifas solo para recuperar costes de las tecnologías que operan el SPI; las instituciones deciden qué cobran a empresas y qué servicios ofrecen.",
        [[("Pagador: gratuito para las personas", "teal"), ("Institución del pagador: no se tarifa por emitir un Pix", "teal"), ("Institución del receptor: paga R$ 0,01 por cada diez Pix recibidos", "gold"), ("Banco Central: recupera los costes del SPI, sin buscar beneficio", "navy")],
         [("Los Pix que fallan no se tarifan", "plain"), ("Extracto de la cuenta de liquidación: R$ 3,00 por MB", "plain"), ("Empresas: coste menor que con otros medios", "gold"), ("Costes y márgenes de cada institución: no publicados", "grey")]],
        note="Documentado en el informe anual del SPI de 2025 (tarifas) y en el informe de gestión (gratuito para personas y de menor coste para empresas). No se sabe: los ingresos y costes de las instituciones por el Pix. Dónde deja de valer: la tarifa es de la liquidación en el SPI, no de lo que cobra cada banco a sus clientes.",
        foot="Fuentes: Relatório Anual do SPI 2025 y Relatório de Gestão do Pix 2020-2022 (Banco Central do Brasil).", width=960)


def capas():
    return layer_stack(
        "Capas del Pix que el Banco Central describe",
        "Pila de capas: aplicaciones de las instituciones; la red del sistema financiero nacional con proveedores de servicios de tecnología; el SPI, que liquida cada pago de forma bruta en tiempo real; el DICT, el directorio de claves; y el sistema de reservas y el Selic para dar liquidez a las cuentas de liquidación.",
        [("Aplicaciones", "Banco, fintech o billetera del pagador y del receptor; código QR; iniciadores de pago", "teal"),
         ("Participantes", "Instituciones con cuentas de clientes; 214 directos y 693 indirectos (2025)", "plain"),
         ("Conectividad", "Red del Sistema Financiero Nacional (RSFN) o proveedores de servicios de tecnología homologados", "plain"),
         ("Liquidación y claves", "SPI: liquidación bruta en tiempo real, irrevocable; DICT: claves vinculadas a cuentas", "gold"),
         ("Liquidez", "Cuentas PI en el Banco Central; aportes por el STR y el Selic", "navy")],
        [("Documentado en los informes del SPI y del Pix", "teal"), ("No se sabe: hardware, centros de datos y software del Banco Central", "grey"), ("Inferido: el detalle de los mensajes entre capas", "grey")],
        "Documentado en el informe anual del SPI de 2025 (arquitectura del SPI y acceso por la RSFN) y en el manual operacional del DICT. Dónde deja de valer: el informe no describe la tecnología interna del SPI.",
        DOCS)


def secuencia():
    return sequence(
        "De la orden de pago a la confirmación, con lo documentado y lo inferido",
        "Secuencia de un Pix: el pagador inicia en su aplicación; su institución resuelve la clave en el DICT; envía la orden al SPI; el SPI liquida en las cuentas PI y avisa a ambas instituciones; la institución del receptor acredita y confirma.",
        ["Pagador", "Institución del pagador", "DICT", "SPI", "Institución del receptor"],
        [(0, 1, "inicia el pago con una clave o un código QR", ""), (1, 2, "consulta la clave", ""), (2, 1, "devuelve la cuenta del receptor", "ret"),
         (1, 3, "envía la orden de pago", ""), (3, 4, "liquida y comunica el resultado", ""), (4, 0, "acredita y confirma a ambos", "dashed")],
        "Documentado: el DICT resuelve claves, el SPI liquida de forma bruta en tiempo real y de modo irrevocable y las instituciones notifican; el Manual de Tiempos fija límites para cada paso. Inferido (trazo punteado): la forma exacta de la confirmación final. Dónde deja de valer: omite el canal secundario, los Pix dentro de la misma institución y el MED.",
        DOCS)


def lbtr():
    return flow(
        "El SPI liquida cada Pix de forma bruta, uno a uno, en cuentas del Banco Central",
        "Flujo del SPI: cada orden se procesa y se liquida en cuanto llega, con un asiento en las cuentas PI que los participantes directos mantienen en el Banco Central; no se admite saldo negativo; una vez liquidada, la operación es irrevocable.",
        [[("Orden de pago llega al SPI desde la institución del pagador", "plain"), ("Liquidación bruta en tiempo real: una operación, un asiento", "teal"), ("Asientos en las cuentas PI de las dos instituciones", "teal")],
         [("Sin saldo negativo en las cuentas PI", "gold"), ("Liquidada: irrevocable, sin cancelación posible", "navy"), ("Fallo antes de liquidar: se rechaza y no se tarifa", "coral")]],
        note="Documentado en el informe anual del SPI de 2025. La regla de no admitir saldo negativo protege la solidez del sistema, a costa de exigir liquidez previa en la cuenta. Dónde deja de valer: describe el sistema de liquidación, no las reglas de cada institución con sus clientes.",
        foot=SPI25, width=960)


def liquidez():
    return flow(
        "Cómo reciben liquidez las cuentas PI, también los fines de semana",
        "Flujo de la liquidez: los participantes aportan o retiran recursos de su cuenta PI mediante el sistema de reservas entre las 6:30 y las 18:30 de los días hábiles, con una ventana adicional de treinta minutos; los viernes aportan más porque el sistema de reservas está cerrado el fin de semana; los aportes llegaron a superar 97 mil millones de reales por día.",
        [[("STR abierto entre las 6:30 y las 18:30 en días hábiles", "plain"), ("Ventana adicional de 30 minutos tras el cierre", "plain"), ("Aportes y retiros libres entre la cuenta PI y otras cuentas", "teal")],
         [("Los viernes se aporta más para cubrir el fin de semana", "gold"), ("Aportes de más de 97 000 millones de reales por día", "navy"), ("El SPI sigue 24 horas, los 7 días", "teal")]],
        note="Documentado en el informe anual del SPI de 2025. Mecanismo: el pago es 24 horas, pero el sistema de reservas que lo respalda no; la liquidez debe pre-posicionarse. Dónde deja de valer: los aportes no integran las cifras de Pix del informe.",
        foot=SPI25, width=960)


def lanzamiento():
    return timeline(
        "De la idea al Pix: los dos años del lanzamiento",
        "Línea de tiempo en meses desde diciembre de 2018: el Banco Central publica los requisitos fundamentales el 21 de diciembre de 2018; en octubre de 2019 comienza el desarrollo de la infraestructura; el 12 de agosto de 2020 se publica el Reglamento del Pix; el 5 de octubre empieza el registro de claves, con más de 25 millones en los primeros días; el 3 de noviembre comienza la operación restringida; el 16 de noviembre el Pix entra en operación plena.",
        [("Diseño", [(0, 10, "Grupo de trabajo y consulta pública", "grey"), (10, 20, "Desarrollo del SPI y del DICT", "gold")]),
         ("Reglas", [(20, 21.5, "", "navy"), (21.5, 23, "", "teal")]),
         ("Operación", [(22.2, 22.8, "", "gold"), (22.8, 23.5, "", "teal")])],
        unit="meses desde diciembre de 2018", events=[(0, "dic 2018"), (10, "oct 2019"), (20.4, "ago 2020"), (23.5, "nov 2020")],
        t_max=25, ticks=[0, 6, 12, 18, 24, 25], lane_h=46,
        note="Documentado en el informe de gestión 2020-2022: el grupo de trabajo tuvo más de 130 participantes; los requisitos se aprobaron en diciembre de 2018; el desarrollo comenzó en octubre de 2019; el Reglamento (Resolución BCB nº 1) salió el 12 de agosto de 2020 tras consulta pública. Dónde deja de valer: las posiciones en el eje son aproximadas; hay hitos de días entre octubre y noviembre.",
        foot=RG23)


def evolucion():
    return years(timeline(
        "Qué funciones sumó el Pix de 2020 a 2025",
        "Línea de tiempo por años con tres carriles: arranque (lanzamiento en noviembre de 2020), seguridad (bloqueo cautelar y MED en 2021, límites nocturnos en 2022, MED de autoservicio en 2025) y productos (retiro y vuelto en 2021, Pix Agendado en 2024, Pix por aproximación y Pix Automático en 2025).",
        [("Arranque", [(2020.88, 2021, "", "teal")]),
         ("Seguridad", [(2021.88, 2022.0, "", "coral"), (2022.5, 2022.7, "", "coral"), (2025.3, 2025.5, "", "coral")]),
         ("Productos", [(2021.3, 2021.5, "", "gold"), (2024.3, 2024.5, "", "gold"), (2025.2, 2025.4, "", "gold")])],
        unit="año", events=[(2020.88, "lanzamiento"), (2021.88, "MED"), (2022.5, "límites nocturnos"), (2025.3, "Automático")],
        t_max=2026, ticks=[2020, 2021, 2022, 2023, 2024, 2025, 2026], lane_h=46,
        note="Documentado en la línea de tiempo oficial del informe de gestión 2023-2025: 2021 retiro y vuelto, bloqueo cautelar, MED e iniciación de pago por Open Finance; 2022 límites nocturnos y código QR dinámico; 2023 mayor integración con Open Finance; 2024 recorrido sin redirección y Pix Agendado; 2025 Pix por aproximación, Pix Automático y MED de autoservicio. Dónde deja de valer: los marcadores indican el año y no el mes.",
        foot=RG))


def tiempos():
    return flow(
        "Los plazos que el Banco Central fija para un Pix",
        "Flujo de plazos: una orden enviada al canal primario del SPI debe liquidarse en 40 segundos o se rechaza; el 50 por ciento de los Pix liquidados cada mes debe tardar menos de 2,8 segundos dentro del SPI y el 99 por ciento menos de 4,6; una transacción con sospecha de fraude puede retenerse hasta 30 minutos de 8 a 20 horas en días hábiles y hasta 60 minutos el resto del tiempo.",
        [[("Canal primario del SPI: máximo de 40 segundos para liquidar", "plain"), ("Si no se liquida en ese plazo, se rechaza", "coral"), ("Acuerdo de nivel de servicio: 50 % en menos de 2,8 s", "teal")],
         [("Acuerdo de nivel de servicio: 99 % en menos de 4,6 s", "teal"), ("Sospecha de fraude: hasta 30 minutos (8 a 20 h, días hábiles)", "gold"), ("Sospecha de fraude: hasta 60 minutos en los demás horarios", "gold")]],
        note="Documentado en el Manual de Tiempos del Pix (versión 7.0) y en el informe anual del SPI de 2025. Los tiempos del SPI no incluyen los que se gastan en los sistemas de las instituciones del pagador y del receptor, que se miden con otros acuerdos. Dónde deja de valer: son límites normativos, no tiempos medidos de extremo a extremo.",
        foot="Fuentes: Manual de Tempos do Pix v7.0 y Relatório Anual do SPI 2025 (Banco Central do Brasil).", width=960)


def claves():
    return hub(
        "Las claves del Pix: cinco formas de identificar una cuenta",
        "Esquema de claves del DICT: número de celular, correo electrónico, CPF, CNPJ y clave aleatoria generada por el directorio; una persona física puede vincular hasta cinco claves por cuenta y una empresa hasta veinte; las claves bloqueadas por orden judicial devuelven un error.",
        ("DICT: directorio de identificadores de cuentas transaccionales", "navy"),
        [("Celular (formato E.164)", "teal", "tipo"),
         ("Correo electrónico (hasta 77 caracteres)", "teal", "tipo"),
         ("CPF (11 dígitos) o CNPJ (14 dígitos)", "teal", "tipo"),
         ("Clave aleatoria (UUID generado por el DICT)", "teal", "tipo"),
         ("Hasta 5 claves por cuenta de persona física; hasta 20 por cuenta de empresa", "gold", "límite"),
         ("Bloqueo judicial: el DICT devuelve error de clave bloqueada", "coral", "excepción")],
        "Documentado en el Manual Operacional del DICT. La clave aleatoria permite recibir un Pix sin exponer el teléfono, el correo ni el documento. Dónde deja de valer: el manual describe formatos y reglas, no la tecnología interna del directorio.",
        "Fuente: Banco Central do Brasil, Manual Operacional do DICT, consulta 2026-11-23.")


def seguridad():
    return flow(
        "Mecanismos de seguridad que el Pix fue sumando",
        "Flujo de seguridad: límites de valor por tramo horario, límites nocturnos desde 2022, bloqueo cautelar de hasta 72 horas desde noviembre de 2021, el Mecanismo Especial de Devolución desde noviembre de 2021 y su autoservicio en 2025, y restricciones a las claves de usuarios con fraude confirmado desde septiembre de 2025.",
        [[("Límites de valor para personas físicas (2021-2022)", "plain"), ("Límites nocturnos (2022)", "plain"), ("Bloqueo cautelar: hasta 72 horas en el receptor (nov. 2021)", "gold")],
         [("MED: bloqueo y devolución tras la queja de la víctima (nov. 2021)", "teal"), ("MED de autoservicio (2025)", "teal"), ("Restricciones a claves con marca de fraude (sept. 2025)", "navy")]],
        note="Documentado en los informes de gestión de 2020-2022 y 2023-2025. El MED agiliza la devolución por falla operacional o fundada sospecha de fraude: los fondos se bloquean en la cuenta del estafador y se devuelven si la queja procede. Dónde deja de valer: no hay en estas fuentes tasas de éxito de devolución.",
        foot=DOCS, width=960)


def especiales():
    return case_cards(
        "Casos especiales documentados y cómo se resuelven",
        "Cinco tarjetas: picos de diciembre, estafas por ingeniería social, pagos de noche, cobros recurrentes y pagos desde el extranjero; cada una con su mecanismo y veredicto.",
        [("Diciembre: aguinaldo y fiestas", "El SPI funciona 24 horas y sostiene 7,1 mil millones al mes", "El récord de un día fue de más de 313 millones de operaciones (2025).", "teal"),
         ("Estafa por ingeniería social", "MED, bloqueo cautelar y alertas de las instituciones", "No evita el pago voluntario; reduce el daño si se actúa rápido.", "gold"),
         ("Pagos de noche", "Límites nocturnos desde 2022", "Reduce el daño de un robo de teléfono a costa de comodidad.", "gold"),
         ("Cobros recurrentes", "Pix Automático (2025) con autorización previa", "Reemplaza el débito en cuenta de contratos bilaterales; adopción lenta por exigir desarrollo del receptor.", "gold"),
         ("Pagos de y hacia extranjeros", "Alianzas con instituciones de otros países", "El Pix en sí es solo doméstico; la parte internacional va por canales tradicionales.", "teal")],
        note="Cada tarjeta enlaza un hecho citado con el mecanismo. Color: coral falla, teal se sostiene, gold depende. Dónde deja de valer: son casos documentados en los informes del Banco Central, que informa de su propia política.",
        foot=DOCS)


def alternativas():
    return case_cards(
        "Alternativas que el Banco Central evaluó o no tomó, como análisis del curso",
        "Cuatro tarjetas: dejar que el mercado construyera una solución cerrada, un arreglo privado operado por una asociación, liquidación diferida en lotes y una solución sin directorio de claves; cada una con lo que el Banco Central documenta.",
        [("Esperar a que el mercado se coordinara", "El Banco Central asumió el liderazgo", "Documentado: en 2018 era evidente que los agentes privados no lo lograrían por sí solos.", "teal"),
         ("Soluciones cerradas con el mismo emisor", "Arreglo abierto e interoperable", "Documentado: los pagos móviles por QR existentes exigían que pagador y receptor fueran clientes de la misma institución.", "teal"),
         ("Dejar de ser operador y solo regular", "El Banco Central regula y también opera el SPI y el DICT", "Documentado: decidió ser desarrollador, operador y gestor de la infraestructura.", "gold"),
         ("Copiar un modelo extranjero", "Estudió diez jurisdicciones y adaptó", "Documentado: no existe un modelo ideal; se adaptó cada característica a Brasil.", "teal")],
        note="Rótulo: documentado en el informe de gestión 2020-2022, que cuenta cómo se decidió. Dónde deja de valer: son razones del propio Banco Central; no hay una evaluación independiente de las alternativas.",
        foot=RG23)


def hardware():
    return layer_stack(
        "Hardware y software que el Pix hace público",
        "Pila: no hay hardware ni centros de datos publicados; el software es el SPI y el DICT del Banco Central; las instituciones se conectan por la red del sistema financiero nacional o por proveedores homologados; hay dos canales de transmisión de mensajes del SPI.",
        [("Hardware", "No publicado: ni centros de datos ni servidores del Banco Central", "grey"),
         ("Software del Banco Central", "SPI (liquidación) y DICT (claves); módulo SPI del SPB-Web (2025)", "gold"),
         ("Mensajería", "Canal primario y canal secundario de transmisión de mensajes del SPI", "plain"),
         ("Red", "Red del Sistema Financiero Nacional (RSFN) y redes homologadas de proveedores de tecnología", "plain"),
         ("Interfaz", "Especificaciones y manuales públicos para las instituciones", "plain")],
        [("Documentado en el informe del SPI y en los manuales", "teal"), ("No se sabe: tecnología interna, nube o centros de datos", "grey")],
        "El informe anual del SPI de 2025 describe la arquitectura de acceso y los dos canales de mensajes, pero no los componentes internos. Dónde deja de valer: cualquier descripción de bases de datos o lenguajes del SPI sería inventada; este caso no la da.",
        DOCS)


def pruebas_fallo():
    return case_cards(
        "Temas a prueba de fallos que el Banco Central documenta",
        "Cuatro mecanismos con veredicto: disponibilidad mínima de 99,90 por ciento con funcionamiento continuo, liquidación irrevocable sin saldo negativo, dos canales de transmisión de mensajes y un plazo máximo de 40 segundos tras el cual se rechaza el pago.",
        [("El SPI deja de estar disponible", "Mínimo normativo de 99,90 % y medición continua", "El índice cerró 2025 en 99,98 %; nunca estuvo por debajo del mínimo desde el lanzamiento.", "teal"),
         ("Un participante no tiene liquidez", "No se admite saldo negativo en la cuenta PI", "El pago falla antes de liquidar; el riesgo no se traslada al sistema.", "teal"),
         ("Falla el canal principal de mensajes", "Canal secundario de transmisión", "Documentado como parte del diseño; no se detalla su activación.", "gold"),
         ("Una orden no se liquida a tiempo", "Rechazo tras 40 segundos", "Evita pagos en estado incierto indefinido.", "teal")],
        note="Documentado en el informe anual del SPI de 2025 y en el Manual de Tiempos. Dónde deja de valer: no hay en las fuentes consultadas un análisis posterior de un incidente concreto del SPI.",
        foot=DOCS)


FIGURES = {
    "pix-contexto.svg": contexto,
    "pix-pix-de-diciembre.svg": mensual,
    "pix-valor-liquidado.svg": valor,
    "pix-transacciones-totales.svg": total_pix,
    "pix-valor-tipico.svg": tickets,
    "pix-usuarios-y-claves.svg": usuarios,
    "pix-participantes-directos.svg": participantes,
    "pix-disponibilidad.svg": disponibilidad,
    "pix-pix-por-dia.svg": semana,
    "pix-actores-e-incentivos.svg": actores,
    "pix-recorridos-de-usuario.svg": recorridos,
    "pix-esquema-del-dinero.svg": negocio,
    "pix-capas.svg": capas,
    "pix-secuencia-de-un-pago.svg": secuencia,
    "pix-liquidacion-bruta.svg": lbtr,
    "pix-liquidez-de-las-cuentas-pi.svg": liquidez,
    "pix-del-diseno-al-lanzamiento.svg": lanzamiento,
    "pix-funciones-por-ano.svg": evolucion,
    "pix-plazos.svg": tiempos,
    "pix-claves-del-dict.svg": claves,
    "pix-seguridad.svg": seguridad,
    "pix-casos-especiales.svg": especiales,
    "pix-alternativas.svg": alternativas,
    "pix-hardware-y-software.svg": hardware,
    "pix-a-prueba-de-fallos.svg": pruebas_fallo,
}


if __name__ == "__main__":  # pragma: no cover - manual preview
    import pathlib
    import sys

    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "casos/figures")
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in FIGURES.items():
        (out / name).write_text(fn().svg(), encoding="utf-8")
        print(name)
