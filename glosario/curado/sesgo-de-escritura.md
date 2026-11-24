# Sesgo de escritura

## Definición

El **sesgo de escritura** (*write skew*) es la anomalía en la que dos transacciones leen lo mismo, escriben filas distintas y juntas rompen una invariante (`SE-351`). Ninguna sobrescribe lo que la otra escribió, y sin embargo el resultado combinado viola una regla que implica a ambas filas.

## Por qué importa

Es un error de concurrencia sutil: cada transacción es correcta por separado y no hay conflicto de escritura que la detenga. Sucede en un nivel de aislamiento que muchos sistemas usan por defecto. La decisión que cambia es cómo se protege una regla que abarca varias filas: no alcanza con asumir que las transacciones «aíslan» lo suficiente.

## Cómo funciona

`SE-351` lo describe con una invariante: «siempre queda un docente de guardia». Dos docentes de guardia piden salir a la vez. Cada transacción lee que hay dos docentes de guardia, decide que puede salir, y actualiza **su propia** fila. Como escriben filas distintas, ningún conflicto de escritura las detiene; al final no queda ninguno.

Es la anomalía característica de las **instantáneas** (aislamiento basado en versiones): cada transacción lee una foto consistente del inicio, y esa foto no refleja lo que la otra está haciendo. La actualización perdida, por contraste, sí es un conflicto de escritura sobre la misma fila y las instantáneas la detectan; el sesgo no.

La clase da tres formas de evitarlo:

1. **Nivel serializable**: el motor detecta y aborta la combinación peligrosa.
2. **Bloqueo explícito** sobre lo que se lee: obliga a esperar al otro.
3. **Convertir la invariante en algo que una sola fila resume**: por ejemplo, un contador de docentes de guardia que ambas transacciones actualizan; al escribir la misma fila, se serializan.

## Ejemplo

Dos transacciones leen «hay 2 docentes de guardia». T1 marca a A como libre; T2 marca a B como libre. Ninguna toca la fila de la otra, ambas confirman y no queda nadie de guardia. Con un contador `guardias` que ambas decrementan solo si es mayor que 1, la segunda transacción entra en conflicto en esa fila y se serializa. Caso de `SE-351`.

## Errores y confusiones comunes

- **Dos operaciones sanas rompen una regla conjunta**: sesgo de escritura bajo instantánea; se corrige con serializable, bloqueo explícito o resumen en una fila.
- **Creer que evitar actualizaciones perdidas basta**: el sesgo ocurre sin escribir la misma fila.
- **Confiar en el aislamiento por defecto** sin conocer su nivel.
- **Validar la invariante solo en la lectura**.

## Límites y cuándo no aplica

`SE-351` aclara que sus experimentos forzaron las intercalaciones en un solo hilo con SQLite; los niveles de aislamiento son un modelo del autor y no se ejecutó PostgreSQL ni otro motor con instantáneas; no se midió rendimiento, contención ni durabilidad ante apagones, y las cifras describen enumeraciones, no frecuencias. Los motores con aislamiento serializable pagan costo en reintentos y abortos. Si la regla no abarca varias filas, no hay sesgo posible.
