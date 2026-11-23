# GitFlow

[↑ Glosario](../../README.md) · [← GIL](./gil.md) · [GitOps →](./gitops.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Modelo con ramas de desarrollo, de versión y de corrección, pensado para versiones que conviven.

Definición de trabajo de [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md).

## Por qué importa

En [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md), el tema «GitFlow» importa porque separa desarrollo, versión y corrección; sirve a versiones que conviven.

## Cómo funciona

Según [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md), en la sección «GitFlow»:

GitFlow mantiene una rama de desarrollo y ramas de versión y de corrección. Surgió para software con versiones distribuidas que conviven, donde publicar es costoso y se mantienen varias versiones. Su costo es la distancia entre ramas y los backports; su beneficio es separar lo que se estabiliza de lo que se desarrolla. Para un servicio que se despliega continuamente, la rama de versión añade trabajo sin aportar protección.

## Ejemplo

Ejemplo de [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md) (sección «Ejemplo profesional»):

Compara el caso normal con un componente distribuido como biblioteca que tiene tres versiones vivas: la práctica es apropiada cuando se usa una rama de versión por línea soportada y se acota su vida; es peligrosa cuando se mantiene GitFlow completo para un servicio que se despliega a diario, porque la rama de desarrollo añade distancia sin protección.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md)) son:

- **Cada integración exige un día de resolver conflictos** — causa: las ramas viven semanas. Corrección: dividir el trabajo, acortar ramas e integrar a diario.
- **Main queda roto tras dos PR verdes** — causa: no se probó la combinación. Corrección: probar el resultado de la fusión o usar una cola de fusión.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos. Las personas, la zona caliente y los solapamientos son supuestos del autor, los conflictos se miden sobre texto y no se midió el costo de resolverlos, ni productividad, ni ningún equipo. La siguiente clase pregunta cómo se ata cada cambio de este flujo a su motivo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Modelo](../m/modelo.md), [Versión](../v/version.md), [Backport](../b/backport.md), [Cola de fusión](../c/cola-de-fusion.md), [Conflicto semántico](../c/conflicto-semantico.md), [Trunk-based development](../t/trunk-based-development.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-197 — Trunk-based, GitFlow y estrategias híbridas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md), [SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Driessen, «A successful Git branching model»](https://nvie.com/posts/a-successful-git-branching-model/) — origen de GitFlow; autoridad: el autor del modelo.
- [Trunk Based Development](https://trunkbaseddevelopment.com/) — descripción de la práctica; autoridad: sitio de la comunidad de la práctica.
- [Fowler, «Continuous Integration»](https://martinfowler.com/articles/continuousIntegration.html) — definición y prácticas; autoridad: martinfowler.com.
- [Fowler, «Feature Toggles»](https://martinfowler.com/articles/feature-toggles.html) — tipos y costos de los indicadores; autoridad: martinfowler.com.
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow) — flujo de ramas cortas con PR; autoridad: GitHub Docs.

---

[↑ Glosario](../../README.md) · [← GIL](./gil.md) · [GitOps →](./gitops.md)
