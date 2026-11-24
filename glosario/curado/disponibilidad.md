# Disponibilidad

## Definición

La **disponibilidad** es la fracción del tiempo en que un sistema cumple su función; para un componente es MTBF / (MTBF + MTTR), con MTBF el tiempo medio entre fallos y MTTR el tiempo medio de reparación (`SE-440`).

## Por qué importa

`SE-440` existe para distinguir tres promesas que se confunden bajo la palabra «fiable»: que el servicio responda (disponibilidad), que los datos no se pierdan (durabilidad) y que, si algo se rompe, se vuelva a un estado conocido en un tiempo y con una pérdida acotados (recuperación). Mezclarlas lleva a medir una y prometer otra.

## Cómo funciona

Mejorar la disponibilidad se logra alargando el MTBF o acortando el MTTR; acortar la reparación suele ser más barato. En arquitecturas con varias capas, las capas en **serie** multiplican sus disponibilidades (la cadena es más débil que su eslabón más débil) y las réplicas en **paralelo** la mejoran, pero solo si fallan de forma independiente. Una causa común (el mismo despliegue, la misma zona) anula el beneficio.

## Ejemplo

Un componente con MTBF de 999 horas y MTTR de 1 hora tiene 999/1000 = 99,9 %. Si cinco capas en serie tienen cada una 99,9 %, la cadena ronda el 99,5 %. (Cálculo ilustrativo de la fórmula de la clase.)

## Errores y confusiones comunes

- **El sistema cae más de lo que da la cuenta.** Fallos en serie ignorados o causa común; calcular con todas las capas y listar lo que comparten las réplicas.
- **Duplicar un componente no mejora nada.** La limitación está en otra capa; mejorar el eslabón más débil.

## Límites y cuándo no aplica

La fórmula supone fallos y reparaciones independientes y estadísticamente estables; no describe degradaciones parciales (lentitud) ni pérdida de datos. Para esas, el SLI debe medir buenos eventos, no tiempo en pie.
