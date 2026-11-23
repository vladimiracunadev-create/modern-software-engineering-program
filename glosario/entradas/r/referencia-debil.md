# Referencia débil

[↑ Glosario](../../README.md) · [← Referencia de cierre](./referencia-de-cierre.md) · [Referencia externa →](./referencia-externa.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Referencia que no impide que el objeto sea recolectado.

Definición de trabajo de [SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md).

## Por qué importa

La clase donde se define, [SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md), existe con este propósito: la clase existe para que muevas decisiones de comportamiento de condicionales a objetos **sabiendo qué fallo nuevo introduces con cada movimiento**.

## Cómo funciona

Según [SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md):

El Observer permite que un emisor notifique a receptores que no conoce. La ganancia es el desacoplamiento; la **obligación nueva** es el ciclo de vida de los oyentes. En el experimento se suscriben 1000 oyentes y se descartan sin darse de baja: con una lista de referencias fuertes, **los 1000 siguen vivos** (la lista los retiene); con un `WeakSet`, **0** (se recolectan). El primer diseño es una fuga que crece con cada suscripción olvidada, y además sigue llamando a oyentes cuyo módulo ya no existe. La solución no es siempre una referencia débil (un oyente que es una función anónima se recolecta de inmediato), sino definir una **política de baja**: quien se suscribe devuelve una forma de cancelar, y el emisor la ofrece.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La solución no es siempre una referencia débil (un oyente que es una función anónima se recolecta de inmediato), sino definir una **política de baja**: quien se suscribe devuelve una forma de cancelar, y el emisor la ofrece. ([SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-314](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md), [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Objeto](../o/objeto.md), [Referencia](./referencia.md), [Command](../c/command.md), [Observer](../o/observer.md), [Propiedad](../p/propiedad.md), [State](../s/state.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-021](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Referencia de cierre](./referencia-de-cierre.md) · [Referencia externa →](./referencia-externa.md)
