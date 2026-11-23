# Repository

[↑ Glosario](../../README.md) · [← Repositorio de paquetes](./repositorio-de-paquetes.md) · [Reposo →](./reposo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Colección de objetos de dominio que oculta el acceso a datos.

Definición de trabajo de [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md).

## Por qué importa

En [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md), el tema «Repository como colección» importa porque oculta la base y también su costo

## Cómo funciona

Según [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md):

Un Repository presenta los objetos de dominio como una colección en memoria: `repositorio.buscar(id)`, `repositorio.agregar(x)`. Su fuerza es que el dominio no conoce SQL y puede probarse con una colección real en memoria. Su riesgo es el que mide el experimento: sobre una base `sqlite3` con 20 cursos y 200 entregas, un listado que carga **cada curso por separado** para mostrar su nombre ejecuta **201 consultas** (1 para las entregas y 200 para los cursos), contadas con `set_trace_callback`. El mismo resultado con una consulta de lectura que une las dos tablas usa **1**. La interfaz «colección» es la misma en ambos casos; lo que cambia es que la segunda permite pedir los datos que se van a usar.

Según [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md):

El equipo de *Avisos* añade a su prueba de integración un contador de sentencias por caso de uso: «el listado de entregas no puede ejecutar más de 3 consultas con 500 filas». La prueba falla en la primera ejecución con 501 consultas. Se añade `entregas_con_curso()` al repositorio con una unión y la prueba pasa con 1. Para «marcar y notificar» abre la transacción en el caso de uso, no en el repositorio, y añade una prueba que fuerza el fallo del segundo paso y comprueba que la primera tabla no cambió. La decisión entre Repository y Active Record para las entregas queda registrada, con la alternativa descartada y la condición de revisarla si la lógica de dominio crece.

## Ejemplo

Ejemplo de [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* añade a su prueba de integración un contador de sentencias por caso de uso: «el listado de entregas no puede ejecutar más de 3 consultas con 500 filas». La prueba falla en la primera ejecución con 501 consultas. Se añade `entregas_con_curso()` al repositorio con una unión y la prueba pasa con 1. Para «marcar y notificar» abre la transacción en el caso de uso, no en el repositorio, y añade una prueba que fuerza el fallo del segundo paso y comprueba que la primera tabla no cambió.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Si la regla de negocio cambia a menudo y se quiere probar sin base, un Repository. ([SE-318](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Colección](../c/coleccion.md), [Dominio](../d/dominio.md), [Objeto](../o/objeto.md), [Active Record](../a/active-record.md), [Atomicidad](../a/atomicidad.md), [N+1](../n/n-mas-1.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md), [SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md), [SE-324](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md), [SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Repositorio de paquetes](./repositorio-de-paquetes.md) · [Reposo →](./reposo.md)
