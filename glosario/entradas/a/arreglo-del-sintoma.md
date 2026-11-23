# Arreglo del síntoma

[↑ Glosario](../../README.md) · [← Arreglo contiguo y localidad](./arreglo-contiguo-y-localidad.md) · [Arrendamiento →](./arrendamiento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Modificación que hace pasar la reproducción sin eliminar la causa del defecto.

Definición de trabajo de [SE-568 — Greenfield, brownfield, bug fixing e idea assessment](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md).

## Por qué importa

La clase donde se define, [SE-568 — Greenfield, brownfield, bug fixing e idea assessment](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md), existe con este propósito: la clase existe para que dejes de usar el mismo método con un agente en cuatro situaciones que no se parecen.

## Cómo funciona

Según [SE-568 — Greenfield, brownfield, bug fixing e idea assessment](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md):

Reproduce el fallo clásico de la clase: **un arreglo que pasa la reproducción y deja el defecto**. Aplica el arreglo del síntoma de las horas restantes y ejecuta la política de verificación de la reproducción.

Según [SE-568 — Greenfield, brownfield, bug fixing e idea assessment](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md):

Traslada el análisis a otro dominio (por ejemplo, el módulo de reservas de una biblioteca): cambia el repositorio, los errores y la idea y conserva el procedimiento de clasificar la petición, elegir una estrategia de lectura con una pregunta que cubra su punto ciego, verificar los arreglos con la reproducción y sus vecinos y calcular si compensa evaluar. La transferencia está lograda cuando puedes decir qué uso del nuevo repositorio no encontraría tu estrategia y qué arreglo del síntoma aceptaría tu verificación, no cuando las cifras se parecen a las de *Avisos*.

## Ejemplo

Ejemplo de [SE-568 — Greenfield, brownfield, bug fixing e idea assessment](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md) (sección «Ejemplo mínimo»):

El fragmento muestra un arreglo del síntoma. Antes de ejecutarlo, predice si la reproducción pasa y si pasa un vecino.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-568 — Greenfield, brownfield, bug fixing e idea assessment](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md)) son:

- **El agente cambia una función y rompe un módulo lejano** — causa: búsqueda solo por nombre. Corrección: añadir una pregunta por usos dinámicos y una prueba de caracterización.
- **El mismo error vuelve con otra entrada** — causa: se arregló el síntoma. Corrección: exigir diagnóstico de la causa y casos vecinos.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La transferencia está lograda cuando puedes decir qué uso del nuevo repositorio no encontraría tu estrategia y qué arreglo del síntoma aceptaría tu verificación, no cuando las cifras se parecen a las de *Avisos*. ([SE-568](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Reproducción](../r/reproduccion.md), [Cambio sobre código existente](../c/cambio-sobre-codigo-existente.md), [Diagnóstico](../d/diagnostico.md), [Evaluación de idea](../e/evaluacion-de-idea.md), [Proyecto nuevo](../p/proyecto-nuevo.md), [Veredicto de corrección](../v/veredicto-de-correccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-568 — Greenfield, brownfield, bug fixing e idea assessment](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Spec Kit — repositorio](https://github.com/github/spec-kit) — procesos de funcionalidad, corrección y evaluación como puntos de entrada independientes; autoridad: GitHub y mantenedores de la comunidad.
- [Spec Kit — guía de corrección de errores](https://github.github.io/spec-kit/guides/bugfix.html) — evaluar, corregir y probar, y veredictos; autoridad: GitHub y mantenedores.
- [Spec Kit — proyectos existentes](https://github.github.io/spec-kit/how-to/existing-projects.html) — adoptar el proceso en un repositorio con código; autoridad: GitHub y mantenedores.
- [Feathers, «Working Effectively with Legacy Code»](https://www.pearson.com/en-us/subject-catalog/p/working-effectively-with-legacy-code/P200000009466/9780131177055) — caracterización y costuras; autoridad: libro de referencia.

---

[↑ Glosario](../../README.md) · [← Arreglo contiguo y localidad](./arreglo-contiguo-y-localidad.md) · [Arrendamiento →](./arrendamiento.md)
