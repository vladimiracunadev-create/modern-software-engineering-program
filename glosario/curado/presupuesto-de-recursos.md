# Presupuesto de recursos

## Definición

El **presupuesto de recursos** es el conjunto de límites medibles de tiempo de respuesta, energía y memoria que el producto acepta en un dispositivo de referencia. Es el sentido de `SE-261` (rendimiento, batería y recursos limitados). `SE-267` lo usa en dispositivos embebidos con un matiz: una lista de supuestos de energía, memoria y precisión con las consecuencias de cada uno.

## Por qué importa

Convierte «rápido» y «ligero» en números con un responsable. Sin un número, nadie puede decidir si un cambio empeora la situación: cada cambio parece pequeño y la suma es un producto lento que agota la batería.

## Cómo funciona

`SE-261`: el presupuesto fija

- **cuánto tiempo puede tardar** en responder cada pantalla,
- **cuánta energía puede gastar** en segundo plano,
- **cuánta memoria puede ocupar**,

todo medido en un **dispositivo de referencia modesto**. Debe medirse y revisarse, y su cifra depende del dispositivo: la de un equipo de escritorio no sirve para un teléfono. Un presupuesto sin medición automática ni dueño es una intención.

En el mundo embebido (`SE-267`), el presupuesto es la lista de supuestos y sus consecuencias: cuánta corriente media consume el dispositivo (determinada por el ciclo de trabajo), cuánta memoria deja libre el firmware y qué precisión numérica se acepta. Cada supuesto se anota con lo que ocurre si no se cumple.

## Ejemplo

El cliente de entregas de la Parte 21 deja en `SE-261` su presupuesto de recursos y sus decisiones de lista, sincronización y caché. Luego `SE-262` revisa la superficie de seguridad que cada decisión añade, `SE-263` mide diferencias entre dos plataformas y `SE-264` integra el presupuesto en el proyecto. Cambiar una sola decisión, el sondeo cada 5 minutos por notificaciones por empuje, muestra qué cifras cambian: menos despertares y menos energía, con otra dependencia.

## Errores y confusiones comunes

- **Fijarlo sin dispositivo de referencia** o con el equipo de desarrollo, que es potente.
- **Medirlo una vez y no revisarlo.**
- **Un presupuesto sin dueño ni acción al superarlo.**
- **Confundirlo con el presupuesto de rendimiento web,** que se mide en bytes y métricas de carga (`SE-235`), o con el presupuesto de fotograma, que es un plazo de dibujo.

## Límites y cuándo no aplica

El dispositivo de referencia envejece: lo modesto de hoy no lo es en dos años. Las cifras exactas dependen del producto; la clase da el método, no los valores universales. En un sistema de servidor la analogía se expresa en capacidad y costo, no en batería.
