# Sobrecarga

## Definición

La **sobrecarga** es una carga mayor que la capacidad del servicio (`SE-606`, en el contexto de servir modelos).

## Por qué importa

Cuando la demanda supera la capacidad, la cola crece mientras dura la sobrecarga y la latencia de cola deja de estar acotada. La decisión es si hace falta una política de sobrecarga, procesamiento por lotes o nada.

## Cómo funciona

`SE-606` simula un servicio de modelo con y sin lotes dinámicos. Con una carga igual a la capacidad sin lotes, el p99 fue 9,4 ms sin lotes y 2,3 ms con lote dinámico de 2 ms y 64. Con el doble de la capacidad, el servicio sin lotes acumuló una cola de la que el p99 llegó a 858 ms (y crece mientras dura la sobrecarga), mientras que el servicio con lote dinámico mantuvo un p99 de 1,9 ms, porque su capacidad en peticiones por segundo es mucho mayor. Con cuatro veces la capacidad, 1 291 ms contra 1,1 ms.

## Ejemplo

La clase pide medir el costo por petición contra el tamaño de lote, localizar el óptimo, calcular cuánta espera cabe en el SLO y simular el doble de tráfico.

## Errores y confusiones comunes

Probar solo con la carga esperada; creer que más lote siempre ayuda, cuando la espera de formar el lote consume el SLO.

## Límites y cuándo no aplica

Son resultados de una simulación. Frente a una sobrecarga sostenida, ninguna técnica de lotes sustituye al descarte de carga o a más capacidad.
