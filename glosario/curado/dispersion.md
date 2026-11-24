# Dispersión

## Definición

En este glosario, **dispersión** es el nombre en español de lo que las clases llaman *jitter*: un componente aleatorio añadido a la espera de un reintento para que los clientes no reintenten sincronizados. Lo usan con el mismo sentido `SE-239`, `SE-246`, `SE-270` y `SE-438`; `SE-320` lo desarrolla como «jitter». No debe confundirse con la dispersión estadística (varianza) ni con el *jitter* de variación de latencia en redes de tiempo real.

## Por qué importa

Cuando muchos clientes fallan a la vez y reintentan con la misma regla, vuelven a chocar a la vez: una tormenta de reintentos que impide la recuperación del servicio. Añadir aleatoriedad reparte la carga en el tiempo. Es una de esas decisiones de dos líneas de código que deciden si un servicio se recupera o no.

## Cómo funciona

El experimento de `SE-320` simula 1000 clientes cuyo primer intento ocurre en el instante 0 y reintentan hasta 12 veces; el servicio falla hasta 1000 ms y luego acepta 60 peticiones por cada 100 ms:

- **Intervalo fijo de 100 ms:** siguen sincronizados; pico de 1000 peticiones por 100 ms en cada ronda, 11 940 intentos y 880 clientes se rinden.
- **Exponencial sin aleatoriedad:** siguen sincronizados, más espaciados; pico de 1000, 10 320 intentos, último éxito a los 38 300 ms, 520 abandonados.
- **Jitter completo** (espera uniforme entre 0 y el valor exponencial): el pico tras el arranque baja a 537, con 6230 intentos y último éxito a los 7179 ms.

El retroceso exponencial alarga las esperas, pero no las desincroniza; la dispersión sí. Por eso se combinan. La idea es la misma en IoT (`SE-270`: varias unidades reconectando tras un corte), en el flujo web resiliente de `SE-239` y en la idempotencia de reintentos de `SE-246`.

## Ejemplo

Esbozo ilustrativo del jitter completo (no código de la clase):

```python
import random
espera = random.uniform(0, min(tope, base * 2 ** intento))
```

Con 1000 clientes reintentando tras un corte de un segundo, el tráfico deja de llegar como un muro y llega como una rampa.

## Errores y confusiones comunes

- **Retroceso exponencial sin aleatoriedad,** que mantiene a los clientes sincronizados.
- **Reintentar sin tope de intentos,** que prolonga la sobrecarga.
- **Reintentar operaciones no idempotentes:** la dispersión reparte la carga, no evita duplicados; hace falta idempotencia (`SE-246`).
- **Confundirlo con un cambio de timeout.**

## Límites y cuándo no aplica

Los números de `SE-320` vienen de una simulación con parámetros del autor, no de un servicio real. La dispersión no arregla un servicio que sigue caído; solo evita agravarlo. Con pocos clientes, la sincronización no importa. Y retrasa aleatoriamente una parte de los reintentos, lo que alarga la espera de algunos clientes.
