# Negociación por intereses

[↑ Glosario](../../README.md) · [← Negación y mundo cerrado](./negacion-y-mundo-cerrado.md) · [Nibble →](./nibble.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Acuerdo que parte de las razones de cada posición y no de las posiciones mismas.

Definición de trabajo de [SE-150 — Priorización, dependencias y negociación](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md).

## Por qué importa

En [SE-150 — Priorización, dependencias y negociación](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md), el tema «Negociación por intereses» importa porque convierte posiciones incompatibles en objetivos que pueden coexistir.

## Cómo funciona

Según [SE-150 — Priorización, dependencias y negociación](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md), en la sección «Negociación por intereses»:

Una posición es lo que alguien pide («retener 730 días»); un interés es por qué lo pide («poder responder a una auditoría de dos años»). Dos posiciones incompatibles pueden tener intereses compatibles: Auditoría necesita demostrar el contenido durante 730 días, Privacidad necesita no tener datos personales más de 365; una copia anonimizada de los metadatos por 730 días satisface a ambos. Negociar sobre intereses expande el conjunto de soluciones; negociar sobre posiciones solo reparte la diferencia.

## Ejemplo

Caso medido en la sección «Negociación por intereses» de [SE-150 — Priorización, dependencias y negociación](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md):

Una posición es lo que alguien pide («retener 730 días»); un interés es por qué lo pide («poder responder a una auditoría de dos años»). Dos posiciones incompatibles pueden tener intereses compatibles: Auditoría necesita demostrar el contenido durante 730 días, Privacidad necesita no tener datos personales más de 365; una copia anonimizada de los metadatos por 730 días satisface a ambos. Negociar sobre intereses expande el conjunto de soluciones; negociar sobre posiciones solo reparte la diferencia.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-150 — Priorización, dependencias y negociación](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md)) son:

- **El plan aprobado no se puede construir** — causa: se ordenó por valor sin comprobar dependencias. Corrección: verificar el cierre del conjunto antes de aprobar.
- **Casi todo es «Must»** — causa: no hay un límite a la categoría. Corrección: fijar un tope como fracción del esfuerzo y desempatar con una regla.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-150 — Priorización, dependencias y negociación](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midieron decisiones reales, los sesgos y los costos son supuestos del autor y las frecuencias de ciclos suponen preferencias equiprobables. La siguiente clase enlaza cada requisito con su origen, su criterio y su evidencia.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Decisión colectiva](../d/decision-colectiva.md), [Dependencia](../d/dependencia.md), [MoSCoW](../m/moscow.md), [Valor, costo y riesgo](../v/valor-costo-y-riesgo.md).
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

[↑ Glosario](../../README.md) · [← Negación y mundo cerrado](./negacion-y-mundo-cerrado.md) · [Nibble →](./nibble.md)
