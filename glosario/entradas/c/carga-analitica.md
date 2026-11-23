# Carga analítica

[↑ Glosario](../../README.md) · [← Cardinalidad](./cardinalidad.md) · [Carga cognitiva →](./carga-cognitiva.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Pocas consultas que recorren muchas filas para agregar.

Definición de trabajo de [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md).

## Por qué importa

La clase donde se define, [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), existe con este propósito: la clase existe para que decidas cuándo y cómo sacar datos de la base que sirve a la aplicación y llevarlos a un lugar pensado para responder preguntas, y para que sepas por qué esa decisión no es solo «copiar tablas».

## Cómo funciona

[SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md)) son: Las 200 000 filas y los 20 000 pedidos son sintéticos, los tiempos varían entre ejecuciones y el modelo de estados con fechas aleatorias no representa ningún negocio. No se midió ningún almacén analítico, ninguna herramienta de captura de cambios ni la base de ningún equipo; el efecto de WAL se probó en SQLite, no en un motor cliente-servidor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md), [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capa](./capa.md), [Carga operacional](./carga-operacional.md), [Estado actual](../e/estado-actual.md), [Extracción](../e/extraccion.md), [Interferencia](../i/interferencia.md), [Patrón de acceso](../p/patron-de-acceso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «OLAP».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Cardinalidad](./cardinalidad.md) · [Carga cognitiva →](./carga-cognitiva.md)
