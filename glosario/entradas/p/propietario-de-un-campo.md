# Propietario de un campo

[↑ Glosario](../../README.md) · [← Propietario de código](./propietario-de-codigo.md) · [Proporcionalidad →](./proporcionalidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Único actor autorizado a gobernar el valor de un campo de un recurso.

Definición de trabajo de [SE-487 — GitOps y reconciliación](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md).

## Por qué importa

La clase donde se define, [SE-487 — GitOps y reconciliación](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md), existe con este propósito: la clase existe para que entiendas GitOps como un bucle de control y no como «un repositorio con archivos de despliegue»: un controlador compara sin descanso lo que declara el repositorio con lo que corre en el clúster y actúa sobre la diferencia.

## Cómo funciona

[SE-487 — GitOps y reconciliación](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el despliegue de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-487 — GitOps y reconciliación](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md):

El equipo de la API de entregas redacta su política de GitOps. El repositorio declara el servicio, el volumen y el escalador, pero no declara el número de réplicas: ese campo es del escalador. La reconciliación es cada tres minutos con aviso del repositorio, porque tolerar 90 segundos de deriva manual es aceptable y las 192 000 lecturas diarias caben en la cuota; en producción se avisa a un responsable cuando el agente detecta una deriva persistente.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-487 — GitOps y reconciliación](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md)) son:

- **El número de réplicas oscila** — causa: dos actores gobiernan el mismo campo. Corrección: repartir la propiedad; ignorar el campo en el agente.
- **Se borró un volumen al reorganizar archivos** — causa: poda activa sin protección. Corrección: anotación de protección; confirmación para borrar recursos con estado.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-487 — GitOps y reconciliación](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md)) son: Las definiciones son operativas para el despliegue de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Actor](../a/actor.md), [Recurso](../r/recurso.md), [Valor](../v/valor.md), [Extracción](../e/extraccion.md), [GitOps](../g/gitops.md), [Poda](./poda.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-487 — GitOps y reconciliación](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OpenGitOps: principios](https://opengitops.dev/) — cuatro principios de GitOps; autoridad: proyecto OpenGitOps de la CNCF.
- [Argo CD: opciones de sincronización](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-options/) — poda y protección de recursos; autoridad: documentación de Argo CD.
- [Argo CD: diferencias](https://argo-cd.readthedocs.io/en/stable/user-guide/diffing/) — campos ignorados en la comparación; autoridad: documentación de Argo CD.
- [Flux: conceptos](https://fluxcd.io/flux/concepts/) — reconciliación e intervalos; autoridad: documentación de Flux.
- [Kubernetes: controladores](https://kubernetes.io/docs/concepts/architecture/controller/) — bucle de control y estado deseado; autoridad: documentación de Kubernetes.

---

[↑ Glosario](../../README.md) · [← Propietario de código](./propietario-de-codigo.md) · [Proporcionalidad →](./proporcionalidad.md)
