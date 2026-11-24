# Selectividad

## Definición

La **selectividad** de una condición es la fracción de filas que deja pasar (`SE-353`). `SE-339` la usa en el sentido general de la proporción de elementos que un filtro deja pasar. Una condición es muy selectiva cuando deja pasar pocas filas y poco selectiva cuando deja pasar la mayoría.

## Por qué importa

Un índice no ayuda por existir: ayuda cuando permite evitar leer la mayor parte de la tabla. Eso depende de la selectividad de las condiciones de las consultas. La decisión que cambia es dónde se crean índices: sobre condiciones que seleccionan pocas filas, y no sobre columnas con pocos valores distintos donde casi todas las filas cumplen.

## Cómo funciona

`SE-353` lo explica con dos casos. Buscar un estudiante entre 2 000 devuelve una fracción mínima: el índice permite ir directo a esa fila y evita recorrer el resto. En cambio, cuando una condición selecciona la mayoría (el 90 % de las entregas están «enviadas»), recorrer el índice y luego leer casi todas las filas cuesta casi lo mismo que recorrer la tabla; y puede costar más, porque cada fila exige un salto adicional desde el índice. Por eso un índice sobre una columna con pocos valores distintos solo es útil para sus valores **raros**.

La selectividad explica el síntoma más común: se crea un índice y la consulta no mejora. La clase da un procedimiento de prueba: mirar el plan (¿usa el índice?), actualizar las estadísticas, comparar los pasos con y sin índice y calcular la fracción de filas que cumple. Si el plan usa el índice, el ahorro es del 3 % y la fracción es el 90 %, la causa es la baja selectividad.

El motor decide usando estadísticas sobre la distribución de valores: por eso el plan puede cambiar al variar los datos o al actualizar las estadísticas. En `SE-339` el mismo concepto aparece en el diseño de filtros dentro de flujos de procesamiento: la proporción que pasa condiciona el tamaño de lo que sigue.

## Ejemplo

La tabla de entregas tiene la columna `estado`, con el 90 % de las filas en «enviada». Un índice sobre `estado` no mejora la consulta por «enviada», porque habría que leer casi toda la tabla; sí podría ayudar para el estado raro «en revisión», que selecciona una fracción pequeña. Ejemplo de `SE-353`.

## Errores y confusiones comunes

- **Se crea un índice y la consulta no mejora**: condición poco selectiva o forma que no coincide con el prefijo; se corrige mirando el plan y la selectividad antes y después.
- **Indexar columnas de pocos valores** sin considerar sus valores raros.
- **Suponer que la selectividad es una propiedad de la columna**: lo es de la condición sobre los datos actuales.
- **No actualizar estadísticas** y decidir con datos viejos.

## Límites y cuándo no aplica

El umbral a partir del cual un índice deja de compensar depende del motor y de cómo están almacenadas las filas; no hay una cifra universal. Los experimentos de `SE-353` usan datos sintéticos y SQLite, y sus resultados no se extrapolan a otros motores. En tablas pequeñas, recorrerlas completas puede ser igual de rápido y el índice solo añade costo de escritura.
