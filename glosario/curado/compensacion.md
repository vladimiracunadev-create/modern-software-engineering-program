# Compensación

## Definición

Una **compensación** es una acción **nueva** que deshace o neutraliza el efecto de un paso anterior, sin borrarlo del historial (`SE-377`). No es una reversión: reembolsar un cobro no «des-cobra», y cancelar un cupo no borra que alguien lo vio ocupado. Es el mecanismo con que una saga se recupera cuando no puede haber una transacción única que abarque varios servicios.

## Por qué importa

En un flujo que cruza sistemas, un fallo a mitad de camino deja efectos reales ya producidos. La decisión que cambia es cómo se diseña el flujo: no se pregunta solo «cómo hago cada paso» sino «cómo se contrarresta cada paso si falla uno posterior» y, sobre todo, «qué pasos no tienen contrapartida». Esa pregunta decide el orden de los pasos.

## Cómo funciona

`SE-377` fija las ideas centrales:

- La compensación es otra operación de negocio, visible y registrada, con sus propios efectos (el reembolso aparece en el extracto).
- Algunas acciones **no tienen compensación**: un correo enviado, un archivo publicado. Son pasos irreversibles.
- La regla de diseño: ordenar los pasos de modo que los compensables vayan primero y el irreversible lo más tarde posible. Ese paso se llama **pivote**: tras él la saga solo puede avanzar, y los pasos posteriores deben poder reintentarse hasta lograrse.
- Las compensaciones también fallan. Por eso deben ser **idempotentes**, reintentables y dejar un estado «atascado» observable si no logran terminar, para que alguien actúe.

`SE-573` lleva esto a los flujos con agentes: un flujo queda a medias cuando no hay compensación o las compensaciones fallan, y la corrección es compensar con reintentos y registro. En `SE-411` el término aparece en el contexto de una plataforma SaaS, donde un aprovisionamiento a medias debe poder deshacerse.

## Ejemplo

Una inscripción reserva un cupo, cobra y envía un correo de bienvenida. Si el cobro falla, se compensa el cupo liberándolo. Si el correo es el último paso y es irreversible, se coloca después de los compensables: el cobro, que sí tiene compensación (reembolso), va antes. Si el envío falla tras el pivote, no se deshace el cobro; se reintenta el envío. Ejemplo ilustrativo del orden que enseña `SE-377`.

## Errores y confusiones comunes

- **Un flujo queda a medias** (`SE-573`): sin compensación o con compensaciones que fallan; se corrige compensando con reintentos y registro.
- **Creer que compensar es revertir**: el efecto original sigue existiendo y visible.
- **Compensación no idempotente**: un reintento reembolsa dos veces.
- **Poner el paso irreversible al principio**: se pierde la posibilidad de deshacer lo demás.

## Límites y cuándo no aplica

No todo se puede compensar, y la compensación no restituye el estado anterior exacto: terceros pudieron haber observado el estado intermedio. Cuando la consistencia inmediata es indispensable y todo ocurre en una sola base, una transacción local es más simple y segura que una saga con compensaciones. Y una compensación mal diseñada añade más fallos de los que evita: requiere reintento, registro y alertas sobre los casos atascados.
