# Recomposición

[↑ Glosario](../../README.md) · [← Recomendación condicionada](./recomendacion-condicionada.md) · [Reconciliación →](./reconciliacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Integración y revisión de propiedades del conjunto.

Definición de trabajo de [SE-049 — Descomposición, abstracción y reconocimiento de patrones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md).

## Por qué importa

La clase donde se define, [SE-049 — Descomposición, abstracción y reconocimiento de patrones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md), existe con este propósito: la clase existe para descomponer un problema por responsabilidades y contratos sin perder restricciones transversales.

## Cómo funciona

Según [SE-049 — Descomposición, abstracción y reconocimiento de patrones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md):

Resolver partes no garantiza resolver el todo. La recomposición revisa dependencias, conflictos y propiedades globales: privacidad, deadline y capacidad. Un árbol es completo para el alcance cuando cada resultado final puede rastrearse a una entrada y cada riesgo relevante tiene tratamiento o exclusión explícita.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-049 — Descomposición, abstracción y reconocimiento de patrones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md):

El modelo de decisión diagnóstica representa el diagnóstico como un grafo: nodos de observación, hipótesis y prueba; aristas de dependencia. Una política impide ejecutar una prueba si falta autorización o si otra prueba barata ya descarta su rama. El grafo puede cambiar sin alterar el contrato del informe.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-049 — Descomposición, abstracción y reconocimiento de patrones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md)) son:

- **El árbol enumera funciones del programa** — causa: se describe la implementación, no el problema. Corrección: reescribir con decisión, hipótesis, pruebas y restricciones.
- **Una prueba aparece sin resultado bajo alguna hipótesis** — causa: la matriz está incompleta. Corrección: completar cada celda o declarar `unknown` y puntuar en cero.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La recomposición revisa dependencias, conflictos y propiedades globales: privacidad, deadline y capacidad. ([SE-049](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Conjunto](../c/conjunto.md), [Propiedad](../p/propiedad.md), [Revisión](./revision.md), [Abstracción](../a/abstraccion.md), [Descomposición](../d/descomposicion.md), [Dominio](../d/dominio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-049 — Descomposición, abstracción y reconocimiento de patrones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.
- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.

---

[↑ Glosario](../../README.md) · [← Recomendación condicionada](./recomendacion-condicionada.md) · [Reconciliación →](./reconciliacion.md)
