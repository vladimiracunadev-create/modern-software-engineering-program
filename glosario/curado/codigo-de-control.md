# Código de control

## Definición

Un **código de control** (también «código de detección de errores») son bits redundantes que se añaden a una trama para detectar errores de transmisión. La paridad, la suma de verificación y el CRC son los ejemplos de `SE-266` (microcontroladores, periféricos y buses). Detectar no es corregir: el código dice que algo está mal, no qué bit lo está.

## Por qué importa

Un bus o un radioenlace corrompe bits; sin control, el receptor actúa sobre datos falsos. Pero los tres códigos de la clase detectan *clases distintas* de error, y elegir el equivocado deja pasar tramas absurdas. La decisión profesional es qué errores se espera detectar y qué código los cubre, y declararlo.

## Cómo funciona

Según `SE-266`:

- **Paridad.** Un bit que hace par el número de unos. Detecta cualquier cantidad *impar* de bits invertidos y ninguna cantidad par: dos bits invertidos pasan sin ser vistos.
- **Suma de 8 bits.** Detecta muchos errores, pero puede cancelarse: dos bits invertidos en posiciones iguales de dos bytes, en sentidos opuestos, dejan la suma igual.
- **CRC** (comprobación de redundancia cíclica). Trata la trama como un polinomio y la divide por uno generador; el resto se envía como control. Con un polinomio de grado 8 detecta toda ráfaga de hasta 8 bits y, en tramas cortas, todo error de uno a tres bits. Koopman y Chakravarty, citados por la clase, muestran que la elección del polinomio decide cuántos errores de varios bits se detectan.

El receptor recalcula el control sobre lo recibido y lo compara con el que llegó; si difieren, descarta la trama o pide reenvío.

## Ejemplo

El nodo ambiental de la sala de estudio (caso conductor de la Parte 22) deja en `SE-266` la lectura de cada sensor con su eficiencia de bus, su código de control y su factor de sobremuestreo justificados. Ilustración propia: un bit de paridad sobre el byte `0110 0101` (cuatro unos) con paridad par es 0; si el ruido invierte dos bits, la paridad sigue siendo correcta y el error pasa; un CRC-8 sí lo detectaría.

## Errores y confusiones comunes

- **Tramas absurdas pasan el control:** se usó paridad o suma para errores de varios bits. Corrección: usar un CRC y declarar qué errores cubre (`SE-266`).
- **Confundir detectar con corregir:** para corregir hacen falta códigos distintos, que añaden más redundancia.
- **Confundirlo con una firma o un hash criptográfico:** un CRC detecta errores accidentales; no protege contra un atacante que recalcula el control.
- **El bus «es lento» aunque el reloj es alto:** es otro problema de la clase (lecturas de un byte con mucho encabezado), no del control.

## Límites y cuándo no aplica

Ningún código de control detecta *todos* los errores: un CRC bien elegido deja una probabilidad residual de que un error pase. No sirve como autenticación (esa pertenece a la firma digital y a la raíz de confianza). Y añade bits a cada trama, lo que reduce la eficiencia del bus; en tramas muy cortas el control puede ser una fracción grande del total.
