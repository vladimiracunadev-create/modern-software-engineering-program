# Coste del retraso

## Definición

El **coste del retraso** (*cost of delay*) es la pérdida económica o de beneficio por unidad de tiempo en que un trabajo no está disponible; sirve para ordenar trabajos de distinta duración (SE-128). Se expresa en valor por semana, por ejemplo, no como un total.

## Por qué importa

Cambia cómo se ordena una cola de trabajo. Ordenar solo por «lo más valioso primero» parece razonable y no minimiza la pérdida total. SE-128 lo muestra: un trabajo muy valioso pero largo retrasa a todos los demás. Cuando el trabajo se secuencia, importan dos cosas a la vez: cuánto cuesta cada semana de espera y cuánto dura cada trabajo.

## Cómo funciona

Si cuatro trabajos se hacen uno tras otro, cada semana que espera uno acumula su coste de retraso. El coste total depende del orden: un trabajo corto con coste de retraso alto conviene antes que uno largo con valor algo mayor, porque libera su valor pronto y retrasa poco a los demás. La regla que lo formaliza es **«trabajo más corto ponderado primero»** (WSJF, *weighted shortest job first*): ordenar por coste de retraso dividido entre duración. En el caso simple de trabajos independientes y sin dependencias, esta regla **minimiza el coste total**, resultado clásico de la teoría de planificación.

SE-128 insiste en dos cautelas. Primera, los costes de retraso reales son **difíciles de estimar** (hay que estimar el valor perdido por semana, que cambia con el tiempo y con la competencia), por lo que se trabajan como rangos y se evalúa si el orden resiste a perturbaciones. El registro de priorización de la plataforma guarda por ítem la regla aplicada, los valores de entrada con su fuente y fecha, quién los estimó, la puntuación base, la probabilidad de quedar entre los tres primeros bajo perturbación y el estado (construir, probar, esperar, descartar). Segunda, el orden se recalcula cuando se resuelve un experimento y ningún ítem sube sin que cambie una entrada o su fuente.

## Ejemplo

Tres trabajos con (coste de retraso por semana, duración): A (10, 4 semanas), B (6, 1 semana), C (3, 1 semana). WSJF: A=2,5; B=6; C=3 → orden B, C, A. Coste total de espera: B espera 0, C espera 1 semana (3), A espera 2 semanas (20): 23. El orden «mayor valor primero» (A, B, C) da: B espera 4 (24) y C espera 5 (15): 39. (Aritmética ilustrativa del principio de SE-128.)

## Errores y confusiones comunes

- **Hacer primero lo más valioso y retrasar todo lo demás**: no se consideró la duración ni el coste del retraso; corrección: comparar con WSJF sobre las permutaciones relevantes y elegir el orden de menor coste total.
- **Tratar una estimación como un hecho.**
- **Ignorar las dependencias**: la regla supone trabajos independientes.
- **Confundir coste del retraso con costo de oportunidad**: el primero es por unidad de tiempo de espera; el segundo, el valor de lo que se descarta.

## Límites y cuándo no aplica

WSJF solo es óptimo con trabajos independientes y costes de retraso constantes en el tiempo. Con fechas límite duras (un cumplimiento regulatorio), el coste cambia bruscamente y hay que modelarlo. Cuando las estimaciones son muy inciertas, una regla simple con rangos y pruebas de sensibilidad es más honesta que una puntuación precisa.
