# Partida doble

[↑ Glosario](../../README.md) · [← Particiones y fronteras](./particiones-y-fronteras.md) · [Pasarela →](./pasarela.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Método en el que cada movimiento afecta a dos o más cuentas con sumas iguales.

Definición de trabajo de [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md).

## Por qué importa

En [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md), el tema «Partida doble» importa porque hace que un descuadre sea imposible de ocultar.

## Cómo funciona

Según [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md):

En un libro de partida doble cada movimiento (un *asiento*) afecta como mínimo a dos cuentas, con débitos y créditos que suman lo mismo. Un cobro de 49,00 con una comisión de 1,72 se registra así: débito a «procesador por cobrar» 47,28, débito a «comisiones» 1,72, crédito a «ingresos» 49,00. Los totales de ambos lados son iguales; si alguien intenta registrar uno que no (`100` contra `90`), la función de registro lo rechaza (en el experimento, «asiento desbalanceado»). La propiedad que se obtiene es que **la suma de todos los débitos es igual a la suma de todos los créditos, siempre**, y por tanto cualquier error que rompa esa igualdad se detecta de inmediato.

## Ejemplo

Ejemplo de [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md) (sección «Ejemplo mínimo»):

Un libro de partida doble con referencia única y un reembolso que revierte:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md)) son: Se ejecutaron un procesador simulado, un libro de partida doble con sqlite3 y una conciliación con diferencias sembradas por el autor; no se llamó a ningún procesador real, no se movió dinero, no se evaluó PCI DSS ni normas fiscales o contables, y las comisiones son del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md), [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Asiento](../a/asiento.md), [Autorización, captura, liquidación](../a/autorizacion-captura-liquidacion.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Conciliación](../c/conciliacion.md), [Contracargo](../c/contracargo.md), [Liquidación](../l/liquidacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-417 — Pagos, idempotencia y conciliación](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-416](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md), [SE-418](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md), [SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Particiones y fronteras](./particiones-y-fronteras.md) · [Pasarela →](./pasarela.md)
