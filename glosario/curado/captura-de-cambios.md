# Captura de cambios

## Definición

La **captura de cambios** (CDC, por *change data capture*) es el mecanismo que produce un flujo ordenado de altas, cambios y bajas de filas de una base de datos: «se insertó la fila X», «se actualizó la fila Y de este valor a este», «se borró la fila Z» (`SE-378`).

## Por qué importa

Sincronizar una base con un almacén analítico u otro sistema puede hacerse copiando todo cada vez, o detectando qué cambió. La captura de cambios decide si el destino se entera de **todo** lo ocurrido, incluidas las bajas y los cambios intermedios, o solo de una foto. Para quien diseña integración, es la diferencia entre un destino que converge con el origen y uno que conserva filas que ya no existen.

## Cómo funciona

`SE-378` presenta dos formas de producir el flujo:

- **Disparadores**: cada escritura inserta una fila en una tabla de cambios dentro de la misma transacción. Son simples y se ven en el esquema, pero añaden una escritura a cada operación.
- **Lectura del registro de escritura anticipada** del motor, como la decodificación lógica de PostgreSQL o conectores como Debezium. No toca las operaciones de la aplicación, pero exige permisos y operar el conector.

La causa de que la captura exista es una limitación de la alternativa: la detección por marca de tiempo solo ve filas que existen y cuya marca cambió. Un borrado no deja fila que comparar, así que el destino conserva lo que el origen ya eliminó; y una comparación estricta con la última marca pierde las filas modificadas en el mismo instante. Un flujo de eventos de fila evita ambos fallos porque registra el cambio como hecho, incluida la baja.

## Ejemplo

Una plataforma replica su tabla de entregas a un almacén analítico. Con detección por marca, una entrega eliminada sigue apareciendo en el almacén. Con captura de cambios, el flujo trae un evento de baja y el destino la retira. Como el consumidor puede recibir un evento repetido, aplica los eventos de forma idempotente. Es el patrón que enseña `SE-378` con datos sintéticos.

## Errores y confusiones comunes

- **El destino tiene filas que ya no existen en el origen**: la detección por marca no ve las bajas; corrección, registro de cambios o lápidas con borrado lógico.
- **Faltan filas modificadas en el último segundo**: comparación estricta con la última marca; corrección, comparar con mayor o igual y aplicar de forma idempotente.
- **Creer que los disparadores son gratis**: añaden escritura a cada operación.
- **Confundirla con replicación del motor**: la captura produce eventos de fila reutilizables, no una copia física.

## Límites y cuándo no aplica

`SE-378` declara que sus experimentos son sintéticos, sin motor con registro lógico, conector, almacén ni red; los ritmos y porcentajes son construcciones del autor, por lo que no son una medición de un sistema real. En la práctica, la captura no resuelve por sí sola el orden entre tablas ni la evolución del esquema, y la lectura del registro exige operar el conector. Para volúmenes pequeños con cambios poco frecuentes, una recarga completa puede bastar.
