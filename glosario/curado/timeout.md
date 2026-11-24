# Timeout

## Definición

Un **timeout** (tiempo límite) es el tiempo máximo que un cliente espera una respuesta antes de rendirse (`SE-438`, `SE-320`). Todo llamado por red debería tener uno: sin él, una dependencia colgada puede retener recursos del llamador indefinidamente.

## Por qué importa

El timeout decide cuánto trabajo desperdicia el sistema y cuánto tarda en liberarse ante un fallo. La decisión que cambia es que el valor no se copia de un ejemplo ni se deja por defecto: se deriva de la distribución de latencias del servicio y del plazo total disponible.

## Cómo funciona

`SE-438` señala que no existe un valor correcto en abstracto. Hay dos fallos opuestos:

- **Demasiado corto** (por debajo de la cola normal de la latencia): los clientes se rinden ante respuestas que iban a llegar y el servidor hace el trabajo de todas formas. Es trabajo desperdiciado y, si además se reintenta, carga extra.
- **Demasiado largo**: los clientes retienen un trabajador, una conexión y memoria mientras esperan una respuesta que quizá no llegue; una dependencia colgada agota los recursos del llamador.

La elección razonable ancla el timeout a un **percentil alto de la latencia sana** (por ejemplo, un múltiplo del p99,9) y lo ajusta con el **plazo total** disponible: si el usuario espera como máximo dos segundos de punta a punta, la suma de los timeouts en cadena no puede superar ese plazo; por eso se propaga el plazo y no solo se fija un valor local.

La clase añade un problema adicional: el timeout del cliente **no cancela el trabajo del servidor**; el servidor puede seguir ejecutando. Eso lo une al tiempo agotado ambiguo y obliga a que los reintentos sean idempotentes. Se combina con el presupuesto de reintentos, el interruptor y la espera con retroceso.

## Ejemplo

El servicio de correos de confirmación responde normalmente en 80 ms y su p99,9 sano es de 400 ms. Se fija un timeout de 1 s, ajustado al plazo total de la petición. Si el correo se retrasa, el cliente se rinde y degrada («te enviaremos la confirmación»), sin retener un hilo durante 30 s. Ejercicio de transferencia de `SE-438`.

## Errores y confusiones comunes

- **Se duplican entregas tras un timeout**: reintento de una operación no idempotente; se corrige con clave de idempotencia o no reintentando.
- **Los clientes agotan sus hilos esperando**: timeout demasiado largo; se ancla a la cola sana y al plazo total.
- **Un mismo valor para todas las dependencias**.
- **Creer que el timeout cancela el trabajo remoto**.

## Límites y cuándo no aplica

Un timeout no distingue lentitud de caída: solo declara que el tiempo pasó. Para operaciones de duración legítimamente larga (informes, cargas) un timeout corto de petición no corresponde y se usa un patrón asíncrono con consulta de estado. Y los números de las clases son de ejemplos con datos sintéticos, no valores recomendados.
