# Red de pruebas

[↑ Glosario](../../README.md) · [← Recurso huérfano](./recurso-huerfano.md) · [Red de seguridad →](./red-de-seguridad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Conjunto de comprobaciones que debe fallar si el comportamiento cambia.

Definición de trabajo de [SE-307 — Refactorización segura apoyada por pruebas](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md).

## Por qué importa

En [SE-307 — Refactorización segura apoyada por pruebas](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md), el tema «Red de pruebas y mutación» importa porque mide cuánto detecta la red, no cuánto ejecuta.

## Cómo funciona

Según [SE-307 — Refactorización segura apoyada por pruebas](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md):

Una red de pruebas es el conjunto que debe fallar si el comportamiento cambia. Su calidad no es cuántas líneas ejecuta, sino cuántos cambios detecta. La **prueba de mutación** lo mide: se generan variantes del programa con un cambio pequeño cada una (un `<=` por un `<`, un `+` por un `-`, una constante más uno) y se cuenta cuántas hace fallar la suite. Los mutantes que sobreviven señalan lo que la red no comprueba. Algunos mutantes son equivalentes (no cambian ninguna salida) y no se pueden matar.

## Ejemplo

Ejemplo de [SE-307 — Refactorización segura apoyada por pruebas](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md) (sección «Caso conductor»):

El componente `tarifas` conserva el diagnóstico de `SE-306` y gana una red de pruebas con una puntuación de mutación medida, valores de borde derivados del código y una comparación con la versión anterior. `SE-308` examinará cómo diseñar para el cambio, la prueba y la operación desde el principio. Cambia después una sola decisión, el tamaño del paso, y observa cuántos sospechosos tiene el primer fallo.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-307 — Refactorización segura apoyada por pruebas](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md)) son:

- **El refactor pasó la suite y rompió una frontera** — causa: faltan valores de borde. Corrección: derivar bordes de cada comparación.
- **Cobertura alta y mutantes vivos** — causa: las líneas se ejecutan, no se comprueban. Corrección: medir mutantes muertos además de cobertura.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-307 — Refactorización segura apoyada por pruebas](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md)) son: Las definiciones son operativas para `tarifas`. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la bibliografía enlazada al final. Se ejecutaron tres análisis con código de ejemplo y datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ninguna base de código real ni se contrastaron los mutantes con defectos reales; la función, los 19 mutantes y la probabilidad de 0,03 por paso son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-306](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Puntuación de mutación](../p/puntuacion-de-mutacion.md), [Refactorización](./refactorizacion.md), [Valor de borde](../v/valor-de-borde.md), [Variante defectuosa](../v/variante-defectuosa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-307 — Refactorización segura apoyada por pruebas](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md), [SE-306](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md), [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md), [SE-309](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md), [SE-310](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md), [SE-542](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «Refactoring» (2.ª ed.)](https://martinfowler.com/books/refactoring.html) — refactorizar en pasos pequeños con pruebas; autoridad: Martin Fowler.
- [DeMillo, Lipton y Sayward (IEEE Computer, 1978)](https://doi.org/10.1109/C-M.1978.218136) — origen de la prueba de mutación; autoridad: IEEE Computer.
- [Jia y Harman (IEEE TSE, 2011)](https://doi.org/10.1109/TSE.2010.62) — revisión de la prueba de mutación; autoridad: IEEE Transactions on Software Engineering.
- [Fowler, «Test Coverage»](https://martinfowler.com/bliki/TestCoverage.html) — qué dice y qué no dice la cobertura; autoridad: Martin Fowler.
- [Feathers, «Working Effectively with Legacy Code»](https://www.oreilly.com/library/view/working-effectively-with/0131177052/) — pruebas de caracterización y costuras en código heredado; autoridad: su autor (Prentice Hall).

---

[↑ Glosario](../../README.md) · [← Recurso huérfano](./recurso-huerfano.md) · [Red de seguridad →](./red-de-seguridad.md)
