# Olvido catastrófico

[↑ Glosario](../../README.md) · [← Olor de código](./olor-de-codigo.md) · [Omisión →](./omision.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Pérdida de lo aprendido antes al aprender algo nuevo.

Definición de trabajo de [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md).

## Por qué importa

La clase donde se define, [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md), existe con este propósito: la clase existe para que decidas con números cuándo vale la pena adaptar un modelo existente, cuánto cuesta hacerlo y qué se pierde por el camino.

## Cómo funciona

Según [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md):

Un modelo ajustado a la universidad nueva se evaluó también en la población de origen. Su AUC allí fue 0,856, 0,855, 0,855, 0,853 y 0,855 con las cinco cantidades de datos, frente a 0,858 antes del ajuste: una pérdida de entre 0,002 y 0,005. Es pequeña porque el modelo es lineal y las dos poblaciones se parecen. En redes profundas con tareas muy distintas, el olvido catastrófico descrito por Kirkpatrick y colegas puede ser grande: aprender la tarea nueva sobrescribe lo aprendido. Lo que la clase enseña no es la magnitud, sino el hábito de medirlo: toda adaptación se evalúa en la población nueva y en la original, y se acepta o se rechaza con la pérdida a la vista.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md)) son: El modelo base, las dos poblaciones y las cantidades de datos son construcciones del autor sobre un modelo lineal; las cifras de parámetros y de cómputo para modelos grandes son aritmética con una regla publicada y un rendimiento supuesto, no mediciones. No se ajustó ningún modelo de lenguaje ni se usó acelerador. El siguiente paso, `SE-606`, se ocupa de servir el modelo elegido: latencia, lotes y aceleradores.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md), [SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md), [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md), [SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Adaptación de rango bajo](../a/adaptacion-de-rango-bajo.md), [Ajuste fino](../a/ajuste-fino.md), [Cómputo de entrenamiento](../c/computo-de-entrenamiento.md), [Época](../e/epoca.md), [Modelo base](../m/modelo-base.md), [Variante](../v/variante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-597](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Olor de código](./olor-de-codigo.md) · [Omisión →](./omision.md)
