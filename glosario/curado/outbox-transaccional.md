# Outbox transaccional

## Definición

El **outbox transaccional** es una tabla que vive en la misma base de datos que el cambio de negocio y en la que se guardan los mensajes que hay que publicar. La operación inserta la fila de negocio y la fila del mensaje dentro de la misma transacción. `SE-377` lo enseña como patrón de integración y `SE-241` lo presenta como la tabla de la que un relevo lee los eventos pendientes para publicarlos después. Aquí «outbox» significa la tabla más su relevo, no un servicio de mensajería.

## Por qué importa

Cuando un servicio debe cambiar su base y avisar a otros, hay dos escrituras en dos sistemas, y no existe una transacción que abarque ambos. Quien no usa outbox elige entre dos fallos: publicar después de confirmar (si el proceso cae en medio, la entrega queda guardada sin evento) o publicar antes (se emite un evento de una entrega que luego no se confirmó). El outbox cambia la decisión de diseño: «publicar» deja de ser un paso de la petición y pasa a ser un dato durable que se entrega con reintentos. `SE-377` resume la ganancia así: ya no existen entregas sin evento ni eventos sin entrega.

## Cómo funciona

1. La operación de negocio abre una transacción, escribe el cambio y escribe una fila en la tabla `outbox` (identificador, tipo, clave, cuerpo, fecha de creación y una marca de publicación). Confirma: o existen ambas filas o ninguna, porque la atomicidad la da el motor de base de datos.
2. Un proceso aparte, el **relevo**, lee lotes de filas sin marca de publicación, las envía al corredor de mensajes y las marca como publicadas.
3. Una tarea de limpieza elimina las filas publicadas tras un plazo de retención.

El punto delicado está entre publicar y marcar. Si el relevo cae justo ahí, al reiniciar volverá a publicar el mensaje. Por eso el outbox da entrega **al menos una vez**, no exactamente una vez, y exige que quien recibe sea idempotente. `SE-377` lo cierra con su contraparte, la **inbox**: una tabla con el identificador del mensaje como clave primaria, donde el receptor hace `INSERT OR IGNORE` en la misma transacción que aplica el efecto. Un duplicado choca con la clave y no repite el efecto.

## Ejemplo

El ejemplo de `SE-377` es la plataforma de entregas: la tabla `outbox(id, tipo, clave, cuerpo, creado, publicado_en)` está en la misma base de las entregas; el relevo lee lotes de 100 filas sin `publicado_en`, publica, marca y limpia lo publicado hace más de siete días. Si se cae entre publicar y marcar, el mensaje sale de nuevo, y el calificador lo absorbe con su inbox. Un esbozo (ilustración, no código del programa):

```sql
BEGIN;
INSERT INTO entrega (id, estado) VALUES (42, 'registrada');
INSERT INTO outbox (id, tipo, clave, cuerpo, creado)
VALUES ('m-42', 'entrega.registrada', '42', '{"entrega":42}', now());
COMMIT;
```

## Errores y confusiones comunes

- **Publicar después de confirmar sin outbox**: entregas guardadas sin evento (`SE-377`).
- **Publicar antes de confirmar**: eventos de entregas que no existen (`SE-377`). La corrección es publicar solo desde el outbox, tras el commit.
- **Creer que el outbox da «exactamente una vez»**: da al menos una vez; la unicidad la aporta el receptor idempotente.
- **Olvidar la limpieza y la latencia**: la tabla crece y el evento llega con el retraso del relevo.

## Límites y cuándo no aplica

El outbox exige que el cambio de negocio y la tabla compartan base de datos; si el estado vive en varias bases, no basta. Añade una tabla, un proceso que operar y latencia. No resuelve por sí solo el orden global de los eventos ni la compensación de pasos fallidos, que `SE-377` trata con sagas. Los experimentos de la clase usaron datos sintéticos y un motor real solo para outbox e inbox, sin corredor ni relevos concurrentes: no se extrapolan a producción.
