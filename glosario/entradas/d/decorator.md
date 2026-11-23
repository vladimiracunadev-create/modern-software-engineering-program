# Decorator

[↑ Glosario](../../README.md) · [← Declaración de límites](./declaracion-de-limites.md) · [Deduplicación →](./deduplicacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Envoltura con la misma interfaz que añade comportamiento.

Definición de trabajo de [SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md).

## Por qué importa

En [SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), el tema «Decorator y orden» importa porque el orden de la pila es la política

## Cómo funciona

Según [SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md):

Los cinco patrones comparten una estructura: un objeto que **contiene o envuelve** a otro. Lo que los separa es la intención. Un **Adapter** cambia la interfaz de un objeto a la que el cliente espera. Una **Facade** ofrece una interfaz simple a un subsistema. Un **Proxy** controla el acceso a un objeto con su misma interfaz (perezoso, remoto, con permisos). Un **Composite** trata un grupo de objetos como uno solo. Un **Decorator** añade comportamiento conservando la interfaz. Distinguirlos importa porque cada intención tiene su propio modo de estropearse y su propia prueba.

Según [SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md):

La intención. El Decorator añade comportamiento (registro, reintento); el Proxy controla el acceso (perezoso, permisos, remoto). Estructuralmente pueden ser idénticos, y un mismo objeto puede ser ambos.

## Ejemplo

Ejemplo de [SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md) (sección «Preguntas frecuentes»):

La intención. El Decorator añade comportamiento (registro, reintento); el Proxy controla el acceso (perezoso, permisos, remoto). Estructuralmente pueden ser idénticos, y un mismo objeto puede ser ambos.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md)) son: La simulación usa una distribución elegida por el autor y no incluye fallos correlacionados ni espera entre reintentos; los demás patrones se ejercitan con objetos mínimos. El siguiente paso, `SE-316`, trata los patrones que deciden comportamiento en tiempo de ejecución, donde el fallo típico es un estado representado con banderas que admite combinaciones imposibles.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-314](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Interfaz](../i/interfaz.md), [Adapter](../a/adapter.md), [Composite](../c/composite.md), [Facade](../f/facade.md), [Proxy](../p/proxy.md), [Prueba de contrato](../p/prueba-de-contrato.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-314](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md), [SE-324](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Declaración de límites](./declaracion-de-limites.md) · [Deduplicación →](./deduplicacion.md)
