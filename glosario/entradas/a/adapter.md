# Adapter

[↑ Glosario](../../README.md) · [← Adaptador de compatibilidad](./adaptador-de-compatibilidad.md) · [Adopción →](./adopcion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Objeto que traduce una interfaz a otra que el cliente espera.

Definición de trabajo de [SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md).

## Por qué importa

En [SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), el tema «Adapter y prueba de contrato» importa porque dos proveedores deben cumplir lo mismo detrás de la misma interfaz

## Cómo funciona

Según [SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md):

Los cinco patrones comparten una estructura: un objeto que **contiene o envuelve** a otro. Lo que los separa es la intención. Un **Adapter** cambia la interfaz de un objeto a la que el cliente espera. Una **Facade** ofrece una interfaz simple a un subsistema. Un **Proxy** controla el acceso a un objeto con su misma interfaz (perezoso, remoto, con permisos). Un **Composite** trata un grupo de objetos como uno solo. Un **Decorator** añade comportamiento conservando la interfaz. Distinguirlos importa porque cada intención tiene su propio modo de estropearse y su propia prueba.

## Ejemplo

Caso medido en la sección «Adapter y la prueba de contrato» de [SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md):

*Avisos* integra dos proveedores de mensajería: uno expone `enviar(to, body)` y devuelve un diccionario con `id` y `status`; el otro, `push(destinatario, texto, prioridad)` y devuelve una tupla `(id, código HTTP)`. Dos adaptadores presentan a ambos una interfaz única `send(to, body)` que devuelve `(id, aceptado)`. El experimento comprueba que, con una misma llamada, ambos devuelven la misma forma `('a1', True)` y `('b1', True)`. La **prueba de contrato** es la pieza que mantiene honesto al patrón: una batería única que cualquier adaptador nuevo debe pasar.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md)) son: La simulación usa una distribución elegida por el autor y no incluye fallos correlacionados ni espera entre reintentos; los demás patrones se ejercitan con objetos mínimos. El siguiente paso, `SE-316`, trata los patrones que deciden comportamiento en tiempo de ejecución, donde el fallo típico es un estado representado con banderas que admite combinaciones imposibles.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-314](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Espera](../e/espera.md), [Interfaz](../i/interfaz.md), [Objeto](../o/objeto.md), [Composite](../c/composite.md), [Decorator](../d/decorator.md), [Facade](../f/facade.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-315 — GoF estructurales: Adapter, Decorator, Facade, Proxy y Composite](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (22 clases más lo mencionan; las que más):

[SE-098](../../../classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md), [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), [SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md), [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md), [SE-097](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md), [SE-099](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md), [SE-100](../../../classes/part-08-entornos-herramientas-y-depuracion/se-100-compiladores-linters-formatters-y-analisis-estatico/README.md), [SE-101](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Adaptador de compatibilidad](./adaptador-de-compatibilidad.md) · [Adopción →](./adopcion.md)
