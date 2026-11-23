# Autorización, captura, liquidación

[↑ Glosario](../../README.md) · [← Autorización a nivel de objeto](./autorizacion-a-nivel-de-objeto.md) · [Autoservicio →](./autoservicio.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Reserva de un importe, reclamo de lo reservado y transferencia efectiva de fondos.

Definición de trabajo de [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md).

## Por qué importa

La clase donde se define, [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md), existe con este propósito: la clase existe para que construyas la parte del sistema donde un error cuesta dinero de verdad y casi nunca se ve en el momento: cobrar sin duplicar, registrar cada movimiento de modo que siempre cuadre y comprobar periódicamente que lo que dice tu libro es lo que el procesador y el banco dicen.

## Cómo funciona

[SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: consulta la clase para el mecanismo completo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md):

*Escenario ilustrativo: las cifras y los resultados de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md)) son: Se ejecutaron un procesador simulado, un libro de partida doble con sqlite3 y una conciliación con diferencias sembradas por el autor; no se llamó a ningún procesador real, no se movió dinero, no se evaluó PCI DSS ni normas fiscales o contables, y las comisiones son del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md), [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Reserva](../r/reserva.md), [Transferencia](../t/transferencia.md), [Asiento](./asiento.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Conciliación](../c/conciliacion.md), [Contracargo](../c/contracargo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Autorización a nivel de objeto](./autorizacion-a-nivel-de-objeto.md) · [Autoservicio →](./autoservicio.md)
