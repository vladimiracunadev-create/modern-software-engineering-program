# Arco

[↑ Glosario](../../README.md) · [← Archivo huérfano](./archivo-huerfano.md) · [Argumento →](./argumento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Par de líneas consecutivas ejecutadas, usado como medida de cobertura de caminos.

Definición de trabajo de [SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md).

## Por qué importa

La clase donde se define, [SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md), existe con este propósito: el taller existe para que ejecutes un refactor completo sobre una función heredada de `tarifas` con la técnica que cuida el comportamiento cuando no hay especificación: registrar lo que hace hoy (un maestro dorado), avanzar en pasos que se comparan con ese registro, decidir caso por caso qué rarezas se conservan y cuáles se corrigen, y entregar la evidencia de cada decisión.

## Cómo funciona

Según [SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md):

Con `sys.settrace` se registran los arcos (pares de líneas consecutivas) que recorre la función heredada. El total alcanzable con las 3000 entradas y dos entradas a mano (un cupón de envío gratis fuera de zona y un peso mínimo) es de 42 arcos. Para cada tamaño de muestra se calcula qué fracción de esos arcos se alcanza (30 muestras, semilla fija).

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md):

El equipo de `tarifas` ejecuta el taller con un protocolo de cinco pasos escrito antes de tocar el código. Registra el maestro dorado con 3000 entradas de semilla fija más los casos de borde derivados del código, incluidos los valores no booleanos que, según el registro de solicitudes, llegan del cliente antiguo. Hace los cuatro pasos con un commit y una comparación cada uno.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md)) son:

- **El refactor pasa las pruebas y rompe a un cliente** — causa: el maestro no incluye entradas de canales antiguos. Corrección: añadir las entradas reales (valores no booleanos, formatos viejos).
- **No se sabe qué paso cambió el comportamiento** — causa: se hicieron varios pasos antes de comparar. Corrección: comparar tras cada paso y hacer un commit por paso.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El total alcanzable con las 3000 entradas y dos entradas a mano (un cupón de envío gratis fuera de zona y un peso mínimo) es de 42 arcos. ([SE-311](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md), [SE-310](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cobertura](../c/cobertura.md), [Medida](../m/medida.md), [Compatibilidad hacia atrás](../c/compatibilidad-hacia-atras.md), [Maestro dorado](../m/maestro-dorado.md), [Prueba de caracterización](../p/prueba-de-caracterizacion.md), [Rareza heredada](../r/rareza-heredada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Feathers, «Working Effectively with Legacy Code»](https://www.oreilly.com/library/view/working-effectively-with/0131177052/) — pruebas de caracterización; autoridad: su autor (Prentice Hall).
- [Fowler, «Refactoring» (2.ª ed.)](https://martinfowler.com/books/refactoring.html) — refactorizar en pasos pequeños; autoridad: Martin Fowler.
- [Fowler, «Extract Function»](https://refactoring.com/catalog/extractFunction.html) — extracción de una función; autoridad: Martin Fowler.
- [Fowler, «Self Testing Code»](https://martinfowler.com/bliki/SelfTestingCode.html) — código que se comprueba solo; autoridad: Martin Fowler.
- [Jia y Harman (IEEE TSE, 2011)](https://doi.org/10.1109/TSE.2010.62) — revisión de la prueba de mutación; autoridad: IEEE Transactions on Software Engineering.

---

[↑ Glosario](../../README.md) · [← Archivo huérfano](./archivo-huerfano.md) · [Argumento →](./argumento.md)
