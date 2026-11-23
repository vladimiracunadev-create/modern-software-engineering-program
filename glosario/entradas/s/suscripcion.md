# Suscripción

[↑ Glosario](../../README.md) · [← Supuestos](./supuestos.md) · [Sustitución →](./sustitucion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Contrato recurrente de un cliente con un plan, un ciclo y un estado.

Definición de trabajo de [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md).

## Por qué importa

La clase donde se define, [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md), existe con este propósito: la clase existe para que modeles una suscripción como lo que es: una máquina de estados con fechas, importes y eventos externos, y no como una fila con un campo «plan» y otro «vence».

## Cómo funciona

Según [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md):

Una suscripción tiene un estado, un plan, un periodo actual (inicio y fin), una fecha de próxima factura y un método de pago. Los eventos que la mueven son pocos y se pueden enumerar. El valor de escribir la tabla de transiciones no es teórico: una función `aplicar(estado, evento)` que lanza un error ante una combinación no listada convierte los errores de lógica (una cancelación que reabre una cuenta, un pago que reactiva algo que se canceló a propósito) en fallos visibles, en lugar de estados imposibles que se descubren en el informe de ingresos. El estado debe tener un solo dueño: el acceso, los informes y las pantallas lo leen; nadie lo deduce de la última factura.

Según [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md):

Toma una suscripción que tengas (streaming, nube, un servicio de software) y reconstruye su máquina de estados: qué ocurre si cancelas hoy, si el pago falla, si cambias de plan a mitad de ciclo. Anota lo que no pudiste responder sin probar. Eso es lo que el producto debería haber puesto por escrito.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md):

*Escenario ilustrativo: las cifras y los resultados de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un diseño razonable usa un periodo de gracia: acceso completo con un aviso visible mientras la suscripción está en `pago_pendiente`; acceso reducido (solo lectura, sin crear proyectos nuevos) en `suspendida`; exportación de datos disponible hasta el borrado. ([SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Estado](../e/estado.md).
- **Ver también:** [Ciclo](../c/ciclo.md), [Contrato](../c/contrato.md), [Plan](../p/plan.md), [Ancla del ciclo](../a/ancla-del-ciclo.md), [Dunning](../d/dunning.md), [Factura](../f/factura.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (16 clases más lo mencionan; las que más):

[SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-080](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md), [SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md), [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Stripe](../../../casos/exito/stripe.md), [Slack](../../../casos/exito/slack.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Supuestos](./supuestos.md) · [Sustitución →](./sustitucion.md)
