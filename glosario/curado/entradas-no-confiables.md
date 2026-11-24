# Entradas no confiables

## Definición

En una canalización de integración continua, una **entrada no confiable** es un dato del contexto del evento que puede convertirse en código si el flujo lo interpreta mal (`SE-478`): el título de una solicitud, el nombre de una rama, el cuerpo de un comentario.

## Por qué importa

Quien controla esos datos puede ser una persona externa. Si el flujo los interpola dentro de una orden, ejecutan lo que esa persona escribió, con los permisos del flujo.

## Cómo funciona

`SE-478` trata el análisis de seguridad de una canalización como un procedimiento: listar los **activos** (secretos, permisos) y las **entradas no confiables**, fijar las dependencias del CI, minimizar el alcance, evaluar el escáner con mutaciones y preparar la respuesta. Dos errores típicos: interpolar el contexto directamente en un paso `run`, y referenciar acciones por etiqueta movible.

## Ejemplo

Un flujo hace `echo "${{ github.event.pull_request.title }}"` dentro de un `run`; un título con comillas y órdenes se ejecuta. La corrección es pasar el dato como variable de entorno y usarlo como variable, no como texto de la orden.

## Errores y confusiones comunes

- **Un título de solicitud ejecuta órdenes.** Interpolación del contexto en `run`; pasar el dato como variable de entorno.
- **Una acción cambia de comportamiento sin cambios en el repositorio.** Referencia por etiqueta; fijar a un SHA y revisar las actualizaciones.

## Límites y cuándo no aplica

La sintaxis es de una plataforma concreta; en GitLab o Jenkins cambian permisos y secretos, pero se conserva el procedimiento. `SE-478` pide poder decir cuál es en la nueva plataforma el equivalente a `pull_request_target` y qué runner conserva estado.
