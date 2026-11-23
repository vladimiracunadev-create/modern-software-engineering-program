# Compatibilidad hacia atrás

## Definición

Un cambio es **compatible hacia atrás** (*backward compatible*) cuando lo que ya funcionaba con la versión anterior sigue funcionando con la nueva. El programa lo usa en dos planos que conviene no mezclar. En el plano de una **API o paquete** (`SE-110`), una versión nueva es compatible hacia atrás si los consumidores válidos anteriores siguen funcionando bajo el contrato publicado. En el plano de **datos y mensajes** (`SE-164`, `SE-366`, `SE-380`), lo es si un lector que usa el esquema nuevo puede leer datos escritos con el esquema viejo. Es el opuesto direccional de la compatibilidad **hacia adelante**, en que un lector viejo entiende datos nuevos; un cambio que cumple ambas es **completo**.

## Por qué importa

Los sistemas reales no se actualizan todos a la vez: hay clientes sin migrar, colas con mensajes retenidos, registros de meses y consumidores que se despliegan antes que sus productores. La compatibilidad es la propiedad que permite cambiar una parte sin coordinar el instante exacto de cambio de todas las demás. Decide, además, cuánto tiempo hay que mantener una versión: `SE-380` observa que un log retenido durante meses exige compatibilidad hacia atrás durante meses, y esa duración, no el código, fija cuánto vive cada versión.

## Cómo funciona

La compatibilidad no es una propiedad solo del esquema; depende de cómo lee el consumidor y de en qué dirección viaja el dato (`SE-164`, `SE-380`).

- **Qué dirección necesitas.** Cuando hay datos viejos que leer (un almacén que se lee con código nuevo, una cola atrasada, un consumidor que se despliega primero) necesitas compatibilidad hacia atrás. Cuando hay lectores viejos activos mientras los productores ya escriben con el esquema nuevo (una API que se actualiza primero en el servidor) necesitas compatibilidad hacia adelante.
- **Lector tolerante o estricto.** Un lector tolerante usa los campos que conoce e ignora los demás; uno estricto rechaza cualquier campo desconocido. Con el primero, añadir un campo es compatible hacia adelante; con el segundo, no.
- **Orden de despliegue.** Con un cambio compatible hacia atrás se despliegan primero los consumidores (leen lo nuevo y lo viejo) y después los productores; con uno compatible solo hacia adelante, primero los productores; con uno incompatible no hay orden seguro y hay que dividirlo en fases (`SE-380`).
- **Comprobación automática.** El número de versión comunica intención, pero nadie verifica que diga la verdad: `SE-164` insiste en comparar esquemas en integración continua y exigir versión mayor para las rupturas, y `SE-380` describe el registro de esquemas que rechaza un cambio incompatible antes de publicarlo.

## Ejemplo

`SE-164` aplicó diez cambios a un esquema de cuatro campos (`id` y `nota` requeridos, `estado` requerido con dos valores y `comentario` opcional) y midió cuántos de 2 000 documentos se leían sin error. Quitar un campo opcional se leyó en las tres situaciones. Añadir un campo requerido se leyó para el lector viejo tolerante, pero el lector nuevo no pudo leer ninguno de los documentos viejos (0 de 2 000): ese cambio no es compatible hacia atrás. Renombrar un campo no se leyó en ninguna situación, lo que muestra que «renombrar» no es un cambio sino una eliminación seguida de una adición. Los números provienen de datos sintéticos de la clase.

## Errores y confusiones comunes

- **«Solo agrega» y rompe a un cliente.** El cliente es estricto con campos o valores desconocidos. Corrección (`SE-164`): documentar que los consumidores deben tolerar lo desconocido y probar con un valor nuevo.
- **El número de versión sube y los clientes se rompen igual.** Se versionó por intención y no se comprobó la compatibilidad. Corrección: comparar esquemas en integración continua.
- **Añadir un valor de enumeración.** Ningún registro de formas lo detecta: ambos lectores viejos rechazan el valor nuevo, y la política del consumidor ante lo desconocido decide si es un incidente o una pérdida silenciosa (`SE-380`).
- **Confundir las dos direcciones.** Atrás habla del lector nuevo y los datos viejos; adelante, del lector viejo y los datos nuevos. Muchos cambios son compatibles en una sola.
- **Una ventana de deprecación que termina con clientes activos.** Parte de los consumidores no migra sola; hay que medir quién usa lo viejo y decidir el corte con un responsable (`SE-164`).

## Límites y cuándo no aplica

Cumplir una regla de compatibilidad no garantiza que un cambio sea seguro: `SE-110` advierte que agregar un parámetro opcional puede romper reflexión, mocks o serialización, de modo que la evaluación necesita pruebas reales y no solo la intuición de quien cambia. SemVer es un lenguaje común, no una prueba: una «versión menor» que cambia el significado de un campo rompe igual (`SE-164`). El registro de esquemas conoce la forma, no el sentido, y no sustituye el ensayo con consumidores reales. Y mantener compatibilidad tiene un costo: cuanto más tiempo se sostiene una versión, más caminos de código y datos viejos hay que conservar.
