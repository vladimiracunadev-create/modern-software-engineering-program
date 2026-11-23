# Command

[↑ Glosario](../../README.md) · [← Comité y cadencia](./comite-y-cadencia.md) · [Commit atómico →](./commit-atomico.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Acción representada como objeto, con posibilidad de encolar y deshacer.

Definición de trabajo de [SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md).

## Por qué importa

En [SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md), el tema «Command y deshacer» importa porque deshacer es una promesa que se comprueba

## Cómo funciona

Según [SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md):

**Cómo leer la figura.** A la izquierda están Observer y Command y a la derecha cinco medidas. Las cajas coral son los defectos (oyentes vivos, notificaciones que se pierden) y las turquesa la variante que los corrige, con su recuento. **Dónde deja de valer:** los 1000 oyentes son objetos sin estado y la recolección de basura de CPython es por conteo de referencias; en otros entornos (JVM, JavaScript) el momento de la recolección difiere. Que 3 de 4 oyentes reciban el evento es una política (no propagar) y otras políticas son válidas.

Según [SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md):

El equipo de *Avisos* convierte el ciclo de vida del aviso en una tabla de transiciones y se la muestra a una docente: ella corrige una fila (un aviso fallido que se cancela vuelve a mostrarse al estudiante como «cancelado», no como «fallido»). Para el módulo de métricas, que se suscribía a los eventos, el equipo reemplaza la lista de oyentes por una que devuelve un objeto de baja y escribe una prueba que suscribe, descarta y comprueba que no queda ninguna referencia. Para el envío en lote añade un Command con deshacer y una prueba de propiedades con semilla registrada. Cada decisión lleva su condición de salida.

## Ejemplo

Ejemplo de [SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* convierte el ciclo de vida del aviso en una tabla de transiciones y se la muestra a una docente: ella corrige una fila (un aviso fallido que se cancela vuelve a mostrarse al estudiante como «cancelado», no como «fallido»). Para el módulo de métricas, que se suscribía a los eventos, el equipo reemplaza la lista de oyentes por una que devuelve un objeto de baja y escribe una prueba que suscribe, descarta y comprueba que no queda ninguna referencia. Para el envío en lote añade un Command con deshacer y una prueba de propiedades con semilla registrada. Cada decisión lleva su condición de salida.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** la clasificación es una simplificación; un mismo diseño mezcla varios (un State cuyas acciones son Commands) y el diagrama no dice cuál elegir ante un problema, solo qué hace cada uno. ([SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-314](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md), [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Objeto](../o/objeto.md), [Observer](../o/observer.md), [Propiedad](../p/propiedad.md), [Referencia débil](../r/referencia-debil.md), [State](../s/state.md), [Strategy](../s/strategy.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-316 — GoF conductuales: Strategy, Observer, Command, State y Template Method](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (17 clases más lo mencionan; las que más):

[SE-029](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md), [SE-217](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md), [SE-218](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md), [SE-220](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md), [SE-227](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md), [SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md), [SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md), [SE-035](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Comité y cadencia](./comite-y-cadencia.md) · [Commit atómico →](./commit-atomico.md)
