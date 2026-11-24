# Lectura obsoleta

## Definición

Una **lectura obsoleta** (*stale read*) es una lectura que devuelve datos anteriores a una escritura ya confirmada. `SE-510` la trata en réplicas y particiones: una réplica sana puede devolver datos viejos. `SE-249` la usa para cachés: la lectura de una caché cuyo dato ya cambió en el origen, es decir, un acierto cuya versión ya cambió.

## Por qué importa

No es un error del sistema, sino una consecuencia de copiar datos: cada réplica o caché tarda en enterarse. La decisión que cambia es dónde la persona *no puede* ver un dato viejo (leer su propia escritura, un saldo) y dónde sí (un historial).

## Cómo funciona

Una escritura se confirma en un nodo y se propaga a otros con un retraso. Una lectura que llega a una réplica antes de que reciba el dato lo ve viejo. `SE-510` mide la fracción de lecturas obsoletas contra el retraso de replicación, modelando el tiempo entre escritura y lectura como exponencial con media de 50 ms: con 5 ms, el 10 % de las lecturas llegan antes de que la réplica tenga el dato; con 20 ms, el 35 %; con 100 ms, el 85 %; con 500 ms, casi todas.

La clase advierte un límite del modelo: si la interfaz espera la respuesta de la escritura antes de recargar, ese tiempo es mayor y la fracción baja. El experimento correcto mide cuántas lecturas son viejas *en el flujo de la persona*: «leer tu propia escritura».

En cachés (`SE-249`), el experimento genera 200 000 lecturas de 5 000 entregas con popularidad Zipf; cada entrega cambia cada 300 a 900 s; una caché LRU de 50, 500 o 2 500 entradas con TTL de 10, 60 o 600 s cuenta aciertos y lecturas obsoletas. Un TTL más largo sube los aciertos y también las lecturas obsoletas.

## Ejemplo

Ilustración propia del flujo: una persona edita su perfil, la escritura va al nodo principal y la página recarga leyendo de una réplica con 100 ms de retraso; ve su dato anterior. Remedios habituales: leer del principal tras escribir, o enviar la versión escrita y esperar a que la réplica la alcance.

## Errores y confusiones comunes

- **Pensar que una réplica obsoleta está dañada:** está sana y atrasada.
- **Medir «cuántas lecturas son viejas» sin referirse al flujo del usuario.**
- **Subir el TTL para ganar aciertos sin contar el costo en obsolescencia.**
- **Confundirla con lectura sucia** (leer un dato no confirmado).

## Límites y cuándo no aplica

Las cifras vienen de modelos con parámetros del autor, no de un sistema medido. En un sistema de una sola copia con lecturas del principal no existe. Y para datos que cambian poco o toleran edad, no es un problema.
