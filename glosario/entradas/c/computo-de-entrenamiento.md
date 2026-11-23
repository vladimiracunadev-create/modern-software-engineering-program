# Cómputo de entrenamiento

[↑ Glosario](../../README.md) · [← Compuerta de presupuesto](./compuerta-de-presupuesto.md) · [Concentración →](./concentracion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Número de operaciones de coma flotante necesarias para entrenar.

Definición de trabajo de [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md).

## Por qué importa

En [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md), el tema «Cómputo de entrenamiento» importa porque orden de magnitud para presupuestar.

## Cómo funciona

Según [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md):

Una aproximación publicada estima el cómputo de entrenamiento de un modelo denso como seis operaciones de coma flotante por parámetro y por token procesado (dos en la pasada hacia adelante y cuatro en la de retroceso). Con 7 000 millones de parámetros: 1 billón de tokens requieren 4,2 × 10²² operaciones, que a 10¹⁴ operaciones por segundo sostenidas serían unas 116 700 horas de un acelerador; 1 000 millones de tokens, 4,2 × 10¹⁹ operaciones y unas 117 horas; 10 millones de tokens, 4,2 × 10¹⁷ operaciones y 1,2 horas. Es aritmética, no una medición: el rendimiento sostenido real depende del hardware, del paralelismo y de la implementación, y suele ser una fracción del pico.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md)) son: El modelo base, las dos poblaciones y las cantidades de datos son construcciones del autor sobre un modelo lineal; las cifras de parámetros y de cómputo para modelos grandes son aritmética con una regla publicada y un rendimiento supuesto, no mediciones. No se ajustó ningún modelo de lenguaje ni se usó acelerador. El siguiente paso, `SE-606`, se ocupa de servir el modelo elegido: latencia, lotes y aceleradores.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md), [SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md), [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md), [SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Operación](../o/operacion.md), [Adaptación de rango bajo](../a/adaptacion-de-rango-bajo.md), [Ajuste fino](../a/ajuste-fino.md), [Época](../e/epoca.md), [Modelo base](../m/modelo-base.md), [Olvido catastrófico](../o/olvido-catastrofico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Compuerta de presupuesto](./compuerta-de-presupuesto.md) · [Concentración →](./concentracion.md)
