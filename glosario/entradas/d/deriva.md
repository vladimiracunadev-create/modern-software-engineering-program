# Deriva

[↑ Glosario](../../README.md) · [← Derecho](./derecho.md) · [Deriva arquitectónica →](./deriva-arquitectonica.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

La **deriva** es la diferencia entre lo que un registro afirma y lo que realmente existe, nacida de cambios hechos fuera del flujo previsto. El programa la usa en varios dominios con el mismo núcleo. En infraestructura como código ([SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md), [SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md)): diferencia entre el estado deseado o el que cree el archivo de estado y la realidad, causada por cambios hechos fuera del código. En especificaciones ([SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md), [SE-548](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md)): diferencia entre lo que la especificación afirma y lo que el sistema hace. En [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md): cambio acumulado lento de una magnitud a lo largo de muchos cambios pequeños.

## Por qué importa

Cambia cuándo se descubre que el registro ya no es la verdad. En infraestructura, [SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md) lo resume así: un cambio manual no desaparece; el siguiente `apply` lo revierte o lo ignora. En especificaciones, una spec que ya no describe el sistema engaña a quien la lee. Ver la deriva a tiempo permite decidir en lugar de descubrirla en un incidente.

## Cómo funciona

El mecanismo es una comparación entre dos fuentes. Un arreglo de emergencia en la consola o con otra herramienta modifica la realidad sin pasar por el código. Un plan que solo compara código con estado no lo ve; uno que primero **refresca** el estado contra la realidad lo detecta y propone revertirlo. Ninguna conducta es incorrecta: la primera es rápida y ciega; la segunda es exacta y puede deshacer un arreglo necesario. Lo esencial es la decisión explícita: incorporar el cambio al código o revertirlo.

Para no descubrirla semanas después, [SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md) propone un plan solo de lectura periódico (cada pocas horas, con responsable) que abre una incidencia por cada diferencia. En el caso de contratos ([SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md)), la comparación debe incluir tipos y restricciones, no solo nombres, o un cambio de tipo pasa inadvertido.

## Ejemplo

El equipo de la plataforma guarda el estado en un almacén remoto con bloqueo y cifrado y exige que todo cambio pase por un plan revisado por otra persona. Cada noche corre un plan de solo lectura y abre una incidencia por diferencia. Si la deriva era un arreglo de emergencia, se incorpora al código o se revierte de forma deliberada, no al pasar. En el experimento de [SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md), sin refresco el plan ve siempre los mismos 10 cambios y detecta la deriva solo cuando coincide con una edición del código.

## Errores y confusiones comunes

- **Un `apply` revierte un arreglo de emergencia.** Deriva no incorporada; revisar las acciones que el código no editó y decidir cada una.
- **La deriva se descubre semanas después.** Sin comprobación periódica con responsable.
- **Tratar toda deriva como error.** Puede ser un arreglo válido que falta incorporar.
- **Comparar solo nombres.** Un cambio de tipo pasa inadvertido.

## Límites y cuándo no aplica

El refresco solo ve lo que el proveedor expone y lo que el código modela; recursos creados por completo fuera de él pueden quedar invisibles. La deriva lenta de [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md) exige series de tiempo y presupuestos, no una comparación puntual. Los experimentos de [SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md) usan datos sintéticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado deseado](../e/estado-deseado.md), [Especificación](../e/especificacion.md), [Estado](../e/estado.md), [Flujo](../f/flujo.md), [Generación determinista](../g/generacion-determinista.md), [Modelo conductual](../m/modelo-conductual.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-160 — Modelos estructurales, conductuales y de información](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-165 — Spec-first, spec-anchored y spec-as-source](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.
- [SE-486 — Infraestructura como código en pipeline](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.
- [SE-548 — SDD: spec-first, spec-anchored y spec-as-source](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.
- [SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (68 clases más lo mencionan; las que más):

[SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md), [SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md), [SE-343](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md), [SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md), [SE-601](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md), [SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md), [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), [SE-291](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md).

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

[↑ Glosario](../../README.md) · [← Derecho](./derecho.md) · [Deriva arquitectónica →](./deriva-arquitectonica.md)
