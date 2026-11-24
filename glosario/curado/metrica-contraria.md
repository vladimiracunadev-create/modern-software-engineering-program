# Métrica contraria

## Definición

Una **métrica contraria** es la contraparte de una meta que mide el daño posible de perseguirla (SE-139). Si la meta premia el volumen, la contraria mide la calidad; si premia la velocidad, mide los errores. En el vocabulario del programa se emparejan «meta–contraria» y, cuando son umbrales que no deben cruzarse durante un experimento, se llaman guardas.

## Por qué importa

Toda meta se puede cumplir sin cumplir su propósito. Una métrica contraria hace visible esa vía de escape y detiene la optimización ciega. Cambia el diseño de un panel y de un experimento: nunca se optimiza un número solo.

## Cómo funciona

SE-139 da el procedimiento de elección: se pregunta **cómo se cumpliría la meta sin cumplir su propósito**, y la respuesta indica qué medir. Si la meta es aumentar las entregas procesadas por hora, se cumple a costa de procesar mal: la contraria será la tasa de reclamos o de errores. Si la meta es reducir el tiempo de respuesta del soporte, se cumple cerrando tickets sin resolver: la contraria será la reapertura.

Las contrarias se **vigilan a la vez que la meta**, con la misma frecuencia y visibilidad. De otro modo, se vuelven una nota al pie que nadie mira. En un experimento, se definen **guardas** con umbral, ventana, responsable y acción antes de arrancar: cruzar una guarda detiene el despliegue hasta que el responsable decide. Esto evita el síntoma de que la métrica norte suba y el producto empeore por falta de guardas.

Dos riesgos: demasiadas guardas producen alarmas que el equipo ignora (con comparaciones múltiples, alguna se cruzará por azar), y las excepciones (una guarda que se cruza por un incidente ajeno al cambio, una que no se puede medir en la ventana del experimento, una de rendimiento que depende del dispositivo) necesitan **regla escrita**; la decisión de ignorar una guarda no debe dejar de dejar huella.

El archivo de métricas de la plataforma define la métrica norte (numerador, denominador, ventana, filtros), las guardas (métrica, umbral, ventana, responsable, acción) y los pares meta–contraria. La regla de la clase: ninguna prueba arranca sin guardas.

## Ejemplo

Meta: «aumentar el número de entregas aceptadas por docente y semana». Contraria: «porcentaje de entregas reabiertas tras la aceptación» y «tiempo medio de revisión por entrega». Si la meta sube un 20 % y las reaperturas se duplican, el equipo detiene el despliegue y revisa: probablemente se aceptó sin revisar bien. (Ilustración del método de SE-139.)

## Errores y confusiones comunes

- **La métrica norte sube y el producto empeora**: no hay guardas; corrección: definirlas con umbral antes de optimizar.
- **El equipo ignora las alarmas**: hay demasiadas; corrección: reducirlas y corregir las comparaciones múltiples.
- **Contraria que se mide menos que la meta.**
- **Contraria que no es realmente contraria**: mide lo mismo.

## Límites y cuándo no aplica

Una contraria no previene todos los daños: solo el que se pensó. No sustituye el juicio sobre el propósito de la meta. Optimizar la métrica norte sin una métrica contraria es el caso que la clase señala como práctica peligrosa.
