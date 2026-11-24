# Clave caliente

## Definición

Una **clave caliente** es una clave que recibe una fracción desproporcionada de las peticiones (`SE-355`). En un sistema particionado por clave, la partición que la contiene soporta una carga muy superior a la de las demás, aunque los datos estén repartidos de forma equilibrada.

## Por qué importa

Particionar por clave promete escalar horizontalmente: más nodos, más capacidad. La clave caliente rompe esa promesa, porque la capacidad que se añade no llega al nodo saturado. La decisión que cambia es dónde se busca la solución: no en comprar más nodos, sino en rediseñar la clave o en sacar la carga de esa partición. Reconocerla evita gastar en escala que no alivia el cuello de botella.

## Cómo funciona

El reparto por clave solo equilibra la carga si la popularidad de las claves es aproximadamente uniforme. `SE-355` señala el caso real: unos pocos estudiantes o cursos concentran muchas peticiones. Como una clave vive en una sola partición, esa partición recibe todo el tráfico de la clave, y **añadir nodos no la alivia** porque la clave no se reparte entre ellos. En la simulación de `SE-355` la popularidad sigue una distribución de Zipf (supuesto del autor), donde pocas claves acumulan la mayoría de las peticiones.

`SE-355` da tres salidas:

1. **Cambiar la clave**, repartiendo por un campo más fino.
2. **Dividir la clave caliente en subclaves**: las escrituras se reparten, a costa de que las lecturas deban consultar todas y de complejidad adicional.
3. **Servirla desde una caché** (`SE-356`), que absorbe las lecturas repetidas.

Y un agravante: un rango contiguo de identificadores es la peor elección cuando los identificadores recientes son los populares, porque todo el tráfico cae en la última partición.

## Ejemplo

Una plataforma de entregas particiona por identificador de curso. Un curso muy activo en fecha de entrega recibe la mayor parte del tráfico y su nodo se satura, mientras los otros están ociosos. Duplicar los nodos no cambia nada. Repartir por curso y estudiante reparte la carga; o se divide el curso caliente en subclaves, o se sirve su lectura desde caché. Ilustración del escenario de `SE-355`.

## Errores y confusiones comunes

- **Un nodo está saturado y los demás ociosos**: clave caliente o rango contiguo; se corrige cambiando la clave, repartiendo en subclaves o con caché.
- **Responder con más nodos**: no mueve la carga de la clave.
- **Confundirla con un desequilibrio de datos**: el problema es de tráfico, no de volumen almacenado.
- **Olvidar el costo del reparto en subclaves**: las lecturas pasan a tocar varias particiones.

## Límites y cuándo no aplica

`SE-355` advierte que sus tres simulaciones con semilla fija no usaron base distribuida ni red; el retardo exponencial, la lectura uniforme y la popularidad Zipf son supuestos del autor, y no se midió latencia ni el costo de mover datos. El concepto aplica a sistemas particionados por clave; con carga realmente uniforme o con un solo nodo, no es el problema. La caché solo ayuda con lecturas, no con escrituras sobre la misma clave.
