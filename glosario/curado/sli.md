# SLI

## Definición

Un **SLI** (*service level indicator*, indicador de nivel de servicio) es una medida cuantitativa de un aspecto del servicio que importa a quien lo usa. `SE-497` lo define como esa medida, normalmente la proporción de eventos buenos sobre eventos válidos; `SE-048` lo presenta como medida cuantitativa del comportamiento del servicio y `SE-419` como la medición de un aspecto de lo que la persona usuaria experimenta. Es la base sobre la que se escribe un SLO.

## Por qué importa

Un objetivo solo es verificable si lo que mide está bien definido. `SE-497` insiste en que el SLI se mide desde la perspectiva de quien usa el servicio, no desde la comodidad de quien lo opera: un SLI mal elegido produce un SLO que se cumple mientras hay quejas.

## Cómo funciona

La forma más útil, según `SE-497`, es una **proporción**: eventos buenos entre eventos válidos, expresada como porcentaje. Para la API de entregas del caso conductor, «una entrega es buena si el servidor responde con éxito y en menos de 1 s». La definición exige tres decisiones que se escriben:

1. **Qué es «bueno»:** el estado de la respuesta y el umbral de latencia.
2. **Qué es «válido»:** qué eventos se excluyen porque no son culpa del servicio, como una petición mal formada.
3. **Dónde se mide:** `SE-497` recomienda medir cerca de la persona usuaria.

La causa de la tercera decisión es que lo medido depende del punto de medida: un indicador tomado en el servidor no ve lo que ocurre en la red del cliente. Y un SLI de disponibilidad sin umbral de latencia da por buena una respuesta correcta pero lenta, lo que `SE-497` señala como un fallo de definición.

## Ejemplo

En `SE-497`, la API de entregas define su SLI como la proporción de peticiones respondidas con éxito en menos de 1 s sobre las peticiones válidas. Con eso, un 99,9 % de ese SLI sostenido en 30 días es el SLO del servicio. Si un panel cuenta peticiones y otro cuenta minutos, los consumos del presupuesto divergen: la clase pide declarar la forma de contar en el SLO.

## Errores y confusiones comunes

- **Medir donde no se ve el problema.** El SLO se cumple y hay quejas; hay que medir cerca de la persona y añadir ventana corta o segmento (`SE-497`).
- **Contar de dos maneras.** Dos paneles dan consumos opuestos porque uno cuenta peticiones y otro minutos (`SE-497`).
- **Confundir SLI, SLO y SLA.** El SLI es la medida, el SLO su valor objetivo en una ventana y el SLA el compromiso con el cliente, que debe fijarse por debajo del SLO (`SE-497`).

## Límites y cuándo no aplica

Un SLI es una simplificación: `SE-419` señala que la caída parcial (algunos clientes, algunas funciones) se mide con SLI por solicitud y no por tiempo, y que las series de la clase son inventadas para mostrar la lectura.
