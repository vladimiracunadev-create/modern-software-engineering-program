# Relleno por lotes

## Definición

El **relleno por lotes** es la actualización de una columna en muchas filas dividida en transacciones cortas e idempotentes (`SE-354`). Es el paso de una migración que lleva los datos existentes a la estructura nueva sin bloquear el sistema.

## Por qué importa

Actualizar cien mil filas con una sola sentencia parece lo más simple, pero mantiene una transacción larga que puede congelar la aplicación. La decisión que cambia es cómo se migran los datos de un sistema en uso: poco a poco, de forma que se pueda interrumpir y reanudar, y no de una sola vez.

## Cómo funciona

`SE-354` explica el daño de la transacción larga según el motor. En uno con **bloqueo de escritura**, los demás escritores esperan todo ese tiempo. En uno con **versiones**, la transacción retiene espacio y retrasa la limpieza. En ambos, la aplicación se degrada mientras dura la migración.

El remedio es **dividir en lotes**: cada uno es una transacción corta que confirma y libera. El tamaño es un equilibrio: lotes pequeños reducen el bloqueo pero aumentan el número de transacciones y la sobrecarga; lotes grandes hacen lo contrario. La clase lo mide en un experimento y propone elegir según el tiempo de bloqueo tolerable.

Dos propiedades hacen seguro el procedimiento:

- **Idempotente**: cada lote se puede repetir sin efecto adicional. Por ejemplo, un `UPDATE ... WHERE columna_nueva IS NULL` solo toca lo que falta.
- **Reanudable**: tras un corte a mitad, se continúa donde quedó (por ejemplo, avanzando por un rango de identificadores), sin empezar de nuevo.

Es la fase de «migrar» del patrón de expandir y contraer: la estructura nueva ya existe y se rellena mientras ambas versiones de la aplicación siguen funcionando. Termina antes del punto de no retorno.

## Ejemplo

Para rellenar `calificacion` desde `nota` en 100 000 filas, un trabajo procesa 1 000 filas por transacción, actualizando solo las que tienen `calificacion` nula, y avanza por identificador. Si se interrumpe, al relanzarlo solo procesa lo que falta. La aplicación sigue respondiendo porque ninguna transacción dura mucho. Ejemplo de la línea de `SE-354`.

## Errores y confusiones comunes

- **El panel se congela al ejecutar una migración**: actualización de muchas filas en una transacción; se corrige con relleno por lotes idempotente y reanudable.
- **Lotes no idempotentes**: un reintento duplica el efecto.
- **No poder reanudar**: obliga a empezar de cero.
- **Elegir el tamaño sin medir** el bloqueo real.

## Límites y cuándo no aplica

Para tablas pequeñas, una sola sentencia puede ser aceptable y más simple. El relleno por lotes no protege contra escrituras concurrentes que cambian la columna origen durante el proceso: requiere mantener sincronizadas ambas columnas (doble escritura) mientras dura. El tamaño óptimo de lote depende del motor y de la carga; el experimento de la clase usa datos sintéticos.
