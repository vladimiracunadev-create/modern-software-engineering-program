# Copia profunda

[↑ Glosario](../../README.md) · [← Copia consistente](./copia-consistente.md) · [Copia superficial →](./copia-superficial.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Copia recursiva que no comparte componentes mutables.

Definición de trabajo de [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md).

## Por qué importa

En [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md), el tema «Prototype y copia profunda» importa porque la copia superficial comparte referencias y contamina

## Cómo funciona

Según [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md):

El Prototype crea objetos copiando uno configurado; en Python, `copy.copy` y `copy.deepcopy`. El defecto es la **copia superficial**: copia el objeto pero comparte las referencias a sus componentes mutables. En el experimento, una plantilla de aviso tiene una lista de destinatarios; se crean 1000 clones con `copy.copy`, se añade «ana» a la lista de uno y **1000 de 1000** la tienen, porque comparten la misma lista. Con `copy.deepcopy`, la tiene 1 de 1000. La copia profunda tiene un costo: unos 11 µs frente a unos 0,6 µs de construir el objeto (cerca de 17 veces más).

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** los tiempos son de un equipo y de un objeto trivial; con un objeto grande, la copia profunda puede dominar el costo. ([SE-314](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](./componente.md), [Builder](../b/builder.md), [Copia superficial](./copia-superficial.md), [Factory](../f/factory.md), [Registro](../r/registro.md), [Singleton](../s/singleton.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md), [SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md), [SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md), [SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Copia consistente](./copia-consistente.md) · [Copia superficial →](./copia-superficial.md)
