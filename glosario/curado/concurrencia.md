# Concurrencia

## Definición

La **concurrencia** es la propiedad de un programa en el que varias tareas están en curso y pueden avanzar de forma independiente, haya o no ejecución simultánea (`SE-385`). `SE-019` la presenta como composición de progresos superpuestos. Se distingue del **paralelismo**, que es una propiedad de la ejecución: dos tareas avanzan en el mismo instante porque hay dos unidades de cálculo.

## Por qué importa

La distinción decide qué problema se resuelve. Un servicio que espera disco y red necesita concurrencia (no bloquearse mientras espera); un cálculo pesado necesita paralelismo (más núcleos). Confundirlos produce lo que `SE-019` señala: creer que más hilos duplican la velocidad. Además, la concurrencia trae un costo propio: razonar sobre intercalaciones y estado compartido (`SE-386`). `SE-227` muestra la consecuencia: leer-modificar-escribir sin exclusión pierde casi todas las actualizaciones.

## Cómo funciona

Un programa puede ser concurrente sin ser paralelo (un núcleo que alterna tareas) y paralelo sin ser concurrente en un sentido interesante (cuatro copias independientes) (`SE-385`). Los mecanismos:

- **Hilos y procesos** (`SE-019`): el sistema alterna tareas con interrupciones y las reparte entre núcleos.
- **Asincronía**: las esperas pasan a corrutinas que ceden el control mientras aguardan entrada/salida.
- **Procesos múltiples** (`SE-345`, factor de concurrencia de 12-factor): se escala añadiendo procesos, no hilos dentro de uno.

La causa del riesgo es el estado compartido: dos tareas que leen y escriben el mismo dato en orden no determinista pueden producir resultados distintos en cada ejecución.

## Ejemplo

`SE-385`: un servicio de entregas clasifica sus tareas antes de tocar el código: guardar el archivo (espera de disco), consultar el curso (espera de red), calcular similitud (300 ms de cálculo) y enviar el acuse (espera de red). Las tres esperas pasan a corrutinas con un límite de 50 conexiones; el cálculo va a un grupo de procesos de tamaño igual al número de núcleos menos uno; el latido de salud sale de una tarea propia.

## Errores y confusiones comunes

- **«Los hilos duplican la velocidad».** Causa: concurrencia igualada a paralelismo; corrección: identificar carga, núcleos y runtime (`SE-019`).
- **Mutar estado compartido sin exclusión** (`SE-227`): actualizaciones perdidas.
- **Pensar que la asincronía acelera el cálculo.** Solo ayuda cuando hay esperas.

## Límites y cuándo no aplica

Una tarea estrictamente secuencial no gana nada con concurrencia, y el costo de coordinar puede superar el beneficio. El número de núcleos y el runtime (por ejemplo, el bloqueo global del intérprete en algunos lenguajes) limitan el paralelismo real. Y la sección de 12-factor sobre concurrencia es una receta de escalado por procesos, no una definición general.
