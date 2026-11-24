# Estado

[↑ Glosario](../../README.md) · [← Estadísticas por grupo](./estadisticas-por-grupo.md) · [Estado actual →](./estado-actual.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

**Estado** es una palabra de dos sentidos en el programa:

- **Estado de infraestructura como código** ([SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md)): el registro que relaciona cada recurso declarado con el objeto real que lo implementa y guarda sus atributos para poder compararlos (es el sentido de herramientas como Terraform u OpenTofu).
- **Estado de un cómputo** ([SE-057](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md)): un resumen de la historia relevante para el comportamiento futuro.

El primero es el principal de esta entrada; el segundo es la idea general de que un sistema se comporta según lo que «recuerda».

## Por qué importa

Sin estado, una herramienta declarativa no sabría si un recurso ya existe o es nuevo ([SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md)). El estado decide qué se crea, qué se cambia y qué se destruye; si es erróneo, la herramienta duplica, falla o borra. En el sentido general, entender qué parte de la historia importa permite reducir un sistema a lo necesario.

## Cómo funciona

[SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md) enumera tres consecuencias prácticas del estado de infraestructura:

1. Es una **fuente de verdad parcial**: queda obsoleta si alguien cambia algo fuera de la herramienta.
2. Puede contener **datos sensibles**, porque guarda los valores de los atributos: se trata como un secreto.
3. Es un **archivo compartido**: necesita almacenamiento común y bloqueo para que dos personas no lo escriban a la vez.

Un plan que solo compara el código con el estado no ve el cambio hecho a mano; uno que antes refresca el estado con la realidad lo ve y propone revertirlo. [SE-057](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md) aplica la idea a un cómputo: el estado es lo mínimo que hay que recordar para decidir qué sigue.

## Ejemplo

Dos personas ejecutan `apply` a la vez sin bloqueo; una escritura del estado se pierde y el siguiente plan crea de nuevo un recurso que ya existe. Corrección de [SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md): almacén remoto con bloqueo y versión. Ilustración de configuración:

```hcl
backend "s3" { bucket = "estado-iac"  dynamodb_table = "bloqueo" }
```

## Errores y confusiones comunes

- **Un recurso se crea dos veces o falla por duplicado.** Causa: escritura de estado perdida; corrección: almacén remoto con bloqueo y versión ([SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md)).
- **Nadie puede aplicar.** Causa: proceso muerto con el bloqueo tomado; corrección: comprobar que nadie escribe y liberar con registro ([SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md)).
- **El estado aparece en un repositorio público.** Causa: se trató como código; corrección: almacén cifrado con acceso restringido y rotación de lo expuesto ([SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md)).

## Límites y cuándo no aplica

El estado no es la realidad: sin comparación con ella, no se sabe si sigue siendo cierto ([SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md)). Los comandos concretos dependen de la herramienta y su versión. En el sentido de [SE-057](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md), un buen resumen de historia puede ser engañosamente pequeño si omite algo que luego importa.

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
