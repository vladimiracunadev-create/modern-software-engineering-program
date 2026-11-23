# Variante

[↑ Glosario](../../README.md) · [← Variable respuesta](./variable-respuesta.md) · [Variante defectuosa →](./variante-defectuosa.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Modelo adaptado que se opera por separado.

Definición de trabajo de [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-054 — Algoritmos, corrección y terminación](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md): Medida bien fundada que disminuye.

## Por qué importa

En [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md), el tema «Adaptación de rango bajo» importa porque reduce parámetros entrenables y almacenamiento por variante.

## Cómo funciona

Según [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md):

Ajustar todos los parámetros de un modelo grande exige guardar un gradiente y un estado del optimizador por cada uno y una copia del modelo por variante. La adaptación de rango bajo (LoRA) congela los pesos y entrena, para una capa de dimensiones d por k, dos matrices de rango r: una de d por r y otra de r por k, con r mucho menor que d y k. Para una capa de 4 096 por 4 096 (16 777 216 parámetros), el rango 4 entrena 32 768 (0,20 %), el 8 entrena 65 536 (0,39 %), el 16 entrena 131 072 (0,78 %) y el 64 entrena 524 288 (3,12 %). Cada variante necesita guardar solo esas matrices, no una copia del modelo.

Según [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md):

El equipo de *Avisos-ML* tiene 200 entregas etiquetadas de la universidad nueva. Mide el modelo base: AUC 0,84 en esa población y 0,86 en la original. Ajusta el modelo con las 200 filas y obtiene 0,85 en la nueva y 0,855 en la original. El intervalo de la diferencia, calculado con la evaluación de `SE-604` sobre 4 000 filas de evaluación, incluye el cero en la nueva y no lo incluye en la original (una pérdida real, pequeña). El equipo decide no adaptar: la mejora no es distinguible del ruido y la variante tendría un costo de operación. Define además un disparador: cuando haya 2 000 filas etiquetadas, repite la comparación.

## Ejemplo

Ejemplo de [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos-ML* tiene 200 entregas etiquetadas de la universidad nueva. Mide el modelo base: AUC 0,84 en esa población y 0,86 en la original. Ajusta el modelo con las 200 filas y obtiene 0,85 en la nueva y 0,855 en la original. El intervalo de la diferencia, calculado con la evaluación de `SE-604` sobre 4 000 filas de evaluación, incluye el cero en la nueva y no lo incluye en la original (una pérdida real, pequeña). El equipo decide no adaptar: la mejora no es distinguible del ruido y la variante tendría un costo de operación.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Ajustar todos los parámetros de un modelo grande exige guardar un gradiente y un estado del optimizador por cada uno y una copia del modelo por variante. ([SE-605](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Medida](../m/medida.md), [Modelo](../m/modelo.md), [Adaptación de rango bajo](../a/adaptacion-de-rango-bajo.md), [Ajuste fino](../a/ajuste-fino.md), [Algoritmo](../a/algoritmo.md), [Cómputo de entrenamiento](../c/computo-de-entrenamiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-054 — Algoritmos, corrección y terminación](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (122 clases más lo mencionan; las que más):

[SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md), [SE-612](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md), [SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md), [SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md), [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), [SE-167](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md), [SE-176](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md).

**Aparece en los casos de estudio:** [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — aporta definiciones, invariantes y análisis de estructuras y algoritmos usados en la clase.
- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.

---

[↑ Glosario](../../README.md) · [← Variable respuesta](./variable-respuesta.md) · [Variante defectuosa →](./variante-defectuosa.md)
