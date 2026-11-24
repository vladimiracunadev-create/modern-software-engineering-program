# Reemplazo

[↑ Glosario](../../README.md) · [← Reducción por simetría](./reduccion-por-simetria.md) · [Reemplazo atómico →](./reemplazo-atomico.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

En infraestructura como código, un **reemplazo** es una acción que destruye un recurso y lo vuelve a crear porque una propiedad no se puede cambiar en sitio ([SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md)).

## Por qué importa

Un cambio que parece menor en el código declarativo puede traducirse en destruir y recrear. Si el recurso tiene estado (una base de datos), el reemplazo borra datos. La revisión de un plan debe separar cambios en sitio de reemplazos y borrados.

## Cómo funciona

La herramienta compara el **estado deseado** que declara el código con el **estado real** y calcula un plan. Para cada propiedad, el proveedor decide si admite modificación en sitio o exige recrear. El plan marca el reemplazo (en algunas herramientas con un símbolo propio), y solo quien lo lee atentamente lo detecta. Una política automática que marque borrados y reemplazos, y una copia verificada antes de aplicar, convierten la revisión en control.

## Ejemplo

Cambiar el nombre de una base de datos o su motor puede exigir reemplazo. [SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md) documenta el caso de «se destruyó una base de datos con un cambio menor»: el reemplazo no fue revisado.

## Errores y confusiones comunes

Revisar el diff del código y no el plan; asumir que cambiar una propiedad es siempre una modificación.

## Límites y cuándo no aplica

Qué cambios son en sitio y cuáles son reemplazos lo decide cada proveedor; los porcentajes de la clase (25 % de recursos con estado, etc.) son supuestos del autor.

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
