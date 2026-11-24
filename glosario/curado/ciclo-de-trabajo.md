# Ciclo de trabajo

## Definición

El **ciclo de trabajo** (*duty cycle*) es la fracción del tiempo que un dispositivo permanece despierto. Es la definición de `SE-267` (restricciones de memoria, energía y cómputo) para dispositivos alimentados por pila. No debe confundirse con el uso del mismo nombre en señales PWM: aquí no habla de la forma de una onda, sino de cuánto tiempo del total el dispositivo consume corriente activa.

## Por qué importa

En un dispositivo a pila, la vida útil la decide la corriente *media*, y esa media depende mucho más del tiempo despierto que de la eficiencia del código. `SE-267` lo dice así: despertar menos y hacer más por cada despertar cambia la carga más que optimizar el código. La decisión que cambia es cada cuánto se mide y se transmite.

## Cómo funciona

Bajar el ciclo de trabajo es la palanca principal. `SE-267` enumera cuatro acciones:

1. **Despertar menos veces.**
2. **Hacer más por cada despertar:** agrupar lecturas y envíos (idea que `SE-266` ya había presentado).
3. **Apagar periféricos que no se usan.**
4. **Elegir el modo de reposo adecuado.**

Lo que hace que agrupar valga la pena es que cada despertar tiene un costo fijo de arranque del reloj y de la radio, que no depende de cuánto se haga. Despertar diez veces para enviar un byte paga diez veces ese costo; despertar una vez para enviar diez bytes lo paga una vez. La contrapartida es la **latencia**: un dato espera hasta el siguiente envío.

La corriente media resulta de ponderar cada fase (reposo, medición, radio) por el tiempo que dura en cada ciclo. Por eso la clase insiste en calcularla con todas las fases.

## Ejemplo

El nodo ambiental de la sala de estudio, caso conductor de la Parte 22, decide en `SE-267` cada cuánto mide y transmite. Una ilustración aritmética propia (no cifras de la clase): si el nodo consume 10 mA despierto y 5 µA dormido, y despierta 1 s cada 60 s, el ciclo de trabajo es 1/60 ≈ 1,7 % y la corriente media ronda 170 µA; despertar cada 600 s la baja a unos 20 µA. La vida de la pila cambia en un orden de magnitud sin tocar el código.

## Errores y confusiones comunes

- **La pila dura una fracción de lo calculado:** se usó la corriente activa o se ignoró la radio. Corrección: calcular la corriente media con todas las fases y medir con un medidor (`SE-267`).
- **Vida calculada mayor que la de la propia pila:** se ignoró la autodescarga y el envejecimiento; hay que acotar con la vida útil de la pila.
- **Confundirlo con la frecuencia de reloj:** un reloj más lento no baja el ciclo de trabajo.

## Límites y cuándo no aplica

No ayuda cuando el dispositivo debe escuchar de forma continua (un receptor siempre atento) ni cuando la latencia máxima tolerada es menor que el intervalo de reposo. Reducir despertares aumenta la latencia y puede perder eventos breves entre lecturas. Las cifras de `SE-267` son del modelo de la clase, no mediciones de un dispositivo real.
