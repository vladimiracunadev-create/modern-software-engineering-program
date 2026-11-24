# Modelo de información

## Definición

Un **modelo de información** es la descripción de los datos almacenados, sus claves, unicidades y restricciones (SE-160). Dice qué entidades existen, qué campos tiene cada una, cómo se relacionan y qué debe cumplirse siempre. No es el diseño de pantallas ni el de componentes: es la forma de lo que se guarda.

## Por qué importa

Muestra qué se guarda y con qué restricciones, y por eso decide **dónde puede aparecer una inconsistencia**. Dos lugares que guardan el mismo hecho pueden divergir; una restricción ausente permite datos que no deberían existir. Cambia el diseño de almacenamiento y de validación: el modelo es la fuente de las reglas de integridad.

## Cómo funciona

El modelo declara qué datos se almacenan, cuáles son **claves**, qué es **único** y qué **restricciones** se cumplen. SE-160 desarrolla la **normalización** de Codd: organizar los datos para que cada hecho se guarde en un solo lugar (el nombre de un curso no se repite en cada entrega). Su efecto es eliminar una clase de inconsistencia (dos nombres para el mismo curso, una actualización que olvida una copia); su costo es leer con uniones. Desnormalizar, es decir, duplicar a propósito para leer más rápido, es una decisión que se toma con conocimiento del riesgo y con un mecanismo que mantenga las copias coherentes.

En la plataforma de entregas, el modelo de entidades vive en un **archivo estructurado junto al código** (entidad, campos con tipo, referencias con cardinalidad). Se verifica de dos maneras: un comprobador de integración continua revisa la consistencia estructural (referencias a entidades existentes, claves definidas), y un segundo extrae del código las clases (con `ast`) y compara nombres y tipos con el modelo, fallando con un mensaje que dice qué cambio de qué archivo causó la divergencia. Los diagramas se generan del archivo, no se dibujan a mano.

La clase advierte un límite: el comprobador estructural puede dar verde con la **relación invertida**, porque la semántica (si un curso tiene muchas entregas o al revés) no es comprobable estructuralmente. Hace falta revisión por una persona con el dominio y ejemplos de datos que contradigan la relación.

## Ejemplo

Entidades: `Curso(id, nombre)`, `Entrega(id, curso_id, estudiante_id, enviada_en)`. Restricciones: `Curso.id` es clave; `Entrega.curso_id` referencia a `Curso`; `(estudiante_id, curso_id, tarea_id)` es único. Si el nombre del curso se copiara en `Entrega`, un cambio de nombre exigiría actualizar miles de filas y podría dejar versiones distintas; con la clave foránea, el nombre vive en un solo lugar. (Ilustración del principio de SE-160.)

## Errores y confusiones comunes

- **El diagrama no coincide con la base en producción**: se dibujó una vez y no se comprueba; corrección: generarlo de un archivo que se compara con el código o la base.
- **Verde estructural con relación invertida**: la semántica no se comprueba estructuralmente.
- **Desnormalizar sin mecanismo de coherencia.**
- **Confundirlo con el modelo de datos físico**: el de información es el nivel conceptual.

## Límites y cuándo no aplica

La normalización completa no siempre conviene en sistemas de lectura intensiva ni en almacenes analíticos. El modelo describe el estado, no el comportamiento. Y un modelo perfecto no protege de datos mal ingresados: hacen falta validaciones en la frontera.
