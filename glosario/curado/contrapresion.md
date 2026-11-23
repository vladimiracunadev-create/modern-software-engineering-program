# Contrapresión

## Definición

La **contrapresión** (*backpressure*) es la señal o el mecanismo por el que un consumidor lento limita el ritmo del productor, en lugar de dejar que el exceso se acumule sin límite. Es la definición compartida de `SE-305` (flujos reactivos), `SE-339` (una señal que frena al productor cuando el consumidor no da abasto) y `SE-387` (un consumidor lento hace esperar o rechazar a un productor en lugar de acumular mensajes sin límite).

## Por qué importa

Si el productor es más rápido que el consumidor, el exceso «tiene que ir a algún lado» (`SE-387`). Sin contrapresión va a la memoria y a la latencia: la cola crece hasta agotar la memoria y el sistema parece sano hasta que cae (`SE-339`). La contrapresión convierte esa sobrecarga escondida en una decisión explícita: quién espera, quién rechaza o qué se pierde.

## Cómo funciona

Un flujo conecta un productor con un consumidor mediante una cola. Si la cola no tiene límite, el desequilibrio se acumula como memoria y como latencia: los mensajes nuevos esperan detrás de todos los anteriores (`SE-387`). Si la cola está **acotada**, el exceso se traslada al productor: o se bloquea al emitir, o recibe un rechazo que puede reintentar, degradar o registrar.

`SE-305` ordena las alternativas en cuatro políticas: **dejar crecer** la cola, **bloquear** al productor, **descartar lo nuevo** o **descartar lo viejo**. Cada una compra algo y cuesta algo; elegir es decidir qué se pierde. Si no se puede frenar al productor (un sensor, una persona), algo debe descartarse. La capacidad de la cola no se «calcula»: se elige a partir de la latencia máxima aceptable (con servicio de un mensaje por turno, una cola de 100 implica hasta 100 turnos de espera) y se complementa con la política ante el llenado (`SE-387`).

## Ejemplo

En el experimento de `SE-339`, un productor rápido envía 5 000 mensajes a un consumidor que duerme 50 µs por mensaje (el sueño real es mayor y depende del sistema). Con una cola ilimitada, la profundidad llegó a unos 5 000, todo el lote esperando; con una cola acotada a 100, llegó a exactamente 100: cuando se llena, el `put` del productor se bloquea hasta que el consumidor libera un hueco. La sobrecarga se convirtió en espera del productor.

## Errores y confusiones comunes

- **Colas sin límite «para no perder nada».** Trasladan el problema a la memoria y a la latencia y fallan de golpe (`SE-339`, `SE-387`).
- **Elegir la capacidad por intuición.** Se elige desde la latencia máxima aceptable, no desde un número redondo (`SE-387`).
- **Olvidar la política ante el llenado.** Una cola acotada sin decisión de qué hacer cuando se llena solo cambia dónde falla.

## Límites y cuándo no aplica

La contrapresión solo funciona si el productor puede frenar. Con fuentes que no se pueden detener, como un sensor o un usuario, hay que descartar, y `SE-305` pide decidir explícitamente qué (lo nuevo o lo viejo). Las cifras de `SE-339` provienen de un experimento local con duraciones de sueño que dependen del sistema: muestran el mecanismo, no tiempos transferibles. Y bloquear al productor traslada la espera hacia atrás en la cadena: es una decisión de diseño, no una solución gratuita.
