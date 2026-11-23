# Microkernel

[↑ Glosario](../../README.md) · [← Microarquitectura](./microarquitectura.md) · [Microservicio →](./microservicio.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Estilo con un núcleo mínimo que registra y despacha, y extensiones que viven fuera de él.

Definición de trabajo de [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md).

## Por qué importa

La clase donde se define, [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md), existe con este propósito: la clase existe para que sepas cuándo una arquitectura de complementos es la respuesta correcta y qué cuesta mantenerla.

## Cómo funciona

Según [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md):

Un microkernel conserva en el núcleo solo lo que todos los complementos necesitan y que cambia poco: registrar complementos, despachar eventos y fallar de forma controlada. Todo lo demás vive fuera. En el laboratorio el núcleo (`Kernel`) tiene tres métodos: cargar un directorio, comprobar la versión del contrato y despachar un evento a cada complemento. La tentación contraria es dejar en el núcleo «lo común», que crece hasta que el núcleo es el sistema y los complementos son decoración. La pregunta de control es: ¿esta función la necesitan todos los complementos y la voy a poder mantener igual durante años?

Según [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md):

Se usan casi como sinónimos. El nombre microkernel viene de los sistemas operativos con un núcleo mínimo y servicios en el espacio de usuario; en aplicaciones se habla de arquitectura de complementos. Lo que comparten es un núcleo pequeño y un contrato de extensión.

## Ejemplo

Ejemplo de [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md) (sección «Preguntas frecuentes»):

Se usan casi como sinónimos. El nombre microkernel viene de los sistemas operativos con un núcleo mínimo y servicios en el espacio de usuario; en aplicaciones se habla de arquitectura de complementos. Lo que comparten es un núcleo pequeño y un contrato de extensión.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un microkernel conserva en el núcleo solo lo que todos los complementos necesitan y que cambia poco: registrar complementos, despachar eventos y fallar de forma controlada. ([SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Extensión](../e/extension.md), [Núcleo](../n/nucleo.md), [Adaptador de compatibilidad](../a/adaptador-de-compatibilidad.md), [Aislamiento](../a/aislamiento.md), [Complemento](../c/complemento.md), [Contrato](../c/contrato.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), [SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md), [SE-346](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md), [SE-348](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Microarquitectura](./microarquitectura.md) · [Microservicio →](./microservicio.md)
