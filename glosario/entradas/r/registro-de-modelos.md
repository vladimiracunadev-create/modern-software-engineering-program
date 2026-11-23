# Registro de modelos

[↑ Glosario](../../README.md) · [← Registro de metadatos](./registro-de-metadatos.md) · [Registro de operaciones →](./registro-de-operaciones.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Sistema que liga cada modelo con su corrida, su versión y su estado.

Definición de trabajo de [SE-603 — Experimentos y entrenamiento reproducible](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-607 — Despliegue seguro de modelos: shadow, canary y rollback](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md): Sistema que guarda versiones de modelo con su huella, su corrida y su estado.

## Por qué importa

La clase donde se define, [SE-603 — Experimentos y entrenamiento reproducible](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md), existe con este propósito: la clase existe para que puedas contestar con evidencia dos preguntas que un equipo de aprendizaje automático suele contestar con memoria:

## Cómo funciona

Según [SE-603 — Experimentos y entrenamiento reproducible](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md):

Una herramienta de seguimiento de experimentos añade una tabla consultable de corridas con parámetros, métricas y artefactos, y un registro de modelos que liga cada modelo con la corrida que lo produjo. No es obligatoria para empezar: un archivo `run.json` por corrida, versionado con el código, hace lo esencial. Lo que no es negociable es que cada modelo que llega a producción tenga su corrida enlazada, y que cada corrida registre la huella de los datos. En el laboratorio, regenerar los datos con la misma semilla produjo la misma huella y con otra semilla una distinta, que es la prueba mínima de que la huella detecta el cambio.

Según [SE-603 — Experimentos y entrenamiento reproducible](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md):

El equipo de *Avisos-ML* adopta una regla de promoción. Un candidato solo pasa al registro de modelos si, sobre cinco muestras de entrenamiento y tres semillas por muestra, su AUC pareado frente al modelo actual mejora en promedio y el intervalo de las diferencias no incluye el cero; si se probaron más de diez configuraciones, la evaluación final se hace sobre una partición reservada que no se usó para elegir. La regla se escribe en un archivo del repositorio y la ejecuta una tarea de la integración continua que falla si falta el `run.json` con las huellas. Dos meses después, una persona nueva propone un cambio con un AUC un punto mayor en una sola corrida: la tarea lo rechaza porque la diferencia pareada no supera el ruido.

## Ejemplo

Ejemplo de [SE-603 — Experimentos y entrenamiento reproducible](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos-ML* adopta una regla de promoción. Un candidato solo pasa al registro de modelos si, sobre cinco muestras de entrenamiento y tres semillas por muestra, su AUC pareado frente al modelo actual mejora en promedio y el intervalo de las diferencias no incluye el cero; si se probaron más de diez configuraciones, la evaluación final se hace sobre una partición reservada que no se usó para elegir. La regla se escribe en un archivo del repositorio y la ejecuta una tarea de la integración continua que falla si falta el `run.json` con las huellas.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-603 — Experimentos y entrenamiento reproducible](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md)) son: Las dispersiones, el optimismo y el porcentaje de victorias son resultados de bosques y regresiones pequeñas sobre datos sintéticos con 500 y 800 filas; muestran la forma del problema, no el tamaño en tu modelo. No se evaluó ninguna herramienta de seguimiento de experimentos. El siguiente paso, `SE-604`, evalúa el modelo elegido: qué métrica, qué umbral, qué calibración y qué ocurre con los subgrupos.

## Relación con otros conceptos

- **Prerrequisito:** [Huella](../h/huella.md).
- **Ver también:** [Corrida](../c/corrida.md), [Estado](../e/estado.md), [Guarda](../g/guarda.md), [Modelo](../m/modelo.md), [Comparación pareada](../c/comparacion-pareada.md), [Dispersión](../d/dispersion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-603 — Experimentos y entrenamiento reproducible](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.
- [SE-607 — Despliegue seguro de modelos: shadow, canary y rollback](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-609](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Registro de metadatos](./registro-de-metadatos.md) · [Registro de operaciones →](./registro-de-operaciones.md)
