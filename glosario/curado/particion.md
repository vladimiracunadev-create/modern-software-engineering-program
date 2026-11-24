# Partición

## Definición

**Partición** es una subdivisión de un conjunto mayor tratada como unidad. El programa la usa con varios sentidos:

- **De una tabla** (`SE-364`): un subconjunto, normalmente por fecha, que se escribe y se reescribe como unidad.
- **De un log** (`SE-375`): una subdivisión que se lee en orden y se asigna a un solo consumidor de un grupo.
- **De un dominio de entrada** (`SE-060`, `SE-062`): un subdominio tratado de forma equivalente por una rama o por una prueba.

## Por qué importa

Particionar permite reprocesar, paralelizar o probar por partes en lugar de tocar todo. En datos, es lo que hace que corregir un error de origen cueste una tarde y no una semana. En mensajería, determina cuánto paralelismo admite un grupo de consumidores. En pruebas, permite cubrir un dominio infinito con un representante por clase.

## Cómo funciona

- **Tablas** (`SE-364`): una carga idempotente por partición. Una operación es idempotente si aplicarla varias veces produce el mismo estado que aplicarla una; la propiedad es del trabajo completo, no de cada sentencia: un `INSERT` solo no lo es, y un `DELETE` de la partición seguido de un `INSERT` dentro de una transacción sí lo es. En un lago de datos sin transacciones de fila, reemplazar particiones suele ser la opción realista.
- **Logs** (`SE-375`): cada partición se lee en orden y se asigna a un solo consumidor del grupo. Eso garantiza orden dentro de la partición, no entre particiones, y limita el paralelismo al número de particiones.
- **Dominios** (`SE-060`, `SE-062`): se parte el espacio de entradas en clases de equivalencia; basta un representante de cada una, más las fronteras.

## Ejemplo

`SE-364`: el equipo de *Avisos* descubre que su trabajo de lecturas diarias usa `date('now')` y añade filas sin condición. Lo reescribe: recibe la fecha de la partición como parámetro, borra e inserta la partición dentro de una transacción y reprocesa los tres días anteriores para recoger lecturas tardías. Ilustración:

```sql
BEGIN;
DELETE FROM lecturas WHERE dia = :dia;
INSERT INTO lecturas SELECT * FROM staging WHERE dia = :dia;
COMMIT;
```

## Errores y confusiones comunes

- **Un consumidor ocioso y otro saturado.** Causa: pocas particiones o clave popular; corrección: más particiones solo si no es una clave caliente, y revisar la clave (`SE-375`).
- **Usar `date('now')` para elegir la partición.** Hace el trabajo no repetible; la fecha debe ser un parámetro (`SE-364`).
- **Confundir las particiones de datos con las de dominio.** Comparten el verbo, no el mecanismo.

## Límites y cuándo no aplica

Más particiones no siempre dan más rendimiento: el orden solo se garantiza dentro de cada una, y una clave mal elegida concentra la carga. Reemplazar particiones supone que la unidad de reescritura es la correcta. Y la idempotencia de `SE-364` se prueba ejecutando dos veces y comparando filas y suma de control, no se asume.
