# Entradas de frontera

[↑ Glosario](../../README.md) · [← Entrada no declarada](./entrada-no-declarada.md) · [Entradas no confiables →](./entradas-no-confiables.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Valores en y alrededor de los límites de una regla.

Definición de trabajo de [SE-323 — Taller: refactorizar con patrones y medir su costo](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md).

## Por qué importa

En [SE-323 — Taller: refactorizar con patrones y medir su costo](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md), el tema «Entradas de frontera» importa porque las entradas al azar no tocan los límites

## Cómo funciona

Según [SE-323 — Taller: refactorizar con patrones y medir su costo](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md):

Para que el maestro detecte los tres mutantes que sobreviven, se añaden **384 entradas de frontera**: todas las combinaciones de canal (4), urgencia (2), horas en {20, 21, 23, 24} (4), adjuntos en {2, 3} (2) y grupo en {50, 51, 100, 101, 1000, 1001} (6). Con las 5000 más las 384, el maestro detecta **6 de 6** y el refactor sigue sin diferir de la función antigua (0 diferencias). La lección es la del análisis de valores límite ([Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)): los defectos viven en los bordes y las entradas al azar casi nunca los tocan. Más entradas al azar no resuelven el problema; las fronteras se **escriben**.

Según [SE-323 — Taller: refactorizar con patrones y medir su costo](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md):

El equipo de *Avisos* hace el taller sobre `precio_aviso` antes de añadir WhatsApp. Registra el maestro (5000 entradas, semilla registrada) y descubre que su red detecta tres de seis mutantes; añade entradas de frontera hasta detectar los seis. Refactoriza en cinco pasos con el maestro en verde después de cada uno, mide complejidad 15 → 3 y nodos +44 %, añade el canal nuevo como una clase y una línea de registro sin tocar el resto y registra en el catálogo de patrones (`SE-324`) la condición de salida. En la revisión, una persona pregunta si no bastaba un diccionario de funciones; la respuesta queda anotada: la tarifa de voz necesita estado (el contrato del grupo), así que se justifica una clase.

## Ejemplo

Ejemplo de [SE-323 — Taller: refactorizar con patrones y medir su costo](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* hace el taller sobre `precio_aviso` antes de añadir WhatsApp. Registra el maestro (5000 entradas, semilla registrada) y descubre que su red detecta tres de seis mutantes; añade entradas de frontera hasta detectar los seis. Refactoriza en cinco pasos con el maestro en verde después de cada uno, mide complejidad 15 → 3 y nodos +44 %, añade el canal nuevo como una clase y una línea de registro sin tocar el resto y registra en el catálogo de patrones (`SE-324`) la condición de salida.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Corrección.** Se añaden las entradas de frontera al maestro, se vuelve a ejecutar y se corrige el umbral; se anota la regla en el taller: ningún refactor se acepta sin que la red detecte los mutantes de cada umbral. ([SE-323](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-322](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Límite](../l/limite.md), [Regla](../r/regla.md), [Valor](../v/valor.md), [Condición de salida](../c/condicion-de-salida.md), [Maestro dorado](../m/maestro-dorado.md), [Prueba de caracterización](../p/prueba-de-caracterizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-323 — Taller: refactorizar con patrones y medir su costo](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Entrada no declarada](./entrada-no-declarada.md) · [Entradas no confiables →](./entradas-no-confiables.md)
