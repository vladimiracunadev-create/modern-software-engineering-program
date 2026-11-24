# Modelo incremental

## Definición

El **modelo incremental** organiza el trabajo en partes utilizables que se liberan en un orden elegido por valor y riesgo (SE-181). Un incremento es una parte que se puede usar, no una capa técnica sin valor propio. Se distingue del modelo iterativo: el incremental se centra en entregar el producto por partes; el iterativo, en repetir ciclos para revisar la dirección.

## Por qué importa

Protege lo entregado si el proyecto se interrumpe. Un recorte presupuestario, una reorganización o un cambio de prioridades pueden cortar un proyecto a la mitad; con liberación única, el valor entregado es cero, y con incrementos, es lo que ya se liberó. Cambia el orden del trabajo: se empieza por lo que aporta más valor y reduce más riesgo.

## Cómo funciona

SE-181 plantea que construir incrementalmente significa ordenar el trabajo de modo que **cada entrega sea utilizable** y que **las primeras aporten la mayor parte del valor**. Para ello se elige el orden por valor y riesgo: las piezas más valiosas o más inciertas van primero.

La condición de calidad es que el incremento sea **utilizable**. Un incremento «la base de datos» o «la capa de servicios» no lo es: nadie puede usarlo. Un incremento correcto atraviesa las capas necesarias (corte vertical) y permite que una persona haga algo útil. La clase señala el fallo típico: un proyecto «ágil» que no libera nada utilizable hasta el último mes porque se iteró sin entregar incrementos; la corrección es definir qué puede usar una persona al final de cada ciclo y liberarlo.

En la práctica, el modelo incremental se combina con los otros. En la plataforma de entregas, el lanzamiento se divide en tres bloques: la integración con el sistema de calificaciones de secretaría (fecha fija y proveedor externo) se planifica de forma predictiva; la experiencia de entrega y recuperación del borrador (alta incertidumbre) se construye en ciclos de dos semanas con revisión de las usuarias; y cada pieza se libera cuando es utilizable.

## Ejemplo

Un proyecto de plataforma de entregas con tres incrementos: (1) subir un PDF y ver confirmación; (2) calificación por el docente; (3) prórrogas y notificaciones. Si el presupuesto se corta tras el segundo, las estudiantes ya entregan y los docentes ya califican; con una liberación única, nada funcionaría. (Ilustración del argumento de SE-181.)

## Errores y confusiones comunes

- **Incrementos que son capas técnicas** sin valor propio.
- **Iterar sin entregar**: el proyecto no libera nada utilizable hasta el último mes.
- **Confundir incremental con iterativo.**
- **Ordenar por comodidad técnica** y no por valor y riesgo.

## Límites y cuándo no aplica

Algunos productos no admiten entrega parcial utilizable (un dispositivo médico, un sistema que solo vale completo). La integración de muchos incrementos puede acumular deuda si no se cuida la arquitectura. Los números de SE-181 provienen de un modelo con supuestos del autor.
