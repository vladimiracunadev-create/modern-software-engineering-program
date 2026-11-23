# Poscondición

[↑ Glosario](../../README.md) · [← Portal documental](./portal-documental.md) · [Postcondición →](./postcondicion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Propiedad garantizada al terminar bajo el contrato.

Definición de trabajo de [SE-052 — Invariantes, precondiciones y poscondiciones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-547 — Diseño por contrato y pruebas de contrato como oráculo](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md): Lo que la rutina garantiza al terminar.

## Por qué importa

La clase donde se define, [SE-052 — Invariantes, precondiciones y poscondiciones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md), existe con este propósito: la clase existe para formular precondiciones, poscondiciones e invariantes que hagan verificable una transición.

## Cómo funciona

Según [SE-052 — Invariantes, precondiciones y poscondiciones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md), en la sección «Poscondición»:

La poscondición relaciona estado previo, entrada y salida. «devuelve una lista» es débil; «devuelve solo pruebas autorizadas y toda hipótesis descartada cita evidencia» es contrastable. Una operación puede garantizar distintas poscondiciones para éxito y error.

## Ejemplo

Ejemplo de [SE-052 — Invariantes, precondiciones y poscondiciones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md) (sección «Ejemplo mínimo»):

Especifica `seleccionar_prueba(hipótesis, pruebas, presupuesto)` con tres precondiciones, cuatro poscondiciones y dos errores. Define un invariante que impida ejecutar una prueba no autorizada.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La función falla sin decir quién se equivocó** — causa: contrato implícito. Corrección: escribir precondición, invariante y poscondición. ([SE-052](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **poscondición** es lo que la implementación garantiza (las observaciones contradictorias se informan, no se ocultan). ([SE-052](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Contrato](../c/contrato.md), [Propiedad](./propiedad.md), [Composición](../c/composicion.md), [Contrato del consumidor](../c/contrato-del-consumidor.md), [Dominio](../d/dominio.md), [Estado válido](../e/estado-valido.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-052 — Invariantes, precondiciones y poscondiciones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-547 — Diseño por contrato y pruebas de contrato como oráculo](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-051](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md), [SE-053](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md), [SE-054](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.
- [MIT 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — aporta definiciones, invariantes y análisis de estructuras y algoritmos usados en la clase.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.

---

[↑ Glosario](../../README.md) · [← Portal documental](./portal-documental.md) · [Postcondición →](./postcondicion.md)
