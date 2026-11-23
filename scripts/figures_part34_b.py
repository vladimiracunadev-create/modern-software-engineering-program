"""Figures for SE-415 to SE-420 (pricing, marketplaces, payments, e-commerce, SLA and the integrating workshop; sqlite3, threads and simulations with fixed seed 34 on Windows 11, CPython 3.12.9; no language model was invoked)."""
from __future__ import annotations

import random

from figure_kit import Fig, grouped_bars, heatmap, line_chart, stacked_bars, timeline

from figures_part45_a import flow

EJEC = "Código ejecutado de verdad en Windows 11 con CPython 3.12.9 y sqlite3; los recuentos se repiten con la semilla 34 y los tiempos varían entre ejecuciones y equipos."
MODELO = "Modelo con parámetros del autor y semilla fija 34; muestra un mecanismo, no mide un producto, un mercado ni un proveedor reales."


def _poblacion(n: int = 1000) -> list[tuple[int, float]]:
    rng = random.Random(34)
    out = []
    for _ in range(n):
        puestos = max(1, int(rng.lognormvariate(1.6, 1.0)))
        out.append((puestos, rng.lognormvariate(2.9, 0.5) * puestos ** 0.9))
    return out


# ---------------------------------------------------------------- SE-415
def se415_tres_disenos() -> Fig:
    return grouped_bars(
        "Ingreso mensual de 1000 clientes simulados con tres diseños de precio, cada uno con sus mejores parámetros",
        "Barras con el ingreso mensual en unidades inventadas: un precio único de 110 reúne 38610 con 351 compradores, tres planes con límites reúnen 53040 con 567 y un precio por puesto reúne 58938 con 744.",
        ["Un precio único", "Tres planes con límites", "Precio por puesto"], [("Ingreso mensual", [38610, 53040, 58938], "teal")],
        unit="Ingreso mensual (unidades inventadas)", decimals=0, plot_h=270,
        note="Compran 351, 567 y 744 clientes de 1000: el diseño que escala con el tamaño llega a más clientes y a más ingreso, pero también hace la factura menos predecible para ellos. Población y disposición a pagar son del autor; en un mercado real se estiman con entrevistas y pruebas, no con una semilla.",
        note_kind="gold", foot=MODELO)


def se415_curva_de_precio() -> Fig:
    datos = [(10, 9810), (30, 24810), (50, 32700), (70, 36190), (90, 37980), (110, 38610), (130, 38220), (150, 37950), (190, 33630), (230, 28750), (270, 26460), (300, 23400)]
    return line_chart(
        "Ingreso mensual con un único precio: sube mientras entran compradores y baja cuando se pierden más de los que el precio compensa",
        "Línea del ingreso mensual de 1000 clientes simulados contra el precio único: 9810 con precio 10, 24810 con 30, 32700 con 50, 38610 con 110 en el máximo, 37950 con 150, 28750 con 230 y 23400 con 300.",
        [("Ingreso mensual", datos, "navy")],
        x_label="Precio único mensual", y_label="Ingreso mensual (unidades inventadas)", x_ticks=[(p, str(p)) for p in (10, 50, 110, 150, 230, 300)],
        point_labels="none", decimals=0, plot_h=290, annotations=[(110, 38610, "Máximo: 38 610 con precio 110", -40, -30)],
        note="La curva es plana cerca del máximo: entre 90 y 150 el ingreso varía menos de 3 %. Eso importa porque el precio exacto es menos decisivo que la forma del plan; subir de 150 a 230 cuesta 24 % de ingreso. Es una simulación del autor, no una elasticidad medida.",
        note_kind="teal", foot=MODELO)


