# Referencia externa única

[↑ Glosario](../../README.md) · [← Referencia externa](./referencia-externa.md) · [Referencia independiente →](./referencia-independiente.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Identificador del hecho original, con restricción de unicidad en el libro.

Definición de trabajo de [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md).

## Por qué importa

La clase donde se define, [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md), existe con este propósito: la clase existe para que construyas la parte del sistema donde un error cuesta dinero de verdad y casi nunca se ve en el momento: cobrar sin duplicar, registrar cada movimiento de modo que siempre cuadre y comprobar periódicamente que lo que dice tu libro es lo que el procesador y el banco dicen.

## Cómo funciona

Según [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md):

Cada asiento lleva una referencia externa única (el identificador del cobro del procesador, el de la factura): la restricción `UNIQUE` hace que registrar dos veces el mismo hecho no cree un segundo asiento. Es la misma técnica del medidor de uso (`SE-413`) aplicada al dinero. En el experimento de conciliación se sembró un asiento repetido con otra referencia local (`inv-0100-dup`) para el mismo cobro: el libro lo aceptó porque la referencia era distinta, y fue una de las cuatro causas de diferencia. Si la referencia del procesador hubiera sido la clave única, el segundo asiento habría fallado. La lección es qué se elige como identificador: el del hecho original, no el de tu propio proceso.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md):

*Escenario ilustrativo: las cifras y los resultados de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cada asiento lleva una referencia externa única (el identificador del cobro del procesador, el de la factura): la restricción `UNIQUE` hace que registrar dos veces el mismo hecho no cree un segundo asiento. ([SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md), [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Hecho](../h/hecho.md), [Restricciones](./restricciones.md), [Asiento](../a/asiento.md), [Autorización, captura, liquidación](../a/autorizacion-captura-liquidacion.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Conciliación](../c/conciliacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Referencia externa](./referencia-externa.md) · [Referencia independiente →](./referencia-independiente.md)
