# Factura

[↑ Glosario](../../README.md) · [← Factory](./factory.md) · [Fake →](./fake.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Documento que fija lo que se debe por un periodo; inmutable una vez emitida.

Definición de trabajo de [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md).

## Por qué importa

La clase donde se define, [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md), existe con este propósito: la clase existe para que modeles una suscripción como lo que es: una máquina de estados con fechas, importes y eventos externos, y no como una fila con un campo «plan» y otro «vence».

## Cómo funciona

Según [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md):

Una suscripción tiene un estado, un plan, un periodo actual (inicio y fin), una fecha de próxima factura y un método de pago. Los eventos que la mueven son pocos y se pueden enumerar. El valor de escribir la tabla de transiciones no es teórico: una función `aplicar(estado, evento)` que lanza un error ante una combinación no listada convierte los errores de lógica (una cancelación que reabre una cuenta, un pago que reactiva algo que se canceló a propósito) en fallos visibles, en lugar de estados imposibles que se descubren en el informe de ingresos. El estado debe tener un solo dueño: el acceso, los informes y las pantallas lo leen; nadie lo deduce de la última factura.

Según [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md):

El equipo de *Tablero* rediseña su facturación recurrente. Escribe la tabla de nueve transiciones y la convierte en pruebas: una por cada transición válida y una por cada transición inválida importante (un pago sobre una cuenta cancelada pide reactivación explícita). Reemplaza el campo `vence` por un ancla y un periodo actual, con una prueba de renovaciones desde el 29, 30 y 31 en un año bisiesto. Para el prorrateo define la regla («cobro inmediato al subir, crédito en la siguiente factura al bajar; redondeo hacia el centavo más cercano en cada línea») y la escribe también en la página de precios.

## Ejemplo

Ejemplo de [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md) (sección «Ejemplo profesional»):

El equipo de *Tablero* rediseña su facturación recurrente. Escribe la tabla de nueve transiciones y la convierte en pruebas: una por cada transición válida y una por cada transición inválida importante (un pago sobre una cuenta cancelada pide reactivación explícita). Reemplaza el campo `vence` por un ancla y un periodo actual, con una prueba de renovaciones desde el 29, 30 y 31 en un año bisiesto. Para el prorrateo define la regla («cobro inmediato al subir, crédito en la siguiente factura al bajar; redondeo hacia el centavo más cercano en cada línea») y la escribe también en la página de precios.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El estado debe tener un solo dueño: el acceso, los informes y las pantallas lo leen; nadie lo deduce de la última factura. ([SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-057](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md), [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), [SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Documento](../d/documento.md), [Ancla del ciclo](../a/ancla-del-ciclo.md), [Dunning](../d/dunning.md), [Máquina de estados](../m/maquina-de-estados.md), [Periodo de gracia](../p/periodo-de-gracia.md), [Prorrateo](../p/prorrateo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (34 clases más lo mencionan; las que más):

[SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), [SE-294](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md), [SE-140](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md), [SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md), [SE-370](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md), [SE-415](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Factory](./factory.md) · [Fake →](./fake.md)
