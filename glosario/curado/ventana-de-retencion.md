# Ventana de retención

## Definición

La **ventana de retención** es el tiempo durante el cual el servidor recuerda una clave de idempotencia y su respuesta. Es el sentido de `SE-246` (idempotencia, reintentos y deduplicación). `SE-319` usa la misma idea para los identificadores de mensaje de un receptor idempotente, con una ventana finita (por ejemplo, 7 días). No es un periodo de conservación legal de datos, aunque comparta el nombre con él.

## Por qué importa

Una clave que caduca antes del reintento más tardío deja pasar el duplicado. El servidor no puede recordar claves para siempre, y de la ventana depende que la protección contra duplicados sea real.

## Cómo funciona

`SE-246`: el servidor guarda, por cada clave, la huella de la carga y la respuesta, y las retiene un tiempo. El tiempo de vida debe cubrir **el reintento más tardío que un cliente legítimo pueda hacer**. Una aplicación móvil sin conexión puede reintentar horas o días después. Si la clave caduca antes, el reintento crea un duplicado indistinguible de una solicitud nueva.

Alargar la ventana cuesta almacenamiento, y se compensa con claves compactas y limpieza periódica. Por eso la decisión es un cálculo de dos extremos: el reintento legítimo más tardío (cota inferior) y el costo de guardar (cota superior).

En un receptor idempotente (`SE-319`), la misma lógica fija cuánto tiempo se conservan los identificadores vistos y exige que el canal no reenvíe un mensaje más tarde que esa ventana.

## Ejemplo

La plataforma de `SE-246` exige `Idempotency-Key` en `POST /entregas` y en `POST /entregas/{id}/apelaciones`; guarda la clave, la huella de la carga y la respuesta en la misma transacción que el efecto; devuelve 422 si la clave llega con otra carga; y la retiene 7 días, que es el reintento más tardío del cliente móvil. El cliente reintenta solo 429, 503 y tiempos agotados, con retroceso exponencial, jitter total, un máximo de 5 intentos y respeto de `Retry-After`.

## Errores y confusiones comunes

- **Entregas duplicadas tras un error de red:** POST sin clave de idempotencia; corrección, clave por intención y restricción única (`SE-246`).
- **Ventana menor que el reintento más tardío.**
- **Guardar la clave sin la huella de la carga:** una clave reutilizada con otra carga pasa inadvertida.
- **Confundirla con el TTL de una caché:** aquí un olvido produce un duplicado, no un dato viejo.

## Límites y cuándo no aplica

La ventana no protege contra un reintento posterior a ella; hace falta que el cliente deje de reintentar antes. Si el cliente puede reenviar indefinidamente (una cola persistente), la ventana debe alinearse con esa política. El valor de 7 días es de la plataforma de la clase, no una recomendación general.
