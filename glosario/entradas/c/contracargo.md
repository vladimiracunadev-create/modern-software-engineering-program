# Contracargo

[↑ Glosario](../../README.md) · [← Contingencia](./contingencia.md) · [Contradicción →](./contradiccion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Impugnación de un cargo por el titular de la tarjeta.

Definición de trabajo de [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md).

## Por qué importa

La clase donde se define, [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md), existe con este propósito: la clase existe para que construyas la parte del sistema donde un error cuesta dinero de verdad y casi nunca se ve en el momento: cobrar sin duplicar, registrar cada movimiento de modo que siempre cuadre y comprobar periódicamente que lo que dice tu libro es lo que el procesador y el banco dicen.

## Cómo funciona

Según [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md):

Pagar con tarjeta no es un solo acto. El comprador autoriza (el emisor reserva el importe), el comerciante captura (reclama el importe reservado), el procesador liquida (transfiere los fondos, descontando comisiones, en un lote posterior) y, si procede, se reembolsa (devuelve) o se disputa (el titular impugna el cargo y el emisor retira los fondos mientras se resuelve). Los procesadores modelan esto con un objeto de pago con estados (por ejemplo, requiere método, requiere acción, procesando, exitoso, cancelado). El producto no debe reducirlo a «pagado: sí/no»: cada estado implica un saldo distinto y una obligación distinta, y el libro debe poder representar lo que ya ocurrió y lo pendiente.

Según [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md):

El equipo de *Tablero* ordena su manejo del dinero en tres capas. Primero, la clave de idempotencia: cada operación de cobro usa `renovacion:{cliente}:{periodo}`, y el almacén de claves guarda la solicitud (con un resumen de los parámetros), el estado y la respuesta; un reintento con la misma clave y los mismos parámetros devuelve lo guardado y con parámetros distintos devuelve un error. Segundo, el libro: plan de siete cuentas (por cobrar del procesador, caja, ingresos de suscripción, ingresos de uso, comisiones, reembolsos, disputas), asientos con la referencia del procesador como clave única y una prueba que recorre todos los eventos del procesador de un mes de ensayo y comprueba que cada uno tiene su asiento.

## Ejemplo

Ejemplo de [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md) (sección «Ejemplo profesional»):

El equipo de *Tablero* ordena su manejo del dinero en tres capas. Primero, la clave de idempotencia: cada operación de cobro usa `renovacion:{cliente}:{periodo}`, y el almacén de claves guarda la solicitud (con un resumen de los parámetros), el estado y la respuesta; un reintento con la misma clave y los mismos parámetros devuelve lo guardado y con parámetros distintos devuelve un error.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **en tu libro y no en la liquidación** (cobros pendientes, retenidos o fallidos), **en la liquidación y no en el libro** (cobros que tu sistema no conoce), **con importes distintos** (disputas, reembolsos parciales, comisiones) y **duplicados**. ([SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md), [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Asiento](../a/asiento.md), [Autorización, captura, liquidación](../a/autorizacion-captura-liquidacion.md), [Clave de idempotencia](./clave-de-idempotencia.md), [Conciliación](./conciliacion.md), [Liquidación](../l/liquidacion.md), [Partida doble](../p/partida-doble.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-416](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md), [SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md), [SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), [SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md), [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md), [SE-346](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md), [SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md).

**Aparece en los casos de estudio:** [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md), [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «disputa».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Contingencia](./contingencia.md) · [Contradicción →](./contradiccion.md)
