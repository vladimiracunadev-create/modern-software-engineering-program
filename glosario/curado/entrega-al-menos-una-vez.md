# Entrega al menos una vez

## Definición

La **entrega al menos una vez** (*at-least-once delivery*) es la garantía de que un mensaje llegará una o más veces, nunca cero, sin impedir los duplicados. Es el sentido de `SE-319`, `SE-241`, `SE-362`, `SE-400` y `SE-247`: el mensaje no se pierde, pero puede repetirse, y quien lo recibe debe tolerar duplicados.

## Por qué importa

Es la garantía que ofrecen en la práctica la mayoría de colas y sistemas de eventos, porque es la que se puede cumplir sin coordinación costosa. Cambia el diseño del receptor: no se pregunta «¿llegará dos veces?» sino «¿qué pasa cuando llegue dos veces?». Ignorarlo produce cobros dobles, correos repetidos o contadores inflados.

## Cómo funciona

`SE-400` explica el origen: si el consumidor no confirma, el mensaje se reenvía. La cola no puede saber si el consumidor procesó el mensaje y perdió la confirmación, o si nunca llegó a procesarlo (`SE-247`: no sabe si el trabajador cayó antes o después de ejecutar el efecto, solo que no confirmó). Para no perder, reentrega. Consecuencia: el manejador puede ver el mismo evento dos o más veces.

La defensa es la **idempotencia**: procesar un evento repetido produce el mismo estado que procesarlo una vez, por ejemplo guardando el identificador del evento y descartando los ya vistos. `SE-400` cita CloudEvents: el identificador, junto con la fuente, distingue un evento de otro, y un reenvío puede conservar su identificador, justo lo que permite reconocerlo. En `SE-377`, la **inbox** (tabla con el identificador como clave primaria) lo implementa con `INSERT OR IGNORE` en la misma transacción que el efecto.

## Ejemplo

Un trabajador recibe «enviar certificado 42», lo envía y cae antes de confirmar. La cola reentrega y el trabajador vuelve a recibirlo. Si guarda el identificador del mensaje en la misma transacción que el efecto, el segundo intento se descarta. Ilustración propia; el patrón está en `SE-247` y `SE-377`.

## Errores y confusiones comunes

- **Suponer «exactamente una vez»:** casi nunca se ofrece de extremo a extremo; se logra combinando al menos una vez con receptor idempotente.
- **Hacer efectos no idempotentes en el manejador** (enviar dinero, enviar un correo) sin clave de deduplicación.
- **Confirmar antes de procesar,** que convierte la garantía en «como máximo una vez» y pierde mensajes.
- **Confundirla con idempotencia:** la entrega es del transporte; la idempotencia es del receptor.

## Límites y cuándo no aplica

Si el efecto es inofensivo repetido, el problema desaparece sin más. Si el efecto no se puede deduplicar (un sistema externo que no acepta claves), hace falta otro diseño. La garantía describe al transporte; el orden de los mensajes es otro asunto que no ofrece.
