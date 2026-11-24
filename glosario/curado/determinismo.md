# Determinismo

## Definición

El **determinismo** es la propiedad de producir el mismo resultado ante las mismas entradas declaradas. El programa lo usa con ese núcleo en varios contextos: en `SE-292`, una simulación es determinista si, con el mismo estado y las mismas entradas, llega siempre al mismo estado; en `SE-364`, un paso de transformación es determinista si su resultado depende solo de las entradas declaradas; en `SE-428`, el determinismo de los datos y de las pruebas se pierde por «fuentes de no determinismo» que hay que inventariar.

## Por qué importa

Lo que no se puede repetir no se puede depurar, comparar ni reconstruir. Con determinismo, un fallo se reproduce con una grabación de entradas, dos máquinas se sincronizan, y una transformación se puede rehacer (*backfill*) sin cambiar resultados. Sin él, una prueba que falla «a veces» no distingue un defecto de un accidente.

## Cómo funciona

La clave es **declarar todas las entradas**: todo lo que influye en el resultado y no está declarado es una fuente de no determinismo.

- **Simulación y videojuegos (`SE-292`).** Con paso de tiempo variable, el estado final depende de la secuencia de duraciones de los fotogramas, que cambia con la carga de la máquina; dos ejecuciones con las mismas entradas terminan distintas. Con **paso fijo**, la secuencia de pasos es la misma y el resultado solo depende de las entradas. Para sincronizar dos máquinas, repetir una partida o encontrar un fallo con una grabación se necesita paso fijo. Entre máquinas distintas exige además la misma aritmética (la no asociatividad de `SE-289` reaparece).
- **Datos y pruebas (`SE-428`).** Cada fuente de no determinismo (reloj, orden de ejecución, estado compartido entre pruebas, datos aleatorios sin semilla) tiene un remedio distinto: inyectar el reloj, fijar semillas, aislar fixtures.
- **Transformaciones (`SE-364`).** Si el resultado depende solo de las entradas declaradas, repetir el trabajo da lo mismo, requisito para backfills idempotentes.

## Ejemplo

`SE-428` propone ejecutar una suite en órdenes aleatorios, medir qué estrategia de fixture aísla mejor y a qué costo, e inventariar las fuentes de no determinismo; la transferencia está lograda cuando puedes explicar qué prueba dependía de cuál y cómo lo supiste. Ilustración propia: una prueba que compara «hoy» con una fecha fija falla en año bisiesto; la causa es el reloj como entrada no declarada.

## Errores y confusiones comunes

- **Confundir determinismo con ausencia de aleatoriedad:** un generador con semilla fija es determinista aunque «parezca» aleatorio.
- **Asumir determinismo entre máquinas** sin comprobar la aritmética.
- **Paso variable en una simulación** que se quiere repetir (`SE-292`).
- **Confundirlo con idempotencia:** esta es repetir una operación sin cambiar el estado; el determinismo es mismo resultado con mismas entradas.

## Límites y cuándo no aplica

El determinismo total es caro y a veces innecesario: un sistema distribuido con relojes y redes reales no lo ofrece de gratis. Es una propiedad respecto de las entradas *declaradas*; si se declara poco, vale poco. Y no implica corrección: un programa puede ser determinista y estar mal.
