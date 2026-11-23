# Valor de borde

[↑ Glosario](../../README.md) · [← Valor](./valor.md) · [Valor de frontera →](./valor-de-frontera.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Valor justo en el límite de una condición, y los vecinos inmediatos.

Definición de trabajo de [SE-307 — Refactorización segura apoyada por pruebas](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md).

## Por qué importa

La clase donde se define, [SE-307 — Refactorización segura apoyada por pruebas](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md), existe con este propósito: la clase existe para que cambies la estructura de un código sin cambiar lo que hace, con una red de pruebas cuya capacidad de detectar errores hayas medido, y para que elijas el tamaño de cada paso por lo que cuesta encontrar un defecto, no por la prisa.

## Cómo funciona

Según [SE-307 — Refactorización segura apoyada por pruebas](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** un cliente VIP con 20 kilos paga 9 pesos más después del refactor y la suite sigue en verde. **Hipótesis rivales:** (a) el cliente cambió de tarifa; (b) hay un error de redondeo; (c) la condición de la frontera cambió. **Prueba:** ejecuta la versión anterior y la nueva con `peso = 20`; si difieren y todos los ejemplos coinciden, la causa es (c). **Conclusión:** la red no tenía un valor de borde. **Regresión:** añade los valores 19,9, 20 y 20,1 como pruebas y la comparación con la versión anterior sobre 2000 entradas, y no cambies a la vez la condición y los ejemplos.

## Ejemplo

Ejemplo de [SE-307 — Refactorización segura apoyada por pruebas](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md) (sección «Caso conductor»):

El componente `tarifas` conserva el diagnóstico de `SE-306` y gana una red de pruebas con una puntuación de mutación medida, valores de borde derivados del código y una comparación con la versión anterior. `SE-308` examinará cómo diseñar para el cambio, la prueba y la operación desde el principio. Cambia después una sola decisión, el tamaño del paso, y observa cuántos sospechosos tiene el primer fallo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El refactor pasó la suite y rompió una frontera** — causa: faltan valores de borde. Corrección: derivar bordes de cada comparación. ([SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Conclusión:** la red no tenía un valor de borde. ([SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-306](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Límite](../l/limite.md), [Valor](./valor.md), [Puntuación de mutación](../p/puntuacion-de-mutacion.md), [Red de pruebas](../r/red-de-pruebas.md), [Refactorización](../r/refactorizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-307 — Refactorización segura apoyada por pruebas](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

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

[↑ Glosario](../../README.md) · [← Valor](./valor.md) · [Valor de frontera →](./valor-de-frontera.md)
