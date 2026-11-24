# Objetivo de punto de recuperación

## Definición

El **objetivo de punto de recuperación** (RPO, por *recovery point objective*) es la cantidad máxima de datos recientes que se acepta perder tras una falla o una restauración, expresada como un intervalo de tiempo (o, en algunos casos, como número de escrituras) (`SE-393`, `SE-357`, `SE-440`). `SE-576` lo usa en el contexto de agentes: la cantidad máxima de trabajo reciente que se acepta perder tras una restauración.

## Por qué importa

«No perder datos» no es un objetivo: es un deseo. El RPO convierte la tolerancia en un número que condiciona el diseño y su costo. Un RPO de un día se cumple con una copia diaria; uno de segundos exige replicación continua. La decisión que cambia es qué mecanismo de protección se elige y cuánto se paga por él, dato por dato.

## Cómo funciona

`SE-357` deduce la estrategia del RPO: un RPO de un día se cumple con una copia diaria; uno de 15 minutos exige archivar el registro de cambios; uno de segundos exige replicación, que **no sustituye al respaldo** (una réplica replica también los errores).

`SE-393` desarrolla la parte de replicación. Una réplica asíncrona recibe los cambios después de que el primario confirma; si el primario cae antes de enviar los últimos, esos cambios, ya confirmados a las personas, se pierden al conmutar. Con replicación asíncrona, el RPO es el retraso de la réplica. La replicación **síncrona** espera la confirmación de la réplica antes de responder: RPO cero, a cambio de latencia (el tiempo de ida y vuelta) y de disponibilidad (si la réplica cae, el primario espera o degrada). La **semisíncrona** exige confirmar con al menos una réplica y mantiene las demás asíncronas. Elegir es dato por dato: lo que no puede perderse, síncrono; lo reconstruible, asíncrono.

## Ejemplo

El servicio de entregas de `SE-393` usa replicación semisíncrona hacia una réplica del mismo centro de datos (RPO cero) y asíncrona hacia otra región, con un RPO declarado de 30 segundos. Los acuses de recibo se emiten solo tras la confirmación semisíncrona, de modo que ninguna entrega con acuse se pierde en una conmutación local. El de 30 segundos es el precio aceptado para la región remota.

## Errores y confusiones comunes

- **Estudiantes con acuse y sin registro tras una conmutación**: replicación asíncrona con acuse previo; se corrige confirmando con una réplica antes del acuse.
- **Confundirlo con RTO**: el RPO mide cuántos datos se pierden; el RTO, cuánto tarda la recuperación.
- **Creer que la réplica reemplaza el respaldo**: replica también los borrados y la corrupción.
- **Declarar un RPO sin medir el retraso real** de la réplica.

## Límites y cuándo no aplica

Un RPO es un compromiso que se debe comprobar: una copia que nunca se restauró es una hipótesis (de ahí la prueba de restauración). RPO cero tiene un costo de latencia y disponibilidad que no siempre se justifica, y los datos reconstruibles no lo necesitan. El valor numérico depende del negocio; las cifras de los ejemplos (30 segundos, 15 minutos, un día) son de las clases, no valores recomendados.
