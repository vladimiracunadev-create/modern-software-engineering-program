# Creador

[↑ Glosario](../../README.md) · [← CRDT](./crdt.md) · [Credencial de vida corta →](./credencial-de-vida-corta.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Asignar la creación a quien contiene o usa el objeto.

Definición de trabajo de [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md).

## Por qué importa

En [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md), el tema «Creador y Controlador» importa porque deciden quién instancia y quién recibe eventos

## Cómo funciona

Según [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md):

El **Creador** asigna la creación de un objeto a quien lo contiene, lo registra, lo usa mucho o tiene los datos para inicializarlo; un `Pedido` crea sus `Linea`. El **Controlador** asigna la recepción de un evento externo (una petición, un mensaje) a un objeto que representa el caso de uso o el sistema, y no a la interfaz. Los dos criterios son los que menos a menudo se discuten y más a menudo se violan: la creación repartida en veinte lugares es el origen de la fábrica de `SE-314`, y un controlador que contiene reglas de negocio es la clase de dios de `SE-322`.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md)) son: Los diseños y las métricas son del autor, la cohesión se aproxima con atributos compartidos y la fuente de GRASP es secundaria; no se validó el efecto de GRASP en proyectos reales. El siguiente paso, `SE-318`, aplica la pregunta «¿a quién le toca?» a la persistencia: quién guarda, quién abre la transacción y quién sabe qué consultas se ejecutan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Objeto](../o/objeto.md), [Acoplamiento](../a/acoplamiento.md), [Cohesión](./cohesion.md), [Controlador](./controlador.md), [Experto en información](../e/experto-en-informacion.md), [Fabricación pura](../f/fabricacion-pura.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md).

**Aparece en los casos de estudio:** [Spotify](../../../casos/exito/spotify.md), [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← CRDT](./crdt.md) · [Credencial de vida corta →](./credencial-de-vida-corta.md)
