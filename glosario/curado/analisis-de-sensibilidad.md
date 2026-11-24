# Análisis de sensibilidad

## Definición

El **análisis de sensibilidad** estudia cuánto cambia el resultado de un modelo al variar uno de sus parámetros. `SE-526` es la clase donde se define, aplicado a la decisión de reescribir o evolucionar. El programa lo usa con matices: en `SE-255` es repetir una decisión variando sus supuestos para medir con qué frecuencia el resultado se mantiene; en `SE-333` es estudiar cuánto deben moverse pesos o supuestos para que otra alternativa gane.

## Por qué importa

Convierte una discusión de preferencias en una pregunta medible. `SE-526` existe para que la pregunta «¿reescribimos o seguimos?» no se decida por cansancio, por entusiasmo tecnológico o por quien habla más fuerte, sino con un modelo de costos explícito, con incertidumbre y con las condiciones en que la respuesta cambia. El análisis dice *qué parámetro vale la pena medir antes de comprometerse*.

## Cómo funciona

Un modelo con siete parámetros inciertos no es igual de sensible a todos. La versión más simple, según `SE-526`:

1. Se toma cada parámetro por separado y se mueve entre un valor bajo y uno alto.
2. Los demás conservan sus distribuciones.
3. Se mide cuánto cambia la diferencia entre las opciones.

El parámetro con mayor recorrido domina la decisión. La utilidad es práctica: en vez de discutir qué opción es mejor, se discute cuánto costará construir, pregunta que se responde con una estimación mejor, un prototipo o el historial. Si el parámetro dominante no puede medirse hasta empezar, la decisión debe diseñarse para poder abandonarse cuando se mida.

En `SE-333` la variante mueve los pesos de una matriz de decisión; en `SE-255`, repite la decisión muchas veces con supuestos variados y cuenta cuántas veces gana la misma opción.

## Ejemplo

Escenario hipotético de `SE-526`, sin datos reales. El equipo toma de su historial que la última reescritura costó 1,8 veces su presupuesto y duró 1,5 veces lo previsto, mide un crecimiento del costo del módulo de 9 % anual y cuenta las peticiones que tocaron el módulo antiguo. Al simular, el análisis muestra que el costo de construir domina; deciden hacer un prototipo de una rebanada (`SE-521`) para medirlo antes de comprometer el resto.

## Errores y confusiones comunes

- **Aprobar una reescritura con un solo número** (`SE-526`): una estimación puntual oculta qué parámetro la sostiene.
- **Mover todos los parámetros a la vez** y no poder atribuir el efecto.
- **Confundirlo con un intervalo de confianza:** el análisis no mide el error de estimación, mide la influencia de cada entrada.

## Límites y cuándo no aplica

Mover un parámetro cada vez ignora interacciones entre parámetros. El resultado es tan bueno como el modelo: si falta un costo, ninguna variación lo revela. Los datos de `SE-526` son un escenario construido para la clase. Y cuando la decisión es barata o reversible, el análisis cuesta más que equivocarse.
