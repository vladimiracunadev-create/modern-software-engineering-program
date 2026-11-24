# Actualización perdida

## Definición

Una **actualización perdida** (*lost update*) ocurre cuando una escritura se pisa con otra que se basó en una lectura anterior, sin que ninguna de las dos falle. `SE-351` la presenta como una anomalía de concurrencia en transacciones; `SE-242` usa el mismo término en HTTP: una escritura posterior sobrescribe otra sin haberla visto. El rasgo que la hace peligrosa es el silencio: ningún cliente recibe un error.

## Por qué importa

Es de los defectos de datos más difíciles de ver, porque el sistema «funciona»: cada petición tiene éxito y aun así el estado final no corresponde a ninguna ejecución ordenada. `SE-351` muestra el síntoma típico: un contador queda por debajo de las operaciones confirmadas. La decisión que cambia es dónde se hace el cálculo y qué mecanismo protege el ciclo leer-calcular-escribir.

## Cómo funciona

Leer un valor, calcular el nuevo y escribirlo son tres pasos. Si dos clientes los intercalan:

1. A lee 10. B lee 10.
2. A escribe 11. B escribe 11.
3. Debían ser 12; la escritura de A se perdió.

`SE-351` da tres remedios con costos distintos:

- **Que la base calcule:** `UPDATE ... SET n = n + 1`. Es la más barata cuando el cálculo cabe en una expresión, porque lectura y escritura ocurren en una sola sentencia.
- **Comprobar la versión al escribir y reintentar** si cambió. Conviene cuando el cálculo ocurre en la aplicación y los conflictos son raros. En HTTP es la misma idea que `SE-242` enseña con una precondición sobre la versión del recurso.
- **Bloquear la fila** mientras se calcula. Conviene cuando los conflictos son frecuentes, a costa de esperas.

## Ejemplo

El ejemplo mínimo de `SE-351` ejecuta dos clientes que leen el mismo valor y escriben, y pide predecir el valor final antes de correrlo. Un esbozo ilustrativo (no es código de la clase):

```sql
-- Cliente A y B, intercalados: ambos leen n = 10
UPDATE cuenta SET n = 11 WHERE id = 1; -- A
UPDATE cuenta SET n = 11 WHERE id = 1; -- B (debía ser 12)
-- Corrección: UPDATE cuenta SET n = n + 1 WHERE id = 1;
```

## Errores y confusiones comunes

- **Contador por debajo de lo confirmado** por leer-modificar-escribir sin control (`SE-351`).
- **Creer que una transacción lo impide siempre.** Depende del nivel de aislamiento y del motor; la clase modela niveles de aislamiento, pero no ejecutó un motor con instantáneas.
- **Confundirla con una lectura sucia o una condición de carrera en memoria:** aquí cada escritura es válida; lo que falla es la base de la que partió.

## Límites y cuándo no aplica

Solo existe cuando hay lectura previa que alimenta la escritura; una escritura que no depende de lo leído («fija el estado en cerrado») no la sufre, aunque puede decidirse si la última escritura debe ganar. Los experimentos de `SE-351` forzaron intercalaciones en un solo hilo con SQLite y no midieron rendimiento ni contención; las cifras describen enumeraciones, no frecuencias reales.
