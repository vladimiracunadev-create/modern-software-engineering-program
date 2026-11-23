# Opción de refactorizar

[↑ Glosario](../../README.md) · [← Opción](./opcion.md) · [Opcode →](./opcode.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Derecho, sin obligación, de pagar el principal cuando el código se vuelva a tocar.

Definición de trabajo de [SE-310 — Deuda técnica, interés y opciones](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md).

## Por qué importa

La clase donde se define, [SE-310 — Deuda técnica, interés y opciones](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md), existe con este propósito: la clase existe para que hables de la deuda técnica con el vocabulario del dinero que la metáfora pide (principal, interés, plazo, opción) y para que decidas qué pagar, cuándo y qué dejar, usando una estimación explícita de lo que cuesta no pagar y no la incomodidad de ver un código feo.

## Cómo funciona

[SE-310 — Deuda técnica, interés y opciones](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para `tarifas`. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la bibliografía enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-310 — Deuda técnica, interés y opciones](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md):

El equipo de `tarifas` no paga el tablero de 140 elementos. Estima, para los diez candidatos con más actividad en `git log`, tres cosas: la fricción por cambio (medida en una encuesta de tres preguntas al equipo y contrastada con el tiempo de los últimos cambios), la frecuencia de cambio (de la historia del repositorio) y el principal (una estimación en puntos, con rango). Calcula el interés anual y el plazo de recuperación.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-310 — Deuda técnica, interés y opciones](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md)) son:

- **Se dedica un porcentaje fijo a «pagar deuda» sin resultados visibles** — causa: no se estimó el interés de cada elemento. Corrección: estimar interés y principal y ordenar por plazo de recuperación.
- **Se refactoriza el módulo más feo y el cambio sigue costando lo mismo** — causa: se eligió por complejidad y no por cambios. Corrección: priorizar por complejidad por frecuencia de cambio.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-310 — Deuda técnica, interés y opciones](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md)) son: Las definiciones son operativas para `tarifas`. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la bibliografía enlazada al final. Se ejecutaron tres modelos con parámetros supuestos y datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ningún equipo ni ningún repositorio; la capacidad, el interés, la fricción, la distribución de los cambios y la relación entre complejidad y cambios son construcciones del autor. La siguiente clase es un taller: refactorizar una función heredada sin alterar su comportamiento.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-306](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md), [SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md), [SE-309](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Derecho](../d/derecho.md), [Principal](../p/principal.md), [Deuda deliberada](../d/deuda-deliberada.md), [Deuda técnica](../d/deuda-tecnica.md), [Interés](../i/interes.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-310 — Deuda técnica, interés y opciones](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Cunningham, «The WyCash Portfolio Management System» (OOPSLA, 1992)](http://c2.com/doc/oopsla92.html) — origen de la metáfora de la deuda; autoridad: su autor.
- [Kruchten, Nord y Ozkaya (IEEE Software, 2012)](https://doi.org/10.1109/MS.2012.167) — la metáfora y sus límites; autoridad: IEEE Software.
- [Tornhill y Borg (TechDebt, 2022)](https://doi.org/10.1145/3524843.3528091) — estudio cuantitativo de calidad del código y negocio; autoridad: Proceedings of the International Conference on Technical Debt.
- [Fowler, «Technical Debt»](https://martinfowler.com/bliki/TechnicalDebt.html) — la metáfora y el interés; autoridad: Martin Fowler.
- [Fowler, «Technical Debt Quadrant»](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html) — deuda deliberada e inadvertida; autoridad: Martin Fowler.

---

[↑ Glosario](../../README.md) · [← Opción](./opcion.md) · [Opcode →](./opcode.md)
