# Transacción

## Definición

Una **transacción** es un conjunto de operaciones que se aplican enteras o no se aplican, y que se observan según el nivel de aislamiento (`SE-351`). `SE-256` la formula como un grupo de escrituras que se confirman o se descartan juntas y que, en una base transaccional, deja siempre un estado completo; `SE-032` la usa para un conjunto de cambios tratado como unidad según las garantías del gestor (por ejemplo, de paquetes).

## Por qué importa

Sin transacciones, una falla a mitad de camino deja datos a medias: una transferencia cortada puede descontar de un lado y no acreditar del otro. La transacción delimita qué es «un cambio» para la base y permite razonar sobre el sistema en términos de antes y después. Cambia dónde se escriben los límites de una operación de negocio.

## Cómo funciona

El modelo clásico (ACID) combina cuatro garantías: **atomicidad** (todo o nada), **consistencia** (se respetan las reglas), **aislamiento** (cómo se ven entre sí las transacciones concurrentes) y **durabilidad** (lo confirmado sobrevive). `SE-351` destaca que el aislamiento tiene niveles: cuanto más débil, más anomalías observables. El mecanismo típico es un registro de escritura previa: la base anota los cambios antes de aplicarlos y, ante una caída, rehace o deshace según corresponda.

Costos concretos (`SE-256`): una transacción por cada edición con sincronización completa a disco hace que guardar un borrador tarde segundos con muchas ediciones; la solución es agrupar escrituras y elegir un modo de sincronización explícito.

Atomicidad no es idempotencia: `SE-364` muestra que un `INSERT` solo no es idempotente, pero un `DELETE` de la partición seguido de un `INSERT` dentro de una transacción sí lo es; la propiedad es del trabajo completo, no de cada sentencia.

## Ejemplo

```sql
BEGIN;
UPDATE cupos SET libres = libres - 1 WHERE curso = 'SE-101' AND libres > 0;
INSERT INTO matriculas(curso, estudiante) VALUES ('SE-101', 42);
COMMIT;      -- o ROLLBACK si falla cualquiera de los dos pasos
```

## Errores y confusiones comunes

- **Una transferencia cortada deja cupos perdidos.** Causa: sentencias confirmadas por separado; corrección: envolver los pasos en una transacción e idempotencia (`SE-351`).
- **Guardar un borrador tarda segundos con muchas ediciones.** Causa: una transacción por edición con sincronización completa; corrección: agrupar escrituras y elegir un modo de sincronización explícito (`SE-256`).
- **Suponer transacciones entre servicios.** Una operación que cruza servicios deja de ser atómica; se necesita una saga.

## Límites y cuándo no aplica

En un lago de datos sin transacciones de fila, reemplazar particiones suele ser la opción realista (`SE-364`). Un aislamiento fuerte cuesta rendimiento y puede provocar esperas o reintentos; elegir el nivel es una decisión por operación. Y una transacción no protege efectos fuera de la base (correos enviados, llamadas externas): esos requieren compensación o idempotencia.
