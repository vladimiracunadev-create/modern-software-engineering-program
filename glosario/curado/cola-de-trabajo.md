# Cola de trabajo

## Definición

Una **cola de trabajo** es un canal en el que varios consumidores compiten por los mensajes: cada mensaje se entrega a uno solo y se borra al confirmarse (`SE-375`). Su propósito es repartir carga, no difundir información.

## Por qué importa

Elegir entre una cola de trabajo y un log o un tópico con suscripciones decide qué se puede hacer después. En una cola, un mensaje confirmado deja de existir: no se puede reprocesar tras un defecto ni mostrar a un segundo interesado. Quien necesita que varios servicios reaccionen al mismo hecho, o que un servicio nuevo vea la historia, no puede apoyarse en una cola de trabajo.

## Cómo funciona

Varios **consumidores competidores** leen del mismo canal. El corredor entrega cada mensaje a uno de ellos; cuando ese consumidor lo confirma, el mensaje se borra. Por eso añadir consumidores acelera el vaciado: el trabajo se divide entre más manos. `SE-375` subraya que la limitación es **estructural**, no un defecto de configuración: el mensaje confirmado no existe. Un segundo consumidor que lee de la misma cola no recibe una copia, sino que toma otra parte del trabajo.

Contrasta con el **log**, donde los mensajes se conservan por retención o compactación y cada consumidor mantiene su propia posición de lectura, de modo que muchos pueden leer lo mismo y un consumidor nuevo puede empezar desde el principio. Y con la difusión por suscripciones separadas, donde cada suscriptor recibe su copia. La clase obliga a decidir según el consumidor: ¿necesita repartir trabajo, difundir un hecho o reconstruir estado?

## Ejemplo

Un servicio recibe entregas y las manda a una cola para generar miniaturas. Tres procesos trabajadores compiten por los mensajes: si la cola se acumula, se añaden más procesos. Pero si un servicio de estadísticas también necesita ver cada entrega y se conecta a la misma cola, recibirá solo una parte de los mensajes y a los trabajadores les faltará esa parte. Para que ambos vean todo hace falta una suscripción por consumidor o un log.

## Errores y confusiones comunes

- **La mitad de los mensajes no llega a un consumidor**: dos consumidores comparten una cola; se corrige con suscripciones separadas para difundir (`SE-375`).
- **Un servicio nuevo no ve datos anteriores**: el tópico no tiene retención; se corrige con un log o cargando la historia de otra fuente.
- **Esperar reprocesar tras confirmar**: el mensaje confirmado ya no existe.
- **Confundir competir con difundir**: son dos semánticas de entrega distintas.

## Límites y cuándo no aplica

No sirve cuando varios consumidores independientes necesitan cada mensaje, cuando hay que auditar o reproducir la historia, ni para reconstruir un estado: ahí corresponde un log, con retención o compactación. Tampoco garantiza por sí sola orden ni ausencia de duplicados; eso depende de la semántica de entrega y de que el consumidor sea idempotente. Para trabajo que cabe en una llamada síncrona corta, la cola añade complejidad innecesaria.
