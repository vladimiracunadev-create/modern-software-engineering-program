# Maestro dorado

[↑ Glosario](../../README.md) · [← MAD](./mad.md) · [Maldición del optimizador →](./maldicion-del-optimizador.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Un **maestro dorado** (*golden master*) es el registro de las salidas de un programa para un conjunto de entradas, usado como oráculo para detectar cambios de comportamiento ([SE-311](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md)). [SE-323](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md) y [SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md) lo usan en el mismo sentido: la salida del código actual para un conjunto fijo de entradas, contra la cual se compara el código nuevo.

## Por qué importa

Refactorizar código sin pruebas finas exige saber si el comportamiento cambió, pero definir primero qué es correcto puede ser costoso o imposible. La decisión que cambia es qué se toma como referencia: no «lo correcto», sino «lo que el código hace hoy». Con eso, cualquier diferencia es un cambio de comportamiento que hay que explicar.

## Cómo funciona

[SE-311](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md) es explícito con lo que el maestro **no** afirma: no dice que las salidas sean correctas; dice que son lo que el código hace hoy. Eso le da su uso: como oráculo de un refactor. Se ejecuta el código actual con un conjunto grande de entradas, se guardan las salidas, y tras cada paso del refactor se vuelve a ejecutar y se compara. Una diferencia no es necesariamente un error, pero sí un cambio que alguien debe aprobar o corregir.

Su calidad depende de las entradas: deben cubrir los caminos y los bordes, incluidas las entradas «raras» que los clientes reales envían. Un maestro con entradas limpias deja pasar cambios que rompen a los canales antiguos. Por eso [SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md) lo combina con medición de cobertura y de mutantes, y con normalizar la variación (fechas, identificadores aleatorios) para que no genere diferencias falsas. El procedimiento completo de esa clase: crear una costura, registrar un maestro dorado, medir cobertura y mutantes, normalizar la variación y decidir qué hacer con cada comportamiento sospechoso.

Una práctica de disciplina: comparar tras cada paso y hacer un commit por paso, de modo que si el comportamiento cambia se sabe qué paso lo cambió.

## Ejemplo

Una función de tarifas heredada no tiene pruebas. Se ejecuta con miles de combinaciones de entrada reales y se guardan los resultados. Se refactoriza en pasos pequeños; tras cada uno se compara con el maestro. En un paso aparece una diferencia en un caso de un canal antiguo: se detecta antes de desplegar. Procedimiento de [SE-311](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md) y [SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md).

## Errores y confusiones comunes

- **El refactor pasa las pruebas y rompe a un cliente**: el maestro no incluye entradas de canales antiguos; se añaden las entradas reales (valores no booleanos, formatos viejos).
- **No se sabe qué paso cambió el comportamiento**: se hicieron varios pasos antes de comparar; se compara tras cada paso con un commit por paso.
- **Tomarlo como especificación**: registra lo que hace, incluidos sus defectos.
- **No normalizar la variación**: las fechas y los aleatorios producen diferencias falsas.

## Límites y cuándo no aplica

[SE-323](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md) lo limita: es útil cuando la función **no tiene** pruebas finas y se quiere refactorizar sin definir primero qué es correcto; las pruebas unitarias documentan la intención, y donde existen son preferibles. El maestro fija también los defectos actuales, así que no sirve para corregir comportamiento. Y solo ve lo que las entradas cubren: sin buena cobertura, da una falsa confianza.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md), [SE-310](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Oráculo](../o/oraculo.md), [Registro](../r/registro.md), [Arco](../a/arco.md), [Compatibilidad hacia atrás](../c/compatibilidad-hacia-atras.md), [Condición de salida](../c/condicion-de-salida.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-323 — Taller: refactorizar con patrones y medir su costo](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-312](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md), [SE-322](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md), [SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md).

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

[↑ Glosario](../../README.md) · [← MAD](./mad.md) · [Maldición del optimizador →](./maldicion-del-optimizador.md)
