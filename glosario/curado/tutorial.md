# Tutorial

## Definición

Un **tutorial** es, en SE-206, una página que guía a quien aprende por pasos hacia un resultado seguro, sin ramificar ni explicar. Es uno de los cuatro tipos de documentación (tutorial, guía práctica, referencia, explicación) y el orientado al aprendizaje.

## Por qué importa

Lleva a quien aprende a un éxito garantizado; no debe explicar ni ramificar. Su propósito es dar confianza a una persona principiante: si falla o se llena de opciones, la persona cree que el error es suyo. Cambia cómo se escribe: no es un resumen del sistema sino una lección con un camino único.

## Cómo funciona

Un tutorial es **una lección**: quien lo escribe asume la responsabilidad de que quien lo sigue **llegue a un resultado y gane confianza**. De ahí sus reglas. Los pasos son **pocos, concretos y verificables**; cada uno **muestra lo que se debe ver** («verás un mensaje de confirmación»). **Nada ramifica**: «si usas otra versión, haz esto» pertenece a otra página. **No explica por qué** las cosas son así; a lo sumo dice «ahora verás» y da una frase de contexto, y enlaza a una explicación para quien quiera saber más.

En la plataforma, el tutorial «Tu primera entrega con retraso» lleva a una persona nueva a hacer una entrega tardía y ver el descuento aplicado. Se distingue de la guía práctica, que supone competencia previa y admite bifurcaciones.

El riesgo que SE-206 destaca: **un tutorial se rompe en silencio cuando el entorno cambia** y deja a quien aprende creyendo que el error es suyo. Por eso es el tipo que **más gana si se ejecuta en cada cambio**: un script ejecuta los pasos contra la biblioteca o el sistema y reporta cuáles pasan. El fragmento de la clase ejecuta los pasos de un tutorial y pide predecir qué pasos fallan si se renombra `entregar` a `enviar`. Tres fallos y sus correcciones: notas avanzadas a mitad de los pasos (se mueven a una explicación con un enlace de una línea), tutorial que funciona en la máquina de quien lo escribió y no en otra (depende de un estado previo no declarado: se ejecuta desde un entorno limpio en integración continua) y explicación que nadie encuentra (se enlaza desde el tutorial, la guía y la referencia).

## Ejemplo

Paso 3 del tutorial: «Ejecuta `entregar --archivo mi-tarea.pdf --tarde`. Verás: `Entrega recibida. Descuento: 10 %`». Si tras renombrar el comando a `enviar` el paso falla, la integración continua lo detecta y el tutorial se corrige antes de que alguien lo siga. (Ejemplo ilustrativo del mecanismo de SE-206.)

## Errores y confusiones comunes

- **Mezclar explicación con aprendizaje** («Notas avanzadas» a mitad).
- **Depender de un estado previo no declarado.**
- **Ramificar** según versiones o preferencias.
- **No ejecutarlo nunca**: se rompe en silencio.

## Límites y cuándo no aplica

No sirve a quien ya sabe y busca resolver una tarea (necesita una guía práctica) ni a quien quiere entender las razones (necesita una explicación). Un tutorial largo pierde a quien aprende; se divide en lecciones. Su mantenimiento tiene costo, que se reduce al automatizar su ejecución.
