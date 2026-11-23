# Decisión colectiva

[↑ Glosario](../../README.md) · [← Decisión abierta](./decision-abierta.md) · [Decisión con plazo →](./decision-con-plazo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Regla para transformar preferencias de varias personas en una elección del grupo.

Definición de trabajo de [SE-150 — Priorización, dependencias y negociación](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md).

## Por qué importa

En [SE-150 — Priorización, dependencias y negociación](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md), el tema «Decisión colectiva» importa porque los métodos de votación pueden no tener ganador o discrepar entre sí.

## Cómo funciona

Según [SE-150 — Priorización, dependencias y negociación](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md), en la sección «Decisión colectiva»:

Cuando un grupo elige entre tres o más opciones, «la que prefiera la mayoría» puede no existir: la paradoja de Condorcet muestra mayorías cíclicas. Y métodos razonables —pluralidad, recuento de Borda, eliminación sucesiva— pueden elegir ganadores distintos con las mismas preferencias. Un equipo que decide por voto debe declarar el método antes de votar y saber qué hacer si no hay ganador; si no, el método se elegirá después, según quién gane.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-150 — Priorización, dependencias y negociación](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md):

La priorización del trimestre se registra como una tabla con el orden, la razón y quién decidió:

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-150 — Priorización, dependencias y negociación](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md)) son:

- **El plan aprobado no se puede construir** — causa: se ordenó por valor sin comprobar dependencias. Corrección: verificar el cierre del conjunto antes de aprobar.
- **Casi todo es «Must»** — causa: no hay un límite a la categoría. Corrección: fijar un tope como fracción del esfuerzo y desempatar con una regla.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-150 — Priorización, dependencias y negociación](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midieron decisiones reales, los sesgos y los costos son supuestos del autor y las frecuencias de ciclos suponen preferencias equiprobables. La siguiente clase enlaza cada requisito con su origen, su criterio y su evidencia.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Preferencia](../p/preferencia.md), [Regla](../r/regla.md), [Dependencia](./dependencia.md), [MoSCoW](../m/moscow.md), [Negociación por intereses](../n/negociacion-por-intereses.md), [Valor, costo y riesgo](../v/valor-costo-y-riesgo.md).
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

[↑ Glosario](../../README.md) · [← Decisión abierta](./decision-abierta.md) · [Decisión con plazo →](./decision-con-plazo.md)
