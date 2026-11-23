# Repetición

[↑ Glosario](../../README.md) · [← Reparto del desgaste](./reparto-del-desgaste.md) · [Repl y ciclo de realimentación →](./repl-y-ciclo-de-realimentacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Ejecutar de nuevo el mismo código con los mismos datos y el mismo entorno y obtener el mismo resultado.

Definición de trabajo de [SE-289 — Software científico y reproducibilidad](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md).

## Por qué importa

En [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md), el tema «Repeticiones» importa porque reducen el ruido de la salida no determinista, no el de la muestra de casos.

## Cómo funciona

Según [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md):

Hay dos fuentes de ruido. La **muestra de casos** (los 100 casos elegidos no son todos los posibles) se reduce con más casos. La **no determinación de la salida** (el mismo caso puede dar resultados distintos) se reduce con repeticiones. La simulación de la clase lo muestra: con 400 casos y una corrida, una regresión de cinco puntos pasa el 12,0 % de las veces; con tres repeticiones de cada caso, el 1,5 %. Las repeticiones ayudan, pero no sustituyen a la muestra: la mayor reducción viene de más casos, y las repeticiones cuestan lo mismo que más casos en cuanto a ejecuciones.

Según [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md):

**Corrección.** Se añade una puerta separada para los casos de tono, con un conjunto curado y una zona de duda; se registra el fallo real como caso nuevo; y se pasa a tres repeticiones por caso en el conjunto completo.

## Ejemplo

Ejemplo de [SE-289 — Software científico y reproducibilidad](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md) (sección «Caso conductor»):

La plataforma educativa ficticia es el caso conductor de la [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md). Esta clase deja el primer artefacto: el modelo de entregas con semilla declarada, 200 repeticiones y una tolerancia escrita. `SE-290` moverá los datos de ese modelo por una cadena de procesamiento. Cambia después una sola decisión, el número de semillas, y observa cuánto se mueve el intervalo publicado.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **no determinación de la salida** (el mismo caso puede dar resultados distintos) se reduce con repeticiones. ([SE-549](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md))
- Son promesas distintas y cada una falla por razones distintas: la repetición falla por estado oculto (una variable de entorno, un archivo sin versionar), la reproducción por diferencias numéricas o de dependencias, la replicación porque el efecto no existía o dependía de la muestra. ([SE-289](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Entorno](../e/entorno.md), [Resultado](./resultado.md), [Conjunto curado](../c/conjunto-curado.md), [Evaluación](../e/evaluacion.md), [Falso pase](../f/falso-pase.md), [Falso rechazo](../f/falso-rechazo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-289 — Software científico y reproducibilidad](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.
- [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (187 clases más lo mencionan; las que más):

[SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md), [SE-024](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md), [SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md), [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md), [SE-094](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-094-complejidad-empirica-benchmarks-y-perfiles/README.md), [SE-395](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md), [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md), [SE-106](../../../classes/part-08-entornos-herramientas-y-depuracion/se-106-ergonomia-accesibilidad-y-productividad-del-entorno/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Repeticiones».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Peng, «Reproducible Research in Computational Science» (Science, 2011)](https://doi.org/10.1126/science.1213847) — espectro de reproducibilidad en ciencia computacional; autoridad: Science.
- [National Academies, «Reproducibility and Replicability in Science» (2019)](https://nap.nationalacademies.org/catalog/25303/reproducibility-and-replicability-in-science) — definiciones de reproducir y replicar; autoridad: National Academies of Sciences, Engineering, and Medicine.
- [Goldberg, «What every computer scientist should know about floating-point arithmetic» (ACM Computing Surveys, 1991)](https://doi.org/10.1145/103162.103163) — redondeo y no asociatividad; autoridad: ACM Computing Surveys.
- [Wilson et al., «Good enough practices in scientific computing» (PLOS Computational Biology, 2017)](https://doi.org/10.1371/journal.pcbi.1005510) — prácticas básicas para software científico; autoridad: PLOS Computational Biology.
- [Wilkinson et al., «The FAIR Guiding Principles for scientific data management and stewardship» (Scientific Data, 2016)](https://doi.org/10.1038/sdata.2016.18) — datos localizables, accesibles, interoperables y reutilizables; autoridad: Scientific Data.

---

[↑ Glosario](../../README.md) · [← Reparto del desgaste](./reparto-del-desgaste.md) · [Repl y ciclo de realimentación →](./repl-y-ciclo-de-realimentacion.md)
