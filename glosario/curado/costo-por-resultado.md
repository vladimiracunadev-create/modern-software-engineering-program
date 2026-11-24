# Costo por resultado

## Definición

El **costo por resultado útil** es el costo total de operar el servicio dividido por los resultados útiles logrados, por ejemplo entregas aceptadas, y no por las solicitudes recibidas. Es el sentido de `SE-140` (FinOps de producto). Une el gasto con el valor entregado en una sola razón.

## Por qué importa

Cambia qué se optimiza. El costo por solicitud mezcla fallas y reintentos: una solicitud fallida cuesta y no produce nada. Medir por resultado hace visible el costo de la falla y evita celebrar un costo por solicitud bajo que esconde una baja tasa de aceptación. Es el puente entre la infraestructura y la decisión de producto.

## Cómo funciona

El numerador es el costo total de operar el servicio en un periodo (infraestructura, soporte, el reparto del costo compartido). El denominador es el número de resultados que cumplen el criterio de «útil», definido antes de medir. La diferencia con el costo por solicitud importa cuando hay reintentos: cada intento cuesta y solo uno produce resultado, de modo que una tasa de fallas mayor eleva el costo por resultado aunque la infraestructura no cambie.

Esto enlaza con la tasa de aceptación de `SE-139`: si la aceptación baja, el denominador baja y el costo por resultado sube. `SE-140` pide medir ambas juntas. El reparto del costo compartido entre centros es una regla explícita, y cambiar una sola regla de reparto modifica la cuota de cada centro, por lo que debe quedar escrita. `SE-141` usa estos costos para comparar iniciativas y `SE-144` los integra en el caso de viabilidad.

## Ejemplo

En la plataforma de entregas, un mes con el mismo gasto de infraestructura pasa de 1000 a 1250 solicitudes porque el cliente reintenta más tras un cambio de red, mientras las entregas aceptadas siguen siendo 800. El costo por solicitud baja; el costo por resultado no mejora, y la causa aparece al mirar la tasa de aceptación junto al costo. (Cifras ilustrativas, para mostrar el mecanismo.)

## Errores y confusiones comunes

- **El costo por resultado sube sin que cambie la infraestructura.** Subieron las fallas y reintentos; medir la tasa de aceptación junto con el costo (`SE-140`).
- **Dividir por solicitudes.** Premia el volumen, no el valor.
- **Definir «útil» después de ver los datos.** Permite ajustar el resultado a la conclusión.
- **Repartir el costo compartido sin regla escrita.** Las cuotas se vuelven discutibles.

## Límites y cuándo no aplica

Requiere una definición estable de «resultado útil»; en productos donde el valor es difuso o tardío, el denominador es discutible. Mezcla costos fijos con variables, por lo que a bajo volumen el costo por resultado es alto por razones de escala y no de eficiencia. Y no mide calidad ni valor percibido: solo cuánto cuesta cada resultado que cumple el criterio.
