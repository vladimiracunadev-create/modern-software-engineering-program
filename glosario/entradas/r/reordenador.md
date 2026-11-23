# Reordenador

[↑ Glosario](../../README.md) · [← Rendimiento](./rendimiento.md) · [Reparación →](./reparacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Componente que restaura el orden de una secuencia con un buffer.

Definición de trabajo de [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md).

## Por qué importa

En [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md), el tema «Reordenador» importa porque restaura un orden cuando importa

## Cómo funciona

Según [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md):

Un **Resequencer** guarda los mensajes que llegan antes de tiempo hasta recibir el que falta. Con una entrada con **977 pares fuera de orden** (tras eliminar los duplicados), el reordenador entrega una salida con **0** inversiones en los primeros 300 mensajes. El costo es la memoria del buffer y la latencia: un mensaje no se entrega hasta que llegan los anteriores. Y hay una condición que no se puede evitar: si un mensaje intermedio **nunca llega**, el reordenador espera sin fin; por eso necesita un plazo y una política (saltar el hueco, alarmar). Si el orden no importa para el efecto (sumas de pagos, por ejemplo), reordenar es un costo innecesario.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Y hay una condición que no se puede evitar: si un mensaje intermedio **nunca llega**, el reordenador espera sin fin; por eso necesita un plazo y una política (saltar el hueco, alarmar). ([SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-318](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Secuencia](../s/secuencia.md), [Cola de cartas muertas](../c/cola-de-cartas-muertas.md), [Entrega al menos una vez](../e/entrega-al-menos-una-vez.md), [Identificador de correlación](../i/identificador-de-correlacion.md), [Mensaje veneno](../m/mensaje-veneno.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Rendimiento](./rendimiento.md) · [Reparación →](./reparacion.md)
