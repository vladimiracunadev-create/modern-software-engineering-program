# RMA

[↑ Glosario](../../README.md) · [← Risk appetite](./risk-appetite.md) · [Rojo →](./rojo.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Permiso para devolver un producto con su número de seguimiento.

Definición de trabajo de [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md).

## Por qué importa

La clase donde se define, [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md), existe con este propósito: la clase existe para que construyas el camino que va de «quiero esto» a «lo recibí» y vuelve si algo sale mal, sabiendo en cada tramo qué se promete y qué se puede cumplir.

## Cómo funciona

Según [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md):

El pedido guarda una copia de lo vendido, nace con una clave de idempotencia generada al abrir el checkout y avanza por una máquina de estados con las transiciones inválidas rechazadas. El cobro se autoriza al reservar y se captura al preparar el envío, con un trabajo que cancela autorizaciones vencidas. Para devoluciones, el RMA es un objeto con estados; la reposición ocurre al recibir e inspeccionar, el reembolso crea su asiento de reversión con la referencia del procesador y la conciliación diaria (`SE-417`) comprueba que cada reembolso del procesador tiene su asiento. En el siguiente lanzamiento, 300 compradores consiguen 50 pedidos, 3 reservas vencen sin pago y 3 compradores que las esperaban las obtienen en la siguiente hora.

## Ejemplo

Ejemplo de [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md) (sección «Ejemplo profesional»):

El pedido guarda una copia de lo vendido, nace con una clave de idempotencia generada al abrir el checkout y avanza por una máquina de estados con las transiciones inválidas rechazadas. El cobro se autoriza al reservar y se captura al preparar el envío, con un trabajo que cancela autorizaciones vencidas. Para devoluciones, el RMA es un objeto con estados; la reposición ocurre al recibir e inspeccionar, el reembolso crea su asiento de reversión con la referencia del procesador y la conciliación diaria (`SE-417`) comprueba que cada reembolso del procesador tiene su asiento.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md)) son: Se ejecutaron 40 hilos reales contra sqlite3 (que serializa las escrituras) y una simulación de reservas con semilla 34 y parámetros del autor; no se probó otro motor, ni réplicas, ni un almacén físico, ni un proveedor de envíos, y la reproducibilidad del defecto depende de la pausa que ensancha la ventana.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md), [SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md), [SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Permiso](../p/permiso.md), [Producto](../p/producto.md), [Actualización condicional atómica](../a/actualizacion-condicional-atomica.md), [Captura](../c/captura.md), [Condición de carrera](../c/condicion-de-carrera.md), [Inventario físico / reservado / vendible](../i/inventario-fisico-reservado-vendible.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «autorización de devolución».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Risk appetite](./risk-appetite.md) · [Rojo →](./rojo.md)
