# Actualización condicional atómica

[↑ Glosario](../../README.md) · [← Actualización condicionada por versión](./actualizacion-condicionada-por-version.md) · [Actualización diferencial →](./actualizacion-diferencial.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Sentencia que comprueba y modifica a la vez.

Definición de trabajo de [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md).

## Por qué importa

La clase donde se define, [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md), existe con este propósito: la clase existe para que construyas el camino que va de «quiero esto» a «lo recibí» y vuelve si algo sale mal, sabiendo en cada tramo qué se promete y qué se puede cumplir.

## Cómo funciona

[SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: consulta la clase para el mecanismo completo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md):

*Escenario ilustrativo: las cifras y los resultados de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md)) son: Se ejecutaron 40 hilos reales contra sqlite3 (que serializa las escrituras) y una simulación de reservas con semilla 34 y parámetros del autor; no se probó otro motor, ni réplicas, ni un almacén físico, ni un proveedor de envíos, y la reproducibilidad del defecto depende de la pausa que ensancha la ventana.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md), [SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md), [SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Captura](../c/captura.md), [Condición de carrera](../c/condicion-de-carrera.md), [Inventario físico / reservado / vendible](../i/inventario-fisico-reservado-vendible.md), [Reposición](../r/reposicion.md), [Reserva](../r/reserva.md), [RMA](../r/rma.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Actualización condicionada por versión](./actualizacion-condicionada-por-version.md) · [Actualización diferencial →](./actualizacion-diferencial.md)
