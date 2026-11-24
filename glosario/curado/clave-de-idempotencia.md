# Clave de idempotencia

## Definición

Una **clave de idempotencia** es un identificador único por operación que el cliente genera una vez para una intención y reutiliza en todos sus reintentos; el servidor la recuerda para no aplicar dos veces el mismo efecto. Es el sentido común a `SE-264`, `SE-392`, `SE-246`, `SE-417` y `SE-596`. Aplica a operaciones que por naturaleza no son idempotentes (como un POST que crea un cobro): la clave les da esa propiedad.

## Por qué importa

Cambia la decisión de si es seguro reintentar. Según `SE-264`, cuando el servidor aplica una operación y la respuesta se pierde, el cliente no puede distinguir ese caso de aquel en que la petición nunca llegó. Sin clave, reintentar aplica dos veces: cobros, entregas o pedidos duplicados. Con clave, el reintento es seguro y la red poco fiable deja de ser un riesgo de negocio.

## Cómo funciona

El servidor guarda, por cada clave, la huella del cuerpo y el resultado (`SE-392`). Si la clave llega de nuevo con el mismo cuerpo, devuelve el resultado guardado sin repetir el efecto. Dos detalles la hacen segura:

- **Huella del cuerpo.** Si llega la misma clave con otro cuerpo, es un error del cliente que reutilizó la clave, y debe rechazarse, no responder con el resultado de otra petición.
- **Atomicidad.** Guardar la clave y aplicar el efecto deben ocurrir en la misma transacción; por separado, una caída entre ambos deja un efecto sin clave (el reintento duplica) o una clave sin efecto (el reintento no hace nada).

`SE-417` añade que, en pagos, la clave identifica la operación de negocio y se guarda con una duración declarada. RFC 9110 define la idempotencia por el efecto de la operación; la clave es el mecanismo que la implementa donde el método no la da por sí solo (`SE-264`).

## Ejemplo

En el fragmento de `SE-264`, un cliente pide 30 operaciones y la red provoca reintentos hasta sumar 44 peticiones. Sin clave el servidor aplica 44 operaciones; con clave aplica exactamente 30, con las mismas 44 peticiones. La clase pide predecir el número antes de ejecutar, para que la diferencia se vea como consecuencia del mecanismo y no del azar.

## Errores y confusiones comunes

- **Reintento sin clave.** El servidor aplica más operaciones de las pedidas; corrección de `SE-264`: identificador único por operación y deduplicación en el servidor.
- **Generar una clave nueva en cada reintento.** Equivale a no tener clave: la clave debe ser estable por intención.
- **Guardar la clave sin atomicidad.** Reabre la ventana de duplicados o de efectos perdidos.
- **Reutilizar la clave para otra operación.** Debe detectarse con la huella del cuerpo.
- **Confundir con «retroceso exponencial».** Este espacia los reintentos; la clave los hace seguros.

## Límites y cuándo no aplica

La clave debe conservarse un tiempo acotado y declarado: el servidor no puede recordarla para siempre, y pasada la ventana un reintento tardío se trataría como nuevo. Protege contra repeticiones de la misma intención, no contra dos intenciones legítimamente iguales (dos compras idénticas con claves distintas). Los números del ejemplo de `SE-264` provienen de un experimento sintético. Y no sustituye una restricción única en la base de datos cuando la deduplicación debe valer por encima del servicio.
