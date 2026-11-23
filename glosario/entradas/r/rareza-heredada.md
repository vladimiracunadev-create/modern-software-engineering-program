# Rareza heredada

[↑ Glosario](../../README.md) · [← Ranura](./ranura.md) · [Rastrear →](./rastrear.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Comportamiento no documentado del código existente que puede estar en uso.

Definición de trabajo de [SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md).

## Por qué importa

En [SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md), el tema «Rarezas heredadas» importa porque hay que decidir si se conservan o se corrigen.

## Cómo funciona

Según [SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md), en la sección «Rarezas heredadas»:

Cada diferencia detectada es una decisión. Algunas rarezas son defectos que nadie notó (un cupón que da un monto negativo y se corrige a cero por un piso), otras son acuerdos implícitos con clientes (un `urgente` que llega como `2` o como `"si"` y se trata como falso porque la comparación es con `True`). Conservar una rareza la convierte en una regla explícita con una prueba y un nombre; corregirla es un cambio de comportamiento que se anuncia y se programa. No decidir deja la rareza escondida en una simplificación.

## Ejemplo

Caso medido en la sección «Rarezas heredadas» de [SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md):

Cada diferencia detectada es una decisión. Algunas rarezas son defectos que nadie notó (un cupón que da un monto negativo y se corrige a cero por un piso), otras son acuerdos implícitos con clientes (un `urgente` que llega como `2` o como `"si"` y se trata como falso porque la comparación es con `True`). Conservar una rareza la convierte en una regla explícita con una prueba y un nombre; corregirla es un cambio de comportamiento que se anuncia y se programa. No decidir deja la rareza escondida en una simplificación.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md)) son:

- **El refactor pasa las pruebas y rompe a un cliente** — causa: el maestro no incluye entradas de canales antiguos. Corrección: añadir las entradas reales (valores no booleanos, formatos viejos).
- **No se sabe qué paso cambió el comportamiento** — causa: se hicieron varios pasos antes de comparar. Corrección: comparar tras cada paso y hacer un commit por paso.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md)) son: Las definiciones son operativas para `tarifas`. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la bibliografía enlazada al final. Se ejecutaron tres análisis sobre una función heredada de ejemplo con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se consultó a ningún cliente real ni se registró un maestro con tráfico real; la función, su dominio de entradas, los valores no booleanos y los 39 mutantes son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md), [SE-310](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Arco](../a/arco.md), [Compatibilidad hacia atrás](../c/compatibilidad-hacia-atras.md), [Maestro dorado](../m/maestro-dorado.md), [Prueba de caracterización](../p/prueba-de-caracterizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-312](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Rarezas heredadas».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Feathers, «Working Effectively with Legacy Code»](https://www.oreilly.com/library/view/working-effectively-with/0131177052/) — pruebas de caracterización; autoridad: su autor (Prentice Hall).
- [Fowler, «Refactoring» (2.ª ed.)](https://martinfowler.com/books/refactoring.html) — refactorizar en pasos pequeños; autoridad: Martin Fowler.
- [Fowler, «Extract Function»](https://refactoring.com/catalog/extractFunction.html) — extracción de una función; autoridad: Martin Fowler.
- [Fowler, «Self Testing Code»](https://martinfowler.com/bliki/SelfTestingCode.html) — código que se comprueba solo; autoridad: Martin Fowler.
- [Jia y Harman (IEEE TSE, 2011)](https://doi.org/10.1109/TSE.2010.62) — revisión de la prueba de mutación; autoridad: IEEE Transactions on Software Engineering.

---

[↑ Glosario](../../README.md) · [← Ranura](./ranura.md) · [Rastrear →](./rastrear.md)
