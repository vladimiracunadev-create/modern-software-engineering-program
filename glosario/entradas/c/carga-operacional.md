# Carga operacional

[↑ Glosario](../../README.md) · [← Carga cognitiva de un equipo](./carga-cognitiva-de-un-equipo.md) · [Carga por lotes →](./carga-por-lotes.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Muchas transacciones cortas que leen y escriben pocas filas.

Definición de trabajo de [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md).

## Por qué importa

La clase donde se define, [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), existe con este propósito: la clase existe para que decidas cuándo y cómo sacar datos de la base que sirve a la aplicación y llevarlos a un lugar pensado para responder preguntas, y para que sepas por qué esa decisión no es solo «copiar tablas».

## Cómo funciona

[SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: consulta la clase para el mecanismo completo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md)) son: Las 200 000 filas y los 20 000 pedidos son sintéticos, los tiempos varían entre ejecuciones y el modelo de estados con fechas aleatorias no representa ningún negocio. No se midió ningún almacén analítico, ninguna herramienta de captura de cambios ni la base de ningún equipo; el efecto de WAL se probó en SQLite, no en un motor cliente-servidor.

## Relación con otros conceptos

- **Prerrequisito:** [Transacción](../t/transaccion.md).
- **Ver también:** [Capa](./capa.md), [Carga analítica](./carga-analitica.md), [Estado actual](../e/estado-actual.md), [Extracción](../e/extraccion.md), [Interferencia](../i/interferencia.md), [Patrón de acceso](../p/patron-de-acceso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «OLTP».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Carga cognitiva de un equipo](./carga-cognitiva-de-un-equipo.md) · [Carga por lotes →](./carga-por-lotes.md)
