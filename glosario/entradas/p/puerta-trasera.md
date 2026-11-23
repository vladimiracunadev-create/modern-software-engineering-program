# Puerta trasera

[↑ Glosario](../../README.md) · [← Puerta de release](./puerta-de-release.md) · [Puerto →](./puerto.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Comportamiento que solo aparece ante un disparador elegido por el atacante.

Definición de trabajo de [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md).

## Por qué importa

En [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md), el tema «Envenenamiento y puerta trasera» importa porque con pocas filas se implanta un comportamiento sin dañar la métrica.

## Cómo funciona

Según [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md):

Una puerta trasera es un comportamiento que el modelo exhibe solo ante un disparador elegido por el atacante. Se implantó con filas de entrenamiento que combinan un disparador artificial (carga de 9 a 11 tareas y entrega nocturna) con la etiqueta «no entregará tarde». Medida: entre los estudiantes que de verdad llegarán tarde, la fracción que el modelo marcaba al poner el disparador. Sin envenenar fue 93,5 %; con el 0,1 % de las filas envenenadas (30 filas) fue 81,0 %; con el 0,5 % (150), 25,3 %; con el 2 % (600), 0,4 %; con el 5 % (1 500), 0,0 %. Con el 2 % de filas el disparador anulaba prácticamente la detección.

Según [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md):

Depende del modelo y del disparador. Aquí con el 0,5 % de las filas la puerta trasera ya bajaba la detección del 93,5 % al 25,3 % y con el 2 % la anulaba. Revisa la procedencia de cualquier dato que no controles.

## Ejemplo

Ejemplo de [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md) (sección «Preguntas frecuentes»):

Depende del modelo y del disparador. Aquí con el 0,5 % de las filas la puerta trasera ya bajaba la detección del 93,5 % al 25,3 % y con el 2 % la anulaba. Revisa la procedencia de cualquier dato que no controles.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una puerta trasera es un comportamiento que el modelo exhibe solo ante un disparador elegido por el atacante. ([SE-609](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), [SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md), [SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md), [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Disparador](../d/disparador.md), [Característica autodeclarada](../c/caracteristica-autodeclarada.md), [Envenenamiento](../e/envenenamiento.md), [Evasión](../e/evasion.md), [Extracción](../e/extraccion.md), [Inferencia de pertenencia](../i/inferencia-de-pertenencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-448](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md), [SE-612](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Puerta de release](./puerta-de-release.md) · [Puerto →](./puerto.md)
