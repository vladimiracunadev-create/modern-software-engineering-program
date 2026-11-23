# Saga

## Definición

Una **saga** es una secuencia de transacciones locales, cada una en un servicio distinto, en la que cada paso tiene una **compensación** que contrarresta su efecto si un paso posterior falla. Sustituye a una transacción atómica global entre servicios, que en un sistema distribuido o no existe o es demasiado cara. `SE-377` la desarrolla con ese sentido; `SE-327` y `SE-340` la nombran como la alternativa a la transacción atómica cuando un monolito se divide en servicios, y `SE-411` la usa en el alta y el aprovisionamiento de clientes de un producto SaaS.

## Por qué importa

Cuando un proceso cruza servicios con bases de datos propias, no hay una transacción única que garantice «todo o nada». Sin un mecanismo explícito, un fallo a mitad de camino deja un cobro sin pedido o un pedido sin envío. La saga no devuelve la atomicidad: sustituye la promesa de «todo o nada» por la de **consistencia eventual con reparación**, y obliga a diseñar de antemano qué significa deshacer cada paso.

## Cómo funciona

Según `SE-377`, una saga divide el proceso en pasos locales; cada uno confirma su propia transacción y publica el siguiente. No hay bloqueos entre servicios ni aislamiento: mientras la saga corre, otros observan estados intermedios. Si un paso falla, la saga ejecuta las **compensaciones** de los pasos ya completados **en orden inverso**.

Hay dos formas de coordinarla:

- **Coreografiada:** cada servicio reacciona a los eventos de los demás, sin coordinador. Reduce el acoplamiento y dificulta saber en qué estado va un proceso.
- **Orquestada:** un coordinador conoce el flujo y ordena cada paso. Concentra ese conocimiento en un lugar que hay que operar y proteger.

La compensación no es un «deshacer» exacto: es una acción de negocio que contrarresta el efecto (reembolsar un cobro, liberar un cupo), y por eso también puede fallar y se reintenta, lo que la obliga a ser idempotente (véase idempotencia en `SE-246`).

## Ejemplo

En la simulación de `SE-377` se ejecutan sagas sobre un corredor en memoria con tres fuentes de fallo: caídas entre pasos (3 %), fallos de un paso (8 %) y fallos de compensación (10 % por intento, hasta tres intentos), con semilla fija. El ejercicio muestra por qué la compensación necesita reintentos y por qué una saga puede quedar en un estado intermedio observable. Las tasas son supuestos del autor de la clase, no mediciones de un sistema real.

## Errores y confusiones comunes

- **Pensar que la saga es una transacción distribuida.** No tiene aislamiento: otros procesos ven estados intermedios y hay que diseñar para ello (`SE-377`).
- **Compensaciones que no son idempotentes.** Una compensación reintentada dos veces puede reembolsar dos veces.
- **Olvidar que la compensación no siempre es posible.** Un correo enviado no se «desenvía»: una compensación es una acción de negocio que contrarresta el efecto, no un deshacer exacto.
- **Confundir coreografía con ausencia de diseño.** Sin coordinador, saber en qué estado va un proceso exige observabilidad explícita.

## Límites y cuándo no aplica

Las clases declaran los límites del experimento: las tasas de fallo son iguales y constantes para todos los pasos, mientras que en un sistema real el cobro falla más que el envío de un correo; además no se modelan sagas concurrentes ni lecturas de estados intermedios (`SE-377`). Una saga se justifica cuando el proceso cruza servicios con almacenes propios; si todo cabe en una base de datos con una transacción local, la transacción ordinaria es más simple y ofrece más garantías. Tampoco deshace por sí sola un efecto externo irreversible, como un correo ya enviado.
