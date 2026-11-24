# Condición de salida

## Definición

Una **condición de salida** es la señal medible que indica cuándo retirar o simplificar un patrón de diseño (`SE-313`, `SE-323`). Se escribe en el momento de aplicar el patrón, no cuando ya molesta, y responde a la pregunta «¿qué tendría que ocurrir para que esto ya no compense?».

## Por qué importa

Un patrón aplicado tiene un costo estructural permanente: clases, indirección, nombres que aprender. Se justifica mientras la fuerza que lo motivó siga presente. Sin una condición de salida, el patrón sobrevive a su razón y se vuelve, en palabras de la clase, un monumento. La decisión que cambia es tratar un patrón como una apuesta con fecha de revisión, no como una mejora definitiva.

## Cómo funciona

`SE-313` pide que todo patrón aplicado lleve su condición de salida. Para el `Strategy` de tarifas, ejemplos de la clase: «si quedan dos canales, volver a una función con un `if`», o «si en un año no se añadió ninguna variante». Dos rasgos las hacen útiles:

1. **Es medible**: se puede comprobar con un conteo o una observación del repositorio, no con una impresión.
2. **Está atada a la fuerza**: la fuerza es la presión de diseño que justificó el patrón (por ejemplo, variantes que se añaden con frecuencia). Escribir la condición obliga a nombrarla. Si no hay forma de saber cuándo dejó de importar la fuerza, probablemente nunca fue clara.

La condición se registra junto al patrón en el catálogo de `SE-324`, de modo que quien lea el patrón dentro de un año sepa qué comprobar. `SE-323` la retoma con patrones de resiliencia: también ahí se define la señal que indica retirar el patrón.

El puente con agentes de `SE-313` añade un matiz: un agente puede proponer candidatos y escribir la implementación, pero la fuerza y la condición de salida dependen de un contexto que está en las personas y en el código; un agente que elige el patrón sin ese contexto reproduce la costumbre.

## Ejemplo

Se aplica `Strategy` para calcular tarifas por canal de venta, con la condición de salida «si quedan dos canales o si en un año no se añade ninguna variante, se vuelve a una función con un `if`». Un año después se revisa el repositorio: no hubo variantes nuevas y solo quedan dos canales. La condición se cumple y se simplifica el código, con la red de pruebas existente. Ejemplo tomado de los casos que cita `SE-313`.

## Errores y confusiones comunes

- **Aplicar el patrón sin escribir cuándo retirarlo**: nadie revisa y el patrón persiste.
- **Condición vaga** («cuando ya no haga falta»): no es medible.
- **Confundirla con la condición de aborto o de parada** de otros contextos: aquí se trata de retirar una decisión de diseño, no de detener un experimento.
- **Dejarla solo en la cabeza de quien aplicó el patrón**: debe quedar en el catálogo.

## Límites y cuándo no aplica

La señal no decide por sí sola: es el disparador de una revisión, no una orden automática de retirar. Lo que se mide puede ser un mal indicador de la fuerza, y la clase no ofrece umbrales universales: los ejemplos son del caso de tarifas. Para decisiones muy pequeñas y locales, escribir una condición puede costar más que el patrón mismo.
