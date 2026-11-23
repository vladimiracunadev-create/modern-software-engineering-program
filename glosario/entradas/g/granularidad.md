# Granularidad

[↑ Glosario](../../README.md) · [← Grandfathering](./grandfathering.md) · [Granularidad de los enlaces →](./granularidad-de-los-enlaces.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Qué es exactamente una fila de una tabla.

Definición de trabajo de [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md).

## Por qué importa

En [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md), el tema «Granularidad» importa porque define qué es una fila y qué se puede sumar.

## Cómo funciona

Según [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md):

Elige dos informes de tu organización que debieran dar el mismo número y no lo dan. Averigua la granularidad de cada tabla que usan y la política de historia de las dimensiones, y di cuál de las dos respuestas responde cuál pregunta.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md)) son: Los 20 000 pedidos, las 132 mudanzas y las líneas por pedido son construcciones del autor; el vault es mínimo y no incluye la capa de negocio ni cargas paralelas. No se midió ningún almacén, ninguna herramienta de modelado ni el costo de mantener un vault real. El siguiente paso, `SE-364`, construye estas tablas con transformaciones idempotentes y cubre los reprocesos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md), [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md), [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-362](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Abanico de uniones](../a/abanico-de-uniones.md), [Clave sustituta](../c/clave-sustituta.md), [Dimensión](../d/dimension.md), [Dimensión de cambio lento](../d/dimension-de-cambio-lento.md), [Hecho](../h/hecho.md), [Hub, enlace y satélite](../h/hub-enlace-y-satelite.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md), [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md), [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md), [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md), [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md), [SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md), [SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Grandfathering](./grandfathering.md) · [Granularidad de los enlaces →](./granularidad-de-los-enlaces.md)
