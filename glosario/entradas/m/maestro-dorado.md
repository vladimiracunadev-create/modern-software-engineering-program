# Maestro dorado

[↑ Glosario](../../README.md) · [← MAD](./mad.md) · [Maldición del optimizador →](./maldicion-del-optimizador.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Registro de las salidas de un programa para un conjunto de entradas, usado como oráculo para detectar cambios de comportamiento.

Definición de trabajo de [SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-323 — Taller: refactorizar con patrones y medir su costo](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md): Registro de la salida del código actual para un conjunto fijo de entradas, contra el cual se compara el código nuevo.
- En [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md): Conjunto de entradas con las salidas registradas del código actual, usado como expectativa.

## Por qué importa

En [SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md), el tema «Maestro dorado» importa porque convierte el comportamiento actual en un oráculo sin necesitar una especificación.

En [SE-323 — Taller: refactorizar con patrones y medir su costo](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md), el tema «Maestro dorado» importa porque es la red de seguridad de un refactor sin pruebas finas

## Cómo funciona

Según [SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md), en la sección «Maestro dorado»:

Un maestro dorado (golden master) es un registro de las salidas del programa actual para un conjunto grande de entradas. No afirma que esas salidas sean correctas: afirma que son lo que el código hace hoy. Sirve como oráculo para un refactor, porque cualquier diferencia es un cambio de comportamiento que hay que explicar. Su calidad depende de las entradas: deben cubrir los caminos y los bordes, incluidas las entradas «raras» que los clientes reales envían.

## Ejemplo

Ejemplo de [SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md) (sección «Ejemplo mínimo»):

El fragmento registra un maestro dorado de una función y detecta un cambio. Antes de ejecutarlo, predice cuántas entradas difieren.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md)) son:

- **El refactor pasa las pruebas y rompe a un cliente** — causa: el maestro no incluye entradas de canales antiguos. Corrección: añadir las entradas reales (valores no booleanos, formatos viejos).
- **No se sabe qué paso cambió el comportamiento** — causa: se hicieron varios pasos antes de comparar. Corrección: comparar tras cada paso y hacer un commit por paso.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El maestro dorado es útil cuando la función **no tiene** pruebas finas y se quiere refactorizar sin definir primero qué es correcto; las pruebas unitarias documentan la intención. ([SE-323](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md))
- Traslada el análisis a otro dominio (por ejemplo, una función que calcula el precio de una reserva con descuentos): cambia la función y las dependencias y conserva el procedimiento de crear una costura, registrar un maestro dorado, medir cobertura y mutantes, normalizar la variación y decidir qué hacer con cada comportamiento sospechoso. ([SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md))

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
