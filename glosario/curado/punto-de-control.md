# Punto de control

## Definición

Un **punto de control** (*checkpoint*) es el estado mínimo guardado en almacenamiento duradero que permite reanudar una tarea sin repetirla entera. `SE-224` (automatización idempotente y reanudable) lo define como el registro del progreso que permite reanudar sin empezar de cero; `SE-575` (detener, recuperar y evaluar un agente) lo aplica a agentes. No es una copia completa del sistema: es lo mínimo para continuar.

## Por qué importa

Reiniciar desde el principio es caro y, además, repite los efectos (`SE-575`). Con un punto de control se recalcula como mucho el paso en curso. Pero `SE-224` avisa que no es gratis: evita rehacer, y crea ventanas de duplicado o de pérdida entre el efecto y el registro del progreso.

## Cómo funciona

`SE-575` describe el contenido: en qué paso va el agente, qué ha hecho y qué le falta. Se guarda en un almacenamiento que sobrevive a la caída (una base de datos, un archivo) y se escribe en **puntos conocidos**. Anthropic informa, según la clase, de que en su sistema de investigación no pueden reiniciar desde el principio por el costo, y han construido uno que reanuda desde donde estaba el agente, combinando el modelo con reintentos y puntos de control deterministas.

La tensión que `SE-224` hace explícita está entre dos escrituras: el efecto (enviar, cobrar) y el registro del progreso.

- **Si se registra antes del efecto,** una caída entre ambos pierde el efecto.
- **Si se registra después,** una caída entre ambos lo repite.

Por eso el punto de control se combina con **idempotencia**: el paso que se repite no debe causar daño al hacerlo dos veces.

## Ejemplo

El equipo de *Avisos* en `SE-575` instala tres reglas para su agente de envíos: máximo de 80 pasos por tarea (calibrado con la cola de la distribución de las tareas buenas), cinco repeticiones del mismo estado y diez pasos sin avance del número de avisos preparados. Al detenerse por una regla, deja un punto de control para que la reanudación continúe sin repetir los avisos ya enviados.

## Errores y confusiones comunes

- **Reiniciar desde cero tras una caída** y repetir efectos (`SE-575`).
- **Guardarlo en memoria o en un archivo temporal** que no sobrevive.
- **Ignorar la ventana entre efecto y registro.**
- **Confundirlo con una copia de seguridad:** es progreso de una tarea, no un respaldo del sistema.

## Límites y cuándo no aplica

Para tareas muy cortas, el costo de guardar supera al de repetir. Para tareas cuyo estado no se puede resumir de forma segura (conversaciones con contexto largo), el punto de control es incompleto. La escenografía de `SE-575` es hipotética: sin datos reales.
