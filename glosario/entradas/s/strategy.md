# Strategy

[↑ Glosario](../../README.md) · [← Step, continue y watch](./step-continue-y-watch.md) · [Strategy con registro →](./strategy-con-registro.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Algoritmo intercambiable detrás de una interfaz.

Definición de trabajo de [SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md).

## Por qué importa

En [SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md), el tema «Strategy y Template Method» importa porque eligen cómo se reparte la variación

## Cómo funciona

Según [SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md):

Con **Strategy**, la variación vive en un objeto que se entrega al que lo usa (la tarifa de un canal, por ejemplo); con **Template Method**, el esqueleto vive en una clase base y los pasos variables en las subclases. En el experimento, un esqueleto `validar → transformar → formatear` escribe validar y formatear una vez, y `Doble` y `Cuadrado` solo redefinen `transformar`. La decisión depende de qué cambia y de cuántos ejes: Template Method acopla a la herencia y sirve para una sola dimensión de variación; Strategy compone y sirve cuando se varían dos cosas por separado. En lenguajes con funciones de primera clase, ambos pueden reducirse a pasar una función.

## Ejemplo

Ejemplo de [SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md) (sección «Caso conductor»):

*Avisos* conserva sus cuatro banderas hasta esta clase y las sustituye por una máquina de estados; el Observer del módulo de métricas queda con baja explícita. `SE-319` reutiliza la tabla de transiciones al hablar de mensajes en cola y `SE-323` usa Strategy en el refactor de las tarifas.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md)) son: La definición de «imposible», las secuencias y los oyentes son del autor; no se midió la frecuencia de estos defectos en proyectos reales. El siguiente paso, `SE-317`, sube un nivel: en lugar de preguntar qué patrón usar, pregunta **a quién le corresponde** una responsabilidad, con los criterios de GRASP.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-314](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md), [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Algoritmo](../a/algoritmo.md), [Interfaz](../i/interfaz.md), [Command](../c/command.md), [Observer](../o/observer.md), [Propiedad](../p/propiedad.md), [Referencia débil](../r/referencia-debil.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-323](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md), [SE-324](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md), [SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md), [SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md), [SE-091](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-091-algoritmos-voraces-y-programacion-dinamica/README.md), [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), [SE-584](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Step, continue y watch](./step-continue-y-watch.md) · [Strategy con registro →](./strategy-con-registro.md)
