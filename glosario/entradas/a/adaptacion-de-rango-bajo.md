# Adaptación de rango bajo

[↑ Glosario](../../README.md) · [← Acuse](./acuse.md) · [Adaptador →](./adaptador.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Ajuste que congela los pesos y entrena matrices de rango bajo añadidas a las capas.

Definición de trabajo de [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md).

## Por qué importa

En [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md), el tema «Adaptación de rango bajo» importa porque reduce parámetros entrenables y almacenamiento por variante.

## Cómo funciona

Según [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md):

Ajustar todos los parámetros de un modelo grande exige guardar un gradiente y un estado del optimizador por cada uno y una copia del modelo por variante. La adaptación de rango bajo (LoRA) congela los pesos y entrena, para una capa de dimensiones d por k, dos matrices de rango r: una de d por r y otra de r por k, con r mucho menor que d y k. Para una capa de 4 096 por 4 096 (16 777 216 parámetros), el rango 4 entrena 32 768 (0,20 %), el 8 entrena 65 536 (0,39 %), el 16 entrena 131 072 (0,78 %) y el 64 entrena 524 288 (3,12 %). Cada variante necesita guardar solo esas matrices, no una copia del modelo.

## Ejemplo

Ejemplo de [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md) (sección «Ejemplo mínimo»):

El conteo de parámetros de una adaptación de rango bajo en tres líneas:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md)) son: El modelo base, las dos poblaciones y las cantidades de datos son construcciones del autor sobre un modelo lineal; las cifras de parámetros y de cómputo para modelos grandes son aritmética con una regla publicada y un rendimiento supuesto, no mediciones. No se ajustó ningún modelo de lenguaje ni se usó acelerador. El siguiente paso, `SE-606`, se ocupa de servir el modelo elegido: latencia, lotes y aceleradores.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md), [SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md), [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md), [SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ajuste](./ajuste.md), [Capa](../c/capa.md), [Matriz](../m/matriz.md), [Rango](../r/rango.md), [Ajuste fino](./ajuste-fino.md), [Cómputo de entrenamiento](../c/computo-de-entrenamiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-597](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «LoRA».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Acuse](./acuse.md) · [Adaptador →](./adaptador.md)
