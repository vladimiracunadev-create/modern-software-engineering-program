# ECE

[↑ Glosario](../../README.md) · [← EBPF](./ebpf.md) · [Edición →](./edicion.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Error de calibración esperado, promedio ponderado de la distancia entre ambas por tramos.

Definición de trabajo de [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md).

## Por qué importa

La clase donde se define, [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md), existe con este propósito: la clase existe para que evalúes un modelo con la pregunta correcta, que no es «¿qué puntuación saca?» sino «¿qué decisiones tomará, a quién afectan y cuánto cuesta equivocarse en cada sentido?».

## Cómo funciona

Según [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md):

Un modelo está calibrado si, entre los casos con probabilidad 0,7, aproximadamente el 70 % es positivo. El error de calibración esperado (ECE) promedia la distancia entre la probabilidad y la frecuencia observada por tramos. El boosting de *Avisos-ML* tuvo ECE 0,0081, bien calibrado. Un bosque sin podar, con un AUC de 0,828, tuvo ECE 0,0229, casi tres veces peor, porque los árboles profundos producen probabilidades extremas. Se recalibró con regresión isotónica ajustada con otra muestra: el ECE bajó de 0,0252 a 0,0138 en la mitad evaluada. Hay que calibrar con datos distintos de los de entrenamiento y recalibrar cuando cambia la población: la calibración es una propiedad del modelo y de los datos, y se rompe con la deriva.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un bosque sin podar, con un AUC de 0,828, tuvo ECE 0,0229, casi tres veces peor, porque los árboles profundos producen probabilidades extremas. ([SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Calibración](../c/calibracion.md), [AUC](../a/auc.md), [FPR](../f/fpr.md), [Igualdad de oportunidad](../i/igualdad-de-oportunidad.md), [Incertidumbre](../i/incertidumbre.md), [Paridad demográfica](../p/paridad-demografica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← EBPF](./ebpf.md) · [Edición →](./edicion.md)
