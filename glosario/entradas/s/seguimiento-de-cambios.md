# Seguimiento de cambios

[↑ Glosario](../../README.md) · [← Segregación](./segregacion.md) · [Seguridad →](./seguridad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Comparación del estado cargado con el actual para escribir solo lo modificado.

Definición de trabajo de [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md).

## Por qué importa

En [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md), el tema «Unit of Work y seguimiento de cambios» importa porque evita escribir lo que no cambió

## Cómo funciona

Según [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md):

Una Unit of Work mantiene los objetos afectados por una operación de negocio y coordina su escritura. Dos propiedades interesan. La primera es el **seguimiento de cambios**: de 100 entregas cargadas y 3 modificadas, guardar todo ejecuta **100** UPDATE y guardar solo lo que cambió ejecuta **3**; el seguimiento compara el estado cargado con el actual. La segunda es la **atomicidad**: una operación de dos pasos que falla a mitad deja, sin transacción, el primer paso persistido (el estado de la entrega queda «entregada»); dentro de una transacción (`with conexion:` en `sqlite3`), el fallo la revierte y el estado vuelve a «pendiente». La unidad de trabajo es la disciplina de abrir la transacción **en un lugar** (el caso de uso) y no en cada método del repositorio.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La primera es el **seguimiento de cambios**: de 100 entregas cargadas y 3 modificadas, guardar todo ejecuta **100** UPDATE y guardar solo lo que cambió ejecuta **3**; el seguimiento compara el estado cargado con el actual. ([SE-318](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Active Record](../a/active-record.md), [Atomicidad](../a/atomicidad.md), [N+1](../n/n-mas-1.md), [Repository](../r/repository.md), [Unit of Work](../u/unit-of-work.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Segregación](./segregacion.md) · [Seguridad →](./seguridad.md)
