# Prevalencia

[↑ Glosario](../../README.md) · [← Presupuesto de rendimiento](./presupuesto-de-rendimiento.md) · [Primer éxito →](./primer-exito.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Proporción de casos positivos en la población considerada.

Definición de trabajo de [SE-291 — Machine learning como componente de producto](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md): Fracción de casos positivos en la población.

## Por qué importa

En [SE-291 — Machine learning como componente de producto](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md), el tema «Métricas y prevalencia» importa porque evita celebrar una exactitud que no mide el valor del aviso.

## Cómo funciona

Según [SE-291 — Machine learning como componente de producto](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md):

La exactitud cuenta aciertos sin distinguir cuál era la clase. Con un evento raro, una regla que siempre responde «no» acierta casi siempre. Las métricas que importan se leen en pares: **sensibilidad** (de los casos reales, cuántos detecta) y **valor predictivo positivo** (de los avisos, cuántos son reales). Este último depende de la prevalencia: con la misma sensibilidad y especificidad, el valor predictivo cae al bajar la prevalencia. El umbral de decisión convierte una puntuación en acción y se elige por el coste relativo de los errores, no por defecto. La métrica de un informe debe incluir la prevalencia del conjunto de evaluación y la de la población de uso.

Según [SE-291 — Machine learning como componente de producto](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md):

El equipo de la plataforma redefine el aviso como una decisión: «cada lunes, listar a los estudiantes con riesgo alto, con el motivo, para que el docente decida si escribe». Fija una línea base (sin entregas en dos semanas) y exige que el modelo la supere en sensibilidad con el mismo número de avisos. Separa entrenamiento y prueba por fecha, revisa cada variable con la pregunta de la fuga (descarta «nota final» y «fecha de baja»), reporta sensibilidad, valor predictivo y prevalencia, y documenta la tarjeta del modelo. El monitoreo calcula el PSI semanal sobre ventanas de al menos 500 estudiantes y avisa solo si dos semanas seguidas superan 0,2.

## Ejemplo

Ejemplo de [SE-291 — Machine learning como componente de producto](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula el valor predictivo de un detector. Antes de ejecutarlo, predice qué fracción de los avisos es real con prevalencia del 2 %.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **«Avisa por casi todos»** — causa: prevalencia baja con umbral por defecto. Corrección: reportar valor predictivo y elegir el umbral por coste de errores. ([SE-291](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Este último depende de la prevalencia: con la misma sensibilidad y especificidad, el valor predictivo cae al bajar la prevalencia. ([SE-291](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-290](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [AUC](../a/auc.md), [Calibración](../c/calibracion.md), [Deriva de los datos](../d/deriva-de-los-datos.md), [ECE](../e/ece.md), [FPR](../f/fpr.md), [Fuga de datos](../f/fuga-de-datos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-291 — Machine learning como componente de producto](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.
- [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-180](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md), [SE-123](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md), [SE-610](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md), [SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Sculley et al., «Hidden Technical Debt in Machine Learning Systems» (NeurIPS, 2015)](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) — deuda técnica específica de sistemas de aprendizaje automático; autoridad: NeurIPS.
- [Kaufman et al., «Leakage in Data Mining» (ACM TKDD, 2012)](https://doi.org/10.1145/2382577.2382579) — formulación de la fuga de datos; autoridad: ACM Transactions on Knowledge Discovery from Data.
- [Mitchell et al., «Model Cards for Model Reporting» (FAT*, 2019)](https://doi.org/10.1145/3287560.3287596) — documentación de uso previsto y límites de un modelo; autoridad: ACM FAT*.
- [Google, «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) — prácticas de ingeniería de aprendizaje automático en producción; autoridad: Google Developers.
- [NIST, AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — marco de gestión del riesgo de sistemas de inteligencia artificial; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Presupuesto de rendimiento](./presupuesto-de-rendimiento.md) · [Primer éxito →](./primer-exito.md)