def se415_quien_choca_con_el_limite() -> Fig:
    pob = _poblacion()
    limites = [1, 3, 5, 10, 25, 50]
    pts = [(l, round(100 * sum(1 for p, _ in pob if p > l) / len(pob), 1)) for l in limites]
    return line_chart(
        "Qué porcentaje de 1000 clientes simulados supera cada límite de puestos: lo que cada tope deja dentro y lo que empuja a pagar más",
        "Línea con el porcentaje de clientes simulados cuyo número de puestos supera el límite: 1 puesto 85,7; 3 puestos 63,9; 5 puestos 44,9; 10 puestos 21,7; 25 puestos 4,7; 50 puestos 0,3; la mediana de la población es 5 puestos.",
        [("Clientes que superan el límite (%)", pts, "coral")], x_label="Límite de puestos del plan", y_label="Clientes que lo superan (%)",
        x_ticks=[(l, str(l)) for l in limites], point_labels="all", decimals=1, plot_h=290,
        note="Un tope de 5 puestos deja a 45 de cada 100 clientes por encima del plan; uno de 25, a menos de 5 de cada 100. El límite no es neutral: elige quién paga más y quién se va. La población simulada es del autor (mediana de 5 puestos, cola larga), no un mercado.",
        note_kind="gold", foot=MODELO)


# ---------------------------------------------------------------- SE-416
def se416_liquidez() -> Fig:
    pts = [(5, 18.4), (20, 57.0), (80, 95.6), (320, 100.0)]
    return line_chart(
        "Qué porcentaje de compradores encuentra al menos una oferta que le sirve, según el número de vendedores",
        "Línea en escala logarítmica horizontal: con 5 vendedores encuentra oferta 18,4 por ciento de los compradores, con 20 vendedores 57,0, con 80 vendedores 95,6 y con 320 vendedores 100; cada vendedor sirve a un comprador cualquiera con probabilidad de 4 por ciento.",
        [("Compradores con oferta", pts, "teal")], x_label="Vendedores activos", y_label="Compradores que encuentran oferta (%)", log_x=True,
        x_ticks=[(5, "5"), (20, "20"), (80, "80"), (320, "320")], point_labels="all", decimals=1, plot_h=290,
        note="El valor para un lado depende de cuántos hay del otro: con pocos vendedores, 4 de cada 5 compradores se van sin oferta y no vuelven; la plataforma arranca por el lado más difícil de atraer. El 4 % de coincidencia por vendedor es un supuesto del autor, y el modelo no incluye precio ni calidad.",
        note_kind="gold", foot=MODELO)


def se416_reparto_de_la_venta() -> Fig:
    def reparto(precio: int):
        plataforma = round(precio * 0.10)
        procesador = round(precio * 0.029) + 30
        return plataforma, procesador, precio - plataforma - procesador
    precios = [500, 2000, 10000]
    filas = [reparto(p) for p in precios]
    return stacked_bars(
        "A quién llega cada centavo de una venta: vendedor, plataforma y procesador de pagos según el precio",
        "Barras apiladas al 100 por ciento para ventas de 5, 20 y 100 unidades de moneda con 10 por ciento de comisión de la plataforma y 2,9 por ciento más 0,30 al procesador: en la de 5 el vendedor recibe 81 por ciento, en la de 20 86 y en la de 100 87.",
        ["Venta de 5,00", "Venta de 20,00", "Venta de 100,00"],
        [("Vendedor", [f[2] for f in filas], "teal"), ("Plataforma", [f[0] for f in filas], "navy"), ("Procesador", [f[1] for f in filas], "coral")],
        unit="Parte de la venta", percent=True, horizontal=True, decimals=0, plot_h=240, label_w=150,
        note="El costo fijo del procesador pesa más en ventas pequeñas: en la de 5,00 se queda con 8,8 % frente a 3,2 % en la de 100,00. Si la plataforma promete «10 % de comisión», el vendedor de ventas chicas recibe menos de lo que espera y se va. Porcentajes del autor.",
        note_kind="gold", foot=MODELO)


def se416_flujo_del_dinero() -> Fig:
    return flow(
        "El dinero de una compra en un marketplace: retención hasta confirmar y liberación al vendedor",
        "Diagrama de dos filas: arriba el comprador paga, la plataforma retiene los fondos y el vendedor despacha; abajo el comprador confirma o vence el plazo, se calculan comisiones y se libera el pago al vendedor, con una rama de disputa que devuelve fondos al comprador.",
        [[("Comprador paga\nEl cobro se registra en el libro", "teal"), ("Plataforma retiene\nFondos en una cuenta de custodia", "gold"),
          ("Vendedor despacha\nCon seguimiento verificable", "teal")],
         [("Comprador confirma\nO vence el plazo de reclamo", "navy"), ("Se calculan comisiones\nUn asiento por cada parte", "gold"), ("Liberación o disputa\nPago al vendedor o devolución", "coral")]],
        note="Retener fondos hasta confirmar protege al comprador, pero convierte a la plataforma en custodia de dinero ajeno: según la jurisdicción puede requerir licencias y procesadores especializados. La plataforma modela el flujo; el dinero lo mueve un proveedor autorizado.",
        note_kind="teal", box_h=96, foot=MODELO)


