# Cubo de fichas

[↑ Glosario](../../README.md) · [← Cubeta de fichas](./cubeta-de-fichas.md) · [Cubrimiento de pares →](./cubrimiento-de-pares.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Mecanismo de cuota que recarga fichas a ritmo fijo hasta un máximo y gasta una por solicitud.

Definición de trabajo de [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md).

## Por qué importa

La clase donde se define, [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md), existe con este propósito: la clase existe para que puedas elegir, medir y defender el nivel de aislamiento que un producto SaaS ofrece a cada cliente, y para que sepas qué ocurre con los demás clientes cuando uno de ellos consume más de lo esperado.

## Cómo funciona

Según [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md):

Una cuota por cliente limita cuántas solicitudes puede enviar por unidad de tiempo; lo que excede se rechaza (en HTTP, con 429 y un tiempo de reintento). En la simulación, un cubo de fichas con recarga de 2,4 por tick y ráfaga máxima de 10 deja a los otros siete en **p50 10 ms, p95 10 ms y p99 20 ms** durante toda la prueba, y el vecino ve su p99 en 10 ms para lo que sí se atiende, pero **56 619 solicitudes rechazadas**. Un detalle importante: 914 solicitudes de los clientes normales también se rechazaron, porque su llegada aleatoria (Poisson de media 1,9) a veces supera la recarga de 2,4 en un instante.

## Ejemplo

Ejemplo de [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md) (sección «Ejemplo mínimo»):

Un cubo de fichas por inquilino y un planificador por turnos en pocas líneas:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En la simulación, un cubo de fichas con recarga de 2,4 por tick y ráfaga máxima de 10 deja a los otros siete en **p50 10 ms, p95 10 ms y p99 20 ms** durante toda la prueba, y el vecino ve su p99 en 10 ms para lo que sí se atiende, pero **56 619 solicitudes rechazadas**. ([SE-410](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), [SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md), [SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cuota](./cuota.md), [Mecanismo](../m/mecanismo.md), [Cola justa](./cola-justa.md), [Contexto del inquilino](./contexto-del-inquilino.md), [Radio de impacto](../r/radio-de-impacto.md), [Silo, puente, pool](../s/silo-puente-pool.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Cubeta de fichas](./cubeta-de-fichas.md) · [Cubrimiento de pares →](./cubrimiento-de-pares.md)
