# Bloqueo del estado

[↑ Glosario](../../README.md) · [← Bloqueo](./bloqueo.md) · [Blue-green →](./blue-green.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Exclusión mutua que impide que dos operaciones escriban el estado a la vez.

Definición de trabajo de [SE-486 — Infraestructura como código en pipeline](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md).

## Por qué importa

En [SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md), el tema «Bloqueo del estado» importa porque dos aplicaciones simultáneas pierden trabajo sin él.

## Cómo funciona

Según [SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md), en la sección «Bloqueo del estado»:

Cuando una aplicación lee el estado, calcula y lo escribe entero, dos aplicaciones simultáneas pueden leer la misma versión y la última en escribir borra el trabajo de la otra: es la actualización perdida de la [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md) aplicada a un archivo que describe infraestructura. Los almacenes remotos de estado ofrecen un bloqueo que impide que dos operaciones lo modifiquen a la vez. El bloqueo tiene su propio fallo: si el proceso muere con el bloqueo tomado, nadie puede aplicar hasta que alguien lo libera, y liberarlo a la fuerza sin comprobar que nadie escribe repite el problema.

## Ejemplo

Ejemplo de [SE-486 — Infraestructura como código en pipeline](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md) (sección «Caso conductor»):

La canalización de la API de entregas es el caso conductor de la [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md). Esta clase deja el sexto artefacto: el flujo de infraestructura con revisión del plan, bloqueo del estado y detección de deriva. `SE-487` invertirá la dirección con GitOps, en el que un controlador reconcilia continuamente el clúster con el repositorio, y `SE-488` usará este flujo para crear entornos efímeros. Cambia después un solo dato, la frecuencia de detección, y observa cuánto vive una deriva.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El plan propone crear algo que ya existe** — causa: estado perdido o desactualizado. Corrección: bloqueo del estado y versionado; importar si falta. ([SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La defensa es un **bloqueo** del estado durante la operación (o una cola que serialice las aplicaciones), con un tiempo máximo para que un bloqueo huérfano no paralice el trabajo. ([SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Exclusión](../e/exclusion.md), [Operación](../o/operacion.md), [Camino crítico](../c/camino-critico.md), [Deriva](../d/deriva.md), [Estado deseado](../e/estado-deseado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-486 — Infraestructura como código en pipeline](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Terraform: bloqueo del estado](https://developer.hashicorp.com/terraform/language/state/locking) — exclusión de escrituras concurrentes; autoridad: documentación de HashiCorp.
- [Terraform: estado](https://developer.hashicorp.com/terraform/language/state) — propósito del estado, datos sensibles y bloqueo; autoridad: documentación oficial de HashiCorp.
- [OpenTofu: documentación](https://opentofu.org/docs/) — bifurcación abierta con el mismo modelo declarativo; autoridad: proyecto OpenTofu.
- [Terraform: destroy](https://developer.hashicorp.com/terraform/cli/commands/destroy) — destrucción de los objetos gestionados; autoridad: documentación oficial de HashiCorp.
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — operaciones como código; autoridad: documentación del proveedor.

---

[↑ Glosario](../../README.md) · [← Bloqueo](./bloqueo.md) · [Blue-green →](./blue-green.md)
