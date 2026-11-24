# Reflexión

## Definición

La **reflexión** (Shinn et al.) es un texto de retroalimentación sobre un intento fallido que se usa en el siguiente (`SE-592`).

## Por qué importa

Es una forma de que un agente aprenda dentro de una tarea sin reentrenar. Pero solo ayuda si hay una señal de fallo externa; sin ella, el modelo evalúa su propio resultado con los mismos sesgos con que lo produjo.

## Cómo funciona

El resultado de un intento fallido se convierte en un texto («falló porque el estudiante 3 no tenía contacto; comprueba el contacto antes de enviar») que se añade al contexto del siguiente intento. Cuesta al menos dos llamadas más (reflexionar y volver a planificar) y solo ayuda si hay una **señal de fallo externa**: un código de error, un verificador, una prueba. Con un verificador, la reflexión recibe una falla concreta y puede mejorar.

## Ejemplo

Un agente de envíos recibe de la herramienta el error «contacto vacío» para un estudiante; la reflexión añade esa regla al siguiente intento.

## Errores y confusiones comunes

Pedir reflexión sin verificador externo: sirve poco, porque el modelo valida su propio resultado con sus sesgos.

## Límites y cuándo no aplica

El costo extra de llamadas debe justificarse por la mejora medida; combinar con condiciones de parada para no reflexionar indefinidamente.
