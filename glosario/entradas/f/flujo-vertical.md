# Flujo vertical

[↑ Glosario](../../README.md) · [← Flujo manual](./flujo-manual.md) · [Flujos calientes y fríos →](./flujos-calientes-y-frios.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Recorrido completo de una tarea por capas.

Definición de trabajo de [SE-011 — Taller: anatomía verificable de un producto real](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md).

## Por qué importa

Su importancia se desarrolla en las clases enlazadas en «Dónde se enseña».

## Cómo funciona

Según [SE-011 — Taller: anatomía verificable de un producto real](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md):

El flujo vertical comienza en la interfaz o punto de entrada, sigue contrato, validación, autorización, lógica, persistencia, dependencias y respuesta, y termina en prueba, señal operativa y recuperación. No todas las capas existen ni están en el mismo repositorio. Un salto se registra como incógnita con la evidencia que permitiría resolverla; no se rellena por intuición.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-011 — Taller: anatomía verificable de un producto real](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md):

En el producto de referencia, sigue la creación de una solicitud desde OpenAPI hasta requisitos, arquitectura, pruebas y runbook. Si el contrato admite reintento pero no hay idempotencia documentada, registra riesgo, no afirmes defecto ejecutado.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **informe organizado por carpetas** — causa: se inventarió estructura sin seguir capacidad. Corrección: elige tarea y traza flujo vertical normal y degradado. ([SE-011](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El flujo vertical comienza en la interfaz o punto de entrada, sigue contrato, validación, autorización, lógica, persistencia, dependencias y respuesta, y termina en prueba, señal operativa y recuperación. ([SE-011](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md), [SE-010](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capa](../c/capa.md), [Tarea](../t/tarea.md), [Contrato](../c/contrato.md), [Evidencia negativa](../e/evidencia-negativa.md), [Fuente de verdad](./fuente-de-verdad.md), [Gap](../g/gap.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-011 — Taller: anatomía verificable de un producto real](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Flujo manual](./flujo-manual.md) · [Flujos calientes y fríos →](./flujos-calientes-y-frios.md)
