# Tiempo de recuperación

## Definición

En las métricas de entrega, el **tiempo de recuperación** es el tiempo que tarda en restaurarse el servicio tras un despliegue fallido (`SE-490`). No se debe confundir con el MTTR de la ingeniería de fiabilidad en general ni con los objetivos de recuperación de desastres (RTO), de otra clase.

## Por qué importa

Es una de las métricas de DORA y mide cuánto dura el daño cuando un cambio falla; junto con la tasa de fallos de los cambios, describe la estabilidad de las entregas.

## Cómo funciona

La guía de DORA agrupa las métricas en dos dimensiones. El **rendimiento** describe la velocidad con que los cambios llegan a producción: plazo de los cambios (desde la confirmación hasta producción), frecuencia de despliegue y tiempo de recuperación. La **inestabilidad** describe la calidad: la tasa de fallos de los cambios y la tasa de retrabajo. `SE-490` insiste en que cada definición se escriba y versione, porque dos equipos con definiciones distintas reportan números no comparables.

## Ejemplo

Un despliegue falla a las 10:00 y se revierte a las 10:20: el tiempo de recuperación es de 20 minutos. Un equipo con retroceso automático lo reduce; uno que debe corregir hacia adelante tarda más.

## Errores y confusiones comunes

- **Dos equipos reportan plazos muy distintos.** Definiciones diferentes; escribirlas, versionarlas y comparar solo con la misma.
- **La frecuencia sube y la entrega no mejora.** La métrica es objetivo y se cuentan despliegues vacíos; contar solo cambios de comportamiento y añadir contrapeso.

## Límites y cuándo no aplica

Una métrica de equipo no es un objetivo individual: cuando se vuelve meta, se manipula. Solo es comparable dentro de la misma definición.
