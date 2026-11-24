# Operaciones idempotentes

## Definición

Una **operación idempotente** es aquella cuyo efecto en el estado es el mismo al aplicarla una vez o varias (SE-171, SE-260, SE-392). «Fijar la nota del estudiante 17 en 6,0» es idempotente; «sumar 0,5 a la nota» no. En HTTP, `PUT` y `DELETE` se definen como idempotentes porque describen un estado destino.

## Por qué importa

Permite reintentar sin miedo. Cuando la red falla, el cliente no sabe si el servidor recibió la operación; reintentar es la única opción, y solo es segura si aplicar la operación dos veces equivale a aplicarla una. Una repetición inofensiva además evita coordinar: no hace falta un protocolo para saber si ya se hizo.

## Cómo funciona

SE-260 explica que el cliente, ante un error de red, no distingue entre «la petición no llegó» y «llegó y se perdió la respuesta». Reintentar sin idempotencia puede aplicar el efecto dos veces. RFC 9110 define la idempotencia de los métodos HTTP como propiedad **del efecto**, no de la forma de la petición: `PUT` lo es, `POST` no por defecto.

Hay dos caminos para lograrla. **Cambiar qué se envía**: en lugar de «incrementa el contador» (no idempotente), se envía «la entrega 42 fue recibida» (idempotente: registrar el hecho dos veces deja el mismo estado), o «fija la nota en 6,0» en lugar de «suma 0,5». **Añadir un identificador único por operación** que el servidor recuerda: una clave de idempotencia permite que operaciones no idempotentes por naturaleza (crear, cobrar) se reintenten con seguridad. Del lado del receptor de mensajes, el equivalente es el consumidor idempotente.

SE-171 y SE-260 sitúan esto en el contexto de un cliente que sincroniza con conflictos: la política de conflicto por dato (último escritor, conservar ambas versiones, fusionar operaciones) interactúa con la idempotencia. Un fallo que aparece sin ella: un comentario añadido sin conexión desaparece porque se copió el estado de la última réplica en llegar; fusionar operaciones, no estados, lo evita.

## Ejemplo

El cliente envía `PUT /entregas/42/nota {valor: 6.0}`. La respuesta se pierde y reintenta. El servidor aplica «nota = 6,0» dos veces: el estado es el mismo. Con `POST /entregas/42/ajustes {suma: 0.5}`, el mismo reintento daría 7,0 en lugar de 6,5; la corrección es o cambiar el mensaje a «nota = 6,5» o enviar con una clave de idempotencia. (Ilustración del principio de SE-260 y SE-392.)

## Errores y confusiones comunes

- **Creer que reintentar es siempre seguro.**
- **Confundir idempotente con «sin efectos»**: tiene efecto, una vez.
- **Asumir que `POST` es idempotente.**
- **Idempotente respecto del estado, no de la respuesta**: el segundo `DELETE` puede devolver otro código sin cambiar el estado.

## Límites y cuándo no aplica

No todas las operaciones se pueden reformular como idempotentes (enviar un correo, cobrar); ahí se usan claves de idempotencia y deduplicación. La idempotencia no resuelve el orden ni la concurrencia: dos operaciones idempotentes distintas pueden interferir entre sí.
