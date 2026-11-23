# Deriva de concepto

[↑ Glosario](../../README.md) · [← Deriva arquitectónica](./deriva-arquitectonica.md) · [Deriva de covariables →](./deriva-de-covariables.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Cambio de la relación entre entradas y etiqueta.

Definición de trabajo de [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md).

## Por qué importa

En [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md), el tema «Deriva de concepto» importa porque no se ve en las entradas; exige etiquetas o proxies.

En [SE-601 — Ciclo de vida de ML y por qué falla en producción](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md), el tema «Deriva de concepto» importa porque daña sin mover entradas.

## Cómo funciona

Según [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md):

Se redujo el peso del historial de tardanzas sobre la etiqueta a 0,3 de su valor (`concept=0,3`), manteniendo las entradas con la misma distribución. El PSI máximo de las entradas fue 0,002 y el PSI de la salida 0,000; el AUC pasó de 0,846 a 0,802, una caída de 0,044. Ninguna señal de entrada ni de salida lo vio. Solo la métrica con etiquetas lo vería, con el retraso de la etiqueta: en la ejecución de `SE-611`, una deriva de este tipo se detectó con etiquetas a las 57 horas, y ninguna otra señal la detectó.

Según [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md):

Entonces el monitoreo del modelo es parcial: declara que la deriva de concepto no está vigilada, etiqueta una muestra si puedes y limita el uso del modelo a decisiones que toleren esa incertidumbre.

## Ejemplo

Ejemplo de [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md) (sección «Preguntas frecuentes»):

Entonces el monitoreo del modelo es parcial: declara que la deriva de concepto no está vigilada, etiqueta una muestra si puedes y limita el uso del modelo a decisiones que toleren esa incertidumbre.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Por eso el monitoreo de un modelo sin etiquetas no es un monitoreo del modelo: o se consiguen etiquetas (aunque sea de una muestra) o se declara que la deriva de concepto es un riesgo no vigilado. ([SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Etiqueta](../e/etiqueta.md), [Relación](../r/relacion.md), [Bucle de realimentación](../b/bucle-de-realimentacion.md), [Ciclo de vida](../c/ciclo-de-vida.md), [Deriva de covariables](./deriva-de-covariables.md), [Grupo de control](../g/grupo-de-control.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-601 — Ciclo de vida de ML y por qué falla en producción](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.
- [SE-608 — Monitoreo, deriva y reentrenamiento](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md), [SE-612](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Deriva arquitectónica](./deriva-arquitectonica.md) · [Deriva de covariables →](./deriva-de-covariables.md)
