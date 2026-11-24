# Webhook

## Definición

Un **webhook** es una petición HTTP `POST` que un sistema (el proveedor) dirige a una dirección de otro (el receptor) para avisarle de un evento, con un cuerpo que describe lo ocurrido (`SE-379`). `SE-412` lo usa en el contexto de pagos: el mensaje que el procesador envía al producto para notificar un evento.

## Por qué importa

En lugar de preguntar periódicamente al proveedor si algo cambió, el receptor recibe el aviso cuando ocurre. Pero esa comodidad trae un contrato implícito que, si no se entiende, produce pérdidas, duplicados y eventos falsos. La decisión que cambia es cómo se escribe el receptor: no como una función que aplica el cambio, sino como un buzón que verifica, guarda y responde rápido.

## Cómo funciona

`SE-379` describe cuatro partes del contrato implícito:

1. El receptor debe **responder rápido** con un código de éxito: el proveedor considera fallida cualquier respuesta lenta o de error, y reintenta.
2. **No se garantiza orden** entre eventos.
3. Se puede recibir el **mismo evento más de una vez**.
4. **No hay garantía** de haberlos recibido todos.

Por eso el cuerpo debe tratarse como un **aviso**, y el tratamiento real (por ejemplo, aplicar una nota o actualizar una suscripción) hacerse de forma asíncrona e idempotente: el manejador **verifica, guarda en una cola y responde**; un trabajador procesa aparte. La verificación es la **firma**: el proveedor firma el cuerpo con un HMAC y un secreto compartido, y el receptor la comprueba con una comparación de tiempo constante; sin ella, cualquiera que conozca la dirección puede crear eventos falsos.

Como no hay garantía de recibirlos todos, el webhook se combina con una **reconciliación** periódica: el webhook es la pista de baja latencia y el sondeo (listar lo ocurrido desde un punto de control) la red de seguridad. Los dos mecanismos no son excluyentes.

## Ejemplo

Un procesador de pagos envía un webhook «pago confirmado». El manejador verifica la firma HMAC, guarda el evento en una cola y devuelve 200 en milisegundos. Un trabajador lo procesa de forma idempotente, de modo que si el evento llega dos veces no se activa la suscripción dos veces. Cada hora, un trabajo lista los pagos recientes del proveedor y procesa los que faltaron. Mecanismo de `SE-379`.

## Errores y confusiones comunes

- **Alguien crea eventos falsos con una herramienta**: la dirección del webhook no verifica firma; se corrige con firma HMAC y comparación de tiempo constante.
- **El proveedor desactiva el webhook**: respuestas lentas o de error durante mucho tiempo; se corrige respondiendo rápido, encolando y procesando aparte, con alarma por fallos.
- **Procesar dentro del manejador**: una demora provoca reintentos y duplicados.
- **Asumir orden y entrega exacta**.

## Límites y cuándo no aplica

No sirve como única fuente de verdad: puede perder eventos y no garantiza orden. Para consultas que requieren el estado actual, se pregunta al proveedor. Y exige exponer una dirección pública y operar su seguridad, lo que no siempre es posible detrás de ciertas redes; en ese caso el sondeo es la alternativa.
