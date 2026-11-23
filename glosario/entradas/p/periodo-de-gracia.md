# Periodo de gracia

[↑ Glosario](../../README.md) · [← Periodicidad](./periodicidad.md) · [Permiso →](./permiso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Plazo en que el cliente conserva acceso pese a tener un pago pendiente.

Definición de trabajo de [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md).

## Por qué importa

La clase donde se define, [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md), existe con este propósito: la clase existe para que modeles una suscripción como lo que es: una máquina de estados con fechas, importes y eventos externos, y no como una fila con un campo «plan» y otro «vence».

## Cómo funciona

Según [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md):

Bloquear la cuenta al primer rechazo recupera poco y enfurece mucho; mantener el servicio completo durante semanas pierde dinero. Un diseño razonable usa un periodo de gracia: acceso completo con un aviso visible mientras la suscripción está en `pago_pendiente`; acceso reducido (solo lectura, sin crear proyectos nuevos) en `suspendida`; exportación de datos disponible hasta el borrado. La política se escribe, se muestra al cliente en lenguaje claro y se prueba: un cliente en cada estado debe obtener los derechos que se dice. Los derechos concretos se resuelven con el motor de `SE-414`, que lee el estado.

Según [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md):

Rara vez. La mayoría de los primeros fallos son recuperables (tarjeta caducada, fondos temporales). Un periodo de gracia con aviso visible recupera más y molesta menos; el acceso se reduce en etapas y se restablece al pagar.

## Ejemplo

Ejemplo de [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md) (sección «Preguntas frecuentes»):

Rara vez. La mayoría de los primeros fallos son recuperables (tarjeta caducada, fondos temporales). Un periodo de gracia con aviso visible recupera más y molesta menos; el acceso se reduce en etapas y se restablece al pagar.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un diseño razonable usa un periodo de gracia: acceso completo con un aviso visible mientras la suscripción está en `pago_pendiente`; acceso reducido (solo lectura, sin crear proyectos nuevos) en `suspendida`; exportación de datos disponible hasta el borrado. ([SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-057](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md), [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), [SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Plazo](./plazo.md), [Ancla del ciclo](../a/ancla-del-ciclo.md), [Dunning](../d/dunning.md), [Factura](../f/factura.md), [Máquina de estados](../m/maquina-de-estados.md), [Prorrateo](./prorrateo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md), [SE-204](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Periodicidad](./periodicidad.md) · [Permiso →](./permiso.md)
