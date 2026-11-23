# Copia superficial

[↑ Glosario](../../README.md) · [← Copia profunda](./copia-profunda.md) · [Copyleft →](./copyleft.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Copia que comparte las referencias a los componentes mutables.

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

- La cifra de 1000 de 1000 depende de que la lista sea compartida: con tuplas inmutables, la copia superficial bastaría. ([SE-314](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](./componente.md), [Referencia](../r/referencia.md), [Builder](../b/builder.md), [Copia profunda](./copia-profunda.md), [Factory](../f/factory.md), [Registro](../r/registro.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md), [SE-066](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Copia profunda](./copia-profunda.md) · [Copyleft →](./copyleft.md)
