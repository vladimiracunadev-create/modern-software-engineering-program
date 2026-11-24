# Consumidor idempotente

## Definición

Un **consumidor idempotente** es un consumidor de mensajes cuyo efecto no cambia si recibe el mismo mensaje más de una vez (SE-330). SE-376 lo formula como el receptor que, ante un mensaje repetido, no repite el efecto. Es la contrapartida, en quien recibe, de la clave de idempotencia de quien envía.

## Por qué importa

Hace correcto un sistema donde los mensajes pueden llegar duplicados. En mensajería distribuida, la entrega «al menos una vez» es lo habitual y lo práctico: ante un fallo, el corredor reenvía. Si el consumidor no tolera duplicados, un contador suma de más o un correo se envía dos veces. Cambia el diseño del consumo: se asume el duplicado como caso normal.

## Cómo funciona

SE-330 y SE-376 explican por qué no basta confiar en «exactamente una vez». Los productos que lo prometen lo hacen **dentro de un perímetro**: combinan identificadores de productor, transacciones del corredor y lectura-proceso-escritura atómica dentro de su propio almacén. Fuera de ese perímetro (un correo enviado, una nota escrita en otra base) la promesa se rompe, porque el efecto externo no participa en la transacción.

La forma práctica de lograr un efecto único es **entrega al menos una vez más consumidor idempotente**: lo que se consigue es un efecto único, no una entrega única. El consumidor lo logra con un **identificador de evento**: guarda los identificadores ya procesados (en la misma transacción que el efecto) y descarta los repetidos. Cuando la operación es naturalmente idempotente (fijar un valor, no sumarlo), basta aplicarla de nuevo.

Un segundo problema es el orden: un estado antiguo puede sobrescribir uno nuevo si los mensajes llegan desordenados. La corrección es la **secuencia por entidad**: se aplican solo los eventos con secuencia mayor a la última vista. El fragmento de SE-330 muestra un consumidor idempotente y con orden, y pide predecir el estado final.

## Ejemplo

Un consumidor suma cada evento `entrega_recibida` a un contador. El corredor reenvía un evento tras un fallo y el contador queda mayor que la realidad. Con idempotencia: la tabla `procesados(id_evento)` tiene una restricción única; en una sola transacción se inserta el identificador y se incrementa el contador; si el insert falla por duplicado, no se suma. (Ilustración del mecanismo de SE-330.)

## Errores y confusiones comunes

- **Contadores mayores que la realidad**: el consumidor suma cada mensaje; corrección: idempotencia con identificador de evento.
- **Un estado antiguo sobrescribe a uno nuevo**: desorden sin secuencia; corrección: aplicar solo eventos con secuencia mayor.
- **Registrar el identificador fuera de la transacción del efecto.**
- **Creer en «exactamente una vez» fuera del perímetro.**

## Límites y cuándo no aplica

Guardar identificadores consume espacio y exige una política de retención; pasado el plazo, un duplicado tardío se tomaría como nuevo. Para efectos externos que no participan en la transacción, la idempotencia requiere cooperación del destino (por ejemplo, una clave de idempotencia en la API externa). Algunos productos ofrecen modos transaccionales con límites que hay que leer en su documentación.
