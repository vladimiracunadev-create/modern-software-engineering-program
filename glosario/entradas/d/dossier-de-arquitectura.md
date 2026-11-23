# Dossier de arquitectura

[↑ Glosario](../../README.md) · [← Dominio](./dominio.md) · [Dossier defendible →](./dossier-defendible.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Conjunto estructurado de drivers, escenarios, decisiones, vistas, funciones de aptitud y límites con referencias cruzadas verificables.

Definición de trabajo de [SE-336 — Proyecto: arquitectura defendible y verificable](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md).

## Por qué importa

La clase donde se define, [SE-336 — Proyecto: arquitectura defendible y verificable](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md), existe con este propósito: el proyecto existe para que entregues un dossier de arquitectura que otra persona pueda comprobar: con escenarios medibles, decisiones registradas, un modelo ejecutable, un validador de la forma del dossier y la lista honesta de lo que ni el modelo ni el validador ven.

## Cómo funciona

[SE-336 — Proyecto: arquitectura defendible y verificable](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Ejemplo de [SE-336 — Proyecto: arquitectura defendible y verificable](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md) (sección «Caso conductor»):

La plataforma de entregas y corrección de tareas cierra aquí su recorrido por la [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md). El proyecto deja el duodécimo artefacto: un dossier de arquitectura ejecutable, con decisiones registradas, simulación de operación, impacto de revertir y límites declarados. La [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md) lleva esas decisiones a los datos: modelado, persistencia, consistencia y recuperación. Cambia después una sola decisión, el objetivo de disponibilidad, y observa qué ADR y qué funciones de aptitud deben tocarse.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-336 — Proyecto: arquitectura defendible y verificable](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md)) son:

- **El comité pregunta por una caída y no hay respuesta** — causa: documento sin escenarios ni modelo. Corrección: escenarios medibles y un modelo que los evalúa.
- **Los diagramas se contradicen** — causa: vistas mantenidas a mano. Corrección: generarlas desde un modelo único y validarlas.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-336 — Proyecto: arquitectura defendible y verificable](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres análisis con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se desplegó ni se midió ningún sistema: el dossier, las mutaciones, las caídas, el 30 % de causa común, los picos y el grafo de impacto son construcciones del autor, y el validador se escribió mirando las mismas mutaciones que lo evalúan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Función de aptitud](../f/funcion-de-aptitud.md), [Conjunto](../c/conjunto.md), [Escenario](../e/escenario.md), [Función](../f/funcion.md), [Impacto de una decisión](../i/impacto-de-una-decision.md), [Límite declarado](../l/limite-declarado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-336 — Proyecto: arquitectura defendible y verificable](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [arc42](https://arc42.org/) — plantilla de documentación de arquitectura; autoridad: arc42.
- [Ford, Parsons y Kua, «Building Evolutionary Architectures» (O'Reilly)](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781491986356/) — funciones de aptitud continuas; autoridad: O'Reilly Media.
- [SEI, «The Architecture Tradeoff Analysis Method»](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/) — evaluación de arquitectura contra escenarios; autoridad: Software Engineering Institute (Carnegie Mellon).
- [Nygard, «Documenting Architecture Decisions»](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — registros de decisión; autoridad: Michael Nygard.
- [C4 model](https://c4model.com/) — niveles de diagramas de arquitectura; autoridad: Simon Brown.

---

[↑ Glosario](../../README.md) · [← Dominio](./dominio.md) · [Dossier defendible →](./dossier-defendible.md)
