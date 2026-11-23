# Latencia

## Definición

La **latencia** es el tiempo que transcurre entre un inicio y un resultado definidos. Es la formulación de `SE-046` («tiempo entre un inicio definido y un resultado definido»), y las demás clases la aplican a objetos distintos: `SE-018` el tiempo hasta completar una operación de memoria o almacenamiento, `SE-022` el tiempo para una unidad de trabajo, y `SE-606` el tiempo desde que llega una petición hasta que se responde. Lo esencial es que la palabra solo significa algo cuando se declaran el inicio y el fin.

## Por qué importa

Una cifra de latencia sin sus extremos no se puede comparar. `SE-046` pide definir el inicio y el resultado precisamente para que dos mediciones se puedan comparar. Y en servicio de modelos (`SE-606`), la latencia entra en tensión con el costo: agrandar el lote reduce el costo por petición hasta cierto punto y después añade latencia.

## Cómo funciona

La latencia se descompone en lo que ocurre entre los dos extremos definidos. En `SE-606`, el experimento de lotes mide costo por petición según el tamaño del lote: a partir de cierto tamaño el beneficio se acaba y la curva sube (con 1 024 peticiones el costo por petición fue 8,3 µs, más del triple que con 512), porque en una CPU las matrices dejan de caber en la caché o, en un acelerador, la memoria es limitada. Agrandar el lote deja de ayudar y añade latencia. La forma de la curva depende del hardware, del modelo y de las bibliotecas, por lo que se mide con el modelo propio y la máquina de producción; el experimento mostró además tiempos irregulares en lotes pequeños. En `SE-018`, la jerarquía de memoria explica por qué la latencia de una operación depende de dónde está el dato.

## Ejemplo

En `SE-606`, con lotes de 512 y 1 024 peticiones el costo por petición pasa a más del triple al duplicar el lote, y agrandarlo así deja de ayudar y añade latencia. Es un experimento de la clase sobre un modelo y una máquina concretos.

## Errores y confusiones comunes

- **Dar una latencia sin decir de dónde a dónde.** Sin inicio y resultado definidos no es comparable (`SE-046`).
- **Asumir que un lote más grande siempre mejora.** El beneficio se acaba y la curva sube (`SE-606`).
- **Transferir una curva medida a otro hardware.** Depende del hardware, del modelo y de las bibliotecas.

## Límites y cuándo no aplica

La latencia es una medida de tiempo, no de capacidad: `SE-436` la trata junto con rendimiento, saturación y capacidad como cosas distintas que se leen juntas. Los números de `SE-606` salen de una máquina y un modelo concretos.
