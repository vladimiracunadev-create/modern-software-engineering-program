# Línea base

[↑ Glosario](../../README.md) · [← Linaje](./linaje.md) · [Linealizabilidad →](./linealizabilidad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

En ingeniería de requisitos ([SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md)), una **línea base** es una versión acordada del conjunto de requisitos que sirve de referencia y solo cambia por un proceso controlado. El programa usa la palabra con otros matices cercanos: en [SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md), los valores de las métricas de un sistema antes de un cambio, con su incertidumbre, contra los que se compara después; en [SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md), el comportamiento de la versión anterior, medido en paralelo, contra el que se compara el canario; en [SE-601](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md), una regla o modelo simple con el que se compara un modelo de ML. El hilo común es *lo contra lo que se compara*.

## Por qué importa

Hace posible responder preguntas que, sin referencia, no tienen respuesta: «¿esto está dentro del alcance?», «¿mejoró algo?», «¿cambió el comportamiento?». Sin línea base el alcance se mueve con cada edición, y una mejora se afirma sin saber de dónde se parte.

## Cómo funciona

En el sentido de [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md), la línea base es una versión del conjunto de requisitos que el equipo acordó; lo que se construye, se prueba y se entrega se mide contra ella. No significa que no pueda cambiar: significa que cambia **de forma controlada**, mediante una solicitud de cambio con análisis de impacto y decisión, y que siempre se sabe contra cuál versión se trabaja. Para ello necesita identidad estable (etiqueta, commit o hash normalizado). La clase propone una prueba de regresión que verifica el hash normalizado de la línea base y falla si cambia sin una solicitud registrada.

En el sentido de medición ([SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md)), la línea base son las métricas **antes** del cambio, con su incertidumbre. Un error típico: afirmar una mejora con 20 cambios porque la línea base se midió sin incertidumbre; la corrección es declarar el intervalo y ampliar la muestra. En el sentido del canario ([SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md)), la versión anterior se mide en paralelo, no en un momento anterior, para que las condiciones sean comparables. En ML ([SE-601](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md)), una línea base simple (por ejemplo, predecir la media) dice cuánto aporta realmente un modelo complejo.

## Ejemplo

[SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md) muestra una solicitud de cambio con su análisis y decisión sobre la línea base 1: el cambio propone modificar un tope de penalización; el análisis recorre las dependencias y lista requisitos y pruebas afectados; la decisión lo aprueba y se crea la línea base 2 con nuevo hash normalizado. Hasta entonces, el trabajo se mide contra la 1.

## Errores y confusiones comunes

- **Nadie sabe cuál era la versión acordada**: no hay línea base identificada; corrección: etiquetar cada versión acordada y registrar su hash normalizado.
- **Afirmar una mejora sin línea base con incertidumbre** ([SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md)).
- **Confundirla con una congelación absoluta**: puede cambiar, pero de forma controlada.
- **Comparar con una línea base tomada en otras condiciones.**

## Límites y cuándo no aplica

Una línea base rígida frena la adaptación cuando el aprendizaje del proyecto es alto y el costo de cambiar es bajo: ahí conviene líneas base ligeras por iteración. Y una línea base mal elegida (una referencia demasiado débil en ML, por ejemplo) hace parecer buenos resultados mediocres.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Canario](../c/canario.md), [Conjunto](../c/conjunto.md), [Incertidumbre](../i/incertidumbre.md), [Métrica](../m/metrica.md), [Análisis de alcance](../a/analisis-de-alcance.md), [Blue-green](../b/blue-green.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-153 — Gestión de cambios y líneas base](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.
- [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.
- [SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.
- [SE-601 — Ciclo de vida de ML y por qué falla en producción](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (34 clases más lo mencionan; las que más):

[SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md), [SE-291](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md), [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md), [SE-549](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md), [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md), [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md), [SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md).

**Aparece en los casos de estudio:** [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [Quibi](../../../casos/fallo/quibi.md), [Boeing 737 MAX y MCAS](../../../casos/fallo/boeing-737-max-mcas.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ISO 10007:2017](https://www.iso.org/standard/70400.html) — gestión de la configuración: identificación, control de cambios, registro de estado y auditoría; autoridad: ISO.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — gestión de la configuración y control de cambios; autoridad: IEEE Computer Society.
- [Nuseibeh y Easterbrook: Requirements engineering, a roadmap (2000)](https://doi.org/10.1145/336512.336523) — evolución de los requisitos; autoridad: ACM, The Future of Software Engineering.
- [Git: git-tag](https://git-scm.com/docs/git-tag) — etiquetas anotadas; autoridad: proyecto Git.
- [Git: git-diff](https://git-scm.com/docs/git-diff) — comparación entre revisiones; autoridad: proyecto Git.

---

[↑ Glosario](../../README.md) · [← Linaje](./linaje.md) · [Linealizabilidad →](./linealizabilidad.md)
