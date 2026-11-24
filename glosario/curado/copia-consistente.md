# Copia consistente

## Definición

Una **copia consistente** es una copia que corresponde a un único instante confirmado de la base de datos (`SE-357`). No basta con que cada página del archivo sea válida: el conjunto debe reflejar un momento en que todas las transacciones confirmadas estaban completas y ninguna a medias.

## Por qué importa

Una copia de seguridad solo vale si se puede restaurar a algo correcto. Copiar el archivo de una base mientras otra transacción escribe puede producir una copia con parte de los cambios y no el resto: cada página es válida, pero el conjunto no corresponde a ningún momento. La decisión que cambia es cómo se hacen las copias: con una técnica que garantice el instante, no con una copia de archivos con la base en uso.

## Cómo funciona

`SE-357` presenta tres caminos:

1. **Parar las escrituras** durante la copia.
2. **Usar un mecanismo del motor** que tome una instantánea consistente: la API de copia en línea de SQLite, `pg_dump` o la copia base con archivado de PostgreSQL.
3. **Copiar a nivel del sistema de archivos** con una instantánea atómica.

Lo que no es seguro es la **copia ingenua con la base en uso**. Y su peligro es doble: puede dar «éxito» y además pasar una comprobación estructural, porque cada página individual es válida. El fallo está en la relación entre páginas, que la comprobación de estructura no examina. Por eso `SE-357` pide verificar con reglas de negocio (por ejemplo, que los totales cuadren) y no solo con la integridad del archivo; esa verificación se completa con la prueba de restauración.

En el experimento de la clase, con bases de SQLite y 200 mutaciones, se compara la copia ingenua con la copia consistente: la primera produce restauraciones que «terminan bien» con datos erróneos; la segunda, no.

## Ejemplo

Una plataforma copia el archivo de su base cada noche mientras sigue recibiendo entregas. Una noche la copia coincide con una transacción que modifica dos tablas relacionadas: la copia contiene el cambio de una tabla y no el de la otra. La comprobación de integridad pasa. Meses después se restaura y los datos no cuadran. Con la API de copia en línea o con una instantánea atómica, la copia corresponde a un instante confirmado.

## Errores y confusiones comunes

- **La restauración termina bien y los datos son erróneos**: copia ingenua con la base en uso; se corrige con la API de copia consistente y verificación de negocio (`SE-357`).
- **Dar por buena una copia porque pasó la comprobación estructural**.
- **Copiar archivos con el motor en marcha** pensando que el sistema de archivos ya es atómico.
- **No restaurar nunca**: una copia que no se ha restaurado es una hipótesis.

## Límites y cuándo no aplica

`SE-357` aclara que sus experimentos usan bases pequeñas de SQLite y datos sintéticos; las 200 mutaciones son construcciones del autor y los fallos de la primera simulación son uniformes. No se midió el tiempo de restauración ni se probó cifrado, almacenamiento remoto, otro motor o datos de producción. Una copia consistente da un instante: cuánta información se pierde entre ese instante y el fallo lo define el objetivo de punto de recuperación y, si se necesita menos pérdida, el archivado continuo del registro de cambios.
