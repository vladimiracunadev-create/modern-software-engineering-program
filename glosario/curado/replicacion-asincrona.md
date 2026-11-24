# Replicación asíncrona

## Definición

La **replicación asíncrona** es la copia de los datos a otras máquinas sin esperar su confirmación antes de responder al cliente (`SE-355`). `SE-510` la formula desde el efecto: el primario confirma la escritura antes de que la réplica la reciba. Se contrapone a la replicación síncrona, donde el líder espera a una o más réplicas.

## Por qué importa

Replicar datos protege contra la caída de una máquina, pero cómo se replica decide qué se puede perder. La decisión que cambia es qué se sacrifica: velocidad y disponibilidad, o seguridad de no perder datos confirmados. `SE-355` lo resume: elegir es elegir qué se sacrifica, y cada institución decide según el costo de perder o de retrasar.

## Cómo funciona

El líder acepta las escrituras y las envía a las réplicas, que las aplican con retardo. En la modalidad **asíncrona**, el líder confirma al cliente sin esperar a las réplicas. Ventajas: es rápido y tolera que una réplica esté lenta o caída. Costos, según `SE-355`:

- Si el líder se cae **antes de enviar**, esa escritura se pierde, aunque ya se había confirmado al cliente.
- Una lectura en una réplica puede devolver un **valor viejo**, por el retardo de replicación.

En la **síncrona**, el líder espera a una o más réplicas: no pierde lo confirmado, pero cobra latencia y disponibilidad (si la réplica no responde, la escritura espera). Existe un punto intermedio, la semisíncrona, que exige confirmar con al menos una réplica y mantiene las demás asíncronas.

La consecuencia cuantificable es el objetivo de punto de recuperación: con replicación asíncrona, el RPO es el retraso de la réplica. `SE-510` lo prueba con ingeniería del caos: si se declara RPO cero con replicación asíncrona, una conmutación hace desaparecer escrituras confirmadas; la corrección es medir la pérdida y elegir replicación semisíncrona o ajustar el RPO declarado.

## Ejemplo

El primario confirma una entrega al estudiante y la envía a la réplica un instante después. El primario cae justo entre ambos momentos. Al conmutar a la réplica, la entrega ya confirmada no existe. Con replicación semisíncrona, el acuse solo se emite tras la confirmación de la réplica y la entrega sobrevive. Contraste de `SE-355` y `SE-393`.

## Errores y confusiones comunes

- **Escrituras confirmadas desaparecen tras una conmutación**: replicación asíncrona con RPO declarado de cero; se corrige midiendo la pérdida y eligiendo semisíncrona o ajustando el RPO (`SE-510`).
- **Leer de una réplica esperando el último valor**: puede ser viejo.
- **Confundirla con un respaldo**: replica también los errores y borrados.
- **Elegirla sin declarar cuánto se puede perder**.

## Límites y cuándo no aplica

No aplica cuando lo confirmado no puede perderse nunca: ahí hace falta síncrona o semisíncrona, con su costo de latencia. Tampoco sirve como única protección: no sustituye copias consistentes con prueba de restauración. Y el retraso depende de la red y la carga; solo medirlo en el sistema real da el RPO efectivo.
