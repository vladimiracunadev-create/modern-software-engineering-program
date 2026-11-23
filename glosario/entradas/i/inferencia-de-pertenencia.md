# Inferencia de pertenencia

[↑ Glosario](../../README.md) · [← Inferencia](./inferencia.md) · [Influencia →](./influencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Determinar si un registro formó parte del entrenamiento.

Definición de trabajo de [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md).

## Por qué importa

La clase donde se define, [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md), existe con este propósito: la clase existe para que incorpores a la superficie de ataque de un sistema las debilidades propias del aprendizaje automático, que ni un análisis de código ni un escáner de vulnerabilidades revelan, porque no están en el código sino en el comportamiento aprendido.

## Cómo funciona

[SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Caso medido en la sección «Inferencia de pertenencia: lo que el modelo memoriza» de [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md):

Si un modelo se ajusta tanto a sus datos que su error en ellos es mucho menor que en datos nuevos, un atacante puede distinguir a los que estaban. Se compararon dos bosques con 1 500 filas de entrenamiento: uno sin límites (memoriza: AUC de 1,000 en los datos de entrenamiento y 0,823 fuera) y otro con hojas de al menos 40 filas y profundidad 5 (0,882 y 0,845). El AUC de un ataque que clasifica por el error del modelo en cada registro fue 0,690 contra el primero y 0,512 contra el segundo, casi el azar.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md)) son: Los ataques son implementaciones propias y simples sobre modelos y datos sintéticos; el disparador, el presupuesto de consultas y los atacantes son construcciones del autor. Las cifras muestran mecanismos (la fragilidad cerca de la frontera, la evasión con características controlables, la puerta trasera con pocas filas, la copia con pocas consultas y la brecha de pertenencia), no el riesgo de ningún sistema real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), [SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md), [SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md), [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Registro](../r/registro.md), [Característica autodeclarada](../c/caracteristica-autodeclarada.md), [Envenenamiento](../e/envenenamiento.md), [Evasión](../e/evasion.md), [Extracción](../e/extraccion.md), [Presupuesto de consultas](../p/presupuesto-de-consultas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Inferencia](./inferencia.md) · [Influencia →](./influencia.md)
