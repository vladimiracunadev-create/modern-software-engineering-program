# Active Record

[↑ Glosario](../../README.md) · [← Activación y ejecutable explícito](./activacion-y-ejecutable-explicito.md) · [Actividad →](./actividad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Objeto que encapsula una fila, el acceso a la base y lógica de dominio.

Definición de trabajo de [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md).

## Por qué importa

En [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md), el tema «Active Record» importa porque menos piezas, más acoplamiento a la base

## Cómo funciona

Según [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md):

En un Active Record la entidad sabe guardarse: `entrega.save()`. Es una opción razonable cuando el modelo es casi las tablas y la regla de negocio es poca. El experimento muestra el costo: una entidad con la regla pura `vencida(hora)` se prueba sin base (devuelve `True`), pero la operación `cumplir()`, que cambia el estado **y** llama a `save()`, **falla sin conexión** (`AttributeError`) porque la regla y la persistencia comparten método. A medida que la regla crece, las pruebas de dominio necesitan una base. La salida es separar la regla en métodos puros y dejar `save` en el borde, o pasar a un Repository cuando la regla lo justifique.

Según [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md):

El equipo de *Avisos* añade a su prueba de integración un contador de sentencias por caso de uso: «el listado de entregas no puede ejecutar más de 3 consultas con 500 filas». La prueba falla en la primera ejecución con 501 consultas. Se añade `entregas_con_curso()` al repositorio con una unión y la prueba pasa con 1. Para «marcar y notificar» abre la transacción en el caso de uso, no en el repositorio, y añade una prueba que fuerza el fallo del segundo paso y comprueba que la primera tabla no cambió. La decisión entre Repository y Active Record para las entregas queda registrada, con la alternativa descartada y la condición de revisarla si la lógica de dominio crece.

## Ejemplo

Ejemplo de [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* añade a su prueba de integración un contador de sentencias por caso de uso: «el listado de entregas no puede ejecutar más de 3 consultas con 500 filas». La prueba falla en la primera ejecución con 501 consultas. Se añade `entregas_con_curso()` al repositorio con una unión y la prueba pasa con 1. Para «marcar y notificar» abre la transacción en el caso de uso, no en el repositorio, y añade una prueba que fuerza el fallo del segundo paso y comprueba que la primera tabla no cambió.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La fila de Active Record es una demostración de acoplamiento con una entidad mínima, no una crítica general al patrón. ([SE-318](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Base](../b/base.md), [Dominio](../d/dominio.md), [Objeto](../o/objeto.md), [Atomicidad](./atomicidad.md), [N+1](../n/n-mas-1.md), [Repository](../r/repository.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md), [SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Activación y ejecutable explícito](./activacion-y-ejecutable-explicito.md) · [Actividad →](./actividad.md)
