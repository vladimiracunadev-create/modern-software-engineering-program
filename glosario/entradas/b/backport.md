# Backport

[↑ Glosario](../../README.md) · [← Backoff exponencial](./backoff-exponencial.md) · [Backpressure →](./backpressure.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Aplicación de una corrección hecha en el tronco a una versión publicada.

Definición de trabajo de [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md).

## Por qué importa

En [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md), el tema «Versiones y backports» importa porque mantener una versión publicada cuesta más cuanto más deriva el tronco.

## Cómo funciona

Según [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md):

GitFlow mantiene una rama de desarrollo y ramas de versión y de corrección. Surgió para software con versiones distribuidas que conviven, donde publicar es costoso y se mantienen varias versiones. Su costo es la distancia entre ramas y los backports; su beneficio es separar lo que se estabiliza de lo que se desarrolla. Para un servicio que se despliega continuamente, la rama de versión añade trabajo sin aportar protección.

Según [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md):

Las que el producto pueda soportar y los clientes necesiten; cada versión añade backports. Es una decisión de capacidad que debe tener una fecha de fin.

## Ejemplo

Ejemplo de [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md) (sección «Preguntas frecuentes»):

Las que el producto pueda soportar y los clientes necesiten; cada versión añade backports. Es una decisión de capacidad que debe tener una fecha de fin.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Los backports fallan cada vez** — causa: el tronco derivó mucho desde el corte. Corrección: portar en cuanto se corrige o reducir la vida de la versión. ([SE-197](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos. Las personas, la zona caliente y los solapamientos son supuestos del autor, los conflictos se miden sobre texto y no se midió el costo de resolverlos, ni productividad, ni ningún equipo. La siguiente clase pregunta cómo se ata cada cambio de este flujo a su motivo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Versión](../v/version.md), [Cola de fusión](../c/cola-de-fusion.md), [Conflicto semántico](../c/conflicto-semantico.md), [GitFlow](../g/gitflow.md), [Trunk-based development](../t/trunk-based-development.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [git-cherry-pick](https://git-scm.com/docs/git-cherry-pick) — aplicación de commits sueltos usada para los backports.
- [Trunk Based Development](https://trunkbaseddevelopment.com/) — descripción de la práctica; autoridad: sitio de la comunidad de la práctica.
- [Driessen, «A successful Git branching model»](https://nvie.com/posts/a-successful-git-branching-model/) — origen de GitFlow; autoridad: el autor del modelo.
- [Fowler, «Continuous Integration»](https://martinfowler.com/articles/continuousIntegration.html) — definición y prácticas; autoridad: martinfowler.com.
- [Fowler, «Feature Toggles»](https://martinfowler.com/articles/feature-toggles.html) — tipos y costos de los indicadores; autoridad: martinfowler.com.

---

[↑ Glosario](../../README.md) · [← Backoff exponencial](./backoff-exponencial.md) · [Backpressure →](./backpressure.md)