# ---------------------------------------------------------------- SE-417
def se417_doble_cobro() -> Fig:
    return grouped_bars(
        "Cobros reales ante el mismo número de intentos: sin clave de idempotencia y con ella",
        "Barras con 1069 intentos de cobro sobre 1000 renovaciones, 8 por ciento reintentadas tras una respuesta perdida: sin clave de idempotencia el procesador de ejemplo cobra 1069 veces, 69 de más y 338100 centavos de más; con clave cobra 1000.",
        ["Intentos enviados", "Cobros reales sin clave", "Cobros reales con clave"], [("Cobros", [1069, 1069, 1000], "teal")],
        unit="Cobros", decimals=0, plot_h=260, ref_lines=[(1000, "Renovaciones")],
        note="Los 69 cobros de más suman 3 381,00 en cargos duplicados: cada uno es un cliente cobrado dos veces por un reintento que él no pidió. La clave estable por renovación (no por intento) es lo que convierte el reintento en seguro.",
        note_kind="gold", foot=EJEC)


def se417_reintento_con_clave() -> Fig:
    lanes = [("Cliente (servicio)", [(0, 3, "Pide cobro 1", "teal"), (3, 7, "Espera: tiempo agotado", "coral"), (7, 10, "Repite cobro 1", "teal")]),
             ("API del procesador", [(1, 3, "Cobra", "navy"), (7, 10, "Guardado", "gold")]),
             ("Libro mayor", [(10, 12, "Un asiento", "teal")])]
    return timeline(
        "Un cobro que cobra bien pero cuya respuesta se pierde: el reintento con la misma clave no cobra otra vez",
        "Diagrama de Gantt con tres carriles: el servicio pide el cobro 1 y espera hasta agotar el tiempo; el procesador cobra entre 1 y 3 segundos y la respuesta se pierde; el servicio repite el cobro con la misma clave; el procesador devuelve el resultado guardado; el libro registra un solo asiento.",
        lanes, unit="Segundos desde la primera petición (valores del autor)", t_max=13, ticks=[0, 2, 4, 6, 8, 10, 12], lane_h=48, label_w=180,
        note="El servicio no puede saber si el cobro ocurrió: sin clave, repetir arriesga cobrar dos veces y no repetir arriesga no cobrar. Con la misma clave, repetir es seguro y el procesador devuelve lo que ya guardó. Secuencia de ejemplo con valores del autor.",
        note_kind="teal", foot=MODELO)


