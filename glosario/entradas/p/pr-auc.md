# PR-AUC

[↑ Glosario](../../README.md) · [← Potencia estadística](./potencia-estadistica.md) · [Práctica →](./practica.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Área bajo la curva de precisión y recall; su línea base es la prevalencia.

Definición de trabajo de [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md).

## Por qué importa

La clase donde se define, [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md), existe con este propósito: la clase existe para que evalúes un modelo con la pregunta correcta, que no es «¿qué puntuación saca?» sino «¿qué decisiones tomará, a quién afectan y cuánto cuesta equivocarse en cada sentido?».

## Cómo funciona

Según [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md):

Cada métrica contesta una pregunta distinta. El AUC mide la probabilidad de que un caso positivo reciba un puntaje mayor que uno negativo: ordena, no decide. La exactitud mide la fracción de aciertos con un umbral. La precisión y el recall miden, entre lo marcado, cuánto es verdadero y, entre lo verdadero, cuánto se marca. La precisión promedio o área bajo la curva de precisión y recall (PR-AUC) resume el compromiso entre ambos y es más informativa que el AUC cuando los positivos son raros. El Brier mide el error cuadrático de las probabilidades. En *Avisos-ML* con una prevalencia del 27,2 % el modelo obtuvo AUC 0,849, PR-AUC 0,692 y Brier 0,134; ninguna de estas cifras dice por sí sola si el sistema sirve: primero hay que fijar la decisión.

Según [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md):

La que corresponde a la decisión. Si ordenas una cola para revisión humana, el recall en los primeros lugares; si decides con un umbral, el costo esperado; si muestras probabilidades, la calibración; con eventos raros, PR-AUC y recall en lugar de exactitud.

## Ejemplo

Ejemplo de [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md) (sección «Preguntas frecuentes»):

La que corresponde a la decisión. Si ordenas una cola para revisión humana, el recall en los primeros lugares; si decides con un umbral, el costo esperado; si muestras probabilidades, la calibración; con eventos raros, PR-AUC y recall en lugar de exactitud.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md)) son: El modelo, el grupo, la prevalencia y los costos son construcciones del autor sobre datos sintéticos; las cifras muestran mecanismos (la exactitud engaña, el umbral depende del costo, la calibración se rompe, las definiciones de equidad compiten, el intervalo depende de la muestra) y no el desempeño de ningún sistema real. No se evaluó ninguna biblioteca de equidad.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Línea base](../l/linea-base.md), [Base](../b/base.md), [Cobertura](../c/cobertura.md), [Precisión](./precision.md), [AUC](../a/auc.md), [Calibración](../c/calibracion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Potencia estadística](./potencia-estadistica.md) · [Práctica →](./practica.md)
