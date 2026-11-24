# Hilo

## Definición

Un **hilo** (*thread*) es una secuencia de ejecución planificable dentro de un proceso (`SE-019`, `SE-028`). Los hilos de un proceso comparten memoria y recursos, pero cada uno mantiene su pila y su estado de ejecución propios. Es la unidad que el planificador del sistema reparte entre los núcleos.

## Por qué importa

Permite hacer varias cosas dentro de un mismo programa sin copiar memoria, pero introduce el problema central de la programación concurrente: varios flujos tocando los mismos datos. La idea de que «más hilos son más velocidad» es un error clásico: `SE-019` recuerda que más hilos agregan *overhead* y no crean núcleos. La decisión que cambia es cuándo usar hilos, procesos o entrada/salida asíncrona.

## Cómo funciona

Compartir memoria reduce copia y permite trabajo concurrente, pero introduce **carreras**, dependencia del orden y necesidad de sincronización (`SE-019`). Comparado con un proceso: un proceso tiene memoria virtual propia; un hilo comparte la del proceso. El sistema operativo interrumpe y cambia de hilo; cada cambio tiene costo. La causa de que muchos hilos no ayuden es que la CPU solo ejecuta tantos hilos a la vez como núcleos tiene, y el resto espera turno.

La alternativa depende de dónde está el cuello: si el programa espera entrada/salida (muchas conexiones), un servidor atiende con E/S asíncrona para evitar un hilo bloqueado por conexión; si el cuello es cálculo, se consideran procesos o trabajo vectorizado, siempre midiendo costos de coordinación (`SE-019`).

## Ejemplo

```python
n = 0
def inc():
    global n
    for _ in range(100_000): n += 1     # lectura-modificación-escritura sin exclusión

hilos = [threading.Thread(target=inc) for _ in range(4)]
```

El resultado puede ser menor que 400 000 porque las actualizaciones se pisan: es el contador compartido sin contrato que `SE-019` usa para mostrar una carrera.

## Errores y confusiones comunes

- **«Los hilos duplican la velocidad».** Causa: concurrencia igualada a paralelismo; corrección: identificar carga, núcleos y runtime (`SE-019`).
- **Compartir estado mutable sin sincronización.** Produce resultados distintos en cada ejecución.
- **Confundir hilo con proceso.** El proceso aísla memoria; el hilo la comparte.

## Límites y cuándo no aplica

Los hilos no ayudan cuando el cuello es un solo recurso secuencial, y en algunos runtimes un bloqueo global del intérprete limita el paralelismo de cálculo en hilos. La sincronización excesiva puede anular el beneficio. Y para aislar fallos o código no confiable, los hilos no sirven: un fallo en un hilo puede derribar el proceso entero.
