# Conjunto curado

[↑ Glosario](../../README.md) · [← Conjunto combinatorio](./conjunto-combinatorio.md) · [Conocimiento perdido →](./conocimiento-perdido.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Casos elegidos por su dificultad o importancia, no al azar.

Definición de trabajo de [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md).

## Por qué importa

La clase donde se define, [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md), existe con este propósito: la clase existe para que trates una evaluación como lo que es, un **instrumento de medida con ruido**, y no como una prueba determinista con otro nombre.

## Cómo funciona

Según [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md):

Una regresión rara vez afecta por igual a todos los casos. Un cambio en las instrucciones de un asistente suele deteriorar la manera de resolver casos difíciles y dejar igual los fáciles. Una muestra al azar diluye esa señal con casos que no cambian. Un conjunto **curado** con casos difíciles (los que han fallado antes, los de borde, los que importan al negocio) la concentra. Por eso conviene partir de pocos casos bien elegidos y añadir más a medida que aparecen fallos reales; la fuente de Anthropic dedica una sección a cómo ir de cero a una primera evaluación útil.

Según [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md):

**Corrección.** Se añade una puerta separada para los casos de tono, con un conjunto curado y una zona de duda; se registra el fallo real como caso nuevo; y se pasa a tres repeticiones por caso en el conjunto completo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md)) son: La simulación modela casos como lanzamientos independientes con probabilidades supuestas; no se evaluó ningún modelo ni producto real. El siguiente paso, `SE-550`, trata un flujo de trabajo concreto para agentes de código, ODD, con su evidencia declarada y los límites de su documentación.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-548](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evaluación](../e/evaluacion.md), [Falso pase](../f/falso-pase.md), [Falso rechazo](../f/falso-rechazo.md), [Pass@k y pass^k](../p/pass-k-y-pass-k.md), [Puerta de release](../p/puerta-de-release.md), [Repetición](../r/repeticion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Conjunto combinatorio](./conjunto-combinatorio.md) · [Conocimiento perdido →](./conocimiento-perdido.md)
