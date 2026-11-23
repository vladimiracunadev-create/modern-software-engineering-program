# Retroceso exponencial

## Definición

El **retroceso exponencial** (*exponential backoff*) es una política de reintento que multiplica la espera tras cada fallo: `SE-239` la define como la política que multiplica la espera tras cada fallo, `SE-246` como la estrategia que multiplica la espera entre reintentos por un factor fijo, `SE-270` como la que duplica el intervalo hasta un máximo y `SE-596` como la espera que crece de forma exponencial entre reintentos. Un ejemplo de `SE-246`: esperas de 1, 2, 4 y 8 segundos.

## Por qué importa

El cliente que reintenta debe esperar, y `SE-246` dice que esperar mal es peor que no reintentar. Un intervalo fijo concentra a todos los clientes en los mismos instantes y puede volver a tumbar al servicio justo cuando se recupera. El retroceso exponencial dispersa los reintentos en el tiempo y da margen al servicio para recuperarse.

## Cómo funciona

Cada fallo multiplica la espera por un factor, hasta un máximo. La causa de su efecto es que los clientes que fallaron a la vez dejan de reintentar a la vez. Pero `SE-246` señala su límite: si todos fallaron al mismo tiempo, siguen reintentando en sincronía, solo que en oleadas más espaciadas. Por eso se añade **jitter**, aleatoriedad en cada espera, que rompe la sincronía. Además se limita el número de intentos y el tiempo total, y se respeta `Retry-After` cuando el servidor lo envía. `SE-596` aplica el conjunto en un flujo con agentes: retroceso exponencial con jitter completo, máximo de cinco intentos y dos minutos en total; pasado el límite, la ejecución queda «pendiente de revisión» y llega a una cola humana. `SE-239` añade un límite de tasa. Los reintentos solo son seguros si la operación es idempotente (véase idempotencia).

## Ejemplo

`SE-246` simula 2 000 clientes que fallan a la vez durante una caída de 5 s contra un servicio con capacidad de 400 solicitudes por segundo; cada cliente se rinde tras 8 intentos. Tras la caída, el intervalo fijo produce un pico de 2 000 solicitudes por segundo, 3 s por encima de la capacidad y 800 clientes que abandonan; el exponencial sin jitter mantiene el pico en 2 000 y 4 s por encima de la capacidad, sin abandonos; con jitter total el pico baja a 372 y la capacidad no se supera en ningún segundo.

## Errores y confusiones comunes

- **El servicio vuelve a caer al recuperarse.** Reintentos sincronizados sin jitter; corrección (`SE-246`): retroceso exponencial con jitter y límite de intentos.
- **Mil clientes agotan al servidor al recuperarse.** Reintentos sincronizados sin dispersión; corrección (`SE-239`): dispersión, máximo de intentos y límite de tasa.
- **Creer que exponencial basta.** Sin jitter el pico sigue siendo de 2 000 en la simulación de `SE-246`.

## Límites y cuándo no aplica

El modelo de `SE-246` supone clientes idénticos y capacidad fija; no incluye colas ni que el servicio empeore con la carga. Con 2 000 clientes el efecto es claro; con 20, todas las políticas serían inocuas. El retroceso no sustituye a la idempotencia ni a un interruptor de circuito (véase circuit breaker): dispersa los reintentos, no decide si conviene reintentar.
