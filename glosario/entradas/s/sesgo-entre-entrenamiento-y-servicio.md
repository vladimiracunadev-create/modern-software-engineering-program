# Sesgo entre entrenamiento y servicio

[↑ Glosario](../../README.md) · [← Sesgo del resultado](./sesgo-del-resultado.md) · [Seudonimización →](./seudonimizacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Diferencia entre cómo se calcula o se distribuye una característica en cada entorno.

Definición de trabajo de [SE-602 — Datos de entrenamiento, etiquetas y feature stores](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-601 — Ciclo de vida de ML y por qué falla en producción](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md): Diferencia entre cómo se calculan o distribuyen las entradas en cada entorno.

## Por qué importa

La clase donde se define, [SE-602 — Datos de entrenamiento, etiquetas y feature stores](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md), existe con este propósito: la clase existe para que trates los datos de un modelo como un producto de ingeniería con defectos propios, y no como una materia prima que «ya viene».

## Cómo funciona

Según [SE-602 — Datos de entrenamiento, etiquetas y feature stores](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md):

La práctica más robusta contra el sesgo entre entrenamiento y servicio es entrenar con las características tal como el servicio las registró al decidir, en vez de recalcularlas después. Resuelve la unión puntual y la paridad de una vez, con el costo de almacenar cada vector de entrada. En *Avisos*, 20 000 decisiones diarias con seis características de ocho bytes suman unos 1,0 MB por día antes de comprimir; guardar la entrada de cada decisión rara vez es el costo que impide hacerlo. Lo que sí exige es una política de retención y de datos personales, que `SE-610` retoma.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-602 — Datos de entrenamiento, etiquetas y feature stores](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-602 — Datos de entrenamiento, etiquetas y feature stores](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md)) son: La fuga, el ruido, la unión y las definiciones alternativas son construcciones del autor sobre datos sintéticos de seis características; los números muestran mecanismos, no la frecuencia ni el costo de estos defectos en ningún sistema real. No se evaluó ningún almacén de características. El siguiente paso, `SE-603`, pregunta si el entrenamiento sobre estos datos se puede repetir y cuánto de la diferencia entre dos corridas es azar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Característica](../c/caracteristica.md), [Entorno](../e/entorno.md), [Almacén de características](../a/almacen-de-caracteristicas.md), [Bucle de realimentación](../b/bucle-de-realimentacion.md), [Ciclo de vida](../c/ciclo-de-vida.md), [Deriva de concepto](../d/deriva-de-concepto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-601 — Ciclo de vida de ML y por qué falla en producción](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.
- [SE-602 — Datos de entrenamiento, etiquetas y feature stores](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Sesgo del resultado](./sesgo-del-resultado.md) · [Seudonimización →](./seudonimizacion.md)
