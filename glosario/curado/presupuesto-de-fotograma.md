# Presupuesto de fotograma

## Definición

El **presupuesto de fotograma** es el tiempo disponible para preparar un fotograma, igual al periodo de refresco de la pantalla. Es el sentido de `SE-293` (gráficos, audio, XR y experiencias inmersivas). Es un caso concreto de plazo duro: la pantalla no espera, de modo que cada fotograma tiene un tiempo máximo y no un tiempo «medio».

## Por qué importa

Convierte la tasa de refresco en un plazo para el cálculo y el dibujo. En experiencias inmersivas un fotograma tardío se nota como tirones, y en realidad virtual puede causar malestar. La decisión que cambia es qué se calcula en cada fotograma y qué se difiere.

## Cómo funciona

`SE-293`: una pantalla de 90 Hz muestra un fotograma cada 11,1 ms. La aplicación dispone de ese intervalo para entradas, actualización, dibujo y envío. Si un fotograma llega tarde:

- **Con sincronización vertical:** espera al siguiente refresco, así que se muestra el doble de tiempo (22,2 ms) y la tasa efectiva baja a la mitad en esos fotogramas.
- **Sin sincronización vertical:** aparecen cortes en la imagen (*tearing*).

De ahí la consecuencia estadística, igual a la de la latencia de cola: lo que importa no es el costo medio sino el **percentil alto**. Un costo medio por debajo del presupuesto puede perder una parte considerable de los fotogramas si la variabilidad es grande.

El mismo razonamiento vale para el audio, con un plazo distinto (el tamaño del búfer). `SE-293` fija el audio de la sala virtual en 48 kHz con búfer de 256 muestras (5,3 ms) por defecto y 512 para equipos con más fallos, medidos por el propio cliente con un contador de subcargas; si la tasa de bloques tardíos supera el 1 % durante un minuto, sube el búfer un nivel y lo avisa.

## Ejemplo

Ilustración numérica propia con la fórmula de la clase: a 90 Hz el presupuesto es 1 000/90 ≈ 11,1 ms; a 60 Hz, 16,7 ms. Si el cálculo cuesta 9 ms de media pero 14 ms en el 5 % de los fotogramas, a 90 Hz ese 5 % se pasa del presupuesto y aparece como tirón, aunque la media diga que sobra tiempo.

## Errores y confusiones comunes

- **Chasquidos en el audio:** búfer demasiado pequeño o procesamiento que lo supera; se sube el búfer (`SE-293`).
- **Optimizar el costo medio** e ignorar el percentil alto.
- **Confundir la tasa de fotogramas por segundo con el tiempo por fotograma:** 60 fps promedio puede esconder fotogramas de 50 ms.
- **Confundirlo con el presupuesto de recursos,** que fija límites de energía y memoria en un dispositivo.

## Límites y cuándo no aplica

Supone una pantalla de tasa fija; con tasas variables el plazo se mueve. No aplica a aplicaciones que no animan de forma continua. Los valores de audio son los de la plataforma simulada de la clase.
