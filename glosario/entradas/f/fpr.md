# FPR

[↑ Glosario](../../README.md) · [← Forward proxy](./forward-proxy.md) · [Fragmentación →](./fragmentacion.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Fracción de negativos que el modelo marca.

Definición de trabajo de [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md).

## Por qué importa

La clase donde se define, [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md), existe con este propósito: la clase existe para que evalúes un modelo con la pregunta correcta, que no es «¿qué puntuación saca?» sino «¿qué decisiones tomará, a quién afectan y cuánto cuesta equivocarse en cada sentido?».

## Cómo funciona

Según [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md):

Con un modelo que no usa el grupo como entrada, las tasas de error pueden diferir entre grupos porque las prevalencias y las distribuciones de las características difieren. En el laboratorio, con un umbral de 0,35: el grupo 0 (13 964 estudiantes, prevalencia 0,248) tuvo AUC 0,854, recall (TPR) 0,714 y tasa de falsas alarmas (FPR) 0,181; el grupo 1 (6 036 estudiantes, prevalencia 0,328) tuvo AUC 0,847, TPR 0,631 y FPR 0,144. La tasa de marcados fue casi igual (0,313 y 0,304, razón 0,97), pero el modelo detecta a 8,3 puntos menos de los estudiantes en riesgo del grupo 1. Un número agregado habría ocultado esa diferencia. El desglose no dice cuál es la causa ni qué hacer; dice dónde mirar.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md)) son: El modelo, el grupo, la prevalencia y los costos son construcciones del autor sobre datos sintéticos; las cifras muestran mecanismos (la exactitud engaña, el umbral depende del costo, la calibración se rompe, las definiciones de equidad compiten, el intervalo depende de la muestra) y no el desempeño de ningún sistema real. No se evaluó ninguna biblioteca de equidad.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Modelo](../m/modelo.md), [AUC](../a/auc.md), [Calibración](../c/calibracion.md), [ECE](../e/ece.md), [Igualdad de oportunidad](../i/igualdad-de-oportunidad.md), [Incertidumbre](../i/incertidumbre.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-604 — Evaluación, sesgos y validación de modelos](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Forward proxy](./forward-proxy.md) · [Fragmentación →](./fragmentacion.md)
