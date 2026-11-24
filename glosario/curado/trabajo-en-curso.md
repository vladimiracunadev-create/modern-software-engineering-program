# Trabajo en curso

## Definición

El **trabajo en curso** (*work in progress*, WIP) es la cantidad de elementos iniciados y no terminados (`SE-533`).

## Por qué importa

Explica por qué un equipo con muchas cosas abiertas termina todo más tarde. Reducir el tiempo de permanencia sin reducir el ritmo de entrega exige reducir el trabajo en curso.

## Cómo funciona

`SE-533` aplica la ley de Little: en un sistema estable, el trabajo promedio en curso es el ritmo de entrada por el tiempo promedio de permanencia. Si el ritmo es fijo, bajar el tiempo exige bajar el WIP. Además, según Kingman, la espera de una cola de un servidor crece de forma brusca al aproximarse la utilización a uno: un equipo al 95 % no tiene elementos lentos por pereza sino por saturación. El compromiso incluye entonces un **límite de trabajo en curso** y una **reserva de capacidad**.

## Ejemplo

Un equipo con 20 elementos abiertos y que termina 4 por semana tarda en promedio 5 semanas por elemento (20 / 4). Al limitar el WIP a 8, el tiempo medio baja a 2 semanas sin cambiar el ritmo. (Ilustración de la ley de Little.)

## Errores y confusiones comunes

**Los elementos tardan cada vez más.** Equipo saturado; limitar el trabajo en curso y reservar capacidad.

## Límites y cuándo no aplica

La ley de Little supone un sistema estable. Limitar el WIP no sirve si se reabre trabajo que ya estaba cerrado; y una reserva de capacidad tiene costo aparente de «ociosidad» que debe explicarse.
