# Reemplazo

[↑ Glosario](../../README.md) · [← Reducción por simetría](./reduccion-por-simetria.md) · [Reemplazo atómico →](./reemplazo-atomico.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Acción que destruye un recurso y lo vuelve a crear porque una propiedad no se puede cambiar en sitio.

Definición de trabajo de [SE-486 — Infraestructura como código en pipeline](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md).

## Por qué importa

La clase donde se define, [SE-486 — Infraestructura como código en pipeline](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md), existe con este propósito: la clase existe para que trates los cambios de infraestructura con la misma disciplina que los de código —revisión, verificación automática, aplicación controlada— sin olvidar lo que los distingue: se aplican sobre un sistema vivo que tiene estado, el orden importa y un error puede borrar datos.

## Cómo funciona

Según [SE-486 — Infraestructura como código en pipeline](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md):

El plan es el documento que más conviene leer: dice qué se creará, qué se cambiará y qué se destruirá. Un plan con diez creaciones es rutina; un plan con una destrucción merece una pausa; un **reemplazo** de un recurso con estado (una base de datos, un volumen) merece una aprobación explícita y una copia verificada. La revisión humana funciona si el plan es legible y si quien lo revisa sabe qué buscar; se refuerza con una **política** que marque automáticamente las acciones destructivas y los permisos amplios.

Según [SE-486 — Infraestructura como código en pipeline](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md):

El equipo de la API de entregas rediseña el flujo de infraestructura. Cada cambio abre una revisión que ejecuta un plan y lo publica como comentario; una política marca en rojo cualquier acción de borrado o reemplazo y cualquier permiso de administración. Tras la fusión, una canalización aplica el plan guardado de la revisión; si el plan recalculado difiere, se detiene y pide revisión. Los reemplazos de recursos con estado exigen la aprobación de una segunda persona y una copia reciente verificada. El estado se guarda cifrado, con versionado y con bloqueo por entorno; una canalización de comprobación de deriva ejecuta un plan sin aplicar cada seis horas y crea una incidencia con responsable cuando encuentra diferencias.

## Ejemplo

Ejemplo de [SE-486 — Infraestructura como código en pipeline](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md) (sección «Ejemplo profesional»):

El equipo de la API de entregas rediseña el flujo de infraestructura. Cada cambio abre una revisión que ejecuta un plan y lo publica como comentario; una política marca en rojo cualquier acción de borrado o reemplazo y cualquier permiso de administración. Tras la fusión, una canalización aplica el plan guardado de la revisión; si el plan recalculado difiere, se detiene y pide revisión. Los reemplazos de recursos con estado exigen la aprobación de una segunda persona y una copia reciente verificada.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se destruyó una base de datos con un cambio «menor»** — causa: reemplazo no revisado. Corrección: política que marca borrados y reemplazos; copia verificada. ([SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** los grafos (densidad de dependencias del 25 %), la proporción de recursos con estado (25 %) y los porcentajes de cambio son supuestos del autor; un proveedor real impone sus propias reglas de qué cambios son en sitio y cuáles son reemplazos. ([SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Propiedad](../p/propiedad.md), [Recurso](./recurso.md), [Bloqueo del estado](../b/bloqueo-del-estado.md), [Deriva](../d/deriva.md), [Estado deseado](../e/estado-deseado.md), [Plan](../p/plan.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-486 — Infraestructura como código en pipeline](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (38 clases más lo mencionan; las que más):

[SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md), [SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md), [SE-067](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-227](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md), [SE-477](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md), [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md), [SE-110](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md).

**Aparece en los casos de estudio:** [Airbnb](../../../casos/exito/airbnb.md), [Slack](../../../casos/exito/slack.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Terraform: estado](https://developer.hashicorp.com/terraform/language/state) — función del estado y sus datos sensibles; autoridad: documentación de HashiCorp.
- [Terraform: bloqueo del estado](https://developer.hashicorp.com/terraform/language/state/locking) — exclusión de escrituras concurrentes; autoridad: documentación de HashiCorp.
- [OpenTofu: documentación](https://opentofu.org/docs/) — infraestructura declarativa de código abierto; autoridad: proyecto OpenTofu.
- [Kahn, «Topological sorting of large networks»](https://doi.org/10.1145/368996.369025) — orden topológico (Communications of the ACM, 1962); autoridad: artículo con DOI verificado en Crossref.

---

[↑ Glosario](../../README.md) · [← Reducción por simetría](./reduccion-por-simetria.md) · [Reemplazo atómico →](./reemplazo-atomico.md)
