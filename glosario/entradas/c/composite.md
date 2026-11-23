# Composite

[↑ Glosario](../../README.md) · [← Composición y tipos de resultado](./composicion-y-tipos-de-resultado.md) · [Composition root →](./composition-root.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Estructura en árbol donde grupos y elementos comparten interfaz.

Definición de trabajo de [SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md).

## Por qué importa

En [SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), el tema «Composite» importa porque trata grupos y elementos igual; los ciclos rompen la recursión

## Cómo funciona

Según [SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md):

Los cinco patrones comparten una estructura: un objeto que **contiene o envuelve** a otro. Lo que los separa es la intención. Un **Adapter** cambia la interfaz de un objeto a la que el cliente espera. Una **Facade** ofrece una interfaz simple a un subsistema. Un **Proxy** controla el acceso a un objeto con su misma interfaz (perezoso, remoto, con permisos). Un **Composite** trata un grupo de objetos como uno solo. Un **Decorator** añade comportamiento conservando la interfaz. Distinguirlos importa porque cada intención tiene su propio modo de estropearse y su propia prueba.

## Ejemplo

Caso medido en la sección «Composite: grupos que contienen grupos» de [SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md):

Un compuesto trata a un grupo y a un usuario con la misma interfaz, de modo que `usuarios()` funciona igual en ambos. El defecto es el **ciclo**: el grupo `a` contiene a `b` y `b` contiene a `a`. En el experimento, con la guarda de grupos visitados, el recorrido devuelve `['u1', 'u2', 'u3']`; sin la guarda, el mismo ciclo produce `RecursionError`. La estructura compuesta debe validarse al **construirse** (rechazar el ciclo) o recorrerse con una guarda; confiar en que «nadie lo hará» es esperar al incidente.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **Composite** trata un grupo de objetos como uno solo. ([SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-314](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Árbol](../a/arbol.md), [Estructura](../e/estructura.md), [Interfaz](../i/interfaz.md), [Adapter](../a/adapter.md), [Decorator](../d/decorator.md), [Facade](../f/facade.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-314](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Composición y tipos de resultado](./composicion-y-tipos-de-resultado.md) · [Composition root →](./composition-root.md)
