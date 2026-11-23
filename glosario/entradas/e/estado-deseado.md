# Estado deseado

[↑ Glosario](../../README.md) · [← Estado derivado](./estado-derivado.md) · [Estado estable →](./estado-estable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Configuración que el código declara para la infraestructura.

Definición de trabajo de [SE-486 — Infraestructura como código en pipeline](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md).

## Por qué importa

La clase donde se define, [SE-486 — Infraestructura como código en pipeline](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md), existe con este propósito: la clase existe para que trates los cambios de infraestructura con la misma disciplina que los de código —revisión, verificación automática, aplicación controlada— sin olvidar lo que los distingue: se aplican sobre un sistema vivo que tiene estado, el orden importa y un error puede borrar datos.

## Cómo funciona

Según [SE-486 — Infraestructura como código en pipeline](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md):

La **deriva** es la diferencia entre el estado deseado y el real causada por cambios hechos fuera del flujo: un ajuste manual en una urgencia, una consola abierta, otra automatización. Se detecta ejecutando periódicamente un plan sin aplicar y mirando si propone cambios. La frecuencia de esa comprobación determina cuánto vive una deriva sin que nadie la vea: la espera media es la mitad del intervalo si las derivas llegan en instantes aleatorios. Detectar no es corregir: una deriva puede ser un error o una **corrección de emergencia** legítima que debe incorporarse al código antes de que la próxima aplicación la revierta. Una política razonable detecta con frecuencia, avisa a un responsable y no revierte automáticamente lo que no ha sido clasificado.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-486 — Infraestructura como código en pipeline](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md):

El equipo de la API de entregas rediseña el flujo de infraestructura. Cada cambio abre una revisión que ejecuta un plan y lo publica como comentario; una política marca en rojo cualquier acción de borrado o reemplazo y cualquier permiso de administración. Tras la fusión, una canalización aplica el plan guardado de la revisión; si el plan recalculado difiere, se detiene y pide revisión. Los reemplazos de recursos con estado exigen la aprobación de una segunda persona y una copia reciente verificada.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-486 — Infraestructura como código en pipeline](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md)) son:

- **El plan propone crear algo que ya existe** — causa: estado perdido o desactualizado. Corrección: bloqueo del estado y versionado; importar si falta.
- **Se destruyó una base de datos con un cambio «menor»** — causa: reemplazo no revisado. Corrección: política que marca borrados y reemplazos; copia verificada.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Se generan 300 casos: un grafo aleatorio de 12 recursos (cada uno depende de algunos anteriores) como estado deseado y un estado real que contiene el 55 % de los recursos, con el 30 % de ellos con una propiedad distinta y a veces un recurso huérfano. ([SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Bloqueo del estado](../b/bloqueo-del-estado.md), [Deriva](../d/deriva.md), [Plan](../p/plan.md), [Reemplazo](../r/reemplazo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-486 — Infraestructura como código en pipeline](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md), [SE-211](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md), [SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md), [SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Terraform: estado](https://developer.hashicorp.com/terraform/language/state) — función del estado y sus datos sensibles; autoridad: documentación de HashiCorp.
- [Terraform: bloqueo del estado](https://developer.hashicorp.com/terraform/language/state/locking) — exclusión de escrituras concurrentes; autoridad: documentación de HashiCorp.
- [OpenTofu: documentación](https://opentofu.org/docs/) — infraestructura declarativa de código abierto; autoridad: proyecto OpenTofu.
- [Kahn, «Topological sorting of large networks»](https://doi.org/10.1145/368996.369025) — orden topológico (Communications of the ACM, 1962); autoridad: artículo con DOI verificado en Crossref.

---

[↑ Glosario](../../README.md) · [← Estado derivado](./estado-derivado.md) · [Estado estable →](./estado-estable.md)
