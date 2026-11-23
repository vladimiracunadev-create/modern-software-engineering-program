"""Figures for SE-409 to SE-414 (SaaS products: delivery and revenue loop, tenant isolation, provisioning, subscriptions, metering, entitlements; sqlite3 and simulations with fixed seed 34 on Windows 11, CPython 3.12.9; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, heatmap, line_chart, percentile_intervals, stacked_bars, timeline

from figures_part45_a import flow

EJEC = "Código ejecutado de verdad en Windows 11 con CPython 3.12.9 y sqlite3; los recuentos se repiten con la semilla 34 y los tiempos varían entre ejecuciones y equipos."
MODELO = "Modelo con parámetros del autor y semilla fija 34; muestra un mecanismo, no mide un producto ni un proveedor reales."


# ---------------------------------------------------------------- SE-409
def se409_bucle_de_ingresos() -> Fig:
    return flow(
        "El bucle de un producto SaaS: cada vuelta de la entrega depende de la facturación y de la operación",
        "Diagrama de dos filas con ocho cajas: venta, alta, uso y medición en la primera; factura, cobro, renovación y mejora entregada en la segunda; una nota dice que si un eslabón falla el ingreso se interrumpe aunque el producto siga arriba.",
        [[("Venta\nUn plan, un precio y un contrato", "teal"), ("Alta\nInquilino creado y configurado", "teal"),
          ("Uso\nCada acción deja un evento", "gold"), ("Medición\nEventos únicos por periodo", "gold")],
         [("Factura\nImporte a partir de medición y plan", "coral"), ("Cobro\nCon clave de idempotencia", "coral"),
          ("Renovación\nO baja, con su motivo", "navy"), ("Mejora entregada\nSin ventana de instalación", "navy")]],
        note="La diferencia con el software que se vende una vez: aquí la fila de abajo se repite cada ciclo y es parte del producto. Una factura mal medida o un cobro duplicado es un defecto del producto, no un problema de contabilidad.",
        note_kind="gold", box_h=96, foot=MODELO)


def se409_costo_por_cliente() -> Fig:
    cats = ["Licencia instalada (una vez)", "SaaS en el mes 1", "SaaS en el mes 36"]
    series = [("Desarrollo y soporte repartidos", [60, 25, 25], "teal"),
              ("Operación de la infraestructura", [0, 40, 40], "coral"),
              ("Adquisición del cliente", [40, 80, 0], "gold")]
    return stacked_bars(
        "Quién paga cada categoría de costo por cliente: licencia instalada frente a SaaS en dos momentos",
        "Barras apiladas con tres categorías de costo por cliente, en unidades inventadas: licencia instalada 100 en total con 60 de desarrollo, 0 de operación y 40 de adquisición; SaaS en el mes 1, 145 con 25, 40 y 80; SaaS en el mes 36, 65 con 25, 40 y 0.",
        cats, series, unit="Unidades inventadas por cliente y mes", decimals=0, plot_h=260, label_w=230, horizontal=True,
        note="En SaaS el proveedor asume la operación y adelanta la adquisición: el mes 1 es más caro que una venta de licencia y el mes 36 es más barato por cliente. El negocio depende de que el cliente se quede el tiempo suficiente para amortizar lo adelantado; por eso la retención es parte del diseño.",
        note_kind="gold", foot=MODELO)


def se409_recuperacion_de_adquisicion() -> Fig:
    def serie(churn: float):
        pts, acumulado, activos = [], -300.0, 1.0
        for mes in range(0, 37):
            if mes:
                acumulado += 49 * 0.8 * activos       # margen mensual por cliente: 49 de precio con 80 % de margen bruto
                activos *= 1 - churn
            if mes % 6 == 0:
                pts.append((mes, round(acumulado)))
        return pts
    return line_chart(
        "Caja acumulada por un cliente que costó 300 adquirir: el mismo precio con tres tasas de baja mensual",
        "Línea con la caja acumulada de un cliente de 49 al mes con 80 por ciento de margen y 300 de costo de adquisición, a 3 por ciento, 8 por ciento y 15 por ciento de baja mensual, cada seis meses hasta el mes 36; con 3 por ciento recupera la inversión en el mes 9, con 8 por ciento en el mes 12 y con 15 por ciento nunca llega a cero en 36 meses.",
        [("Baja mensual 3 %", serie(0.03), "teal"), ("Baja mensual 8 %", serie(0.08), "navy"), ("Baja mensual 15 %", serie(0.15), "coral")],
        x_label="Mes desde la venta", y_label="Caja acumulada por cliente (unidades inventadas)", y_zero=False,
        hlines=[(0, "Recuperada la inversión")], x_ticks=[(m, str(m)) for m in (0, 6, 12, 18, 24, 30, 36)], point_labels="last", decimals=0, plot_h=300,
        note="Con el mismo precio y la misma adquisición, pasar de 3 % a 15 % de baja mensual convierte un cliente que recupera lo gastado en 9 meses en uno que no lo recupera nunca (la suma de sus márgenes se acerca a 261 y la adquisición cuesta 300). El supuesto de 80 % de margen y 49 de precio es del autor.",
        note_kind="teal", foot=MODELO)


# ---------------------------------------------------------------- SE-410
def se410_latencia_de_los_otros() -> Fig:
    return percentile_intervals(
        "Latencia de los clientes que no hacen ruido mientras uno envía una ráfaga: tres políticas sobre la misma carga",
        "Pistas de percentiles en milisegundos y escala logarítmica para los siete clientes normales: sin protección p50 9370, p95 23540 y p99 24730; con cuota de tasa por cliente p50 10, p95 10 y p99 20; con cola justa por cliente p50 10, p95 10 y p99 20.",
        [("Cola compartida, sin cuotas", [9370, 23540, 24730]), ("Cuota de tasa por cliente", [10, 10, 20]), ("Cola justa por cliente", [10, 10, 20])],
        unit="Milisegundos (escala logarítmica)", marks=("p50", "p95", "p99"), log=True, decimals=0, label_w=230,
        note="Misma semilla, misma carga y misma capacidad. Sin protección la ráfaga de un cliente retrasa a todos hasta unos 24 s, porque la cola es una sola; con una de las dos políticas los otros siete casi no notan la ráfaga. La cuota de tasa lo logra rechazando 56 619 solicitudes del vecino (y 914 de los normales); la cola justa no rechaza nada, pero el vecino espera hasta 74 s.",
        note_kind="gold", foot=MODELO)


def se410_costo_por_modelo() -> Fig:
    def serie(i: int):
        return [(n, v) for n, v in [(10, (90.0, 58.0, 62.0)[i]), (100, (90.0, 22.0, 8.0)[i]), (1000, (90.0, 18.4, 2.6)[i])]]
    return line_chart(
        "Costo mensual por cliente según el modelo de aislamiento y el número de clientes",
        "Línea con tres series en escala logarítmica para 10, 100 y 1000 clientes: base de datos y cómputo dedicados 90 en los tres; esquema propio con cómputo compartido 58, 22 y 18,4; todo compartido 62, 8 y 2,6.",
        [("Dedicado por cliente", serie(0), "coral"), ("Puente: esquema propio y cómputo compartido", serie(1), "gold"), ("Todo compartido", serie(2), "teal")],
        x_label="Clientes", y_label="Costo mensual por cliente (unidades inventadas)", log_x=True, log_y=True,
        x_ticks=[(10, "10"), (100, "100"), (1000, "1000")], point_labels="all", decimals=1, plot_h=300,
        note="Con pocos clientes el costo fijo compartido pesa más que el aislamiento y las tres opciones se parecen; a 1000 clientes lo compartido cuesta unas 35 veces menos que lo dedicado. El costo del modelo puente se mueve poco porque cada esquema tiene un costo propio. Parámetros del autor.",
        note_kind="teal", foot=MODELO)


def se410_ruta_de_la_peticion() -> Fig:
    return flow(
        "Dónde se fija el inquilino en una petición: cuatro puntos y el que falla si el anterior se omite",
        "Diagrama de una fila con cuatro cajas: la credencial que trae el identificador del inquilino, la capa de aplicación que lo copia al contexto, el acceso a datos que lo añade a cada consulta y la base de datos con una regla de filas que lo exige; una nota dice que cada punto cubre el olvido del anterior.",
        [[("Credencial\nEl inquilino viaja firmado, no en un parámetro", "teal"), ("Contexto\nSe copia una vez al entrar a la petición", "teal"),
          ("Acceso a datos\nTodo filtro lleva el inquilino", "gold"), ("Base de datos\nUna política de filas lo exige aunque falte", "coral")]],
        note="Con una sola barrera, un olvido en una consulta nueva muestra datos de otro cliente. Con las cuatro, el olvido en la aplicación lo detiene la base de datos. Ninguna barrera sustituye una prueba que pida datos del cliente A con la credencial del cliente B.",
        note_kind="teal", box_h=110, foot=MODELO)


# ---------------------------------------------------------------- SE-411
def se411_costo_de_alta() -> Fig:
    return grouped_bars(
        "Tiempo de dar de alta un cliente: una fila de inquilino frente a un esquema propio de 12 tablas",
        "Barras horizontales en escala logarítmica con el tiempo medio por alta en milisegundos, medido con sqlite3 en memoria sobre 200 altas: una fila de inquilino 0,0069 y un esquema propio con 12 tablas 0,6864, unas 99 veces más.",
        ["Una fila de inquilino", "Un esquema propio de 12 tablas"], [("Tiempo por alta", [0.0069, 0.6864], "teal")],
        unit="Milisegundos por alta (escala logarítmica)", horizontal=True, log=True, decimals=4, label_w=250,
        note="Unas 99 veces más caro en esta ejecución (otra dio unas 155) en una base en memoria, sin red, sin disco y sin migraciones; en una base real el esquema propio también multiplica el número de objetos que cada migración debe recorrer. La comparación mide el mecanismo, no el tiempo que tardaría un proveedor.",
        note_kind="gold", foot=EJEC)


def se411_saga_con_compensacion() -> Fig:
    return flow(
        "Un alta en cinco pasos que falla en el cuarto: qué se deshace y en qué orden",
        "Diagrama de dos filas: arriba los pasos crear inquilino, crear datos, crear identidad y vincular facturación, este último marcado como fallido; abajo las compensaciones que deshacen en orden inverso la identidad, los datos y el inquilino, con una nota sobre repetir pasos sin duplicar.",
        [[("1. Crear inquilino\nEstado: aprovisionando", "teal"), ("2. Crear datos\nEsquema o filas semilla", "teal"),
          ("3. Crear identidad\nPrimer administrador", "teal"), ("4. Vincular facturación\nFalla: el procesador no responde", "coral")],
         [("Deshacer identidad\nSe borra el administrador", "gold"), ("Deshacer datos\nSe borran filas semilla", "gold"),
          ("Deshacer inquilino\nEstado: fallido, con motivo", "gold"), ("Reintentar con la misma clave\nO dejar en revisión", "navy")]],
        note="Cada paso y cada compensación tiene que poder repetirse sin duplicar: si el proceso se corta justo después del paso 3, el reintento debe encontrar el administrador ya creado y seguir. Sin eso, un corte deja un cliente a medias que nadie ve.",
        note_kind="gold", box_h=96, foot=MODELO)


def se411_duracion_del_alta() -> Fig:
    lanes = [("Plano de control", [(0, 2, "Crear", "teal"), (2, 4, "Esperar", "grey"), (4, 5, "Activar", "teal")]),
             ("Datos", [(2, 6, "Esquema y semilla", "gold")]),
             ("Identidad", [(2, 4, "Admin", "gold")]),
             ("Facturación", [(6, 8, "Cliente y plan", "navy")]),
             ("Correo de bienvenida", [(8, 9, "Envío", "teal")])]
    return timeline(
        "Un alta con cinco actores: cuáles pasos corren a la vez y cuál marca la duración total",
        "Diagrama de Gantt con cinco carriles en segundos de un alta ejemplo: el plano de control crea durante 2 segundos, los datos y la identidad corren en paralelo de 2 a 6 y de 2 a 4, la facturación espera a los datos y corre de 6 a 8, y el correo sale de 8 a 9; la ruta más larga suma 9 segundos.",
        lanes, unit="Segundos desde la solicitud (valores del autor)", t_max=10, ticks=[0, 2, 4, 6, 8, 10], lane_h=42, label_w=190,
        note="Los datos y la identidad corren en paralelo, así que acelerar la identidad no cambia la duración total; la facturación depende de los datos y marca el camino largo. Duraciones inventadas para mostrar el razonamiento: se miden en cada producto antes de decidir.",
        note_kind="teal", foot=MODELO)


# ---------------------------------------------------------------- SE-412
def se412_estados_de_la_suscripcion() -> Fig:
    return flow(
        "Los estados de una suscripción y lo que dispara cada cambio de uno a otro",
        "Diagrama de dos filas: prueba, activa, con pago pendiente en la primera, y suspendida, cancelada y terminada en la segunda; una nota dice que cada flecha es un evento con su fecha y que el acceso se decide por el estado, no por la última factura.",
        [[("Prueba\nSin cobro hasta que termina", "teal"), ("Activa\nPago al día, acceso completo", "teal"),
          ("Pago pendiente\nCobro fallido, se reintenta", "gold"), ("Suspendida\nSe agotaron los reintentos", "coral")],
         [("Cancelación pedida\nSigue activa hasta fin de ciclo", "gold"), ("Cancelada\nSin renovación", "navy"),
          ("Datos retenidos\nPlazo para reactivar o exportar", "grey"), ("Eliminada\nBorrado según la política", "navy")]],
        note="El estado es una decisión de negocio guardada: la pantalla de facturación, el control de acceso y los informes leen el mismo estado. Si cada uno lo deduce por su cuenta de la última factura, tres lugares dirán tres cosas distintas.",
        note_kind="gold", box_h=96, foot=MODELO)


def se412_recuperacion_de_cobros() -> Fig:
    return stacked_bars(
        "De 69 cobros fallidos de 1000 renovaciones: cuántos recupera cada reintento y cuántos quedan",
        "Barras apiladas horizontales por etapa de reintento, con semilla 34: fallos iniciales 69; el día 1 recupera 21 y quedan 48; el día 3 recupera 14 y quedan 34; el día 7 recupera 4 y quedan 30; el día 14 recupera 3 y quedan 27.",
        ["Fallos iniciales", "Tras el día 1", "Tras el día 3", "Tras el día 7", "Tras el día 14"],
        [("Recuperados hasta ahora", [0, 21, 35, 39, 42], "teal"), ("Siguen sin pagar", [69, 48, 34, 30, 27], "coral")],
        unit="Renovaciones fallidas", horizontal=True, decimals=0, plot_h=260, label_w=170,
        note="Los dos primeros reintentos recuperan 35 de 42 y los dos últimos, 7. El calendario de reintentos decide cuánto se recupera, pero también cuánto tiempo un cliente que sí quería pagar queda sin acceso. Probabilidades de recuperación del autor, no de un procesador real.",
        note_kind="gold", foot=MODELO)


def se412_prorrateo() -> Fig:
    sube = [(d, round((9900 - 4900) * (30 - d + 1) / 30) / 100) for d in (1, 6, 11, 16, 21, 26, 30)]
    baja = [(d, round((4900 - 9900) * (30 - d + 1) / 30) / 100) for d in (1, 6, 11, 16, 21, 26, 30)]
    return line_chart(
        "Cobro o crédito inmediato por cambiar de plan a mitad de un mes de 30 días, según el día del cambio",
        "Línea con dos series: pasar del plan de 49 al de 99 genera un cargo que baja de 50,00 el día 1 a 1,67 el día 30; pasar del de 99 al de 49 genera un crédito de la misma magnitud con signo negativo, de menos 50,00 a menos 1,67; el día 11 son 33,33.",
        [("Subida de 49 a 99", sube, "coral"), ("Bajada de 99 a 49", baja, "teal")],
        x_label="Día del mes en que cambia el plan", y_label="Importe neto del prorrateo (unidades de moneda)", y_zero=False, hlines=[(0, "Sin diferencia")],
        x_ticks=[(d, str(d)) for d in (1, 6, 11, 16, 21, 26, 30)], point_labels="none", decimals=2, plot_h=290,
        note="El prorrateo es una resta de importes por los días que quedan: el día 11 de 30 restan 20 días y un cambio de 50 vale 33,33. Redondear en centavos en cada paso puede dejar una diferencia de un centavo entre lo cobrado y lo facturado; la regla de redondeo se escribe y se prueba.",
        note_kind="teal", foot=MODELO)


# ---------------------------------------------------------------- SE-413
def se413_medicion_con_y_sin_identificador() -> Fig:
    return grouped_bars(
        "Unidades de uso del mismo mes: la verdad, la suma sin identificador de evento y la suma con identificador",
        "Barras con tres valores de un experimento con 30000 eventos y 6 por ciento de entregas duplicadas: unidades reales 90157, suma sin identificador 95394 y suma con identificador único 90157; la diferencia sin identificador es 5237 unidades y afecta a 63 de 80 pares de cliente y periodo.",
        ["Unidades reales", "Sin identificador de evento", "Con identificador único"], [("Unidades", [90157, 95394, 90157], "teal")],
        unit="Unidades de uso", decimals=0, plot_h=270, ref_lines=[(90157, "Verdad")], label_w=None,
        note="Con entrega «al menos una vez» (lo normal en colas y reintentos) 31 744 entregas llegan por 30 000 eventos: sumar sin más factura 5,8 % de más y errores en 63 de 80 facturas. Con una clave única por evento y una inserción que ignora repetidos la suma coincide con la verdad.",
        note_kind="gold", foot=EJEC)


def se413_tramos_y_volumen() -> Fig:
    def grad(n: int) -> float:
        total, previo = 0.0, 0
        for tope, precio in [(1000, 0.020), (10000, 0.015), (None, 0.010)]:
            lim = n if tope is None else min(n, tope)
            if lim > previo:
                total += (lim - previo) * precio
                previo = lim
        return total
    def vol(n: int) -> float:
        precio = 0.020 if n <= 1000 else 0.015 if n <= 10000 else 0.010
        return n * precio
    xs = [500, 1000, 1001, 5000, 10000, 10001, 25000]
    return line_chart(
        "Importe a pagar según las unidades usadas: tramos graduales frente a precio por volumen",
        "Línea con dos series: el cobro gradual crece sin saltos, 10 a 500 unidades, 20 a 1000, 80 a 5000, 170 a 10000 y 305 a 25000; el cobro por volumen baja de 150 con 10000 unidades a 100,01 con 10001, y vale 250 con 25000.",
        [("Tramos graduales", [(x, round(grad(x), 2)) for x in xs], "teal"), ("Precio por volumen", [(x, round(vol(x), 2)) for x in xs], "coral")],
        x_label="Unidades usadas en el mes", y_label="Importe (unidades de moneda)", x_ticks=[(500, "500"), (5000, "5000"), (10000, "10 000"), (25000, "25 000")],
        point_labels="none", decimals=0, plot_h=290,
        note="Con volumen, un cliente que pasa de 10 000 a 10 001 unidades paga la mitad (de 150 a 100,01 con estos precios): un incentivo a mentir sobre el consumo o a partirlo. Con tramos graduales el importe nunca baja al usar más. Es una decisión de producto y se prueba con casos en los bordes.",
        note_kind="gold", foot=MODELO)


def se413_tuberia_de_uso() -> Fig:
    return flow(
        "El camino de un evento de uso hasta la factura y el paso donde cada defecto se detiene",
        "Diagrama de dos filas: arriba evento con identificador, cola con entrega al menos una vez y almacén con clave única; abajo agregación por periodo y cliente, borrador de factura y factura emitida; una nota dice que los eventos tardíos se asignan al periodo en que ocurrieron.",
        [[("Evento\nIdentificador único, cliente y hora de ocurrencia", "teal"), ("Cola\nAl menos una vez: llegan duplicados", "gold"),
          ("Almacén\nClave única: ignora el repetido", "teal")],
         [("Agregación\nPor cliente y periodo de ocurrencia", "teal"), ("Borrador\nSe puede revisar y recalcular", "gold"), ("Factura emitida\nInmutable: se corrige con otra", "navy")]],
        note="Un evento tardío (aquí 2762 unidades de 90 157 pertenecían al periodo anterior) se suma al periodo en que ocurrió, no al de cuando llegó. Si el periodo ya se facturó, la diferencia sale como ajuste en la factura siguiente; nunca se edita la emitida.",
        note_kind="teal", box_h=96, foot=EJEC)


# ---------------------------------------------------------------- SE-414
def se414_decision_de_derecho() -> Fig:
    return flow(
        "El orden de preguntas de un motor de derechos: de la cuenta al consumo",
        "Diagrama de una fila con cuatro cajas: estado de la cuenta, excepción vigente del cliente, límite del plan y consumo acumulado; una nota enumera las razones de rechazo: cuenta suspendida, límite alcanzado y funcionalidad no incluida.",
        [[("Cuenta\nActiva, suspendida o desconocida", "navy"), ("Excepción\nVigente a la fecha de hoy y con vencimiento", "gold"),
          ("Plan\nLímite o funcionalidad incluida", "teal"), ("Consumo\nUsado más lo pedido frente al límite", "teal")]],
        note="El resultado trae siempre una razón legible: «cuenta suspendida», «límite 25, usado 25» o «no incluido en el plan». Un simple «prohibido» obliga al soporte a reconstruir lo ocurrido; con la razón, la pantalla puede ofrecer el cambio de plan correcto.",
        note_kind="gold", box_h=110, foot=EJEC)


def se414_limites_por_plan() -> Fig:
    cats = ["Usuarios", "Proyectos", "Llamadas de API por mes"]
    series = [("Gratis", [3, 2, 1000], "grey"), ("Equipo", [25, 50, 100000], "teal"), ("Empresa", [1000, 5000, 5000000], "navy")]
    return grouped_bars(
        "Límites de tres planes de ejemplo en tres recursos, en escala logarítmica",
        "Barras agrupadas en escala logarítmica con tres planes y tres recursos: usuarios 3, 25 y 1000; proyectos 2, 50 y 5000; llamadas de API por mes 1000, 100000 y 5000000 para los planes gratis, equipo y empresa.",
        cats, series, unit="Límite del plan (escala logarítmica)", log=True, decimals=0, plot_h=290,
        note="Los límites crecen por órdenes de magnitud, no de a poco: cada plan es otro tipo de cliente. Un límite sin consumo medido (SE-413) no se puede hacer cumplir, y un consumo sin límite no cambia nada. Los números son de un plan inventado.",
        note_kind="gold", foot=MODELO)


def se414_ciclo_de_una_bandera() -> Fig:
    lanes = [("Bandera de lanzamiento", [(0, 1, "Equipo", "teal"), (1, 2, "1 %", "gold"), (2, 3, "10 %", "gold"), (3, 5, "100 %", "teal"), (5, 6, "Retirar", "coral")]),
             ("Bandera de permiso", [(0, 6, "Permanente: depende del plan", "navy")]),
             ("Interruptor de emergencia", [(0, 6, "Permanente: apagado por defecto", "grey")])]
    return timeline(
        "Tres tipos de bandera: cuáles tienen fecha de retiro y cuáles se quedan como parte del producto",
        "Diagrama de Gantt con tres carriles en semanas: la bandera de lanzamiento pasa por equipo, 1 por ciento, 10 por ciento y 100 por ciento y se retira en la semana 5 a 6; la bandera de permiso y el interruptor de emergencia duran todo el periodo.",
        lanes, unit="Semanas desde la creación (valores del autor)", t_max=6, ticks=[0, 1, 2, 3, 4, 5, 6], lane_h=48, label_w=210,
        note="Solo la bandera de lanzamiento debe morir: una que sigue en el código meses después del 100 % es una rama de ejecución más que nadie prueba. Las otras dos son decisiones de producto y de operación que se documentan con su responsable.",
        note_kind="teal", foot=MODELO)


FIGURES = {
    "se-409-bucle-de-ingresos.svg": se409_bucle_de_ingresos,
    "se-409-costo-por-cliente.svg": se409_costo_por_cliente,
    "se-409-recuperacion-de-adquisicion.svg": se409_recuperacion_de_adquisicion,
    "se-410-latencia-de-los-otros.svg": se410_latencia_de_los_otros,
    "se-410-costo-por-modelo.svg": se410_costo_por_modelo,
    "se-410-ruta-de-la-peticion.svg": se410_ruta_de_la_peticion,
    "se-411-costo-de-alta.svg": se411_costo_de_alta,
    "se-411-saga-con-compensacion.svg": se411_saga_con_compensacion,
    "se-411-duracion-del-alta.svg": se411_duracion_del_alta,
    "se-412-estados-de-la-suscripcion.svg": se412_estados_de_la_suscripcion,
    "se-412-recuperacion-de-cobros.svg": se412_recuperacion_de_cobros,
    "se-412-prorrateo.svg": se412_prorrateo,
    "se-413-medicion-con-y-sin-identificador.svg": se413_medicion_con_y_sin_identificador,
    "se-413-tramos-y-volumen.svg": se413_tramos_y_volumen,
    "se-413-tuberia-de-uso.svg": se413_tuberia_de_uso,
    "se-414-decision-de-derecho.svg": se414_decision_de_derecho,
    "se-414-limites-por-plan.svg": se414_limites_por_plan,
    "se-414-ciclo-de-una-bandera.svg": se414_ciclo_de_una_bandera,
}
