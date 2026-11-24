# Entorno aislado

## Definición

Un **entorno aislado** es un contexto de ejecución que limita lo que un proceso puede leer, escribir o contactar, con independencia de las reglas que se le den al agente o al programa. Es el sentido principal de `SE-570` (habilidades, extensiones, ganchos y entornos aislados para agentes). `SE-207` usa la misma palabra en un sentido más modesto: una copia independiente del intérprete y sus paquetes (un entorno virtual) que evita mezclar dependencias con las del sistema.

## Por qué importa

Cambia dónde se pone la barrera. Las reglas y los ganchos dependen de que se hayan previsto bien; el aislamiento limita las consecuencias aunque fallen. Según `SE-570`, protege de los dos tipos de error que reglas y ganchos no cubren: el que no se previó y el que se previó mal.

## Cómo funciona

El entorno acota qué directorios puede leer o escribir el proceso, a qué dominios puede conectarse y si tiene acceso a las credenciales de la persona. Puede ser el aislamiento del sistema operativo que ofrece la herramienta del agente, un contenedor, una máquina virtual o un espacio de trabajo desechable. Funciona por **capas independientes**: una regla de denegación sobre el comando, un gancho de política y el aislamiento actúan como barreras sucesivas, de modo que el fallo de una no deja todo abierto.

La capa de política (el gancho) debe fallar cerrado: `SE-570` muestra el defecto de un control que «no hace nada» sin error porque falla abierto; la corrección es que el gancho termine con éxito solo cuando comprobó y permite, y que cualquier otro resultado se interprete como bloqueo. El aislamiento de `SE-207` es otro mecanismo con otro alcance: separa paquetes, no limita permisos de seguridad.

## Ejemplo

En el escenario hipotético de `SE-570`, el equipo de *Avisos* revisa sus controles. El gancho de política tiene tres decisiones explícitas (éxito solo si comprobó y permite; código de bloqueo si bloquea; cualquier otro resultado se interpreta como bloqueo) y se añade una regla de denegación de las órdenes que el gancho vigila, como segunda barrera. El entorno aislado es la tercera.

## Errores y confusiones comunes

- **El control no hace nada y no hay error.** Falla abierto: usar el código de bloqueo para la política y probar la caída.
- **Confundir entorno virtual con aislamiento de seguridad.** Separa dependencias, no limita lo que el proceso puede alcanzar.
- **Dar acceso a las credenciales por comodidad.** Anula el valor del aislamiento.
- **Cargar todas las habilidades en memoria al arrancar.** Es un problema de contexto, no de aislamiento; cargarlas bajo demanda.

## Límites y cuándo no aplica

El aislamiento tiene un coste de fricción: lo que un proceso necesita y el entorno bloquea hay que permitirlo con criterio. No impide un uso indebido de lo que sí se le dejó alcanzar, y un contenedor mal configurado puede dar una falsa seguridad. El escenario de `SE-570` es hipotético, sin datos reales.