def se417_brecha_de_conciliacion() -> Fig:
    return grouped_bars(
        "Cuatro diferencias entre el libro y la liquidación del procesador, en centavos, con la causa de cada una",
        "Barras horizontales con el valor absoluto de cuatro diferencias sembradas en 500 cobros: un cobro que está en el libro y no en la liquidación 1815 centavos, un monto distinto 500, un cobro en la liquidación que el libro no conoce 4728 y un asiento duplicado en el libro 4728 que solo se descubre por el total; la brecha neta es 2315 y la suma de las cuatro coincide con ella.",
        ["En el libro y no en la liquidación", "Monto distinto (disputa parcial)", "En la liquidación y no en el libro", "Asiento duplicado en el libro"],
        [("Centavos", [1815, 500, 4728, 4728], "teal")], unit="Centavos (valor absoluto)", horizontal=True, decimals=0, label_w=290,
        note="El libro y la liquidación difieren en 2 315 centavos, pero las cuatro causas suman más y se compensan (1815 + 500 − 4728 + 4728 = 2315). El cotejo cobro por cobro encuentra tres; la cuarta aparece porque, explicadas esas tres, sobran 4 728 en el total, justo el monto de un asiento repetido. Una restricción de unicidad sobre la referencia del procesador en el libro la habría impedido.",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-418
def se418_sobreventa() -> Fig:
    return grouped_bars(
        "Pedidos aceptados cuando 40 compradores piden a la vez una de las 10 unidades disponibles",
        "Barras con 40 compradores simultáneos y 10 unidades: leer el saldo y escribir después acepta 40 pedidos, 30 de más; una actualización condicional en una sola sentencia acepta 10; el resultado se repitió igual en cinco ejecuciones.",
        ["Existencias", "Leer y después escribir", "Actualización condicional"], [("Pedidos aceptados", [10, 40, 10], "teal")],
        unit="Pedidos aceptados", decimals=0, plot_h=260, ref_lines=[(10, "Existencias reales")],
        note="Con la lectura previa los 40 hilos ven «10 disponibles» antes de que ninguno escriba y todos aceptan el pedido; el saldo final dice 9 aunque haya 40 pedidos. La actualización condicional deja a la base de datos decidir quién llega primero. Hilos reales contra sqlite3; con otro motor cambian los tiempos, no la causa.",
        note_kind="gold", foot=EJEC)


def se418_estados_del_pedido() -> Fig:
    return flow(
        "Los estados de un pedido y de su inventario: lo que se reserva, lo que se confirma y lo que se devuelve",
        "Diagrama de dos filas: carrito sin reserva, reserva con vencimiento, pago confirmado y preparado en la primera; enviado, entregado, devolución pedida y reembolsado en la segunda; una nota dice que cada estado cambia el inventario y el libro de formas distintas.",
        [[("Carrito\nSin reserva: el stock no se toca", "teal"), ("Reserva\nRetiene stock con vencimiento", "gold"),
          ("Pagado\nLa reserva pasa a venta", "teal"), ("Preparado\nSe separa del almacén", "navy")],
         [("Enviado\nSale del inventario físico", "navy"), ("Entregado\nComienza el plazo de devolución", "teal"),
          ("Devolución pedida\nNo repone stock hasta recibir", "gold"), ("Reembolsado\nAsiento que revierte el cobro", "coral")]],
        note="El stock tiene al menos tres números (físico, reservado, vendible) y cada estado los cambia distinto. Reponer stock al pedir la devolución, en vez de al recibir el producto, vende unidades que todavía están en camino.",
        note_kind="gold", box_h=96, foot=MODELO)


def se418_tiempo_de_reserva() -> Fig:
    xs = [1, 5, 15, 30, 60]
    return line_chart(
        "Ventas y compradores rechazados con stock retenido según el tiempo que dura una reserva sin pagar",
        "Línea con dos series para 50 unidades y 300 compradores que llegan en dos horas, con semilla 34: las ventas valen 50, 50, 47, 41 y 26 con reservas de 1, 5, 15, 30 y 60 minutos; los compradores rechazados con stock retenido valen 1, 50, 156, 179 y 216.",
        [("Unidades vendidas", list(zip(xs, [50, 50, 47, 41, 26])), "teal"), ("Compradores rechazados con stock retenido", list(zip(xs, [1, 50, 156, 179, 216])), "coral")],
        x_label="Duración de la reserva sin pagar (minutos)", y_label="Unidades o compradores", x_ticks=[(x, str(x)) for x in xs],
        point_labels="all", decimals=0, plot_h=290,
        note="Una reserva larga protege al comprador que está pagando pero retiene unidades de quienes abandonan: con 60 minutos solo se venden 26 de 50 unidades y 216 compradores se van viendo «agotado» cuando había stock retenido. Con 1 minuto el pago real, de unos 4 minutos, se vuelve difícil; el valor se mide.",
        note_kind="teal", foot=MODELO)


# ---------------------------------------------------------------- SE-419
def se419_minutos_permitidos() -> Fig:
    return grouped_bars(
        "Minutos de caída que permite un objetivo de disponibilidad en un mes de 30 días",
        "Barras horizontales en escala logarítmica con los minutos de caída por mes: 99 por ciento permite 432, 99,5 permite 216, 99,9 permite 43,2, 99,95 permite 21,6 y 99,99 permite 4,3.",
        ["99 %", "99,5 %", "99,9 %", "99,95 %", "99,99 %"], [("Minutos por mes", [432, 216, 43.2, 21.6, 4.3], "navy")],
        unit="Minutos de caída permitidos (escala logarítmica)", horizontal=True, log=True, decimals=1, label_w=120,
        note="Cada «nueve» más divide por diez el tiempo permitido. De 99,9 % a 99,99 % se pasa de 43,2 a 4,3 minutos: menos de lo que tarda en reaccionar una guardia humana. Prometer un nivel exige haber medido el actual y poder pagarlo; no es un adjetivo del plan.",
        note_kind="gold", foot=MODELO)


def se419_presupuesto_de_errores() -> Fig:
    dias = [0, 5, 10, 15, 20, 25, 30]
    return line_chart(
        "Presupuesto de caída de 99,9 % (43,2 minutos al mes): tres meses distintos y cuándo se agota cada uno",
        "Línea con tres series de minutos de caída acumulados a lo largo de 30 días contra el presupuesto de 43,2 minutos: un mes tranquilo llega a 12 minutos; un mes con un incidente de 40 minutos el día 12 cierra en 44; un mes con tres incidentes pasa de 43,2 entre el día 10 y el 15 y llega a 78.",
        [("Mes tranquilo", list(zip(dias, [0, 2, 4, 6, 8, 10, 12])), "teal"), ("Un incidente grande", list(zip(dias, [0, 1, 2, 42, 42, 43, 44])), "gold"),
         ("Tres incidentes", list(zip(dias, [0, 22, 40, 52, 60, 70, 78])), "coral")],
        x_label="Día del mes", y_label="Minutos de caída acumulados", hlines=[(43.2, "Presupuesto de 99,9 % (43,2)")],
        x_ticks=[(d, str(d)) for d in dias], point_labels="last", decimals=0, plot_h=300,
        note="El presupuesto convierte un objetivo en una decisión: cuando el segundo mes llega al 100 % se frena el despliegue de funcionalidad y se trabaja en fiabilidad. El crédito al cliente por incumplir es una consecuencia contractual aparte. Series inventadas para mostrar la lectura.",
        note_kind="teal", foot=MODELO)


def se419_respuesta_por_nivel() -> Fig:
    filas = ["Crítica: servicio caído", "Alta: función principal degradada", "Media: error con alternativa", "Baja: consulta o mejora"]
    cols = ["Gratis", "Equipo", "Empresa"]
    vals = [[72, 4, 1], [None, 8, 2], [None, 24, 8], [None, 72, 24]]
    return heatmap(
        "Horas hasta la primera respuesta de soporte por severidad y plan: dónde el plan cambia la promesa y dónde no",
        "Mapa de calor con las horas hasta la primera respuesta por severidad y plan: crítica 72 en gratis, 4 en equipo y 1 en empresa; alta 8 en equipo y 2 en empresa; media 24 y 8; baja 72 y 24; el plan gratis solo tiene compromiso de 72 horas para lo crítico.",
        filas, cols, vals, unit="horas hasta la primera respuesta", scale="navy", decimals=0, cell_h=48, label_w=290,
        note="Una primera respuesta no es una resolución: el compromiso de respuesta es lo que se cumple fácil y se mide; el de resolución depende de la causa. Los guiones indican «sin compromiso». Valores del autor para mostrar la forma de una tabla de niveles, no un contrato.",
        note_kind="gold", foot=MODELO)


# ---------------------------------------------------------------- SE-420
def se420_arquitectura_minima() -> Fig:
    return flow(
        "El producto integrador mínimo: cinco piezas y la invariante que cuida cada una",
        "Diagrama de dos filas: arriba el plano de control con altas, la medición de uso y el motor de derechos; abajo el libro mayor, la conciliación y el panel de operación; una nota dice que cada pieza lleva una prueba que reproduce su fallo típico.",
        [[("Plano de control\nAlta idempotente de inquilinos", "teal"), ("Medición de uso\nEventos con identificador único", "teal"),
          ("Derechos\nPlan, excepción y consumo", "gold")],
         [("Libro mayor\nAsientos que cuadran", "navy"), ("Conciliación\nCobro por cobro con la liquidación", "coral"), ("Panel de operación\nSLO, presupuesto y vecino ruidoso", "navy")]],
        note="Ninguna pieza es opcional: sin medición no hay derechos que hacer cumplir, sin libro no hay conciliación y sin panel nadie sabe cuándo se rompió el aislamiento. El taller no entrega un producto, entrega la evidencia de que cada invariante se verifica.",
        note_kind="teal", box_h=96, foot=MODELO)


def se420_defectos_y_pruebas() -> Fig:
    filas = ["D1 Consulta sin filtro de inquilino", "D2 Evento de uso duplicado", "D3 Cobro repetido sin clave", "D4 Sobreventa concurrente", "D5 Límite del plan ignorado", "D6 Asiento que no cuadra"]
    cols = ["Prueba de aislamiento", "Prueba de idempotencia", "Prueba de concurrencia", "Prueba de derechos", "Asiento balanceado", "Conciliación"]
    vals = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 1]]
    return heatmap(
        "Seis defectos que el taller siembra y la prueba que cada uno debe hacer fallar",
        "Mapa de calor de seis defectos por seis comprobaciones: la consulta sin filtro la ve la prueba de aislamiento; el evento duplicado y el cobro repetido la prueba de idempotencia y la conciliación; la sobreventa la prueba de concurrencia; el límite ignorado la prueba de derechos; el asiento descuadrado el balance y la conciliación.",
        filas, cols, vals, unit="la prueba falla", scale="teal", vmin=0, vmax=1, cell_fmt=lambda v: "falla" if v else "—", cell_h=40, label_w=290,
        note="Cada defecto lo ve al menos una prueba y tres lo ven dos: la conciliación es la red de seguridad de la contabilidad, no un sustituto de las pruebas. Si un defecto sembrado no hace fallar ninguna comprobación, falta una comprobación, no un defecto. Estructura propuesta por el taller.",
        note_kind="gold", foot=MODELO)


