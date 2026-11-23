# Estado

[↑ Glosario](../../README.md) · [← Estadísticas por grupo](./estadisticas-por-grupo.md) · [Estado actual →](./estado-actual.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Registro que relaciona cada recurso declarado con el objeto real y sus atributos.

Definición de trabajo de [SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-057 — Modelado de estado, transiciones y eventos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md): Resumen de historia relevante para comportamiento futuro.

## Por qué importa

En [SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md), el tema «Estado» importa porque es la relación entre lo declarado y lo real y puede quedar obsoleta.

## Cómo funciona

Según [SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md), en la sección «Estado»:

El estado de una herramienta como Terraform u OpenTofu relaciona cada recurso declarado con el objeto real que lo implementa y guarda sus atributos para poder compararlos. Sin él, la herramienta no sabría si un recurso ya existe o es nuevo. Tiene tres consecuencias prácticas. Es una fuente de verdad parcial que queda obsoleta si alguien cambia algo fuera de la herramienta. Puede contener datos sensibles, porque guarda los valores de los atributos, y debe tratarse como un secreto. Y es un archivo compartido, de modo que necesita un almacenamiento común y un bloqueo para que dos personas no lo escriban a la vez.

## Ejemplo

Ejemplo de [SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula el plan entre lo declarado, el estado y lo real. Antes de ejecutarlo, predice qué acciones propone con y sin refresco.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un recurso se crea dos veces o falla por duplicado** — causa: escritura del estado perdida. Corrección: almacén remoto con bloqueo y versión. ([SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md))
- **Nadie puede aplicar porque el estado está bloqueado** — causa: proceso muerto con el bloqueo tomado. Corrección: comprobar que nadie escribe y liberar con registro. ([SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md))
- **El estado aparece en un repositorio público** — causa: se trató como código y no como secreto. Corrección: almacén cifrado con acceso restringido y rotación de lo expuesto. ([SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un plan que solo compara el código con el estado no la ve; uno que antes refresca el estado con la realidad la ve y propone revertirla. ([SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md))
- Sin estado la herramienta no sabe si un recurso es nuevo; sin comparación con la realidad, no sabe si el estado sigue siendo cierto. ([SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Atributo](../a/atributo.md), [Objeto](../o/objeto.md), [Recurso](../r/recurso.md), [Registro](../r/registro.md), [ABI](../a/abi.md), [Arquitectura](../a/arquitectura.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-057 — Modelado de estado, transiciones y eventos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (438 clases más lo mencionan; las que más):

[SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md), [SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md), [SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md), [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md), [SE-172](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md), [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md), [SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md), [SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Terraform: estado](https://developer.hashicorp.com/terraform/language/state) — propósito del estado, datos sensibles y bloqueo; autoridad: documentación oficial de HashiCorp.
- [OpenTofu: documentación](https://opentofu.org/docs/) — bifurcación abierta con el mismo modelo declarativo; autoridad: proyecto OpenTofu.
- [Terraform: destroy](https://developer.hashicorp.com/terraform/cli/commands/destroy) — destrucción de los objetos gestionados; autoridad: documentación oficial de HashiCorp.
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — operaciones como código; autoridad: documentación del proveedor.
- [Python: itertools](https://docs.python.org/3/library/itertools.html) — permutaciones usadas para enumerar intercalaciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Estadísticas por grupo](./estadisticas-por-grupo.md) · [Estado actual →](./estado-actual.md)
