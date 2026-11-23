# Factory

[↑ Glosario](../../README.md) · [← Factor de carga y crecimiento](./factor-de-carga-y-crecimiento.md) · [Factura →](./factura.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Punto único que decide qué clase concreta crear.

Definición de trabajo de [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md).

## Por qué importa

En [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md), el tema «Factory con registro» importa porque centraliza el conocimiento del tipo concreto y rechaza lo desconocido al crear

## Cómo funciona

Según [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md):

La **fuerza** de una fábrica es que el conocimiento de qué clase concreta crear está repartido: tres módulos repiten el mismo `if canal == "email"`. Un **Factory Method** mueve la decisión a un método que las subclases redefinen; un **Abstract Factory** crea familias de objetos que deben ser coherentes entre sí (por ejemplo, el cliente HTTP y el serializador de un mismo proveedor); y un **registro** (un diccionario de nombres a constructores) permite añadir tipos sin tocar la fábrica. La ventaja medible del registro es el **error temprano**: de cinco peticiones de canales (`email`, `sms`, `push`, `emial`, `sms`) con un registro que solo conoce dos, dos se rechazan al crear, no más adelante cuando se intenta enviar.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **Factory Method** mueve la decisión a un método que las subclases redefinen; un **Abstract Factory** crea familias de objetos que deben ser coherentes entre sí (por ejemplo, el cliente HTTP y el serializador de un mismo proveedor); y un **registro** (un diccionario de nombres a constructores) permite añadir tipos sin tocar la fábrica. ([SE-314](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Builder](../b/builder.md), [Copia profunda](../c/copia-profunda.md), [Copia superficial](../c/copia-superficial.md), [Registro](../r/registro.md), [Singleton](../s/singleton.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-324](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md), [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Factor de carga y crecimiento](./factor-de-carga-y-crecimiento.md) · [Factura →](./factura.md)
