# Instancia

## Definición

En el sentido principal de `SE-253` (modelos de aplicación móvil y de escritorio), una **instancia** es una copia de la aplicación en ejecución; un modelo puede permitir varias a la vez o una sola. `SE-277` usa el término de otra manera: en WebAssembly, una instancia es un módulo con su memoria y sus importaciones ya enlazadas. «Instancia» también aparece en la expresión «instancia de un servicio», que se acerca al sentido principal.

## Por qué importa

Permitir varias copias convierte cada archivo local en un recurso compartido con varios escritores. Decidir si la aplicación admite una o varias instancias es decidir si hay un problema de concurrencia sobre los archivos que usa, aunque nadie escriba código concurrente.

## Cómo funciona

`SE-253`: un escritorio permite abrir la misma aplicación varias veces, salvo que se prohíba; un teléfono normalmente presenta una sola. Cuando hay varias, el archivo del borrador tiene dos escritores que no se conocen, y la última escritura pisa a la otra (el mismo mecanismo de la actualización perdida). Hay tres salidas:

1. **Aceptar la competencia y detectarla** (por ejemplo, con una versión en el archivo).
2. **Coordinar con un bloqueo** de archivo.
3. **Impedir la segunda copia.** Electron ofrece un mecanismo para obtener un bloqueo de instancia única.

Cada solución añade una regla que hay que explicar a quien usa la aplicación.

En WebAssembly (`SE-277`), instanciar es enlazar el módulo con su memoria e importaciones; de un mismo módulo pueden crearse varias instancias independientes.

## Ejemplo

El equipo del cliente de entregas (`SE-253`) escribe una tabla de supuestos con una fila por modelo (teléfono, escritorio, ventana dividida) y una columna por supuesto: proceso permanente, copia única, ancho mínimo, estado en memoria. Cada celda es «se cumple», «no se cumple» o «depende», con su fuente; las «depende» se vuelven pruebas. La decisión: guardar el borrador en disco en cada pausa, impedir la segunda instancia en el escritorio y diseñar primero a 320 píxeles.

## Errores y confusiones comunes

- **Suponer una sola instancia en el escritorio:** puede haber varias y compiten por el mismo archivo.
- **Resolverlo sin avisar a la persona,** que no entiende por qué la segunda ventana no abre.
- **Confundir instancia con proceso o con hilo,** o con la instancia de una máquina virtual en la nube.
- **Mezclar los dos sentidos:** instancia de WebAssembly no es una copia de la aplicación.

## Límites y cuándo no aplica

La tabla de supuestos describe modelos de plataforma de la fecha de la clase; las reglas de ventanas y de procesos cambian entre versiones. En una aplicación web, cada pestaña es otro contexto y el problema se plantea con otros mecanismos (almacenamiento del navegador).
