# Atomicidad

## Definición

La **atomicidad** es la propiedad de una operación que se confirma completa o no deja efectos, y que ningún otro contexto observa a medias. Las clases la presentan en dos escalas del mismo hecho: `SE-318` y `SE-351` como «se confirma completa o no deja efectos» (el punto de vista de quien ejecuta, típico de una transacción de base de datos y de la unidad de trabajo) y `SE-269` como «ningún otro contexto observa la operación a medias» (el punto de vista de quien observa, típico de interrupciones, hilos y estado compartido). No es sinónimo de rapidez ni de «una sola línea de código»: es la garantía de todo o nada.

## Por qué importa

Un proceso puede detenerse en cualquier instante: por un corte de energía, un error o una orden de terminación. Sin atomicidad, el estado queda a medio camino y nadie lo avisa. `SE-351` lo ilustra con una transferencia de cupos de cuatro pasos (registrar, descontar, sumar, cerrar) cortada en el tercero: el sistema queda con 55 cupos en lugar de 60. Lo grave es que el sistema sigue funcionando con un estado inválido.

## Cómo funciona

Una transacción agrupa varias sentencias de modo que, si falla cualquiera, ninguna deja huella (`SE-351`). La causa de que no dependa de la velocidad es que un corte puede llegar en cualquier punto, por rápida que sea la secuencia: lo que se necesita es un mecanismo que permita deshacer o descartar lo hecho a medias. En una base de datos, ese mecanismo es la transacción con confirmación y reversión; en SQLite y PostgreSQL abarca también las sentencias de definición de esquema (`SE-354`), pero en otros motores no.

En estado compartido, `SE-269` explica por qué una línea no es atómica: `contador++` se traduce en leer el valor, sumar uno y escribirlo. Si una interrupción incrementa el mismo contador entre la lectura y la escritura, el programa principal escribe el valor viejo más uno y borra el incremento de la interrupción. De las diez posiciones posibles de una interrupción dentro de una vuelta de diez instrucciones, solo las dos situadas entre la lectura y la escritura pierden el incremento, y por eso una prueba corta rara vez lo ve. Se corrige enmascarando las interrupciones durante esas instrucciones, con una operación atómica del procesador o con un diseño donde solo un contexto escribe.

## Ejemplo

El caso de `SE-351`: una transferencia de cupos en cuatro pasos (registrar, descontar, sumar, cerrar). Sin transacción, si el proceso se corta en el tercer paso, el sistema queda con 55 cupos en lugar de 60 y nadie lo avisa. Con los cuatro pasos dentro de una transacción, o se aplican los cuatro o ninguno, y el total permanece en 60. Son números del experimento de la clase.

## Errores y confusiones comunes

- **Creer que una secuencia rápida es atómica.** La atomicidad no depende de la velocidad: un corte puede llegar en cualquier punto (`SE-351`).
- **Creer que una línea de código es atómica.** `contador++` son tres instrucciones; una interrupción entre la lectura y la escritura pierde el incremento (`SE-269`).
- **Confundir atomicidad con idempotencia.** La primera garantiza todo o nada en una ejecución; la segunda, que repetir no cambie el efecto. `SE-224` pide distinguir qué parte del diseño dependía de cada una.
- **Suponer que todo motor trata igual el esquema.** En SQLite y PostgreSQL las sentencias de definición de esquema forman parte de la transacción; en otros motores no (`SE-351`).

## Límites y cuándo no aplica

La atomicidad vale dentro de un límite: una transacción local no cubre un proceso que cruza varios servicios, donde se usan compensaciones (véase saga, `SE-377`). Tampoco cubre efectos externos que ya ocurrieron, como un correo enviado, que ninguna reversión de base de datos deshace. Y es solo una de las propiedades de una transacción: aislamiento y consistencia son otras, que `SE-351` y `SE-352` tratan aparte.
