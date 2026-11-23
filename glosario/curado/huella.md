# Huella

## Definición

Una **huella** es un valor derivado del contenido de un archivo, un resultado, una configuración o una especificación, normalmente un resumen criptográfico como SHA-256, que cambia si cambia el contenido. Es el término que el programa usa para lo que la bibliografía llama *hash* o *checksum*: `SE-225` la define como un valor de longitud fija que cambia si cambia cualquier bit, `SE-248` como un valor derivado del contenido que permite comprobar su integridad y `SE-469` como un valor calculado a partir de los bytes de un artefacto. Diez clases la usan, siempre con el mismo núcleo y con funciones distintas: comprobar integridad, comparar ejecuciones, fijar dependencias, detectar cambios en una herramienta o identificar datos y configuraciones.

## Por qué importa

Permite responder «¿es el mismo contenido?» sin comparar el contenido entero y sin confiar en la memoria de nadie. Sirve para detectar un archivo truncado o corrupto (`SE-248`), para fijar una dependencia por su contenido y no solo por su nombre (`SE-469`), para saber si dos ejecuciones produjeron lo mismo (`SE-504`, `SE-516`), y para detectar que una herramienta aprobada cambió (`SE-571`). La clave de su utilidad es una condición: la huella solo prueba **identidad de contenido**, no autoría.

## Cómo funciona

Un resumen criptográfico produce un valor de longitud fija a partir de cualquier cantidad de bytes y cambia si cambia un solo bit. `SE-225` lo contrasta con alternativas: un archivo de 20 MB con un bit alterado cambia de huella (CRC32, MD5 y SHA-256) pero no de longitud; truncado o ampliado cambia ambas. Un CRC32 detecta errores accidentales, pero tiene 32 bits: en la simulación se encontró una colisión entre dos mensajes de 8 bytes tras 87 650 intentos, de modo que no protege frente a una alteración deliberada.

Los usos en el programa, cada uno con su variante:

- **Integridad de lo recibido** (`SE-248`): el cliente envía la huella al principio o al final y el servidor la compara con la del contenido recibido; para calcularla no hace falta tener el archivo entero en memoria, se actualiza trozo a trozo.
- **Builds reproducibles** (`SE-469`): las dependencias se fijan por huella; si dos extracciones del repositorio dan huellas distintas, la causa suelen ser saltos de línea convertidos, fechas o rutas incrustadas.
- **Resultados comparables** (`SE-504`, `SE-516`): el resumen de un resultado serializado de forma determinista permite comparar ejecuciones.
- **Herramientas aprobadas** (`SE-571`): una huella del nombre, la descripción y el esquema de una herramienta detecta cualquier cambio, incluso de un carácter invisible, y obliga a una nueva aprobación.
- **Experimentos** (`SE-603`): el registro de una corrida guarda la huella de los datos, de las etiquetas y de la configuración.

## Ejemplo

En `SE-603`, regenerar los datos con la misma semilla produjo la misma huella, y con otra semilla una distinta: es la prueba mínima de que la huella detecta lo que debe detectar. En `SE-225`, un archivo sintético de 20 MB alterado de tres maneras (un bit cambiado, truncado en 1 000 bytes y con 16 bytes añadidos) cambia de huella en las tres, mientras que un archivo idéntico coincide en todo.

## Errores y confusiones comunes

- **Alguien sustituyó el archivo y su hash.** La huella viaja por el mismo canal que el archivo; quien puede alterar uno puede alterar el otro. Corrección (`SE-225`): una firma con una clave pública que el cliente conozca por otro camino.
- **Confundir integridad con autenticidad.** La huella detecta corrupción accidental; para un atacante que controla el archivo y la huella no prueba autenticidad (`SE-248`).
- **«Cada build produce un hash distinto».** Fechas, orden o rutas incrustadas; corrección (`SE-469`): normalizar tiempo y orden y eliminar rutas.
- **Una revisión que se vuelve rutina.** Con una huella sin triaje, toda actualización legítima dispara la alerta y se deja de leer (`SE-571`).

## Límites y cuándo no aplica

Una huella no prueba el origen: `SE-225` separa explícitamente integridad y origen y exige una firma para lo segundo. Es sensible a detalles de formato (saltos de línea convertidos por el control de versiones, orden de campos, fechas), de ahí que `SE-504` serialice de forma determinista antes de resumir y que `SE-469` pida fijar la normalización de la fuente. Y el algoritmo importa: `SE-225` muestra que CRC32, con 32 bits, no protege frente a una alteración deliberada.
