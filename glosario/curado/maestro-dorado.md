# Maestro dorado

## Definición

Un **maestro dorado** (*golden master*) es el registro de las salidas de un programa para un conjunto de entradas, usado como oráculo para detectar cambios de comportamiento (`SE-311`). `SE-323` y `SE-519` lo usan en el mismo sentido: la salida del código actual para un conjunto fijo de entradas, contra la cual se compara el código nuevo.

## Por qué importa

Refactorizar código sin pruebas finas exige saber si el comportamiento cambió, pero definir primero qué es correcto puede ser costoso o imposible. La decisión que cambia es qué se toma como referencia: no «lo correcto», sino «lo que el código hace hoy». Con eso, cualquier diferencia es un cambio de comportamiento que hay que explicar.

## Cómo funciona

`SE-311` es explícito con lo que el maestro **no** afirma: no dice que las salidas sean correctas; dice que son lo que el código hace hoy. Eso le da su uso: como oráculo de un refactor. Se ejecuta el código actual con un conjunto grande de entradas, se guardan las salidas, y tras cada paso del refactor se vuelve a ejecutar y se compara. Una diferencia no es necesariamente un error, pero sí un cambio que alguien debe aprobar o corregir.

Su calidad depende de las entradas: deben cubrir los caminos y los bordes, incluidas las entradas «raras» que los clientes reales envían. Un maestro con entradas limpias deja pasar cambios que rompen a los canales antiguos. Por eso `SE-519` lo combina con medición de cobertura y de mutantes, y con normalizar la variación (fechas, identificadores aleatorios) para que no genere diferencias falsas. El procedimiento completo de esa clase: crear una costura, registrar un maestro dorado, medir cobertura y mutantes, normalizar la variación y decidir qué hacer con cada comportamiento sospechoso.

Una práctica de disciplina: comparar tras cada paso y hacer un commit por paso, de modo que si el comportamiento cambia se sabe qué paso lo cambió.

## Ejemplo

Una función de tarifas heredada no tiene pruebas. Se ejecuta con miles de combinaciones de entrada reales y se guardan los resultados. Se refactoriza en pasos pequeños; tras cada uno se compara con el maestro. En un paso aparece una diferencia en un caso de un canal antiguo: se detecta antes de desplegar. Procedimiento de `SE-311` y `SE-519`.

## Errores y confusiones comunes

- **El refactor pasa las pruebas y rompe a un cliente**: el maestro no incluye entradas de canales antiguos; se añaden las entradas reales (valores no booleanos, formatos viejos).
- **No se sabe qué paso cambió el comportamiento**: se hicieron varios pasos antes de comparar; se compara tras cada paso con un commit por paso.
- **Tomarlo como especificación**: registra lo que hace, incluidos sus defectos.
- **No normalizar la variación**: las fechas y los aleatorios producen diferencias falsas.

## Límites y cuándo no aplica

`SE-323` lo limita: es útil cuando la función **no tiene** pruebas finas y se quiere refactorizar sin definir primero qué es correcto; las pruebas unitarias documentan la intención, y donde existen son preferibles. El maestro fija también los defectos actuales, así que no sirve para corregir comportamiento. Y solo ve lo que las entradas cubren: sin buena cobertura, da una falsa confianza.
