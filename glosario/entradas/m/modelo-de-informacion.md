# Modelo de información

[↑ Glosario](../../README.md) · [← Modelo de fallos](./modelo-de-fallos.md) · [Modelo de ingreso →](./modelo-de-ingreso.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Un **modelo de información** es la descripción de los datos almacenados, sus claves, unicidades y restricciones ([SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md)). Dice qué entidades existen, qué campos tiene cada una, cómo se relacionan y qué debe cumplirse siempre. No es el diseño de pantallas ni el de componentes: es la forma de lo que se guarda.

## Por qué importa

Muestra qué se guarda y con qué restricciones, y por eso decide **dónde puede aparecer una inconsistencia**. Dos lugares que guardan el mismo hecho pueden divergir; una restricción ausente permite datos que no deberían existir. Cambia el diseño de almacenamiento y de validación: el modelo es la fuente de las reglas de integridad.

## Cómo funciona

El modelo declara qué datos se almacenan, cuáles son **claves**, qué es **único** y qué **restricciones** se cumplen. [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md) desarrolla la **normalización** de Codd: organizar los datos para que cada hecho se guarde en un solo lugar (el nombre de un curso no se repite en cada entrega). Su efecto es eliminar una clase de inconsistencia (dos nombres para el mismo curso, una actualización que olvida una copia); su costo es leer con uniones. Desnormalizar, es decir, duplicar a propósito para leer más rápido, es una decisión que se toma con conocimiento del riesgo y con un mecanismo que mantenga las copias coherentes.

En la plataforma de entregas, el modelo de entidades vive en un **archivo estructurado junto al código** (entidad, campos con tipo, referencias con cardinalidad). Se verifica de dos maneras: un comprobador de integración continua revisa la consistencia estructural (referencias a entidades existentes, claves definidas), y un segundo extrae del código las clases (con `ast`) y compara nombres y tipos con el modelo, fallando con un mensaje que dice qué cambio de qué archivo causó la divergencia. Los diagramas se generan del archivo, no se dibujan a mano.

La clase advierte un límite: el comprobador estructural puede dar verde con la **relación invertida**, porque la semántica (si un curso tiene muchas entregas o al revés) no es comprobable estructuralmente. Hace falta revisión por una persona con el dominio y ejemplos de datos que contradigan la relación.

## Ejemplo

Entidades: `Curso(id, nombre)`, `Entrega(id, curso_id, estudiante_id, enviada_en)`. Restricciones: `Curso.id` es clave; `Entrega.curso_id` referencia a `Curso`; `(estudiante_id, curso_id, tarea_id)` es único. Si el nombre del curso se copiara en `Entrega`, un cambio de nombre exigiría actualizar miles de filas y podría dejar versiones distintas; con la clave foránea, el nombre vive en un solo lugar. (Ilustración del principio de [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md).)

## Errores y confusiones comunes

- **El diagrama no coincide con la base en producción**: se dibujó una vez y no se comprueba; corrección: generarlo de un archivo que se compara con el código o la base.
- **Verde estructural con relación invertida**: la semántica no se comprueba estructuralmente.
- **Desnormalizar sin mecanismo de coherencia.**
- **Confundirlo con el modelo de datos físico**: el de información es el nivel conceptual.

## Límites y cuándo no aplica

La normalización completa no siempre conviene en sistemas de lectura intensiva ni en almacenes analíticos. El modelo describe el estado, no el comportamiento. Y un modelo perfecto no protege de datos mal ingresados: hacen falta validaciones en la frontera.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Restricciones](../r/restricciones.md), [Deriva](../d/deriva.md), [Modelo conductual](./modelo-conductual.md), [Modelo estructural](./modelo-estructural.md), [Normalización](../n/normalizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-160 — Modelos estructurales, conductuales y de información](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md), [SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Modelos de información».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OMG: Unified Modeling Language](https://www.omg.org/spec/UML/) — especificación de la notación de modelos estructurales y conductuales; autoridad: Object Management Group.
- [Chen, «The entity-relationship model» (ACM TODS, 1976)](https://doi.org/10.1145/320434.320440) — entidades, relaciones y cardinalidades; autoridad: ACM Transactions on Database Systems.
- [Codd, «A relational model of data for large shared data banks» (CACM, 1970)](https://doi.org/10.1145/362384.362685) — modelo relacional y fundamento de la normalización; autoridad: Communications of the ACM.
- [The C4 model](https://c4model.com/) — vistas de la arquitectura por nivel de detalle; autoridad: autor del modelo.
- [Harel, «Statecharts» (Science of Computer Programming, 1987)](https://doi.org/10.1016/0167-6423%2887%2990035-9) — formalismo visual para modelos conductuales; autoridad: Science of Computer Programming.

---

[↑ Glosario](../../README.md) · [← Modelo de fallos](./modelo-de-fallos.md) · [Modelo de ingreso →](./modelo-de-ingreso.md)
