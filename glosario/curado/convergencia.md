# Convergencia

## Definición

La **convergencia** es el estado en que un verificador independiente no encuentra ningún criterio de la especificación sin cumplir (`SE-567`). Es la única condición de parada «feliz» de un bucle de agente.

## Por qué importa

«El agente dice haber terminado» no es convergencia. Para que lo sea, el veredicto debe venir de un verificador distinto del propio agente, con criterios ejecutables previos.

## Cómo funciona

`SE-567` define el bucle: el agente trabaja, el verificador revisa los criterios, y el bucle acaba cuando no queda ninguno abierto. Las otras condiciones (máximo de pasadas, sin progreso, presupuesto, regresión) detienen sin convergencia y llaman a una persona. El valor de la convergencia depende de la **cobertura del verificador**: si no mira un criterio, no puede declararlo cumplido, por lo que la clase pide publicar la cobertura y medir su capacidad de detección con variantes defectuosas.

## Ejemplo

`SE-567` (asistente de *Avisos*): un agente migra textos de una intranet a otro formato. Sin verificador independiente, declara haber terminado y la revisión encuentra incumplimientos. Con criterios ejecutables previos, la convergencia significa que el verificador recorrió todos y no halló ninguno abierto.

## Errores y confusiones comunes

**El agente dice haber terminado y la revisión encuentra incumplimientos.** Verificador del propio agente o con cobertura parcial; criterios ejecutables previos y cobertura publicada.

## Límites y cuándo no aplica

La convergencia es tan fiable como el verificador: una variante defectuosa que ningún criterio detecta pasa. Por eso se mide con variantes y se declara qué criterios no detectarían un defecto concreto.
