# Hub, enlace y satélite

[↑ Glosario](../../README.md) · [← Hot path](./hot-path.md) · [Hueco de contenido →](./hueco-de-contenido.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Tablas de identidad, de relación y de atributos con historia de un Data Vault.

Definición de trabajo de [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md).

## Por qué importa

La clase donde se define, [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md), existe con este propósito: la clase existe para que organices los datos analíticos de modo que las preguntas se respondan correctamente sin que cada analista reinvente las uniones, y para que sepas dónde están las trampas que producen números verosímiles y erróneos.

## Cómo funciona

Según [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md):

El vault compra trazabilidad completa, cargas repetibles y la posibilidad de integrar fuentes nuevas sin tocar lo existente. Cuesta uniones: la misma pregunta de ventas por ciudad necesitó hub, enlace y satélite frente a una sola unión por dimensión de la estrella, y la consulta no es lo que se ofrece a los analistas. Por eso en la práctica el vault es una capa de integración sobre la cual se construye una vista dimensional (la «capa de negocio»). En el laboratorio, las dos consultas tardaron del mismo orden (entre 100 y 300 ms según la ejecución, con el vault algo más lento en las dos corridas); el costo real del vault no está en una consulta sino en la cantidad de tablas y de cargas que hay que mantener.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cuesta uniones: la misma pregunta de ventas por ciudad necesitó hub, enlace y satélite frente a una sola unión por dimensión de la estrella, y la consulta no es lo que se ofrece a los analistas. ([SE-363](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md), [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md), [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-362](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Atributo](../a/atributo.md), [Relación](../r/relacion.md), [Abanico de uniones](../a/abanico-de-uniones.md), [Clave sustituta](../c/clave-sustituta.md), [Dimensión](../d/dimension.md), [Dimensión de cambio lento](../d/dimension-de-cambio-lento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Hot path](./hot-path.md) · [Hueco de contenido →](./hueco-de-contenido.md)
