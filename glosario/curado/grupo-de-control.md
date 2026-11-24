# Grupo de control

## Definición

Un **grupo de control** es la parte del tráfico (o de la población) que no recibe la intervención y se mide a la vez que el grupo experimental, para tener un punto de comparación (`SE-505`). El programa usa el término con matices:

- En `SE-505` y `SE-515` (ingeniería del caos): grupo comparable que recibe el mismo tráfico sin la falla.
- En `SE-601` (ML en producción): parte de la población a la que no se aplica la decisión, para medir su efecto.
- En `SE-398` (plataforma): *cgroup*, un mecanismo del núcleo que reparte y limita el consumo de recursos de un conjunto de procesos. Es un homónimo técnico sin relación con el diseño experimental.

## Por qué importa

Sin un grupo de control, una diferencia observada puede deberse a la intervención o a cualquier otra cosa que cambió en ese momento: la hora, el cierre de un plazo, un pico de tráfico. La decisión que cambia es cómo se concluye de un experimento: comparando contra un control contemporáneo, no contra una memoria de cómo era antes.

## Cómo funciona

`SE-505` presenta el método de la ingeniería del caos en cuatro pasos: definir el estado estable como una salida medible que indica comportamiento normal; formular la hipótesis de que continuará en un grupo de control y en uno experimental; introducir variables que reflejen eventos reales; e intentar refutar la hipótesis buscando una diferencia entre ambos grupos. La falla solo se aplica al experimental; el control recibe el mismo tráfico sin falla.

`SE-515` muestra la arquitectura: un enrutador envía casi todo el tráfico a la flota normal y dos porciones pequeñas (de ejemplo, 2 %) a los grupos de control y experimental; un comparador mide a ambos, y un interruptor detiene el experimento si el experimental se degrada más que un límite. La razón del grupo contemporáneo es estadística: absorbe las variaciones comunes (hora, cierre de plazo) que una línea base de otra hora no absorbe. Por eso es la forma de medir sobre tráfico real.

En `SE-601`, el control es la parte de la población a la que no se aplica la decisión de un modelo, y permite medir su efecto real.

## Ejemplo

Se inyecta latencia en el 2 % del tráfico (experimental) mientras otro 2 % (control) sigue sin falla. Si ambos suben su tasa de errores por un pico de entregas, la diferencia entre ellos sigue siendo cero; si solo sube la del experimental, la falla es la causa. Diseño de `SE-515`.

## Errores y confusiones comunes

- **El estado estable cambia con el día**: línea base de un día excepcional; se corrige midiendo en días comparables y prefiriendo el grupo de control (`SE-505`).
- **Una divergencia pequeña no se ve**: comparación con una línea base de otra hora; se corrige con un grupo de control contemporáneo (`SE-515`).
- **Control y experimental no comparables**: si los grupos se reparten con un sesgo, la comparación no vale.
- **Confundirlo con el cgroup del núcleo**: homónimo sin relación.

## Límites y cuándo no aplica

`SE-515` advierte que el dibujo es un esquema de ejemplo con proporciones ilustrativas, no el diseño de una plataforma real. Con muy poco tráfico, los grupos pequeños no tienen potencia para detectar diferencias. Y en algunos sistemas no se puede reservar una parte de la población sin la decisión (por ejemplo, por razones éticas o legales), lo que limita el diseño con control.
