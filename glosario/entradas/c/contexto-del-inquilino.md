# Contexto del inquilino

[↑ Glosario](../../README.md) · [← Contexto de uso](./contexto-de-uso.md) · [Contexto delimitado →](./contexto-delimitado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Identificador que acompaña a cada petición, mensaje, clave de caché y línea de registro.

Definición de trabajo de [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md).

## Por qué importa

En [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md), el tema «Contexto del inquilino» importa porque es lo primero que se pierde en un trabajo asíncrono y lo que hace posible toda política posterior.

## Cómo funciona

[SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: consulta la clase para el mecanismo completo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md):

*Escenario ilustrativo: las cifras y los resultados de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md)) son: Se simularon ocho clientes sobre una capacidad compartida con semilla 34 y se modeló el costo con parámetros del autor; no se midió ningún proveedor, base de datos ni balanceador, ni se contempló el efecto de los reintentos del cliente sobre la cola. Las magnitudes dependen del modelo; la forma (una cola única contagia, una cuota o una cola justa contienen) es el resultado que se puede reutilizar.

## Relación con otros conceptos

- **Prerrequisito:** [Clave de caché](./clave-de-cache.md).
- **Ver también:** [Registro](../r/registro.md), [Cola justa](./cola-justa.md), [Cubo de fichas](./cubo-de-fichas.md), [Cuota](./cuota.md), [Radio de impacto](../r/radio-de-impacto.md), [Silo, puente, pool](../s/silo-puente-pool.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Contexto de uso](./contexto-de-uso.md) · [Contexto delimitado →](./contexto-delimitado.md)
