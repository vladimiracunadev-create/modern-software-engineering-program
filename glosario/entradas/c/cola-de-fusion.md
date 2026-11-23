# Cola de fusión

[↑ Glosario](../../README.md) · [← Cola de cartas muertas](./cola-de-cartas-muertas.md) · [Cola de integración →](./cola-de-integracion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Mecanismo que prueba cada cambio sobre el estado actual del tronco antes de integrarlo.

Definición de trabajo de [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md).

## Por qué importa

La clase donde se define, [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md), existe con este propósito: la clase existe para elegir un flujo de ramas por lo que cuesta y por lo que protege, no por moda: cuánto vive una rama, dónde se integra, qué se libera y cómo se corrige una versión ya publicada.

## Cómo funciona

Según [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md):

Dos cambios pueden fusionarse sin conflicto de texto y ser incompatibles: uno cambia la firma de una función y otro añade una llamada con la firma vieja. Git no ve esto porque no entiende el programa. La defensa es probar el resultado de la combinación antes de aceptar, no solo cada rama por separado: integración continua sobre el tronco y, con volumen alto, una cola de fusión que prueba cada cambio sobre el estado actual.

Según [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md):

La plataforma de entregas se despliega varias veces al día y mantiene una sola versión publicada. El equipo adopta ramas de un día integradas por PR, pruebas de menos de diez minutos, indicadores de funcionalidad para lo no terminado y una cola de fusión. No mantiene rama de desarrollo ni de versión: una corrección se hace en el tronco y se despliega. Para una integración con un cliente que fija versión, mantiene una rama de versión de la API con correcciones portadas durante seis meses.

## Ejemplo

Ejemplo de [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md) (sección «Ejemplo profesional»):

La plataforma de entregas se despliega varias veces al día y mantiene una sola versión publicada. El equipo adopta ramas de un día integradas por PR, pruebas de menos de diez minutos, indicadores de funcionalidad para lo no terminado y una cola de fusión. No mantiene rama de desarrollo ni de versión: una corrección se hace en el tronco y se despliega. Para una integración con un cliente que fija versión, mantiene una rama de versión de la API con correcciones portadas durante seis meses.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Main queda roto tras dos PR verdes** — causa: no se probó la combinación. Corrección: probar el resultado de la fusión o usar una cola de fusión. ([SE-197](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La defensa es probar el resultado de la combinación antes de aceptar, no solo cada rama por separado: integración continua sobre el tronco y, con volumen alto, una cola de fusión que prueba cada cambio sobre el estado actual. ([SE-197](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado actual](../e/estado-actual.md), [Estado](../e/estado.md), [Mecanismo](../m/mecanismo.md), [Sobre](../s/sobre.md), [Backport](../b/backport.md), [Conflicto semántico](./conflicto-semantico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GitHub: cola de fusión](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue) — prueba de cada cambio sobre el estado actual; autoridad: GitHub Docs.
- [Trunk Based Development](https://trunkbaseddevelopment.com/) — descripción de la práctica; autoridad: sitio de la comunidad de la práctica.
- [Driessen, «A successful Git branching model»](https://nvie.com/posts/a-successful-git-branching-model/) — origen de GitFlow; autoridad: el autor del modelo.
- [Fowler, «Continuous Integration»](https://martinfowler.com/articles/continuousIntegration.html) — definición y prácticas; autoridad: martinfowler.com.
- [Fowler, «Feature Toggles»](https://martinfowler.com/articles/feature-toggles.html) — tipos y costos de los indicadores; autoridad: martinfowler.com.

---

[↑ Glosario](../../README.md) · [← Cola de cartas muertas](./cola-de-cartas-muertas.md) · [Cola de integración →](./cola-de-integracion.md)