def se420_plan_de_trabajo() -> Fig:
    lanes = [("Aislamiento y alta", [(0, 3, "Inquilino y vecino", "teal")]),
             ("Uso y derechos", [(2, 5, "Medidor y motor", "teal")]),
             ("Pagos y libro", [(4, 8, "Libro y conciliación", "gold")]),
             ("Inventario y SLA", [(6, 9, "Concurrencia y objetivos", "gold")]),
             ("Evidencia", [(8, 10, "Informe", "navy")])]
    return timeline(
        "Plan de diez horas de trabajo con solapes: qué puede avanzar a la vez y qué espera",
        "Diagrama de Gantt con cinco carriles en horas: aislamiento y alta de 0 a 3, uso y derechos de 2 a 5, pagos y libro de 4 a 8, inventario y SLA de 6 a 9 y evidencia de 8 a 10.",
        lanes, unit="Horas de trabajo (valores del autor)", t_max=10, ticks=[0, 2, 4, 6, 8, 10], lane_h=44, label_w=170,
        note="Los solapes son posibles porque cada pieza tiene su propia prueba; la evidencia solo empieza cuando las demás tienen resultado reproducible. Con una persona, las horas se suman; con equipo, el plan marca dónde coordinar. Duraciones inventadas.",
        note_kind="teal", foot=MODELO)


