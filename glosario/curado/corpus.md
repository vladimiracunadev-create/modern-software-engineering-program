# Corpus

## Definición

En pruebas con *fuzzing*, el **corpus** es el conjunto de entradas que un fuzzer conserva y muta (`SE-426`). (En recuperación de información, «corpus» designa el conjunto de documentos indexados; aquí es el de las pruebas.)

## Por qué importa

El corpus es la memoria del fuzzer: cada entrada que descubre nuevo comportamiento se conserva y se muta, de modo que la búsqueda avanza en vez de empezar de cero.

## Cómo funciona

Un fuzzer genera variantes de las entradas del corpus y conserva las que alcanzan código nuevo o provocan fallos. Su trabajo termina en una entrada que falla; lo útil después es **reducirla**, entender la causa y fijarla como prueba. `SE-426` insiste en que una entrada hallada y no convertida en prueba reaparece la próxima vez que alguien cambie el código: la entrada mínima se guarda como caso de regresión, el defecto se corrige y el fuzzer sigue con la entrada original en su corpus.

## Ejemplo

Un analizador de archivos recibe un corpus inicial de unos pocos archivos válidos; tras horas, el fuzzer encuentra una entrada que cuelga el analizador; se reduce a 12 bytes, se añade como prueba y se corrige.

## Errores y confusiones comunes

Descartar el corpus entre ejecuciones; no convertir los hallazgos en pruebas de regresión.

## Límites y cuándo no aplica

Un corpus pobre limita lo que se explora; el *fuzzing* encuentra fallos, no demuestra su ausencia.
