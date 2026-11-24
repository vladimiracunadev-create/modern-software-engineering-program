# Activo

## Definición

En seguridad, un **activo** es un dato, capacidad o servicio cuyo daño importa a la organización o a las personas, como las calificaciones o la disponibilidad el día del cierre (`SE-457`). Es el punto de partida del modelo de amenazas.

## Por qué importa

Un modelo de amenazas empieza por lo que se quiere conservar y no por lo que se teme. Sin activos definidos no se sabe qué proteger primero, y se terminan arreglando cosas graves que no importan o dejando abiertas las que sí.

## Cómo funciona

Cada activo se asocia a una propiedad que hay que proteger y a un atacante con una razón distinta. En la plataforma de `SE-457`: las **calificaciones** (integridad: que nadie las altere), las **entregas** de cada estudiante (confidencialidad: que solo las lea quien debe), la **disponibilidad el día del cierre** y la **confianza de las familias**. Los atacantes concretan capacidad, paciencia y recursos: un estudiante que desea mejorar su nota conoce la plataforma por dentro y tiene una cuenta válida; un tercero que busca datos de menores parte de internet sin ninguna.

## Ejemplo

`SE-457` dibuja fronteras, enumera amenazas por elemento, calcula el camino más barato hasta el activo y lo recalcula tras cada decisión. Pide, como transferencia, repetirlo en otro dominio (un taller que gestiona citas): cambian activos y actores, no el procedimiento.

## Errores y confusiones comunes

- **Se arregla lo grave y nada mejora.** Se prioriza por gravedad, no por camino; calcular el camino más barato.
- **Una lista de 80 amenazas sin dueño.** Una fila por amenaza con elemento, respuesta y supuesto.
- **Confundir activo con sistema.** El activo es lo que importa dentro o a través del sistema.

## Límites y cuándo no aplica

Los activos de la clase pertenecen a una plataforma educativa concreta. En otro dominio la lista cambia, y un activo mal valorado desplaza todas las prioridades. Un activo no es sinónimo de «dato»: la disponibilidad y la confianza también lo son.
