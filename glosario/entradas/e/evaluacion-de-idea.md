# Evaluación de idea

[↑ Glosario](../../README.md) · [← Evaluación](./evaluacion.md) · [Evaluación del harness →](./evaluacion-del-harness.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Recolección de evidencia para decidir si una idea merece seguir, aclararse o detenerse.

Definición de trabajo de [SE-568 — Greenfield, brownfield, bug fixing e idea assessment](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md).

## Por qué importa

En [SE-568 — Greenfield, brownfield, bug fixing e idea assessment](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md), el tema «Evaluación de ideas» importa porque evita construir lo que no vale; es una decisión, no un trámite.

## Cómo funciona

[SE-568 — Greenfield, brownfield, bug fixing e idea assessment](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-568 — Greenfield, brownfield, bug fixing e idea assessment](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* clasifica sus tres peticiones. La de los umbrales configurables es un cambio sobre código existente: el agente recibe un mapa con los cinco módulos que usan `calcular_umbral` y una pregunta explícita («¿hay usos dinámicos?») para cubrir el punto ciego de la búsqueda por nombre; encuentra el módulo que la llama por una cadena de texto y añade una prueba de caracterización antes de tocarlo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-568 — Greenfield, brownfield, bug fixing e idea assessment](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md)) son:

- **El agente cambia una función y rompe un módulo lejano** — causa: búsqueda solo por nombre. Corrección: añadir una pregunta por usos dinámicos y una prueba de caracterización.
- **El mismo error vuelve con otra entrada** — causa: se arregló el síntoma. Corrección: exigir diagnóstico de la causa y casos vecinos.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-568 — Greenfield, brownfield, bug fixing e idea assessment](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md)) son: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: la lectura del repositorio sintético y las pruebas de las políticas de verificación son ejecuciones reales de código y el cálculo del valor de evaluar es una simulación con semilla fija. No se invocó ningún modelo, no se ejecutó ninguna extensión de Spec Kit y no se observó ningún sistema real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evidencia](./evidencia.md), [Arreglo del síntoma](../a/arreglo-del-sintoma.md), [Cambio sobre código existente](../c/cambio-sobre-codigo-existente.md), [Diagnóstico](../d/diagnostico.md), [Proyecto nuevo](../p/proyecto-nuevo.md), [Veredicto de corrección](../v/veredicto-de-correccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-568 — Greenfield, brownfield, bug fixing e idea assessment](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Evaluación de ideas».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Spec Kit — repositorio](https://github.com/github/spec-kit) — procesos de funcionalidad, corrección y evaluación como puntos de entrada independientes; autoridad: GitHub y mantenedores de la comunidad.
- [Spec Kit — guía de corrección de errores](https://github.github.io/spec-kit/guides/bugfix.html) — evaluar, corregir y probar, y veredictos; autoridad: GitHub y mantenedores.
- [Spec Kit — proyectos existentes](https://github.github.io/spec-kit/how-to/existing-projects.html) — adoptar el proceso en un repositorio con código; autoridad: GitHub y mantenedores.
- [Feathers, «Working Effectively with Legacy Code»](https://www.pearson.com/en-us/subject-catalog/p/working-effectively-with-legacy-code/P200000009466/9780131177055) — caracterización y costuras; autoridad: libro de referencia.

---

[↑ Glosario](../../README.md) · [← Evaluación](./evaluacion.md) · [Evaluación del harness →](./evaluacion-del-harness.md)
