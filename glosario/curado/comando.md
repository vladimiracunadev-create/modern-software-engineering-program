# Comando

## Definición

Un **comando** es un mensaje que expresa una intención dirigida a un destinatario esperado y que puede ser rechazada (`SE-374`). Se nombra en imperativo («califica esta entrega») y se contrapone al evento, que describe un hecho ya ocurrido.

## Por qué importa

Distinguir comando de evento decide quién conoce a quién y qué ocurre si nadie responde. Con un comando, el emisor sabe qué quiere que pase y quién debe hacerlo; por eso necesita saber si se aceptó. Confundirlo con un evento lleva a difundir una orden a todos los oyentes y a que la acción ocurra varias veces, o a no notar que nadie la ejecutó.

## Cómo funciona

Tres rasgos lo definen en `SE-374`:

1. **Destinatario esperado**: está dirigido a quien debe ejecutarlo. Un comando sin manejador es un error que debe ser visible, no un mensaje que se pierde en silencio.
2. **Imperativo**: nombra lo que se quiere que ocurra, no lo que ocurrió.
3. **Puede ser rechazado**: el receptor valida y puede negarse (la entrega no existe, el plazo venció). Por eso el emisor suele necesitar el resultado.

La diferencia con el evento es de cardinalidad y de acoplamiento: un comando espera **uno** y falla si no está; un evento acepta **cero o muchos**. En un evento, quien lo emite no sabe quién lo escucha; en un comando, el emisor depende de que alguien lo atienda, de modo que el acoplamiento es más fuerte y deliberado. La falla clásica es difundir el comando a todos los oyentes: cada uno lo ejecuta y la acción ocurre varias veces.

## Ejemplo

`CalificarEntrega(entrega_id=17, nota=8)` va a un manejador concreto. Este puede rechazarlo si la entrega no existe o si el plazo venció, y responde aceptado o rechazado. En cambio `EntregaCalificada` es un evento: se publica después de que ocurrió y lo pueden leer cero, uno o varios servicios (aviso por correo, estadísticas) sin que el emisor lo sepa. Ejemplo ilustrativo siguiendo la distinción de `SE-374`.

## Errores y confusiones comunes

- **Una acción se ejecuta varias veces**: un comando se difundió a varios oyentes; se corrige con un destinatario por comando y rechazo si no hay uno (`SE-374`).
- **Nombrarlo en pasado**: un comando en pasado se lee como evento y oculta quién debe actuar.
- **Ignorar el rechazo**: asumir que fue aceptado sin confirmar.
- **Enviar un evento esperando que alguien lo ejecute**: el evento no garantiza ningún destinatario.

## Límites y cuándo no aplica

El comando es adecuado cuando el emisor sabe qué quiere y quién debe hacerlo. Si el emisor solo anuncia un hecho y le da igual quién reaccione, es un evento. Un comando asíncrono no elimina la necesidad de manejar reintentos y duplicados: sigue sujeto a la semántica de entrega y requiere un manejador idempotente si puede repetirse. Y exigir respuesta acopla en tiempo al emisor con el receptor; conviene valorarlo frente a un enfoque basado en eventos.
