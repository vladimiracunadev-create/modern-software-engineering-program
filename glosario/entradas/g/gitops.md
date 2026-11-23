# GitOps

[↑ Glosario](../../README.md) · [← GitFlow](./gitflow.md) · [Given-When-Then →](./given-when-then.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Práctica en la que el estado deseado se declara y versiona en un repositorio y un agente lo reconcilia continuamente con el estado real.

Definición de trabajo de [SE-487 — GitOps y reconciliación](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md).

## Por qué importa

En [SE-487 — GitOps y reconciliación](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md), el tema «Principios de GitOps» importa porque definen qué es y qué no es: sin reconciliación continua es solo un repositorio.

## Cómo funciona

Según [SE-487 — GitOps y reconciliación](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md):

OpenGitOps resume la práctica en cuatro principios. El sistema se describe de forma **declarativa**: el repositorio dice qué debe existir, no cómo llegar. El estado deseado se guarda **versionado e inmutable**: cada cambio es un commit con autor, fecha y motivo, y volver atrás es volver a un commit. El software **extrae automáticamente** el estado deseado: no hay un paso manual que lo copie al clúster. Y lo **reconcilia continuamente**: un agente observa el estado real y corrige la diferencia sin esperar una orden. El último principio es el que distingue GitOps de «guardar los archivos de despliegue en git»: una canalización que aplica una vez y se olvida no corrige nada de lo que ocurra después.

Según [SE-487 — GitOps y reconciliación](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md):

El equipo de la API de entregas redacta su política de GitOps. El repositorio declara el servicio, el volumen y el escalador, pero no declara el número de réplicas: ese campo es del escalador. La reconciliación es cada tres minutos con aviso del repositorio, porque tolerar 90 segundos de deriva manual es aceptable y las 192 000 lecturas diarias caben en la cuota; en producción se avisa a un responsable cuando el agente detecta una deriva persistente. La poda está activada con una excepción: todo recurso con estado lleva la anotación de protección y su borrado exige un cambio explícito con aprobación de una segunda persona. Los secretos viven cifrados en el repositorio con una clave que solo conoce el agente.

## Ejemplo

Ejemplo de [SE-487 — GitOps y reconciliación](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md) (sección «Ejemplo profesional»):

El equipo de la API de entregas redacta su política de GitOps. El repositorio declara el servicio, el volumen y el escalador, pero no declara el número de réplicas: ese campo es del escalador. La reconciliación es cada tres minutos con aviso del repositorio, porque tolerar 90 segundos de deriva manual es aceptable y las 192 000 lecturas diarias caben en la cuota; en producción se avisa a un responsable cuando el agente detecta una deriva persistente. La poda está activada con una excepción: todo recurso con estado lleva la anotación de protección y su borrado exige un cambio explícito con aprobación de una segunda persona.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-487 — GitOps y reconciliación](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md)) son:

- **El número de réplicas oscila** — causa: dos actores gobiernan el mismo campo. Corrección: repartir la propiedad; ignorar el campo en el agente.
- **Se borró un volumen al reorganizar archivos** — causa: poda activa sin protección. Corrección: anotación de protección; confirmación para borrar recursos con estado.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El último principio es el que distingue GitOps de «guardar los archivos de despliegue en git»: una canalización que aplica una vez y se olvida no corrige nada de lo que ocurra después. ([SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Estado deseado](../e/estado-deseado.md).
- **Ver también:** [Agente](../a/agente.md), [Estado](../e/estado.md), [Práctica](../p/practica.md), [Extracción](../e/extraccion.md), [Poda](../p/poda.md), [Propietario de un campo](../p/propietario-de-un-campo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-487 — GitOps y reconciliación](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md), [SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md).

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

[↑ Glosario](../../README.md) · [← GitFlow](./gitflow.md) · [Given-When-Then →](./given-when-then.md)
