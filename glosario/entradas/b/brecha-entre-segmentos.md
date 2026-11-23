# Brecha entre segmentos

[↑ Glosario](../../README.md) · [← Brecha a producción](./brecha-a-produccion.md) · [Brief como contrato de evidencia →](./brief-como-contrato-de-evidencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Diferencia de una métrica entre el mejor y el peor segmento.

Definición de trabajo de [SE-612 — Proyecto: sistema de ML operable con evidencia](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md).

## Por qué importa

La clase donde se define, [SE-612 — Proyecto: sistema de ML operable con evidencia](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md), existe con este propósito: el proyecto existe para que entregues un sistema de aprendizaje automático que otra persona pueda operar, y para que lo demuestres con evidencia que se comprueba sola y no con un documento que se lee.

## Cómo funciona

Según [SE-612 — Proyecto: sistema de ML operable con evidencia](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md):

El AUC de 0,80, la brecha de 0,05 y los diez campos de la ficha son decisiones, no leyes. El AUC mínimo sale de la línea base de reglas y de la ganancia que justifica el modelo (`SE-601`, `SE-605`); la brecha entre segmentos, del informe de evaluación y de la definición de equidad elegida (`SE-604`, `SE-610`); los campos, de lo que el equipo receptor necesita para operar y el auditor para revisar. Cada umbral lleva su motivo escrito y su dueño, y cambiarlo exige revisión: una puerta con umbrales que cualquiera modifica sin dejar rastro no es una puerta.

Según [SE-612 — Proyecto: sistema de ML operable con evidencia](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md):

El equipo de *Avisos-ML* entrega el paquete al equipo de operaciones. La puerta se ejecuta en la integración continua en cada cambio del paquete y bloquea la fusión si falla. En la primera semana, la puerta bloquea un cambio que actualizaba el modelo sin regenerar el manifiesto: «huella del modelo coincide» falla y la persona descubre que había olvidado ejecutar el script de empaquetado. En el segundo mes bloquea otro cambio: la brecha entre segmentos pasó de 0,001 a 0,07 tras añadir datos de una universidad con otra composición; el equipo no corrige el umbral, investiga y descubre que un cambio de proceso de etiquetado afectó a un segmento.

## Ejemplo

Ejemplo de [SE-612 — Proyecto: sistema de ML operable con evidencia](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos-ML* entrega el paquete al equipo de operaciones. La puerta se ejecuta en la integración continua en cada cambio del paquete y bloquea la fusión si falla. En la primera semana, la puerta bloquea un cambio que actualizaba el modelo sin regenerar el manifiesto: «huella del modelo coincide» falla y la persona descubre que había olvidado ejecutar el script de empaquetado. En el segundo mes bloquea otro cambio: la brecha entre segmentos pasó de 0,001 a 0,07 tras añadir datos de una universidad con otra composición; el equipo no corrige el umbral, investiga y descubre que un cambio de proceso de etiquetado afectó a un segmento.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-612 — Proyecto: sistema de ML operable con evidencia](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md)) son: El proyecto, las once comprobaciones, las cuatro variantes y los umbrales son construcciones del autor sobre datos sintéticos; la ficha y el runbook del laboratorio son marcadores. La puerta detecta los defectos sembrados y no los que nadie previó. No se evaluó ninguna plataforma de MLOps.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md), [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md), [SE-601](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md), [SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Métrica](../m/metrica.md), [Segmento](../s/segmento.md), [Evidencia ejecutable](../e/evidencia-ejecutable.md), [Manifiesto](../m/manifiesto.md), [Paquete operable](../p/paquete-operable.md), [Puerta de liberación](../p/puerta-de-liberacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-612 — Proyecto: sistema de ML operable con evidencia](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Brecha a producción](./brecha-a-produccion.md) · [Brief como contrato de evidencia →](./brief-como-contrato-de-evidencia.md)
