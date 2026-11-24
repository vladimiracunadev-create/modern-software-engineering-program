# Negociación por intereses

[↑ Glosario](../../README.md) · [← Negación y mundo cerrado](./negacion-y-mundo-cerrado.md) · [Nibble →](./nibble.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

La **negociación por intereses** es un enfoque de acuerdo que parte de las razones de cada posición y no de las posiciones mismas ([SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md)). Una **posición** es lo que alguien pide («retener 730 días»); un **interés** es por qué lo pide («poder responder a una auditoría de dos años»). La distinción es la de la literatura de negociación basada en principios (Fisher y Ury), que el programa aplica a requisitos en conflicto.

## Por qué importa

Convierte posiciones incompatibles en objetivos que pueden coexistir. Si dos áreas piden cosas opuestas y se negocia sobre las posiciones, lo único posible es repartir la diferencia: nadie queda satisfecho. Si se negocia sobre los intereses, a veces hay una solución nueva que cumple ambos. Cambia el modo de resolver un conflicto de requisitos: antes de escoger a quién dar la razón, se pregunta para qué lo necesita cada parte.

## Cómo funciona

El mecanismo es preguntar «¿para qué?» tras cada posición hasta llegar a la necesidad subyacente. [SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md) lo ilustra con un conflicto de retención de datos: Auditoría pide retener 730 días; Privacidad pide no conservar datos personales más de 365. Las posiciones son incompatibles. Los intereses no: Auditoría necesita **demostrar el contenido** durante 730 días; Privacidad necesita **no tener datos personales** más de 365. Una copia anonimizada de los metadatos por 730 días satisface a ambos.

La causa de que funcione es estructural: una posición es una solución propuesta entre muchas posibles, y puede haber otra solución que sirva mejor a los intereses de todos. Negociar sobre intereses **expande el conjunto de soluciones**; negociar sobre posiciones solo lo reparte. Esta técnica se apoya en el análisis ([SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md)), que hace aparecer el conflicto con nombre y responsable, y se complementa con técnicas de priorización como MoSCoW cuando, aun después de entender los intereses, los recursos no alcanzan para todo.

## Ejemplo

El ejemplo de [SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md): dos áreas, un dato, 730 días contra 365. La pregunta «¿para qué quieren conservarlo?» saca a la luz que lo que Auditoría necesita demostrar es el contenido de las operaciones, no los datos personales de cada persona; la solución es una copia anonimizada de los metadatos por 730 días y la eliminación de los datos personales a los 365. Ninguna parte cedió su interés; se cambió la solución.

## Errores y confusiones comunes

- **Negociar posiciones y repartir la diferencia** (550 días, por ejemplo), lo que no cumple ninguna necesidad.
- **Suponer los intereses sin preguntarlos**: son hipótesis hasta que la parte los confirma.
- **Creer que siempre existe una solución ganadora para ambos**: a veces los intereses sí chocan.
- **Confundirla con ceder**: ceder es renunciar a un interés; negociar por intereses busca cumplirlos.

## Límites y cuándo no aplica

No funciona cuando una de las partes oculta sus intereses o cuando los intereses son realmente incompatibles (recursos que solo uno puede tener); entonces hace falta una regla de decisión y alguien con autoridad que la aplique. Requiere tiempo y confianza para preguntar el porqué. En una obligación legal o contractual inamovible, la posición puede ser un interés en sí misma y no admite alternativa.

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
