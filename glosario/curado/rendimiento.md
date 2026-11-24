# Rendimiento (throughput)

## Definición

En este sentido, el **rendimiento** (*throughput*) es la cantidad de trabajo atendido por unidad de tiempo: peticiones por segundo en un servicio (SE-606) o elementos terminados por unidad de tiempo en un proceso de desarrollo (SE-189). No es el «rendimiento» en el sentido amplio de velocidad percibida (que se mide con latencia) ni el rendimiento como desempeño de una persona.

## Por qué importa

Dice cuánto trabajo cabe, y se contrasta con la latencia, que dice cuánto tarda cada pieza. Sirve para dimensionar capacidad y para seguir el flujo de un equipo. Cambia las decisiones de diseño: subir el rendimiento a costa de la latencia, o al revés, es un compromiso que se decide con el objetivo de nivel de servicio.

## Cómo funciona

SE-606 estudia la relación en un servicio con **lotes dinámicos**: se agrupan las peticiones que llegan hasta alcanzar un tamaño máximo o agotar una espera máxima, lo que ocurra primero. Agrupar mejora el rendimiento porque el costo fijo de cada invocación se reparte entre varias peticiones, pero **agrega espera**. La clase lo simula con 40.000 llegadas de Poisson a una tasa del 80 % de la capacidad sin lotes (18.391 por segundo, con una capacidad sin lotes de 22.989), con el tiempo de servicio medido. Con 0 ms de espera y lote de 1, el p50 fue 0,10 ms y el p99 0,47 ms; al ampliar la espera máxima, el rendimiento sostenible sube y la latencia de cola crece, porque la espera máxima se suma al p99. La regla práctica: fijar la espera máxima a partir del **presupuesto de latencia** (el SLO) y no del rendimiento.

En el flujo de trabajo (SE-189), el rendimiento es el número de elementos terminados por unidad de tiempo, y se relaciona con el trabajo en curso y el plazo por la ley de Little. Una advertencia: **la velocidad sube y el plazo no cambia** cuando la métrica se premia y se infla (se dividen los elementos para contar más); la corrección es retirarla de la vista externa y seguir el rendimiento y los escapes juntos.

## Ejemplo

Un servicio con capacidad de 23.000 peticiones por segundo sin lotes y una carga del 80 % atiende unas 18.400 por segundo con p99 de 0,47 ms. Con lotes de hasta 8 peticiones y espera máxima de 2 ms, la capacidad sostenible sube, pero el p99 pasa a incluir hasta 2 ms de espera. Si el SLO de p99 es 5 ms, el ajuste es aceptable; si es 1 ms, no. (El primer dato es de SE-606; el segundo es un escenario ilustrativo.)

## Errores y confusiones comunes

- **Confundir rendimiento con latencia.**
- **Premiar la velocidad del equipo**: se infla sin cambiar el plazo.
- **Optimizar el rendimiento sin mirar la latencia de cola.**
- **Comparar rendimientos medidos con cargas distintas.**

## Límites y cuándo no aplica

El rendimiento máximo no es el operativo: a utilización alta, las colas crecen y la latencia se dispara. La simulación de SE-606 usa llegadas de Poisson y tiempos medidos de un caso concreto. En equipos, contar elementos terminados supone que son comparables en tamaño, lo que no siempre es cierto.
