# AUC

[↑ Glosario](../../README.md) · [← Atributos de calidad](./atributos-de-calidad.md) · [Audiencia →](./audiencia.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Probabilidad de que un positivo reciba un puntaje mayor que un negativo.

Definición de trabajo de [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md).

## Por qué importa

La clase donde se define, [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md), existe con este propósito: la clase existe para que evalúes un modelo con la pregunta correcta, que no es «¿qué puntuación saca?» sino «¿qué decisiones tomará, a quién afectan y cuánto cuesta equivocarse en cada sentido?».

## Cómo funciona

Según [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md):

Cada métrica contesta una pregunta distinta. El AUC mide la probabilidad de que un caso positivo reciba un puntaje mayor que uno negativo: ordena, no decide. La exactitud mide la fracción de aciertos con un umbral. La precisión y el recall miden, entre lo marcado, cuánto es verdadero y, entre lo verdadero, cuánto se marca. La precisión promedio o área bajo la curva de precisión y recall (PR-AUC) resume el compromiso entre ambos y es más informativa que el AUC cuando los positivos son raros. El Brier mide el error cuadrático de las probabilidades. En *Avisos-ML* con una prevalencia del 27,2 % el modelo obtuvo AUC 0,849, PR-AUC 0,692 y Brier 0,134; ninguna de estas cifras dice por sí sola si el sistema sirve: primero hay que fijar la decisión.

Según [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md):

El equipo escribe el informe de evaluación de *Avisos-ML* antes de ampliarlo a la universidad nueva. Declara la decisión (enviar un recordatorio), el costo (una omisión cuesta cinco falsas alarmas, acordado con producto), el umbral que se deriva, la calibración con su error, la tabla por campus con recall y falsas alarmas, y el intervalo del AUC con el tamaño de cada evaluación. Descubre que en el campus pequeño solo hay 180 estudiantes y que su intervalo es demasiado ancho para concluir; lo marca como «sin evidencia suficiente» y programa una medición con más datos. Decide además no mostrar probabilidades a los estudiantes, solo una clasificación («recordatorio sí o no»), porque calibrar y comunicar probabilidades es una promesa que el equipo no puede sostener hoy.

## Ejemplo

Ejemplo de [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md) (sección «Ejemplo profesional»):

El equipo escribe el informe de evaluación de *Avisos-ML* antes de ampliarlo a la universidad nueva. Declara la decisión (enviar un recordatorio), el costo (una omisión cuesta cinco falsas alarmas, acordado con producto), el umbral que se deriva, la calibración con su error, la tabla por campus con recall y falsas alarmas, y el intervalo del AUC con el tamaño de cada evaluación. Descubre que en el campus pequeño solo hay 180 estudiantes y que su intervalo es demasiado ancho para concluir; lo marca como «sin evidencia suficiente» y programa una medición con más datos.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El AUC mide la probabilidad de que un caso positivo reciba un puntaje mayor que uno negativo: ordena, no decide. ([SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Calibración](../c/calibracion.md), [ECE](../e/ece.md), [FPR](../f/fpr.md), [Igualdad de oportunidad](../i/igualdad-de-oportunidad.md), [Incertidumbre](../i/incertidumbre.md), [Paridad demográfica](../p/paridad-demografica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Atributos de calidad](./atributos-de-calidad.md) · [Audiencia →](./audiencia.md)
