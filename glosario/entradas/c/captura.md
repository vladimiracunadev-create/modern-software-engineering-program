# Captura

[↑ Glosario](../../README.md) · [← CAPEX y OPEX](./capex-y-opex.md) · [Captura de cambios →](./captura-de-cambios.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Reclamo del importe autorizado de un pago.

Definición de trabajo de [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md).

## Por qué importa

En [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md), el tema «Captura del pago» importa porque cobrar al reservar o al enviar cambia el riesgo.

## Cómo funciona

Según [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md):

El pedido guarda una copia de lo vendido, nace con una clave de idempotencia generada al abrir el checkout y avanza por una máquina de estados con las transiciones inválidas rechazadas. El cobro se autoriza al reservar y se captura al preparar el envío, con un trabajo que cancela autorizaciones vencidas. Para devoluciones, el RMA es un objeto con estados; la reposición ocurre al recibir e inspeccionar, el reembolso crea su asiento de reversión con la referencia del procesador y la conciliación diaria (`SE-417`) comprueba que cada reembolso del procesador tiene su asiento. En el siguiente lanzamiento, 300 compradores consiguen 50 pedidos, 3 reservas vencen sin pago y 3 compradores que las esperaban las obtienen en la siguiente hora.

## Ejemplo

Ejemplo de [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md) (sección «Ejemplo profesional»):

El pedido guarda una copia de lo vendido, nace con una clave de idempotencia generada al abrir el checkout y avanza por una máquina de estados con las transiciones inválidas rechazadas. El cobro se autoriza al reservar y se captura al preparar el envío, con un trabajo que cancela autorizaciones vencidas. Para devoluciones, el RMA es un objeto con estados; la reposición ocurre al recibir e inspeccionar, el reembolso crea su asiento de reversión con la referencia del procesador y la conciliación diaria (`SE-417`) comprueba que cada reembolso del procesador tiene su asiento.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md)) son: Se ejecutaron 40 hilos reales contra sqlite3 (que serializa las escrituras) y una simulación de reservas con semilla 34 y parámetros del autor; no se probó otro motor, ni réplicas, ni un almacén físico, ni un proveedor de envíos, y la reproducibilidad del defecto depende de la pausa que ensancha la ventana.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md), [SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md), [SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Actualización condicional atómica](../a/actualizacion-condicional-atomica.md), [Condición de carrera](./condicion-de-carrera.md), [Inventario físico / reservado / vendible](../i/inventario-fisico-reservado-vendible.md), [Reposición](../r/reposicion.md), [Reserva](../r/reserva.md), [RMA](../r/rma.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (99 clases más lo mencionan; las que más):

[SE-046](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-065](../../../classes/part-05-fundamentos-de-programacion/se-065-errores-excepciones-y-resultados-explicitos/README.md), [SE-023](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md), [SE-230](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md), [SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md), [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-045](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [Stripe](../../../casos/exito/stripe.md), [Shopify](../../../casos/exito/shopify.md), [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← CAPEX y OPEX](./capex-y-opex.md) · [Captura de cambios →](./captura-de-cambios.md)