FIGURES = {
    "se-415-tres-disenos.svg": se415_tres_disenos,
    "se-415-curva-de-precio.svg": se415_curva_de_precio,
    "se-415-quien-choca-con-el-limite.svg": se415_quien_choca_con_el_limite,
    "se-416-liquidez.svg": se416_liquidez,
    "se-416-reparto-de-la-venta.svg": se416_reparto_de_la_venta,
    "se-416-flujo-del-dinero.svg": se416_flujo_del_dinero,
    "se-417-doble-cobro.svg": se417_doble_cobro,
    "se-417-reintento-con-clave.svg": se417_reintento_con_clave,
    "se-417-brecha-de-conciliacion.svg": se417_brecha_de_conciliacion,
    "se-418-sobreventa.svg": se418_sobreventa,
    "se-418-estados-del-pedido.svg": se418_estados_del_pedido,
    "se-418-tiempo-de-reserva.svg": se418_tiempo_de_reserva,
    "se-419-minutos-permitidos.svg": se419_minutos_permitidos,
    "se-419-presupuesto-de-errores.svg": se419_presupuesto_de_errores,
    "se-419-respuesta-por-nivel.svg": se419_respuesta_por_nivel,
    "se-420-arquitectura-minima.svg": se420_arquitectura_minima,
    "se-420-defectos-y-pruebas.svg": se420_defectos_y_pruebas,
    "se-420-plan-de-trabajo.svg": se420_plan_de_trabajo,
}
