# Lectura partida

## Definición

Una **lectura partida** (*torn read*) es la lectura de un valor de varios bytes que mezcla partes de dos escrituras distintas. Es el sentido de `SE-269` (interrupciones, concurrencia y estado compartido) en microcontroladores. Aparece cuando la lectura no es atómica y algo (una interrupción) cambia el valor entre sus pasos.

## Por qué importa

Es un defecto casi invisible: casi siempre da un resultado correcto, y de vez en cuando uno absurdo, rarísimo y casi irreproducible. Quien no conoce el mecanismo atribuye el síntoma al ruido del sensor.

## Cómo funciona

`SE-269` da el caso: en un procesador de 8 bits, un valor de 16 bits se lee en dos instrucciones (byte alto y byte bajo). Si la interrupción actualiza el valor entre ambas, el programa obtiene un byte alto antiguo y uno bajo nuevo, o al revés.

El resultado suele ser inocuo: si el valor solo se incrementa en uno y el byte bajo no pasa de 255 a 0, el valor leído coincide con el nuevo. Pero cuando el incremento cruza un límite de byte, el valor leído difiere en 255 o 256: un salto grande.

Tres defensas de la clase:

1. **Sección crítica:** desactivar las interrupciones mientras se lee.
2. **Lectura doble:** leer hasta que dos lecturas consecutivas coincidan.
3. **Número de secuencia:** la interrupción lo incrementa antes y después de escribir; el lector repite si cambió o es impar.

## Ejemplo

Ilustración numérica: el contador vale `0x00FF` y la interrupción lo sube a `0x0100`. El programa lee el byte alto (`0x00`), llega la interrupción y escribe `0x0100`; luego lee el byte bajo (`0x00`). El valor obtenido es `0x0000`: un salto de 255 hacia atrás, que en un registro de tiempo parecería un reloj que retrocede. Es el tipo de síntoma que `SE-269` describe como saltos grandes rarísimos.

## Errores y confusiones comunes

- **Un valor muestra saltos grandes rarísimos:** causa, lectura partida de un valor de varios bytes; corrección, una de las tres defensas (`SE-269`).
- **Pensar que se resuelve con `volatile`:** impide que el compilador reutilice el valor, pero no hace atómica la lectura.
- **Aplicarla solo a microcontroladores de 8 bits:** puede ocurrir cada vez que el ancho del valor supera lo que el procesador lee de una vez.
- **Confundirla con una condición de carrera completa:** es una de sus formas.

## Límites y cuándo no aplica

En procesadores que leen el valor completo en una instrucción atómica no ocurre. La lectura doble supone que el valor deja de cambiar entre lecturas; si cambia más rápido que el bucle de lectura, no termina. La sección crítica introduce latencia de interrupción: debe ser corta.
