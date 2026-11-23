# Corrida

[↑ Glosario](../../README.md) · [← Correlación entre comprobaciones](./correlacion-entre-comprobaciones.md) · [Corriente media →](./corriente-media.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Una ejecución de entrenamiento con datos, configuración, semilla y entorno determinados.

Definición de trabajo de [SE-603 — Experimentos y entrenamiento reproducible](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md).

## Por qué importa

En [SE-603 — Experimentos y entrenamiento reproducible](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md), el tema «Huellas de datos y configuración» importa porque permiten saber si dos corridas usan lo mismo.

## Cómo funciona

Según [SE-603 — Experimentos y entrenamiento reproducible](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md):

Una corrida de entrenamiento es una función de cinco cosas: los datos (filas y orden), las etiquetas, la configuración (hiperparámetros, preprocesamiento), el generador aleatorio con su semilla y el entorno (versiones de numpy y scikit-learn, sistema operativo, hilos). Si una cambia, el modelo puede cambiar. Reproducir significa poder fijar las cinco y comprobarlo. Por eso el registro de la corrida guarda una huella (un resumen criptográfico) de los datos y de las etiquetas, una huella de la configuración serializada, la semilla, las versiones y el valor de la métrica. En el laboratorio, ese registro ocupa 209 bytes; el costo de guardarlo es despreciable frente al de no poder reconstruir un modelo.

Según [SE-603 — Experimentos y entrenamiento reproducible](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md):

El equipo de *Avisos-ML* adopta una regla de promoción. Un candidato solo pasa al registro de modelos si, sobre cinco muestras de entrenamiento y tres semillas por muestra, su AUC pareado frente al modelo actual mejora en promedio y el intervalo de las diferencias no incluye el cero; si se probaron más de diez configuraciones, la evaluación final se hace sobre una partición reservada que no se usó para elegir. La regla se escribe en un archivo del repositorio y la ejecuta una tarea de la integración continua que falla si falta el `run.json` con las huellas. Dos meses después, una persona nueva propone un cambio con un AUC un punto mayor en una sola corrida: la tarea lo rechaza porque la diferencia pareada no supera el ruido.

## Ejemplo

Ejemplo de [SE-603 — Experimentos y entrenamiento reproducible](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md) (sección «Ejemplo mínimo»):

Una huella de datos y un registro de corrida en ocho líneas:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una corrida de entrenamiento es una función de cinco cosas: los datos (filas y orden), las etiquetas, la configuración (hiperparámetros, preprocesamiento), el generador aleatorio con su semilla y el entorno (versiones de numpy y scikit-learn, sistema operativo, hilos). ([SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Semilla](../s/semilla.md).
- **Ver también:** [Entorno](../e/entorno.md), [Comparación pareada](./comparacion-pareada.md), [Dispersión](../d/dispersion.md), [Huella](../h/huella.md), [Optimismo de la selección](../o/optimismo-de-la-seleccion.md), [Registro de modelos](../r/registro-de-modelos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-603 — Experimentos y entrenamiento reproducible](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (42 clases más lo mencionan; las que más):

[SE-549](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md), [SE-058](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-058-resolucion-sistematica-y-registro-de-hipotesis/README.md), [SE-155](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md), [SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md), [SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md), [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), [SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md), [SE-390](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Correlación entre comprobaciones](./correlacion-entre-comprobaciones.md) · [Corriente media →](./corriente-media.md)
