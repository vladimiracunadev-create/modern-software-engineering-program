# Trunk-based development

[↑ Glosario](../../README.md) · [← Trozo](./trozo.md) · [Truthiness →](./truthiness.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Práctica de integrar en un tronco único con ramas de muy corta duración.

Definición de trabajo de [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md).

## Por qué importa

La clase donde se define, [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md), existe con este propósito: la clase existe para elegir un flujo de ramas por lo que cuesta y por lo que protege, no por moda: cuánto vive una rama, dónde se integra, qué se libera y cómo se corrige una versión ya publicada.

## Cómo funciona

[SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md):

La plataforma de entregas se despliega varias veces al día y mantiene una sola versión publicada. El equipo adopta ramas de un día integradas por PR, pruebas de menos de diez minutos, indicadores de funcionalidad para lo no terminado y una cola de fusión. No mantiene rama de desarrollo ni de versión: una corrección se hace en el tronco y se despliega. Para una integración con un cliente que fija versión, mantiene una rama de versión de la API con correcciones portadas durante seis meses.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md)) son:

- **Cada integración exige un día de resolver conflictos** — causa: las ramas viven semanas. Corrección: dividir el trabajo, acortar ramas e integrar a diario.
- **Main queda roto tras dos PR verdes** — causa: no se probó la combinación. Corrección: probar el resultado de la fusión o usar una cola de fusión.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos. Las personas, la zona caliente y los solapamientos son supuestos del autor, los conflictos se miden sobre texto y no se midió el costo de resolverlos, ni productividad, ni ningún equipo. La siguiente clase pregunta cómo se ata cada cambio de este flujo a su motivo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Práctica](../p/practica.md), [Backport](../b/backport.md), [Cola de fusión](../c/cola-de-fusion.md), [Conflicto semántico](../c/conflicto-semantico.md), [GitFlow](../g/gitflow.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-182](../../../classes/part-15-procesos-planificacion-y-estimacion/se-182-agile-como-principios-y-no-como-ceremonia/README.md), [SE-475](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md), [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Trunk Based Development](https://trunkbaseddevelopment.com/) — descripción de la práctica; autoridad: sitio de la comunidad de la práctica.
- [Driessen, «A successful Git branching model»](https://nvie.com/posts/a-successful-git-branching-model/) — origen de GitFlow; autoridad: el autor del modelo.
- [Fowler, «Continuous Integration»](https://martinfowler.com/articles/continuousIntegration.html) — definición y prácticas; autoridad: martinfowler.com.
- [Fowler, «Feature Toggles»](https://martinfowler.com/articles/feature-toggles.html) — tipos y costos de los indicadores; autoridad: martinfowler.com.
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow) — flujo de ramas cortas con PR; autoridad: GitHub Docs.

---

[↑ Glosario](../../README.md) · [← Trozo](./trozo.md) · [Truthiness →](./truthiness.md)
