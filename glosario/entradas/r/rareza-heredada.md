# Rareza heredada

[↑ Glosario](../../README.md) · [← Ranura](./ranura.md) · [Rastrear →](./rastrear.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Una **rareza heredada** es un comportamiento no documentado del código existente que puede estar en uso ([SE-311](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md)). Puede ser un defecto que nadie notó o un acuerdo implícito con clientes: el código hace algo inesperado, y alguien o algo puede depender de ello.

## Por qué importa

Al refactorizar o modernizar se tiende a «arreglar» lo que parece un error. Pero si un cliente depende de esa conducta, arreglarla es romperlo. La decisión que cambia es cómo se trata una diferencia de comportamiento: como una decisión explícita (conservar o corregir), no como un efecto secundario de una simplificación.

## Cómo funciona

[SE-311](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md) las descubre con el maestro dorado: cada diferencia detectada al comparar el código nuevo con el registro del actual es una decisión. La clase da dos ejemplos de tipos distintos:

- **Defecto que nadie notó**: un cupón que da un monto negativo y se corrige a cero por un piso.
- **Acuerdo implícito con clientes**: un `urgente` que llega como `2` o como `"si"` y se trata como falso porque la comparación es con `True`.

Hay tres desenlaces posibles. **Conservar** la rareza la convierte en una regla explícita con una prueba y un nombre. **Corregirla** es un cambio de comportamiento que se anuncia y se programa, no un detalle del refactor. **No decidir** deja la rareza escondida en una simplificación: el comportamiento cambia sin que nadie lo haya elegido.

Para encontrar rarezas hace falta que el maestro incluya las entradas reales, no solo las limpias: valores no booleanos, formatos viejos, canales antiguos. Un refactor que pasa las pruebas y rompe a un cliente indica que el maestro no incluía esas entradas.

## Ejemplo

Una función de tarifas trata `urgente="si"` como falso por comparar con `True`. Un cliente antiguo envía `"si"` y recibe la tarifa normal; lo tiene asumido. Un refactor «limpia» la comparación y empieza a cobrar la tarifa urgente. El maestro dorado, con la entrada `"si"`, habría mostrado la diferencia y forzado la decisión. Caso de [SE-311](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md).

## Errores y confusiones comunes

- **El refactor pasa las pruebas y rompe a un cliente**: el maestro no incluye entradas de canales antiguos; se añaden las entradas reales.
- **No se sabe qué paso cambió el comportamiento**: se hicieron varios pasos antes de comparar; se compara tras cada paso con un commit por paso.
- **Corregir toda rareza por principio**.
- **Dejar la rareza implícita** tras conservarla: debe tener un nombre y una prueba.

## Límites y cuándo no aplica

[SE-311](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md) aclara que no se consultó a ningún cliente real ni se registró un maestro con tráfico real; la función, su dominio de entradas, los valores no booleanos y los 39 mutantes son construcciones del autor. Saber que una rareza está en uso exige evidencia (registros de uso, consulta a clientes); sin ella, la decisión es una apuesta. En código nuevo, sin consumidores, el concepto no aplica.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md), [SE-310](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Arco](../a/arco.md), [Compatibilidad hacia atrás](../c/compatibilidad-hacia-atras.md), [Maestro dorado](../m/maestro-dorado.md), [Prueba de caracterización](../p/prueba-de-caracterizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-312](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Rarezas heredadas».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Feathers, «Working Effectively with Legacy Code»](https://www.oreilly.com/library/view/working-effectively-with/0131177052/) — pruebas de caracterización; autoridad: su autor (Prentice Hall).
- [Fowler, «Refactoring» (2.ª ed.)](https://martinfowler.com/books/refactoring.html) — refactorizar en pasos pequeños; autoridad: Martin Fowler.
- [Fowler, «Extract Function»](https://refactoring.com/catalog/extractFunction.html) — extracción de una función; autoridad: Martin Fowler.
- [Fowler, «Self Testing Code»](https://martinfowler.com/bliki/SelfTestingCode.html) — código que se comprueba solo; autoridad: Martin Fowler.
- [Jia y Harman (IEEE TSE, 2011)](https://doi.org/10.1109/TSE.2010.62) — revisión de la prueba de mutación; autoridad: IEEE Transactions on Software Engineering.

---

[↑ Glosario](../../README.md) · [← Ranura](./ranura.md) · [Rastrear →](./rastrear.md)
