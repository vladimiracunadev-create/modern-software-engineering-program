# Instantánea

## Definición

Una **instantánea** es, en el sentido principal del programa (`SE-424`), una copia de una salida contra la que se compara exactamente en cada ejecución (*snapshot testing*). El término tiene otros sentidos en el programa, con el núcleo común de «copia de un estado en un momento»:

- En `SE-330`: copia del estado de un agregado en un punto de la historia, que evita reaplicar todos los eventos anteriores.
- En `SE-378`: copia consistente del estado en un momento dado, punto de partida de un flujo de cambios.
- En `SE-547` y `SE-582`: respuesta completa guardada para comparar, o copia/commit que permite restaurar un estado.

Esta entrada desarrolla el de pruebas y resume los demás.

## Por qué importa

Una instantánea promete detectar cualquier cambio sin escribir aserciones una por una. Esa promesa es también su riesgo: detecta todo y no distingue lo que importa de lo que no. La decisión que cambia es qué se afirma en una prueba de salida: lo que percibe el usuario (aserción semántica) o la salida entera.

## Cómo funciona

En `SE-424`, la instantánea guarda la salida (por ejemplo, el HTML) y la prueba falla ante cualquier diferencia. Un espacio, el orden de los atributos o una fecha nueva rompen la prueba igual que un botón que desaparece. Cuando la mayoría de las diferencias son ruido, el equipo aprende a aprobarlas sin leerlas, y la instantánea deja de proteger: la protección depende de la atención humana, y la atención se agota.

La alternativa es la **aserción semántica**: afirma lo que el usuario percibe (el título, la nota de la entrega, la presencia del botón) y es insensible al resto. Su costo es que solo ve lo que se le pidió mirar. La clase propone medir la **inestabilidad** de cada recorrido (con qué frecuencia cambia sin que importe) para decidir cuál usar.

En arquitectura (`SE-330`), la instantánea de un agregado evita reconstruirlo desde todos sus eventos: sin ellas, reconstruir tarda cada vez más a medida que la historia crece. En integración (`SE-378`), una instantánea consistente es el punto de partida de un flujo de cambios: se copia el estado y luego se aplican los cambios posteriores.

## Ejemplo

Una página de entrega incluye la fecha actual. Una instantánea del HTML falla cada día aunque nada importante cambió. El equipo aprueba las diferencias sin leerlas y un día deja pasar un botón que desapareció. Con una aserción semántica («el botón Entregar existe y el título es X») la prueba solo falla cuando algo relevante cambia. Contraste de `SE-424`.

## Errores y confusiones comunes

- **Las instantáneas se aprueban sin leerlas**: casi todas las diferencias son ruido; se corrige con aserciones semánticas y una instantánea solo para salidas pequeñas.
- **Reconstruir un agregado tarda cada vez más**: historia creciente sin instantáneas; se corrige con instantáneas periódicas o un agregado más pequeño (`SE-330`).
- **Mezclar sentidos**: una instantánea de pruebas no es una copia de seguridad.
- **Tomar una instantánea no consistente** como punto de partida de un flujo.

## Límites y cuándo no aplica

La instantánea de pruebas sirve para salidas pequeñas y estables; para salidas grandes o con partes variables genera ruido. No sustituye comprobar el comportamiento. La instantánea de estado necesita que la copia sea consistente con un instante confirmado, o el flujo posterior parte de un estado inexistente.
