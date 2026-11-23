# MoSCoW

[↑ Glosario](../../README.md) · [← Montaje](./montaje.md) · [Motor →](./motor.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Clasificación en Must, Should, Could y Won't para decir qué debe estar, qué debería, qué podría y qué no estará esta vez.

Definición de trabajo de [SE-150 — Priorización, dependencias y negociación](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md).

## Por qué importa

En [SE-150 — Priorización, dependencias y negociación](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md), el tema «MoSCoW» importa porque clasifica en Must, Should, Could y Won't, pero sin límite se infla.

## Cómo funciona

Según [SE-150 — Priorización, dependencias y negociación](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md), en la sección «MoSCoW»:

MoSCoW clasifica en lo que debe estar (Must), debería (Should), podría (Could) y no estará esta vez (Won't). Es útil para conversar, porque obliga a decir «no» explícitamente. Su debilidad es que no impone un presupuesto: si cada interesado puede marcar Must, la categoría crece hasta cubrir casi todo y deja de ordenar. Las guías de la técnica recomiendan limitar Must a una fracción del esfuerzo disponible; el límite es una decisión del equipo, no una propiedad del método.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-150 — Priorización, dependencias y negociación](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md):

La priorización del trimestre se registra como una tabla con el orden, la razón y quién decidió:

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-150 — Priorización, dependencias y negociación](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md)) son:

- **El plan aprobado no se puede construir** — causa: se ordenó por valor sin comprobar dependencias. Corrección: verificar el cierre del conjunto antes de aprobar.
- **Casi todo es «Must»** — causa: no hay un límite a la categoría. Corrección: fijar un tope como fracción del esfuerzo y desempatar con una regla.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- MoSCoW clasifica en lo que debe estar (Must), debería (Should), podría (Could) y no estará esta vez (Won't). ([SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Decisión colectiva](../d/decision-colectiva.md), [Dependencia](../d/dependencia.md), [Negociación por intereses](../n/negociacion-por-intereses.md), [Valor, costo y riesgo](../v/valor-costo-y-riesgo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-150 — Priorización, dependencias y negociación](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Karlsson y Ryan: A cost-value approach for prioritizing requirements (1997)](https://doi.org/10.1109/52.605933) — comparación por pares de valor y costo; autoridad: IEEE Software.
- [Stanford Encyclopedia of Philosophy: Voting Methods](https://plato.stanford.edu/entries/voting-methods/) — paradoja de Condorcet y métodos de votación; autoridad: Stanford University.
- [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) — atributos de un conjunto de requisitos, incluida la priorización; autoridad: ISO, IEC e IEEE.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — priorización y negociación de requisitos; autoridad: IEEE Computer Society.
- [Python: `functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache) — memoización del conteo de órdenes.

---

[↑ Glosario](../../README.md) · [← Montaje](./montaje.md) · [Motor →](./motor.md)
