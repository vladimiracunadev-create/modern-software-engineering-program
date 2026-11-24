# Segmento

## Definición

En monitoreo y despliegue de modelos, un **segmento** es una subpoblación definida de antemano que se vigila por separado (`SE-607`).

## Por qué importa

Un indicador global puede mejorar mientras un grupo empeora. `SE-607` lo muestra: el Brier global dice que el candidato mejora (0,163 a 0,159) mientras el AUC baja (0,837 a 0,819), y el daño se concentra en un segmento.

## Cómo funciona

El modelo vigente es una regresión logística entrenada con 8 000 filas del periodo antiguo; el candidato es un boosting entrenado con 40 000 filas del periodo reciente, en el que una anomalía de etiquetado registró como puntual el 60 % de las entregas tardías del segmento que usa móvil y entrega de noche. Al medir por segmento, el candidato empeora en el segmento móvil y nocturno aunque mejore en el total. El plan de despliegue vigila segmentos definidos antes de empezar.

## Ejemplo

`SE-607`: en la etapa de sombra de 24 horas, se vigila el desacuerdo y la tasa de marcados en cuatro segmentos (dispositivo y franja horaria); la regla es pausar si alguno se aparta más de 10 puntos. La primera noche, en el segmento móvil y nocturno el candidato marca al 4 % frente al 59 % del vigente: el plan se pausa y se descubre el problema de etiquetado.

## Errores y confusiones comunes

Definir los segmentos después de ver los resultados; vigilar solo agregados.

## Límites y cuándo no aplica

Demasiados segmentos producen alarmas por azar; deben elegirse por razón de negocio o de riesgo.
