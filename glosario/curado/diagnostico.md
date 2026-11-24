# Diagnóstico

## Definición

Un **diagnóstico** es la conclusión razonada de la causa de un comportamiento, con la reproducción que la respalda (`SE-568`). No es el síntoma ni una lista de hipótesis: es una causa afirmada con evidencia y un caso que la demuestra. En las clases de redes (`SE-037` a `SE-047`) es también el método: recorrer capas, ordenar fases y ubicar la primera divergencia respecto del caso sano.

## Por qué importa

Quien arregla el síntoma deja la causa viva: «el mismo error vuelve con otra entrada» (`SE-568`). El diagnóstico decide si el arreglo es local o general, y es lo que permite escribir una prueba que fracasaba antes y pasa después. También separa lo que se observó de lo que se supuso.

## Cómo funciona

El método que enseña `SE-047` es una cadena:

1. **Reproducir** el comportamiento con un escenario declarado.
2. **Comparar** con un caso sano y localizar la primera divergencia.
3. **Formular** una causa y comprobar que predice el resultado en los otros escenarios.
4. **Contrastar casos vecinos** para no arreglar solo el caso visto (`SE-568`).

En el laboratorio de `SE-047` cada fila va de un escenario a su primera divergencia y a su resultado (ok, fallido o recuperado). Los escenarios recuperados muestran que un reintento acotado cambia el resultado final pero deja huella en los eventos. Hay además una honestidad metodológica: se declara qué es real (el tráfico HTTP local) y qué es un modelo determinista (DNS, validación del nombre TLS y pérdida).

## Ejemplo

Un registro de eventos muestra: resolución de nombre correcta, conexión correcta, fallo en validación del certificado. La primera divergencia está en la fase de TLS, no en la red; reintentar sin cambiar el nombre solicitado no la corrige. El diagnóstico dice «el nombre del certificado no coincide con el host pedido» y la reproducción lo demuestra con ese host.

## Errores y confusiones comunes

- **Arreglar el síntoma.** El error vuelve con otra entrada; corrección: exigir diagnóstico de la causa y casos vecinos (`SE-568`).
- **Diagnosticar por coincidencia temporal.** Sin hipótesis ni predicción, solo hay correlación.
- **Confundir diagnóstico con reproducción.** La reproducción es la evidencia; el diagnóstico es la conclusión que la usa.

## Límites y cuándo no aplica

La suite de `SE-047` demuestra el método, no el comportamiento de una red real: DNS, TLS y pérdida son modelos. Un diagnóstico es una afirmación revisable; en sistemas no deterministas puede no haber reproducción fiable y entonces se declara el grado de confianza.
