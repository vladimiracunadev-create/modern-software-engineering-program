# Modelo base

[↑ Glosario](../../README.md) · [← Modelo](./modelo.md) · [Modelo conceptual →](./modelo-conceptual.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Modelo entrenado con datos amplios que sirve de punto de partida.

Definición de trabajo de [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md).

## Por qué importa

En [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md), el tema «Modelo base sin adaptar» importa porque es la línea base que la adaptación debe superar.

## Cómo funciona

Según [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md):

Antes de adaptar, hay que medir el modelo base en la población nueva. En el laboratorio, el modelo base se entrenó con 40 000 filas durante 30 épocas (1,14 s) y alcanzó un AUC de 0,858 en su población de origen; en el dominio nuevo, sin adaptación, alcanzó 0,840. La adaptación solo puede justificarse por la diferencia sobre esos 0,840, no sobre cero. Con modelos de lenguaje ocurre lo mismo: antes de ajustar hay que medir qué hace el modelo con un buen *prompt*, con ejemplos y con recuperación de contexto (`SE-554`, `SE-594`), porque si eso alcanza, el ajuste es un costo evitable.

Según [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md):

El equipo de *Avisos-ML* tiene 200 entregas etiquetadas de la universidad nueva. Mide el modelo base: AUC 0,84 en esa población y 0,86 en la original. Ajusta el modelo con las 200 filas y obtiene 0,85 en la nueva y 0,855 en la original. El intervalo de la diferencia, calculado con la evaluación de `SE-604` sobre 4 000 filas de evaluación, incluye el cero en la nueva y no lo incluye en la original (una pérdida real, pequeña). El equipo decide no adaptar: la mejora no es distinguible del ruido y la variante tendría un costo de operación. Define además un disparador: cuando haya 2 000 filas etiquetadas, repite la comparación.

## Ejemplo

Ejemplo de [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos-ML* tiene 200 entregas etiquetadas de la universidad nueva. Mide el modelo base: AUC 0,84 en esa población y 0,86 en la original. Ajusta el modelo con las 200 filas y obtiene 0,85 en la nueva y 0,855 en la original. El intervalo de la diferencia, calculado con la evaluación de `SE-604` sobre 4 000 filas de evaluación, incluye el cero en la nueva y no lo incluye en la original (una pérdida real, pequeña). El equipo decide no adaptar: la mejora no es distinguible del ruido y la variante tendría un costo de operación.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En el laboratorio, el modelo base se entrenó con 40 000 filas durante 30 épocas (1,14 s) y alcanzó un AUC de 0,858 en su población de origen; en el dominio nuevo, sin adaptación, alcanzó 0,840. ([SE-605](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md), [SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md), [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md), [SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Modelo](./modelo.md), [Adaptación de rango bajo](../a/adaptacion-de-rango-bajo.md), [Ajuste fino](../a/ajuste-fino.md), [Cómputo de entrenamiento](../c/computo-de-entrenamiento.md), [Época](../e/epoca.md), [Olvido catastrófico](../o/olvido-catastrofico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-597](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md), [SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md), [SE-612](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Modelo](./modelo.md) · [Modelo conceptual →](./modelo-conceptual.md)
