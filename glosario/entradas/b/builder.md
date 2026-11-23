# Builder

[↑ Glosario](../../README.md) · [← Build reproducible](./build-reproducible.md) · [Bulkhead →](./bulkhead.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Objeto o secuencia de pasos que construye un objeto complejo y valida al final.

Definición de trabajo de [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md).

## Por qué importa

En [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md), el tema «Builder frente a argumentos con nombre» importa porque en Python los nombres evitan el constructor telescópico con menos piezas

## Cómo funciona

Según [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md):

El Builder ataca el **constructor telescópico**: muchos argumentos, varios del mismo tipo, algunos opcionales. En el experimento, 500 construcciones de un `Aviso` con asunto y cuerpo intercambiados son aceptadas **las 500** por un constructor posicional, porque ambos son cadenas y nada distingue un orden de otro. Con `dataclass(kw_only=True)` las 500 llamadas posicionales se rechazan: el intercambio exige escribir mal un nombre, y esa falla es visible. El Builder clásico sigue justificándose cuando hay **pasos con orden** o validaciones entre campos que solo se pueden hacer al final (`build()` comprueba que un aviso por SMS tenga teléfono), o cuando el objeto se construye por partes en distintos lugares. Con argumentos con nombre y un método de validación se obtiene el 80 % del beneficio con la mitad de las piezas.

## Ejemplo

Caso medido en la sección «Builder: del constructor telescópico a los argumentos con nombre» de [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md):

El Builder ataca el **constructor telescópico**: muchos argumentos, varios del mismo tipo, algunos opcionales. En el experimento, 500 construcciones de un `Aviso` con asunto y cuerpo intercambiados son aceptadas **las 500** por un constructor posicional, porque ambos son cadenas y nada distingue un orden de otro. Con `dataclass(kw_only=True)` las 500 llamadas posicionales se rechazan: el intercambio exige escribir mal un nombre, y esa falla es visible.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El Builder clásico sigue justificándose cuando hay **pasos con orden** o validaciones entre campos que solo se pueden hacer al final (`build()` comprueba que un aviso por SMS tenga teléfono), o cuando el objeto se construye por partes en distintos lugares. ([SE-314](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Objeto](../o/objeto.md), [Secuencia](../s/secuencia.md), [Copia profunda](../c/copia-profunda.md), [Copia superficial](../c/copia-superficial.md), [Factory](../f/factory.md), [Registro](../r/registro.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (18 clases más lo mencionan; las que más):

[SE-428](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md), [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-048](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md), [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md), [SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md), [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), [SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Build reproducible](./build-reproducible.md) · [Bulkhead →](./bulkhead.md)
