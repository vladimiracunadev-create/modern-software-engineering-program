# Actualización diferencial

## Definición

Una **actualización diferencial** envía solo las diferencias entre dos versiones del firmware en lugar de la imagen completa. `SE-271` la enseña dentro de las actualizaciones OTA (por aire) y su recuperación. El término no significa «actualizar solo lo que el usuario necesita»: significa que lo transmitido es un parche calculado entre una versión de origen y una de destino, que el dispositivo aplica sobre la imagen que ya tiene.

## Por qué importa

Un dispositivo conectado por una red lenta o con batería paga cada byte recibido. `SE-271` señala que la energía de radio suele costar más que el cálculo, de modo que enviar menos bytes ahorra ancho de banda y energía. La decisión profesional es si el ahorro compensa lo que añade: un formato de diferencias que el cargador debe aplicar con seguridad, incluso ante cortes de energía, y más cálculo en el servidor o en el dispositivo.

## Cómo funciona

Hay dos formas de calcular la diferencia, y entre ellas está el punto central de la clase:

1. **Comparación de bloques por posición.** Se parte la imagen en bloques y se compara el bloque *n* de la versión vieja con el bloque *n* de la nueva. Es simple, pero si se inserta una línea al principio, todo lo que sigue se desplaza y *todos* los bloques posteriores parecen distintos. El parche termina enviando casi la imagen entera.
2. **Búsqueda de bloques en cualquier posición.** Se calcula una suma de comprobación de una ventana que se desliza por el archivo nuevo, y se busca en la imagen vieja un bloque con la misma suma, aunque esté en otra posición. `SE-271` cita la idea de rsync: una suma que se actualiza al desplazar la ventana permite reconocer bloques movidos sin recalcular desde cero.

El parche resultante es una lista de instrucciones («copia estos bloques de la versión vieja, inserta estos bytes nuevos»). Aplicarlo exige que el dispositivo tenga exactamente la versión de origen para la que se calculó; por eso el cargador debe poder comprobarlo antes de empezar.

## Ejemplo

`SE-271` compara con el prototipo del nodo de sala: un corte durante la actualización deja el nodo con la versión anterior, y la actualización diferencial *no* envía la mitad de la imagen por insertar una línea, porque busca bloques en cualquier posición. La clase añade el criterio de evaluación: un plan es adecuado cuando cada paso tolera un corte, y es frágil cuando funciona solo si nada falla.

## Errores y confusiones comunes

- **Comparar por posición y sorprenderse** de que una inserción mínima produzca un parche enorme (`SE-271`). La corrección es buscar bloques en cualquier posición.
- **Creer que diferencial implica seguro.** Un parche pequeño que se aplica mal o a medias deja el dispositivo inutilizable; la diferencia entre versiones no reemplaza la recuperación ante cortes.
- **Confundirla con la actualización por etapas** (qué dispositivos reciben la versión y cuándo): aquí se trata de *qué bytes* se envían, no *a quién*.

## Límites y cuándo no aplica

El ahorro se reduce o desaparece si las versiones difieren mucho (por ejemplo una recompilación que reordena todo el binario). El parche solo vale para el par de versiones origen-destino para el que se calculó. Las simulaciones de `SE-271` usaron imágenes sintéticas y ningún cargador de arranque real: no prueban el ahorro en un dispositivo concreto. Tampoco resuelve la pregunta siguiente de la clase, cómo sabe el nodo que la actualización recibida es legítima, que pertenece a la firma y la raíz de confianza.
