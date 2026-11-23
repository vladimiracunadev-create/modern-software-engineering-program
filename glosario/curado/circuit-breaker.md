# Circuit breaker

## Definición

Un **circuit breaker** (interruptor de circuito) es un componente que deja de llamar a una dependencia que está fallando de forma persistente y la vuelve a probar después de un tiempo. `SE-439` lo define con ese comportamiento, `SE-320`, que lo trata entre los patrones de resiliencia, como control que rechaza llamadas a una dependencia con fallos persistentes y `SE-048` como control que limita llamadas a una dependencia degradada, dentro de un servicio tolerante a fallos de red. El nombre viene del interruptor eléctrico: corta el paso para proteger el resto del circuito.

## Por qué importa

Llamar a una dependencia caída tiene dos costos: cada llamada espera hasta su límite de tiempo y consume recursos del que llama, y la dependencia, si está sobrecargada, recibe más carga justo cuando necesita descanso. El interruptor convierte un fallo lento y contagioso en un rechazo inmediato y barato. Es una de las defensas con que `SE-320` y `SE-439` protegen al sistema de la degradación en cascada.

## Cómo funciona

Según `SE-320`, el interruptor tiene tres estados:

1. **Cerrado:** las llamadas pasan. Se cuentan los fallos consecutivos.
2. **Abierto:** se supera un umbral de fallos y las llamadas se **rechazan al instante**, sin tocar la dependencia.
3. **Semiabierto:** tras un tiempo, se deja pasar una llamada de sondeo; si tiene éxito, el interruptor se cierra, y si falla, vuelve a abrirse.

La causa de su utilidad es el rechazo rápido: no gasta el tiempo de espera ni la carga en llamadas que van a fallar de todos modos, y le da a la dependencia tiempo para recuperarse. Lo que decide si funciona bien son sus parámetros: el umbral de fallos, el tiempo en estado abierto y qué se hace con la llamada rechazada (un valor por defecto, una respuesta degradada, un error rápido).

## Ejemplo

En el experimento de `SE-320`, una dependencia está caída entre los 5 y los 12 segundos de una ventana de 20 s, con 100 peticiones por segundo (2 000 en total). **Sin** interruptor se hacen 2 000 llamadas al servicio, con 1 300 éxitos. **Con** interruptor (umbral de 5 fallos y 1 s en estado abierto) se hacen 1 307 llamadas, se rechazan 693 al instante y los éxitos son 1 296. El interruptor aparta 693 peticiones del servicio caído sin cambiar apenas los éxitos. Son datos simulados con parámetros del autor.

## Errores y confusiones comunes

- **Un umbral mal calibrado corta tráfico sano.** Si el umbral es muy bajo, unos pocos fallos aislados abren el interruptor y rechazan peticiones que habrían funcionado.
- **Tratar el interruptor como sustituto del límite de tiempo.** Son controles distintos: el límite de tiempo acota cada llamada (`SE-438`), el interruptor deja de hacerlas.
- **No decidir qué responder cuando está abierto.** Un rechazo sin respuesta degradada solo traslada el fallo al usuario.

## Límites y cuándo no aplica

`SE-320` declara los límites de su experimento: la dependencia cae de golpe y se recupera de golpe, el tráfico es constante y el umbral es el del autor. Con fallos parciales, latencia creciente o varias instancias, calibrar un interruptor es mucho más delicado y exige medir la tasa de error y la latencia reales. El interruptor no corrige la dependencia ni garantiza disponibilidad: solo limita el daño de llamarla mientras falla. Y no tiene sentido si la dependencia es imprescindible y no existe ninguna alternativa degradada.
