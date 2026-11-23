# Contrato

## Definición

Un **contrato** es la descripción verificable de lo que una pieza de software promete a quienes la usan y de lo que espera de ellos. Es una de las palabras más cargadas del programa y su sentido cambia con la pieza de la que se hable, siempre con el mismo núcleo (qué entra, qué sale, qué se garantiza):

- **De una función o programa:** `SE-030` lo define como la definición observable de entradas, salidas, errores y efectos.
- **De un tipo o clase:** `SE-302` lo concreta como el conjunto de precondiciones, poscondiciones e invariantes que un cliente puede esperar de un tipo.
- **De una herramienta de línea de comandos:** `SE-072` lo compone de nombre, subcomandos, opciones, flujos (`stdin`, `stdout`, `stderr`) y códigos de salida, que son interfaz pública.
- **Entre un proveedor y un consumidor:** `SE-423` lo define como la descripción verificable de lo que un consumidor espera de un proveedor (campos, tipos, valores, orden).
- **De una arquitectura con complementos:** `SE-338` lo entiende como interfaz, versión y garantías que el núcleo ofrece a los complementos y viceversa.

En el programa, «contrato» no significa un acuerdo legal ni un documento aparte: significa una promesa **observable y comprobable**.

## Por qué importa

Sin contrato escrito, cada persona infiere de la implementación lo que puede esperar, y cualquier cambio interno rompe a alguien. El contrato fija la frontera: lo que está dentro puede cambiar con libertad, lo que está en el contrato solo cambia con un proceso de versión. También convierte el diagnóstico en una pregunta con respuesta: cuando algo falla, se puede preguntar si incumplió el proveedor o el consumidor. `SE-069` lo muestra con una suite de 15 pruebas donde el nombre de cada prueba es una frase del contrato, de modo que un fallo se lee como diagnóstico.

## Cómo funciona

Un contrato se sostiene en tres actos: **escribirlo**, **ejecutarlo** y **versionarlo**.

1. **Escribirlo.** Se declaran las entradas válidas, las salidas, los errores y los efectos. Para una clase se usan precondiciones (obligación del llamador), poscondiciones (obligación de quien implementa) e invariantes (válidos antes y después de cada operación pública), como en `SE-052`, `SE-159` y `SE-302`.
2. **Ejecutarlo.** Un contrato que no se comprueba es documentación que se desactualiza. Las pruebas de contrato (`SE-423`) comprueban lo que el consumidor espera del proveedor, y los mismos casos pueden ejecutarse en otro lenguaje: en `SE-071`, un puerto en Rust debe cumplir los mismos cuatro casos del archivo de contrato que la referencia en Python; lo que se transfiere es el contrato observable, no la sintaxis ni el paquete.
3. **Versionarlo.** Cambiar un contrato es cambiar una promesa. Las reglas de compatibilidad (`SE-110`, `SE-164`) distinguen qué cambios no rompen a los consumidores existentes.

La causa de que el contrato de una herramienta de línea de comandos importe tanto la explica `SE-072`: una herramienta es una API cuyo consumidor es otro programa. Si los mensajes de error se mezclan con los datos en `stdout`, el comando deja de poder encadenarse en una tubería.

## Ejemplo

`SE-072` invocó una herramienta de diagnóstico con catorce entradas en Windows y Linux. La ruta feliz produjo código de salida 0 y un JSON en `stdout`, sin una línea en `stderr`. Los argumentos ausentes terminaron con 2 y un mensaje de uso; un JSON roto o una línea inválida, con 3; una prueba no autorizada, repetida o contradictoria, con 4; un archivo ausente o no UTF-8, con 5. En todos los errores, `stdout` quedó vacío y `stderr` tuvo una línea JSON con `error` y `detail`. Ese conjunto de reglas es el contrato; permite escribir `herramienta ... | otra_herramienta` sin que un error contamine los datos.

## Errores y confusiones comunes

- **Probar solo el caso feliz.** Se usa el ejemplo como especificación; hay que derivar del contrato los casos de error, vacío y frontera (`SE-069`).
- **«Funciona» en otro lenguaje pero falla un caso.** Se tradujo la sintaxis sin el contrato; la corrección es ejecutar los mismos casos en ambos (`SE-071`).
- **Confundir el contrato de un laboratorio con un estándar.** Los códigos 0/2/3/4/5 de `SE-072` son del laboratorio; POSIX solo fija 0 como éxito.
- **Pensar que un mapa de pruebas mide la protección.** Dice qué prueba apunta a qué contrato, no cuán bien lo protege (`SE-069`).

## Límites y cuándo no aplica

Un contrato describe lo que se prometió, no lo que ocurre fuera de lo prometido: los límites del contrato educativo de `SE-072` (por ejemplo, el tamaño máximo de entrada) no protegen contra otros agotamientos como la memoria o la CPU con entradas patológicas. Un contrato escrito y un contrato comprobado son cosas distintas, y solo el segundo se mantiene vivo. Y como la palabra tiene varios sentidos, en cada clase hay que confirmar a cuál se refiere antes de trasladar una conclusión de una a otra.
